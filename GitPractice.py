toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

def deleteItem(item):  
   toDoList.remove(item)
   return toDoList
elif print("error")



    

userAns = input("Do you want to add to your list, delete an item or quit? A/D/Q")
if userAns == "A":

   item = input("What item do you want to add?")
   addItem(item)
   userAns = input("Do you want to add to your list, delete an item or quit? A/D/Q")
if userAns == "D":
   item = input("What item do you want to delete")
   deleteItem(item)
   userAns = input("Do you want to add to your list, delete an item or quit? A/D/Q")
   
   
   
  
  
   
   



