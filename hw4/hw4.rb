
class RegistrarInterface
  def register_for_class
    # a student registers for a given class
  end

  def pay_tuition
    # pay my tuition bill -;(
  end

  def set_instructor_for_class
    # assign an instructor to the nenwly-created course
  end

  def get_enrollment_numbers
    # get the current number of students enrolled in the class
  end

  def get_classroom
    # where is the class being taught?  Ryerson 256?
  end

  def get_my_grade
    # did I make an A?
  end

  def enter_grades
    # record the grades for each student so they may be reported
  end

  def add_class_to_quarter_schedule
    # add a newly created class to the current quarter schedule so students may choose to take it
  end

  def run_class
    # kick off the class for the quarter
  end

  def drop_class_from_quarter_schedule
    # remove the class from the quarterly schedule -- maybe not enough students registered for it?
  end

  def drop_class_from_my_schedule
    # I decided not to take the course, so I'm going to choose to take another class
  end
end

class Student
  def initialize
    @my_schedule = RegistrarInterface.new
  end

  def register_for_class
    puts "Student Josephine is preparing to regiser for a new course that she likes"
    puts "Student is registering for the class"
    @my_schedule.register_for_class
    puts "Seems like this education thing is awfully costly...time to pay tuition again!"
    @my_schedule.pay_tuition
    puts "I'm five minutes late, where the heck is the classroom???"
    @my_schedule.get_classroom
    puts "Course is over.  Whew.  What's my grade???"
    @my_schedule.get_my_grade
  end

  def log
    # at the risk of repeating myself...again...
    puts "Now I'm logging"
  end
end

class Registrar
  def initialize
    @registrar_office = RegistrarInterface.new
  end

  def create_class
    puts "Registrar is preparing to create a new course listing"
    puts "Registrar is adding this new course to the course listing for the quarter"
    @registrar_office.add_class_to_quarter_schedule
    puts "Registrar is setting the instructor for this course"
    @registrar_office.set_instructor_for_class
    puts "Registrar is getting the current number of students registered for the course"
    @registrar_office.get_enrollment_numbers
    puts "The quarter has begun!"
    @registrar_office.run_class
  end

  def log
    # at the risk of repeating myself...again...
    puts "Now I'm logging"
  end
end

class Instructor
  def initialize
    @my_schedule = RegistrarInterface.new
  end

  def teach_class
    puts "Professor Rumplestilskin is preparing to teach a new course"
    puts "Professor is getting the current number of students registered for the course"
    @my_schedule.get_enrollment_numbers
    puts "Professor is wondering where his class is, as he only has five minutes to get there"
    @my_schedule.get_classroom
    puts "Course is over.  Whew.  Now I have to assign grades for my students"
    @my_schedule.enter_grades
  end

  def log
    # at the risk of repeating myself...again...
    puts "Now I'm logging"
  end
end

r = Registrar.new
r.create_class()
r.log()

puts ""

i = Instructor.new()
i.teach_class()
r.log()

puts ""

s = Student.new()
s.register_for_class()
r.log()






