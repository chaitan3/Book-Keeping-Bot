#include<stdlib.h>
#include<math.h>
#include "loadmap.h"
#include "preprocess.h"

list_type **save_nodes()
{
  int i, j;
  list_type **res;
  res = (list_type **)malloc(sizeof(list_type *) * rows);
  for(i = 0; i < rows; i++)
  {
    res[i] = (list_type *)malloc(sizeof(list_type) * columns);
    for(j = 0; j < columns; j++)
      res[i][j] = nodes[i][j].type;
  }
  return res;
}

list_type ** process_obstacles_area_map()
{
  int i, j, k, l, m, e, x, y;
  list_type **obs;
  
  obs = (list_type **)malloc(sizeof(list_type *) * rows);
  for(i = 0; i < rows; i++)
  {
    obs[i] = (list_type *)malloc(sizeof(list_type) * columns);
    for(j = 0; j < columns; j++)
      obs[i][j] = nodes[i][j].type;
  }
  
  for(i = 0; i < rows; i++)
  {
    for(j = 0; j < columns; j++)
    {
      if(nodes[i][j].type != closed)
        continue;
      
      m = 0;
      for(k = -1; k <= 1; k++)
      {
        for(l = -1; l <= 1; l++)
        {
          if((i + k >= 0) && (i + k < rows) && (j + l >= 0) && (j + l < columns))
          {
            if(nodes[i + k][j + l].type == closed)
              m++;
          }
        }
      }
      if(m == 9)
        continue;
      
      l = BOT_SAFETY + (BOT_WIDTH / 2);
      k = 0;
      e = 0;
      
      while(l > k)
      {
        for(x = j - l; x <= j + l; x++)
        {
          y = i + k;
          if((y >= 0) && (y < rows) && (x >= 0) && (x < columns) && (obs[y][x] != closed)) 
            obs[y][x] = closed;
          y = i - k;
          if((y >= 0) && (y < rows) && (x >= 0) && (x < columns) && (obs[y][x] != closed)) 
            obs[y][x] = closed;
        }
        
        for(x = j - k; x <= j + k; x++)
        {
          y = i + l;
          if((y >= 0) && (y < rows) && (x >= 0) && (x < columns) && (obs[y][x] != closed)) 
            obs[y][x] = closed;
          y = i - l;
          if((y >= 0) && (y < rows) && (x >= 0) && (x < columns) && (obs[y][x] != closed)) 
            obs[y][x] = closed;
        }
        
        k++;
        e += 8 * k + 5;
        if(e > (4 * l - 1))
        {
          e -= (8 * l - 4);
          l--;
        } 
      }
    }
  }
  
  for(i = 0; i < rows; i++)
  {
    for(j =  0; j < columns; j++)
      nodes[i][j].type = obs[i][j];
  }
  
  return obs;
}
