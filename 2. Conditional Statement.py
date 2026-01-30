
def number_checker():
    print("\n=== Number Checker ===")
    
   
    try:
        number = float(input("Please enter a number: "))
        
        
        if number > 0:
            print(f"The number {number} is POSITIVE")
        elif number < 0:
            print(f"The number {number} is NEGATIVE")
        else:
            print(f"The number is ZERO")
            
    except ValueError:
        print("Error: Please enter a valid number!")


number_checker()
