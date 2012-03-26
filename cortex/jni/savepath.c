#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "loadmap.h"
#include "postprocess.h"
#include "savepath.h"

static int *path[2] = {NULL, NULL};

void add_point_to_path(int x, int y)
{
  static int i = 0;
  
  path[0] = realloc(path[0], sizeof(int) * (i + 1));
  path[1] = realloc(path[1], sizeof(int) * (i + 1));
  path[0][i] = x;
  path[1][i] = y;
  i++;
  
}

int **save_processed_path(int s_x, int s_y, int e_x, int e_y, list_type **res)
{
  int x0, x1, y0, y1;
  int ns, nn, i, j, x, y, x2, y2, k = 0;
  double m;
  
  x0 = s_x;
  y0 = s_y;
  while(!((x0 == e_x) && (y0 == e_y)))
  {
    x1 = path[0][k];
    y1 = path[1][k];
    k++;
    
    int *straight[2] = {NULL, NULL}, *normal[2] = {NULL, NULL};
    
    ns = bresenham_line(x0, y0, x1, y1, straight);
    
    if((y1 - y0) == 0)
    {
      x2 = 0;
      y2 = BOT_WIDTH / 2;
    }
    else
    {
      m = ((double)(x0 - x1)) / (y1 - y0);
      x2 = BOT_WIDTH / (2 * sqrt(m * m + 1));
      y2 = (BOT_WIDTH * m) / (2 * sqrt(m * m + 1));
    }
    nn = bresenham_line(x0 + x2, y0 + y2, x0 - x2, y0 - y2, normal);
    
    for(i = 0; i < nn; i++)
    {
      for(j = 0; j < ns; j++)
      {
        x = straight[0][j] + normal[0][i] - x0;
        y = straight[1][j] + normal[1][i] - y0;
        if((y >= 0) && (y < rows) && (x >= 0) && (x < columns))
          res[y][x] = open2;
      }
    }
    
    free(straight[0]);
    free(straight[1]);
    free(normal[0]);
    free(normal[1]);
    
    x0 = x1;
    y0 = y1;
  }  
  
  return path;
}

int save_path(char *file, int s_x, int s_y, int e_x, int e_y, list_type **res)
{
  FILE *f;
  node *path_node;
  int i, j;
  
  f = fopen(file, "w");
  if(f == NULL)
    return 0;
    
  path_node = &nodes[e_y][e_x];
  while(1)
  {
    res[path_node->y][path_node->x] = open;
    path_node = path_node->parent;
    if((path_node->x == s_x) && (path_node->y == s_y))
      break;
  }
  
  res[path_node->y][path_node->x] = open;
  
  fprintf(f, "P2\n");
  fprintf(f, "%d %d\n", columns, rows);
  fprintf(f, "255\n");
  
  for(i = 0; i < rows; i++)
  {
    for(j = 0; j < columns; j++)
    {
      switch(res[i][j])
      {
        case none:
          fprintf(f, "0\n");
          break;
        case open:
          fprintf(f, "120\n");
          break;
        case closed:
          fprintf(f, "255\n");
          break;
        case open2:
          fprintf(f, "50\n");
          break;
      }
    }
  }
  
  fclose(f);
  free(path[0]);
  free(path[1]);
  return 1;
}
