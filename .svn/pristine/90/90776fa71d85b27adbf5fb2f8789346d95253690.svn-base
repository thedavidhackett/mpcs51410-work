"""
The issue with the original code is that printer is dependent on the concrete
class Cartridge, violating the dependency inversion principle. Because of this
even a simple change to cartridge will now result in errors in printer. In
addition we can't reuse printer with different types of cartridge. The solution
to this is to 1) make use of an abstract interface instead of a concrete class.
To that end I created an abstract Cartridge class with one abstract method. Two
classes realize this abstract interface, a basic cartridge that only takes a
model number and a cartridge with number of pages. 2) We should make use of
dependency injection (which is now necessary anyways because we are using an
abstract class) to inject a concrete class into printer that realizes the
cartridge interface. Now its easy to reuse printer with different cartridges.s
"""

from abc import ABC, abstractmethod

class Cartridge(ABC):
    @abstractmethod
    def details(self) -> None:
        pass


class BasicCartridge(Cartridge):
    def __init__(self, model_num : str) -> None:
        super().__init__()
        self.model_num : str = model_num

    def details(self) -> None:
        print(f"Cartridge is {self.model_num}")

class CartridgeWithNumberOfPages(Cartridge):
    def __init__(self, model_num : str, num_pages : int) -> None:
        super().__init__()
        self.model_num : str = model_num
        self.num_pages : int = num_pages

    def details(self) -> None:
        print(f"Cartridge is {self.model_num} with {self.num_pages} pages")


class Printer:
    def __init__(self, cartridge : Cartridge) -> None:
        self.cartridge = cartridge

    def prepare(self) -> None:
        print("Printer is preparing to print")
        self.cartridge.details()

    def print(self) -> None:
        print("Printer is printing")


if __name__ == "__main__":
    cartridge1 : BasicCartridge = BasicCartridge("X543-44")
    cartridge2 : CartridgeWithNumberOfPages = CartridgeWithNumberOfPages("X543-44", 10)

    printer : Printer = Printer(cartridge1)

    printer.prepare()
    printer.print()

    printer.cartridge = cartridge2

    printer.prepare()
    printer.print()
