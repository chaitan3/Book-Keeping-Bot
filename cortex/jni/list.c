#include<stdlib.h>
#include "list.h"

static int num_open_list = 0;
static node **open_list = NULL;

void free_open_list()
{
  free(open_list);
}

void swap_nodes_in_open_list(int i, int j)
{
  node *temp;
  temp = open_list[i];
  open_list[i] = open_list[j];
  open_list[j] = temp;
}

void add_to_open_list(node *n)
{
  int i, j = num_open_list;
  
  open_list = (node **)realloc(open_list, sizeof(node *) * (num_open_list + 1));

  open_list[j] = n;
  
  do
  {
    if(j == 0)
      break;
      
    if((j % 2) == 0)
      i = j / 2 - 1;
    else
      i = j / 2;
    
    if(open_list[j]->f < open_list[i]->f)
    {
      swap_nodes_in_open_list(i, j);
      j = i;
    }
    else
      break;
      
  }while(i > 0);
  
  num_open_list++;
}
node * remove_open_list(void)
{
  int i = 0, j;
  node *return_node;
  
  if(num_open_list == 0)
    return NULL;
    
  num_open_list--;
  return_node = open_list[0];
  
  open_list[0] = open_list[num_open_list];
  while(i <= (num_open_list - 1)/2) 
  {
    j = i * 2 + 1;
    
    if(j == num_open_list)
    {
      if(open_list[j]->f < open_list[i]->f)
        swap_nodes_in_open_list(i, j);
      break;
    }
      
    if((open_list[i]->f <= open_list[j]->f) && (open_list[i]->f <= open_list[j + 1]->f))
      break;
    else
    {
      if(open_list[j]->f < open_list[j + 1]->f)
      {
        swap_nodes_in_open_list(i, j);
        i = j;
      }
      else
      {
        swap_nodes_in_open_list(i, j + 1);
        i = j + 1;
      }  
    }
  }
  
  return return_node;
}

void resort_open_list(node *n)
{
  int i, j;
  j = search_in_open_list(n);
  
  do
  {
    if(j == 0)
      break;
      
    if((j % 2) == 0)
      i = j / 2 - 1;
    else
      i = j / 2;
    
    if(open_list[j]->f < open_list[i]->f)
    {
      swap_nodes_in_open_list(i, j);
      j = i;
    }
    else
      break;
      
  }while(i > 0);
  
}

int search_in_open_list(node *n)
{
  int i;
  for(i = 0; i < num_open_list; i++)
  {
    if(open_list[i] == n)
      return i;
  }
  return -1;
}

