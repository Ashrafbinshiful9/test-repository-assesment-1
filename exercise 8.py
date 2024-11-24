#exercise8

names = ["Ashraf", "harneet", "aryan","rahim","afsar","ali"] 

search_name = input("Enter the name to search: ")


if search_name in names:
    print(f"'{search_name}' name is on the list.")
else:
    print(f"'{search_name}' the name is not found in the list.")