#include<stdio.h>
#include<stdlib.h>
#include "loadmap.h"

int load_locations(char *file, int *s_x, int *s_y, int *e_x, int *e_y)
{
  FILE *f;
  
  f = fopen(file, "r");
  if(f == NULL) 
    return 0;
    
  fscanf(f, " %*s %d %d ", s_y, s_x);
  fscanf(f, " %*s %d %d ", e_y, e_x);
 
  fclose(f);
    
  return 1;
}

int load_map_from_file(char *file)
{
  int i, j;
  char c;
  FILE *f;
  char buf[50];
  
  f = fopen(file, "r");
  if(f == NULL)
    return 0;
    
  fgets(buf, 50, f);
  fgets(buf, 50, f);
  fscanf(f, " %d %d ", &columns, &rows);
  
  nodes = (node **)malloc(sizeof(node *) * rows);
    
  for(i =  0; i < rows; i++)
  {
    nodes[i] = (node *)malloc(sizeof(node) * columns);
    for(j =  0; j < columns; j++)
    {
      fscanf(f, " %c ", &c);
      if(c == '1')
        nodes[i][j].type = closed;
      else
        nodes[i][j].type = none;
          
      nodes[i][j].x = j;
      nodes[i][j].y = i;
    }
  }
  
  fclose(f);
  
  return 1;
}


