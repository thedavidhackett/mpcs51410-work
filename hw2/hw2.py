"""
The main issue with the original code is that everytime a new payment method is
added in addition to adding a new function to ShoppingCart we have to modify the
call shopping cart method with a new if else condition. Not only is this more work
but creates room for more bugs (what if the type in the condition doesn't match
the payment method?). A strategy pattern works well here. Instead of add new methods
and modifying the call shopping cart method we can give ShoppingCart a paymentmethod
attribute of with type being the abstract base class PaymentMethod with the abstract
method pay. In this way we can define separate payment method classes and can continue
to implement new payment methods without ever modifying shopping cart again. All
shopping cart will need to do is ise is call_shopping_cart method which in turn
calls the pay method of whatever payment method has been injected.
"""

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self) -> None:
        pass

class ShoppingCart:
    def __init__(self, payment_method : PaymentMethod) -> None:
        self.__payment_method = payment_method


    def call_shopping_cart(self) -> None:
        self.__payment_method.pay()

    def set_payment_method(self, payment_method : PaymentMethod) -> None:
        self.__payment_method = payment_method


class Paypal(PaymentMethod):
    def pay(self) -> None:
        print("Paying with paypal")


class CreditCard(PaymentMethod):
    def pay(self) -> None:
        print("Paying with credit card")

class ApplePay(PaymentMethod):
    def pay(self) -> None:
        print("Paying with Apply Pay")

class Sepa(PaymentMethod):
    def pay(self) -> None:
        print("Paying with SEPA")

class Bitcoin(PaymentMethod):
    def pay(self) -> None:
        print("Paying with Bitcoin")


if __name__ == "__main__":
    shopping_cart : ShoppingCart = ShoppingCart(CreditCard())
    shopping_cart.call_shopping_cart()
    shopping_cart.set_payment_method(Bitcoin())
    shopping_cart.call_shopping_cart()
