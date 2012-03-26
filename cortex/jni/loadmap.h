#ifndef LOADMAP_H
#define LOADMAP_H

#include "list.h"

extern int rows, columns;
extern node **nodes;

#define BOT_SAFETY 5
#define BOT_WIDTH 7

int load_map_from_file(char *file);
int load_locations(char *file, int *s_x, int *s_y, int *e_x, int *e_y);
int save_path();
void process_image();

#endif
