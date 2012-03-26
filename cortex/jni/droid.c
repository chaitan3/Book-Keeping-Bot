#include "droid.h"
#include<string.h>

char *droid_full_path(char *file, char *path)
{
  path = realloc(path, strlen(file) + strlen(SDCARD) + 1);
  strcpy(path, SDCARD);
  strcat(path, file);
  return path;
}
