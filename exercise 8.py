#exercise8
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] 

search_name = input("Enter name to search: ")

if search_name in names:
    print("'" + search_name + "' name is on the list.")
else:
    print("'" + search_name + "' name is not in the list.")
