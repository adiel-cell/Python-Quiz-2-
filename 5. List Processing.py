
def number_sorter():
    print("\n=== Five Number Sorter ===")
    
    numbers = []  
    
    print("Please enter five numbers:")
    
    
    for i in range(5):
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)  
        except ValueError:
            print("Invalid input! Please enter a number.")
            return
    
    
    print(f"\nOriginal list: {numbers}")
    
    
    numbers.sort(reverse=True)
    
   
    print(f"Sorted from highest to lowest: {numbers}")
    
    
    print("\nSorted numbers:")
    for i, num in enumerate(numbers, 1):
        print(f"{i}. {num}")


number_sorter()
