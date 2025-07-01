#Student enrollment system

class Student:
    def __init__(self, name, student_id ):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []
    
    def enroll(self, course_name ):
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)
        else:
            print("course is already available in the list")
    
    def drop_course(self, course_name):
        for enrolled_course in self.enrolled_courses:
            if enrolled_course == course_name:
                self.enrolled_courses.remove(course_name)
            else:
                print("cousre is not available")

    def view_course(self):
        print(self.enrolled_courses)





#example = 1
khalid = Student("khalid","N123")
khalid.enroll('bsc')
khalid.drop_course('bsc')
khalid.view_course()

