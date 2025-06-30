#case 4:- Library book management
class LibraryBookManagement :
   def __init__(self, title, author):
       self.title = title
       self.author = author
       self.is_available = True

   def borrow(self):
        if self.is_available == True:
          print("successfully borrowed the book")
          self.is_available = False
        else:
            print("book is unavailable")

   def get_return(self):
       if self.is_available == True:
           print("the books is not available")
       else:
           self.is_available=True
           print("success")

   def get_status(self):
      if self.is_available == True:
         print("available")
         return
      else:
       self.is_available == False
       print("not available")
       return



       
#example 1
khalid = LibraryBookManagement("story","xyz")
khalid.borrow()
khalid.get_return()
khalid.borrow()
khalid.get_status()



#example 2 
madiha = LibraryBookManagement("novels","abc")
madiha.borrow()
madiha.get_return()
madiha.get_status()