#ifndef POST_PROCESS_H
#define POST_PROCESS_H
#include "list.h"

int bresenham_line(int x0,int y0,int x1,int y1, int **points);
int find_shorter_path(int s_x,int s_y,int e_x,int e_y, list_type **obs);
int no_obstacle_in_path(int x0,int y0,int x1,int y1, list_type **obs);

#endif

