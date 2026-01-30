
def even_numbers():
    print("\n=== Even Numbers from 1 to 20 ===")
    
    
    print("Using for loop:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, end=" ")
    
    print("\n\nUsing while loop:")
   
    i = 1
    while i <= 20:
        if i % 2 == 0:
            print(i, end=" ")
        i += 1


even_numbers()
