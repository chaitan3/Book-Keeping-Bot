#ifndef ASTAR_H
#define ASTAR_H

#define DISTANCE 10
#define DIAGDIST 14

void find_path(int start_x, int start_y, int end_x, int end_y);
int add_path_cost(int start_x, int start_y, int end_x, int end_y); 
int calc_heurestic_cost(int start_x, int start_y, int end_x, int end_y); 

#endif
