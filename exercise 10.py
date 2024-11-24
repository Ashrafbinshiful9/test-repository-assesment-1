#exercise10

def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


def main():
    number = int(input("Enter a number: ")) 
    result = check_even_or_odd(number)
    print(result)

main()