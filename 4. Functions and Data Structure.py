
def calculate_area(length, width):
    """Calculates the area of a rectangle"""
    return length * width

def rectangle_area_program():
    print("\n\n=== Rectangle Area Calculator ===")
    
   
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        
        area = calculate_area(length, width)
        print(f"The area of the rectangle with length {length} and width {width} is: {area}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")


rectangle_area_program()
