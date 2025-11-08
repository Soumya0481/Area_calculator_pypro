print("****** AREA CALCULATOR *******")

while True:
    print("""
PRESS 1 TO GET THE AREA OF A SQUARE
PRESS 2 TO GET THE AREA OF A CIRCLE
PRESS 3 TO GET THE AREA OF A RECTANGLE
PRESS 4 TO GET THE AREA OF A TRIANGLE
""")
    print("------------------------------------------------------------------")
    
    choice = int(input("ENTER YOUR CHOICE FROM 1-4: "))

    if choice == 1:
        while True:
            side = float(input("ENTER THE SIDE OF THE SQUARE: "))
            area = side * side
            print("THE AREA OF THE SQUARE IS:", area)
            
            repeat = input("Do you want to continue Square area calculation? (yes/no): ").lower()
            if repeat == "no":
                print("----------------------------------------------------")
                break

    elif choice == 2:
        while True:
            radius = float(input("ENTER THE RADIUS OF THE CIRCLE: "))
            area = (22/7) * radius ** 2
            print("THE AREA OF THE CIRCLE IS:", area)
            
            repeat = input("Do you want to continue Circle area calculation? (yes/no): ").lower()
            if repeat == "no":
                print("----------------------------------------------------")
                break

    elif choice == 3:
        while True:
            length = float(input("ENTER THE LENGTH OF THE RECTANGLE: "))
            breadth = float(input("ENTER THE BREADTH OF THE RECTANGLE: "))
            area = length * breadth
            print("THE AREA OF THE RECTANGLE IS:", area)
            
            repeat = input("Do you want to continue Rectangle area calculation? (yes/no): ").lower()
            if repeat == "no":
                print("----------------------------------------------------")
                break

    elif choice == 4:
        while True:
            base = float(input("ENTER THE BASE OF THE TRIANGLE: "))
            height = float(input("ENTER THE HEIGHT OF THE TRIANGLE: "))
            area = 0.5 * base * height
            print("THE AREA OF THE TRIANGLE IS:", area)
            
            repeat = input("Do you want to continue Triangle area calculation? (yes/no): ").lower()
            if repeat == "no":
                print("----------------------------------------------------")
                break

    else:
        print("❌ Invalid Choice! Please select between 1-4")
        print("----------------------------------------------------")

    repeat_menu = input("Do you want to display the menu again? (yes/no): ").lower()
    if repeat_menu == "no":
        print("✅ THANK YOU FOR USING AREA CALCULATOR!")
        break

print("----------- Calculation End Here -----------")


