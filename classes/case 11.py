from datetime import date

class Course:
   def __init__(self):
      print("init")

   def setName(self, name):
      self.name = name

   def setFrom_date(self,from_date):
      self.from_date = from_date

   def setTo_date(self,to_date):
      self.to_date = to_date
    
   def print_course(self):
      return f"Course(f'name = {self.name}, from_date = {self.from_date} ,to_date = {self.to_date}')"


def add_course(name, from_date = None, to_date =None): 
   course = Course();
   course.setName(name)
   course.setFrom_date(from_date)
   course.setTo_date(to_date)
   return course 




python=add_course("python", "1jan", "20jan")
java = add_course("java","15","30jan")

print(python.print_course())
print(java.print_course())
