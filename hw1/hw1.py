"""
There were a few issues with the original version of this code:
1) Did not honor single responsibility. FinancialReportNotificationManager was both sending and
creating the report.
2) Didn't make use of dependency injection. Instead of injecting NotificationEngine,
FinancialReportNotificationManager was instantiating it in a method. This means it has to be aware
of the exact class name and its requirements for initialization.
3) Dependency injection was going the wrong way. Account seems like the least likely class to change
so the notifier should be injected into account and not the other way around
4) Going off that, based on the requirements we want to keep transaction details and account details
private. Changing the dependency direction makes that easier for accounts.
5) Furthermore many classes need to be aware of the implementation details of other classes.
FinancialReportNotificationManager needs to be aware of the exact fields on transaction to create
a report. The code doesn't make use of public/private interfaces.
6) Finally the code doesn't embrace change. 2, 3, and 5 all go to this same problem, but what if
we want to report something besides transactions? What if the form of notification changes. This
would involve rewriting a lot of the existing code.

In rewriting the code I made the following decisions:

1. Get rid of FinancialReportNotificationManager
2. Create a Notifier interface with the method notify that Emailer realizes, this
can allow for another type of notifier to be used in the future
3. Inject a notifier into Account, now accounts attributes can be private and different
types of notifiers can be used. Granted accounts send_notification method would have to
change if email was no longer used, but probably a somewhat acceptable coupling.
4. Create a reportable interface that requires a get_details method. Transactions will
realize that interface.
5. Make a report class to handle the create of reports. Report is also a container for
reportables. The reports generate method doesn't need to know any fields from the reportable
just that it has a get_details method. This allows for transactions details to be private.
6. Using accessor methods along with the public interface methods allows for each class
to be concerned with its own implementation without having to worry about the implementation
of other classes.
"""

from abc import ABC, abstractmethod
import datetime
from typing import List

class Notifier(ABC):
    @abstractmethod
    def notify(self, contact : str, notification : str) -> None:
        pass

class Reportable(ABC):
    @abstractmethod
    def get_details(self) -> str:
        pass

class Account:
    def __init__(self, acct_num : int, email : str, notifier : Notifier, balance : int = 0) -> None:
        self.__account_number : int = acct_num
        self.__balance : int = balance
        self.__email : str = email
        self.__notifier : Notifier = notifier


    def __get_email(self) -> str:
        return self.__email

    def send_notification(self, notification : str) -> None:
        self.__notifier.notify(self.__get_email(), notification)


class Emailer(Notifier):
    def notify(self, contact: str, notification: str) -> None:
        #print for the example, but email in real life
        print(notification)

class Report():
    def __init__(self, items : List[Reportable]) -> None:
        self.items : List[Reportable] = items

    def generate(self) -> str:
        report_string : str = ""
        item : Reportable
        for item in self.items:
            report_string = report_string + item.get_details() + "\n"

        return report_string

class Transaction(Reportable):
    def __init__(self, amount : int, type : str, date : datetime.date) -> None:
        self.__amount : int = amount
        self.__type : str = type
        self.__date : datetime.date = date
        self.__created_at : datetime.date = datetime.date.today()

    def get_details(self) -> str:
        return f"amount: ${self.__amount}, type: {self.__type}, date: {self.__date}"


if __name__ == "__main__":
    account : Account = Account(12345, "joe@blow.com", Emailer(), 20)
    t1 : Transaction = Transaction(10, "deposit", datetime.date(22, 10, 10))
    t2 : Transaction = Transaction(10, "withdrawal", datetime.date(22, 10, 31))

    report : Report = Report([t1, t2])

    account.send_notification(report.generate())
