using System;

class ShoppingCart
{
   static void Main(string[] args)
   {
      string paymentMethod = "paypal";
      ShoppingCart sc = new ShoppingCart();
      sc.CallShoppingCart(paymentMethod);
   }

   public void CallShoppingCart(string paymentMethod)
   {
      if (paymentMethod == "paypal")
      {
         Console.WriteLine("Paying with paypal");
         payWithPayPal();
      }
      else if (paymentMethod == "creditcard")
      {
         Console.WriteLine("Paying with creditcard");
         payWithCreditCard();
      }
   }

   public void payWithPayPal()
   {
      Console.WriteLine("Paypal Implementation");
   }

   public void payWithCreditCard()
   {
      Console.WriteLine("Credit Card Implementation");
   }

}
