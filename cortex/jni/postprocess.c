#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include "postprocess.h"
#include "savepath.h"
#include "loadmap.h"

//Understand this algo
int bresenham_line(int x0,int y0,int x1,int y1, int **points)
{
  int dx, dy, err, sx, sy, err2, n = 0;
  
  dx = abs(x1 - x0);
  dy = abs(y1 - y0);
  if(x0 < x1)
    sx = 1;
  else
    sx = -1;
  if(y0 < y1)
    sy = 1;
  else
    sy = -1;
    
  err = dx - dy;
    
  while(!((x0 == x1) && (y0 == y1)))
  {
    points[0] = realloc(points[0], sizeof(int) * (n + 1));
    points[1] = realloc(points[1], sizeof(int) * (n + 1));
    points[0][n] = x0;
    points[1][n] = y0;
    n++;
    
    err2 = 2 * err;
    if(err2 > -dy)
    {
      err -= dy;
      x0 += sx;
    }
    if(err2 < dx)
    {
      err += dx;
      y0 += sy;
    }
  }
  return n;
}

int no_obstacle_in_path(int x0,int y0,int x1,int y1, list_type **obs)
{
  
  int *line[2] = {NULL, NULL};
  int n, i, x, y;
  
  n = bresenham_line(x0, y0, x1, y1, line);
  
  for(i = 0; i < n; i++)
  {
    x = line[0][i];
    y = line[1][i];
    if((y >= 0) && (y < rows) && (x >= 0) && (x < columns))
    {
      if(obs[y][x] == closed)
        return 0;
    }
  }
  
  free(line[0]);
  free(line[1]);
  return 1;
  
}

int find_shorter_path(int s_x,int s_y,int e_x,int e_y, list_type **obs)
{
  node *start, *end;
  int n_nodes = 0;
  
  start = &nodes[s_y][s_x];
  end = &nodes[e_y][e_x];
  while(start != (&nodes[e_y][e_x]))
  {
    if(no_obstacle_in_path(start->x, start->y, end->x, end->y, obs))
    {
      start = end;
      end = &nodes[e_y][e_x];
      
      add_point_to_path(start->x, start->y);
      n_nodes++;
    }
    else
      end = end->parent;
  }
  return n_nodes;
}
