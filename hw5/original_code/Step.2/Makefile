#Makefile

all: mfp_printer

# Which compiler
CC=g++

# Where are include files kept
INCLUDE=.

# Options for development
CFLAGS=-g -Wall -ansi

mfp_printer: Main.o Printer.o Cartridge.o
	$(CC) -o mfp_printer Main.o Printer.o Cartridge.o

Main.o: Main.cpp 
	$(CC) -I$(INCLUDE) $(CFLAGS) -c Main.cpp

Printer.o: Printer.cpp 
	$(CC) -I$(INCLUDE) $(CFLAGS) -c Printer.cpp

Cartridge.o: Cartridge.cpp 
	$(CC) -I$(INCLUDE) $(CFLAGS) -c Cartridge.cpp

clean:
	-rm -f *.o mfp_printer *~

