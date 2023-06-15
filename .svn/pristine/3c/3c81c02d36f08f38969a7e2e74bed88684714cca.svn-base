from typing import List
from classes import Course, Restriction, Student, CourseController, RestrictionException, OverloadException, RegistrationClosedException, Lab


def test_get_course_details():
    expected_details : dict = {}
    course : Course = Course(expected_details)
    assert expected_details == course.get_details()

def test_get_student_details():
    expected_details : dict = {}
    student : Student = Student(expected_details)
    assert expected_details == student.get_details()

def test_student_registers():
    course : Course = Course()
    student : Student = Student()
    student.register(course)
    assert course in student.course_load

def test_student_registers_with_restrictions():
    with pytest.raises(RestrictionException) as e:
        course : Course = Course()
        restriction : Restriction = Restriction()
        student : Student = Student()
        student.add_restriction(restriction)
        student.register(course)

def test_student_registers_with_overload():
    with pytest.raises(OverloadException) as e:
        course : Course = Course()
        student : Student = Student(course_limit=0)
        student.register(course)

def test_student_registers_for_closed_class():
    with pytest.raises(RegistrationClosedException) as e:
        course : Course = Course()
        course.closed = True
        student : Student = Student()
        student.register(course)

def test_get_course_by_id():
    course : Course = Course(1)
    course_controller : CourseController = CourseController()
    assert course == course_controller.get_course_by_id(1)

def test_get_course_labs():
    course : Course = Course(1)
    lab : Lab = Lab(1)
    course_controller : CourseController = CourseController()
    assert lab == course_controller.get_course_labs(course.id)


def test_student_drops_course():
    course : Course = Course(1)
    student : Student = Student()
    student.register(course)
    student.drop_course(1)
    assert course not in student.course_load
