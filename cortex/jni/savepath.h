#ifndef SAVE_PATH_H
#define SAVE_PATH_H
#include "list.h"

void add_point_to_path(int x, int y);
int save_path(char *file, int s_x, int s_y, int e_x, int e_y, list_type **res);
int **save_processed_path(int s_x, int s_y, int e_x, int e_y, list_type **res);

#endif
