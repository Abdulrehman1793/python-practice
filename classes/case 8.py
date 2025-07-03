# Case 8:- To Do List

class ToDoList:
    def __init__(self):
        self.task = []
        self.description = True
    
    def add_description(self, description):
            if description  not in self.task:
                self.task.append(description)
                print(f'{description}, is now added')
            else:
                print(f'{description}, is already added')

    def mark_complete(self ,description):
             if description in self.task:
                    self.description = True
                    print(f'{description}, is now completed')
             else:
                    self.description = False
                    print(f'{description}, not completed')
    def Delete_task(self, description):
            if description in self.task:
               self.task.remove(description)
               print(f'{description}, is remove')
            else:
             print(f'{description} is not in the list')
            
    
    def view_task(self):
          print(f'{self.task}')
          
        
            
#example 1              
khalid = ToDoList()
khalid.add_description("shopping")
khalid.add_description("playing")
khalid.add_description("shopping")
khalid.mark_complete("shopping")
khalid.Delete_task("playing")
khalid.view_task()

#example  2
sarah = ToDoList()
sarah.add_description("playing")
sarah.add_description("studying")
sarah.add_description("painting")
sarah.mark_complete("playing")
sarah.mark_complete("painting")
sarah.Delete_task("studying") 
sarah.view_task()