"""
The main issue with the original code is that it violates the interface
segregation principle (ISP). With just one registrar interface each client, the
student, instructor, and registrar is aware of and gets all of the methods
defined in that interface, including many that they do not need because they
will not use them. Instead I defined three separate interfaces, one for each
client. They could have been separated into different functions (like a class
manager and tutition payer etc etc), but for simplicity I defined them based
on the needs of the client. Now even though there is one concrete class,
Registration, that implements all three interfaces I used dependency injection
to give each client the interface it needs and no more than that. In addition
I made a Logger base class since each client logs. It might make more sense to
have made this its own class and injected it into each client but for this
example I went with the easiest solution that was DRY.
"""

from abc import ABC, abstractmethod

class StudentRegistrarInterface(ABC):
    @abstractmethod
    def register_for_class(self) -> None:
        pass

    @abstractmethod
    def pay_tuition(self) -> None:
        pass

    @abstractmethod
    def get_classroom(self) -> None:
        pass

    @abstractmethod
    def get_my_grade(self) -> None:
        print("do you really want to know?")

    @abstractmethod
    def drop_class_from_my_schedule(self) -> None:
        print("class is dropped")

class InstrutorRegistrarInterface(ABC):
    @abstractmethod
    def enter_grades(self) -> None:
        pass

    @abstractmethod
    def get_classroom(self) -> None:
        pass

    @abstractmethod
    def get_enrollment_numbers(self) -> None:
        pass

class RegistrarRegistrarInterface(ABC):
    @abstractmethod
    def get_enrollment_numbers(self) -> None:
        pass

    @abstractmethod
    def run_class(self) -> None:
        pass

    @abstractmethod
    def set_instructor_for_class(self) -> None:
        pass

    @abstractmethod
    def add_class_to_quarter_schedule(self) -> None:
        pass

    @abstractmethod
    def drop_class_from_quarter_schedule(self) -> None:
        pass


class Logger(ABC):
    def log(self) -> None:
        print("Now I'm logging")

class Student(Logger):
    def __init__(self, my_schedule : StudentRegistrarInterface) -> None:
        super().__init__()
        self.__my_schedule : StudentRegistrarInterface = my_schedule

    def register_for_class(self) -> None:
        print("Student Josephine is preparing to regiser for a new course that she likes")
        print("Student is registering for the class")
        self.__my_schedule.register_for_class()
        print("Seems like this education thing is awfully costly...time to pay tuition again!")
        self.__my_schedule.pay_tuition()
        print("I'm five minutes late, where the heck is the classroom???")
        self.__my_schedule.get_classroom()
        print("Course is over.  Whew.  What's my grade???")
        self.__my_schedule.get_my_grade()


class Registrar(Logger):
    def __init__(self, registrar_office : RegistrarRegistrarInterface) -> None:
        super().__init__()
        self.__registrar_office : RegistrarRegistrarInterface = registrar_office

    def create_class(self) -> None:
        self.__registrar_office.add_class_to_quarter_schedule()
        print("Registrar is setting the instructor for this course")
        self.__registrar_office.set_instructor_for_class()
        print("Registrar is getting the current number of students registered for the course")
        self.__registrar_office.get_enrollment_numbers()
        print("The quarter has begun!")
        self.__registrar_office.run_class()

class Instructor(Logger):
    def __init__(self, my_schedule : InstrutorRegistrarInterface) -> None:
        super().__init__()
        self.__my_schedule : InstrutorRegistrarInterface = my_schedule

    def teach_class(self) -> None:
        print("Professor Rumplestilskin is preparing to teach a new course")
        print("Professor is getting the current number of students registered for the course")
        self.__my_schedule.get_enrollment_numbers()
        print("Professor is wondering where his class is, as he only has five minutes to get there")
        self.__my_schedule.get_classroom()
        print("Course is over.  Whew.  Now I have to assign grades for my students")
        self.__my_schedule.enter_grades()


class Registration(StudentRegistrarInterface, InstrutorRegistrarInterface, RegistrarRegistrarInterface):
    def __init__(self) -> None:
        super().__init__()

    def register_for_class(self) -> None:
        print("Student is registered!")

    def pay_tuition(self) -> None:
        print("Tutition is paid!")

    def set_instructor_for_class(self) -> None:
        print("Instructor is assigned!")

    def get_enrollment_numbers(self) -> None:
        print("Wow, this class has a lot of students")

    def get_classroom(self) -> None:
        print("Its here!")

    def get_my_grade(self) -> None:
        print("Are you sure you want to know?")

    def enter_grades(self) -> None:
        print("Just give everyone an A")

    def add_class_to_quarter_schedule(self) -> None:
        print("Class added!")

    def run_class(self) -> None:
        print("Lets go!")

    def drop_class_from_quarter_schedule(self) -> None:
        print("Class dropped!")

    def drop_class_from_my_schedule(self) -> None:
        print("All your classes are dropped!")


if __name__ == "__main__":
    reg : Registration = Registration()
    s : Student = Student(reg)
    i : Instructor = Instructor(reg)
    r : Registrar = Registrar(reg)

    r.create_class()
    r.log()

    i.teach_class()
    i.log()

    s.register_for_class()
    s.log()
