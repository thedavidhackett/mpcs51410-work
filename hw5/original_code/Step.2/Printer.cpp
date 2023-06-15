#include "Printer.h"
#include "Cartridge.h"

void Printer::prepare()
 {
	 cout << "Printer is preparing to print\n";
    string name = "X543-44";
    Cartridge * c = new Cartridge( name );
    delete c;
 }
void Printer::print()
 {
	 cout << "Printer is printing\n";
 }


