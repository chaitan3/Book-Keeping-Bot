#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "droid.h"
#include "list.h"
#include "astar.h"
#include "loadmap.h"

int add_path_cost(int start_x, int start_y, int end_x, int end_y)
{
  if((start_x == end_x) || (start_y == end_y))
    return DISTANCE;
  else
    return DIAGDIST;
}

int calc_heurestic_cost(int start_x, int start_y, int end_x, int end_y)
{
  int x = abs(end_x - start_x), y = abs(end_y - start_y);
  if(x > y)
    return y * DIAGDIST + (x - y) * DISTANCE;
  else
    return x * DIAGDIST + (y - x) * DISTANCE;
}

void find_path(int start_x, int start_y, int end_x, int end_y)
{
  node *curr;
  int i, j, g;
  
  curr = &nodes[start_y][start_x];
  curr->g = 0;
  while(!((curr->x == end_x) && (curr->y == end_y)))
  {
    curr->type = closed;
    i = curr->y - 1;
    if(i < 0)
      i = 0;
    for(; (i <= (curr->y + 1)) && (i < rows); i++)
    {
      j = curr->x - 1;
      if(j < 0)
        j = 0;
      for(; (j <= (curr->x + 1)) && (j < columns); j++)
      {
        
        switch(nodes[i][j].type)
        {
          case closed:
            break;
            
          case open:
            g = curr->g + add_path_cost(curr->x, curr->y, nodes[i][j].x, nodes[i][j].y);
            if(nodes[i][j].g > g)
            {
              nodes[i][j].parent = curr;
              nodes[i][j].g = g;
              nodes[i][j].f = nodes[i][j].g + nodes[i][j].h;
              
              //Can be optimised
              resort_open_list(&nodes[i][j]);
            }
            break;
            
          case none:
            nodes[i][j].type = open;
            nodes[i][j].parent = curr;
            nodes[i][j].g = curr->g + add_path_cost(curr->x, curr->y, nodes[i][j].x, nodes[i][j].y); 
            nodes[i][j].h = calc_heurestic_cost(nodes[i][j].x , nodes[i][j].y, end_x, end_y);
            nodes[i][j].f = nodes[i][j].g + nodes[i][j].h;
            add_to_open_list(&nodes[i][j]);
            break;
            
          default:
            break;
        }
      }
    }
    curr = remove_open_list();
    if(curr == NULL)
      LOGD("No solution exists\n");
  }
}

