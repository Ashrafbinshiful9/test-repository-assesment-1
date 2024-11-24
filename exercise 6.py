#exercise6
correct_password = "1974"

attempts_left = 5

while attempts_left > 0:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Unlocked ")
        break
    else:
        attempts_left -= 1
        print(f"Wrong password. You have {attempts_left} attempts left.")

if attempts_left == 0:
    print("try again in 5 minutes.")
