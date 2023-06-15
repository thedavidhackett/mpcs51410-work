"""
The problem with the original code is that it violates the liskov substitution
principle. While full professors and contractual instructors can become the
department chair teaching assistants cannot. This is fine for the hr manager
who simply wants to ask, but if we had a situation where someone passed a
teaching assistant as an instructor to a function like make_department_chair
we'd have to check if its a teaching assistant. It would be better to define two
separate abstract classes in a hierachy. First an instructor that can have a teaching
load and can respond to become department chair.Teaching assistant will inherit from that.
Then a chairperson class which can become the department chair and should be used
in functions where someone is promoted. This way teaching assistants would throw a
type error in type checking..
"""

from abc import ABC
from typing import List

class Instructor(ABC):
    def schedule_teaching_load(self) -> str:
        return "Teaching load is scheduled"

    def become_department_chair(self) -> str:
        return "Great.  More work, more herding cats, and no more pay"

class ChairPerson(ABC):
    pass


class TeachingAssistant(Instructor):
    def become_department_chair(self) -> str:
        return "I can't be department chair person"

class FullProfessor(Instructor, ChairPerson):
    def become_department_chair(self) -> str:
        return "Damn"

class ContractualInstructor(Instructor, ChairPerson):
    pass



if __name__ == "__main__":
    instructors : List[Instructor] = [FullProfessor(), ContractualInstructor(), TeachingAssistant()]

    instructor : Instructor
    for instructor in instructors:
        print(instructor.become_department_chair())
