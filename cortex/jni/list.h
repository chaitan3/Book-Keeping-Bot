#ifndef LIST_H
#define LIST_H

typedef enum {
  open,
  closed,
  none,
  open2
}list_type;

typedef struct node_t {
  
  struct node_t *parent;
  
  int x;
  int y;
  
  int f;
  int g;
  int h;
  
  list_type type;
  
}node;

void free_open_list();
void swap_nodes_in_open_list(int i, int j);
void add_to_open_list(node *n);
void resort_open_list(node *n);
node * remove_open_list(void);
int search_in_open_list(node *n);
void print_open_list();

#endif

