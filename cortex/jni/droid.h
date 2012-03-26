#include<android/log.h>

#define LOGD(...) __android_log_print(ANDROID_LOG_DEBUG  , "libnav", __VA_ARGS__) 
#define SDCARD "/sdcard/bookbot/"

char *droid_full_path(char *file, char *path);
