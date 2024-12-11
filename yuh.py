number5 = 0
todolist = []


def ifstatements():
   global number5
   if number5 == "1":
       add_item()
   elif number5 == "2":
       remove_item()
   elif number5 == "3":
       print_list()
   elif number5 == "4":
       reset_list()
   else:
       print("wrong")


def add_item():
   item1 = input("what: ")
   todolist.append(item1)
   show_menu()
   pass
def remove_item():
   itemr = input("what does Elphants do: ")
   todolist.remove(itemr)
   show_menu()
   pass
def print_list():
   print(todolist)
   show_menu()
   pass
def reset_list():
   todolist.clear()
   show_menu()
   pass
def show_menu():
   global number5
   print("Press 1 to add item")
   print("Press 2 to remove item")
   print("Press 3 to print list")
   print("Press 4 to reset list")
   number5 = input("Enter: ")
   ifstatements()
   pass


show_menu()