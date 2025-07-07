# Case :-simple contack book


from asyncio.windows_events import NULL


class Contact:
    def __init__(self,name , phone_number , email = None):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def get_info(self):
        return f'name: {self.name}, phone_number: {self.phone_number}, email: {self.email}'

class ContactBook:
    def __init__(self):
       self.contacts = []

    def add_contact(self,name,phone_number, email):
        self.contacts.append(Contact(name, phone_number, email))

    def find_contact(self, name):
       for row in self.contacts:
          if row.name==name:
             return row
          
    def delete_contact(self,name):
        for contact in self.contacts:
          if name == contact.name:
             self.contacts.remove(contact)
             return
          else:
             print(f"Record not found for {name}")

    def list_all_contact(self):
        for contact in self.contacts:
           print(contact.get_info())

    def update_contact(self, name ,updated_name ,updated_number, updated_email):
       for x in self.contacts:
          if x.name.lower() == name.lower():
             if updated_number is not None:
                x.phone_number=updated_number 
             if updated_name is not None:
                x.name = updated_name
             if   updated_email is not None:
                x.email = updated_email 
       
        

#example 1
person = ContactBook()
person.add_contact("Khalid", 111 , "khankhalid")
person.add_contact("sarah", 545213315,"gyjhvcgbdhtdcc")
person.add_contact("Hamza", 9865321,"gyjhvcgbdhtdcc")
person.add_contact("Hassan", 8521047,"gyjhvcgbdhtdcc")

person.update_contact("Khalid","Khan",None, None)

person.list_all_contact()
person.delete_contact("sarah")
sarah=person.find_contact("sarah")



           
        
        