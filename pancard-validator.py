# panCard= input("Please write down valid pan card number\n");
panCard = 'ABCJK4953L'

# Task 1: Accepts a string representing a 10-digit PAN number as an argument.

if(len(panCard) != 10):
    print("Invalid pan card");
    exit();

# Task 2:Extracts the 4th character of the PAN number.

categoryIdentifier = panCard[3]
print(categoryIdentifier)
    
# Task 3:Uses conditional statements (e.g., if-elif-else) to determine the corresponding PAN category based on the 4th character.

def panCategory():
    category='';
    if(categoryIdentifier == 'P'):
        category ='Individual';
    elif(categoryIdentifier == 'H'):
       category ='Hindu Undivided family';
    elif(categoryIdentifier=='C'):
       category ='Company';
    elif(categoryIdentifier == "F"):
       category =" Firm ";
    elif(categoryIdentifier ==  "T"):
       category ="trust";
    elif(categoryIdentifier == "A"):
       category =" Association of Persons";
    elif(categoryIdentifier == "B"):
       category =" Body of Individual";
    elif(categoryIdentifier == "L" ):
       category =" Local Authority";
    elif(categoryIdentifier == "J"):
       category =" Artificial Juridical Person";
    return category; 

print(f'{panCard} is of {panCategory()}')

print('Program completed')