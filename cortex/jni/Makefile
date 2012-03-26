CC = gcc
FLAGS = -Wall -g -O2
LIBS = -lm
TARGET = ../algo
OBJ = astar.o list.o loadmap.o main.o savepath.o preprocess.o postprocess.o
all: $(TARGET)
$(TARGET): $(OBJ)
	$(CC) $(LIBS) $(OBJ) -o $@
%.o : %.c
	$(CC) $(FLAGS) -c $<
clean:
	rm -f $(OBJ) $(TARGET) 
