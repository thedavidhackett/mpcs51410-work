from typing import List


class Course:
    def __init__(self, id : int = 0, details : dict = {}) -> None:
        self.id = id
        self.closed : bool = False
        self.details : dict = details

    def get_details(self) -> dict:
        return self.details

class Lab(Course):
    def __init__(self, course_id : int, id: int = 0, details: dict = {}) -> None:
        super().__init__(id, details)
        self.course_id = course_id

class Restriction():
    pass

class User:
    def __init__(self, details : dict = {}) -> None:
        self.details : dict = details

    def get_details(self) -> dict:
        return self.details

class Student(User):
    def __init__(self, course_limit = 3) -> None:
        super().__init__()
        self.course_load : List[Course] = []
        self.restrictions : List[Restriction] = []
        self.course_limit : int = course_limit

    def register(self, course : Course) -> None:
        pass

    def get_restrictions(self) -> List[Restriction]:
        return self.restrictions

    def add_restriction(self, restriction : Restriction) -> None:
        pass

    def drop_course(self, course_id) -> None:
        pass

    def reschedule_course(self, course_id) -> None:
        pass


class CourseController():
    def __init__(self) -> None:
        pass

    def get_course_by_id(self, id : int) -> Course:
        pass

    def get_course_labs(self, id : int) -> List[Lab]:
        pass

class RestrictionException(Exception):
    pass

class OverloadException(Exception):
    pass

class RegistrationClosedException(Exception):
    pass
