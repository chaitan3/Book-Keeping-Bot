#include<stdio.h>
#include<stdlib.h>
#include<jni.h>

#include "droid.h"
#include "loadmap.h"
#include "preprocess.h"
#include "astar.h"
#include "postprocess.h"
#include "savepath.h"

int rows, columns;
node **nodes = NULL;

JNIEXPORT jint JNICALL Java_bot_cortex_BookBotMain_pathplanner(JNIEnv *env, jobject obj, \
  jintArray path_x, jintArray path_y)
{
  int i;
  int e_x, e_y, s_x, s_y;
  list_type **obs, **res;
  char *path = NULL;
  int **tmp_path;
  int n_nodes;
  
  s_x = 91;
  s_y = 255;
  e_x = 74;
  e_y = 68;
  //locations in s_x, e_x...
  
  path = droid_full_path("map.pbm", path);
  if(!load_map_from_file(path))
    LOGD("Unable to load map file\n");
    
  LOGD("%dx%d: (%d, %d) -> (%d, %d)\n", columns, rows, s_y, s_x, e_y, e_x);
  
  res = save_nodes();
  
  LOGD("Pre-processing Image..... ");
  fflush(stdout);
  obs = process_obstacles_area_map();
  LOGD("Done\n");
  
  LOGD("Finding Path..... ");
  fflush(stdout);
  find_path(s_x, s_y, e_x, e_y);
  LOGD("Soluton found\n");
  
  LOGD("Calculating Shorter Path....");
  fflush(stdout);
  n_nodes = find_shorter_path(s_x, s_y, e_x, e_y, obs);
  LOGD("Done\n");
  
  tmp_path = save_processed_path(s_x, s_y, e_x, e_y, res);
  (*env)->SetIntArrayRegion(env, path_x, 0, n_nodes, tmp_path[0]);
  (*env)->SetIntArrayRegion(env, path_y, 0, n_nodes, tmp_path[1]);
  
  path = droid_full_path("result.pgm", path);
  if(!save_path(path, s_x, s_y, e_x, e_y, res))
    LOGD("Unable to save result\n");
  
  free(path);
  
  for(i = 0; i < rows; i++)
    free(res[i]);
  free(res);
  
  for(i = 0; i < rows; i++)
    free(obs[i]);
  free(obs);
  
  free_open_list();
  for(i = 0; i < rows; i++)
    free(nodes[i]);
  free(nodes);
  
  return (jint)n_nodes;
}
