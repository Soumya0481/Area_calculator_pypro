print("******AREA CALCULATOR*******")
while True:
    print(""" PRESS 1 TO GET THE AREA OF THE SQUARE
        PRESS 2 TO GET THE AREA OF THE CIRCLE
        PRESS 3 TO GET THE AREA OF THE RECTANGLE
        PRESS 4 TO GET THE AREA OF TRIANGLE""")
    print("-------------------------------------------------------------------------------------------------")
    choice=int(input("ENTER YOUR CHOICE FROM 1-4\n"))
    if choice==1:
        while True:
            side=int(input("ENTER THE SQUARE'S SIDE VALUE\t"))
            area=side*side
            print("THE AREA OF THE SQURE is ",area)
            repeat=input("Do you contine the sqare are calculation:\t")
            if repeat=="no":
                print("---------------------------------------------------- ")
                break
    elif choice==2:
        while True:
            radious=int(input("ENTER THE RADIOUS OF THE CIRCLE\t"))
            area=(22/7)*radious**2
            print("THE AREA OF THE CIRCLE IS",area)
            repeat=input("Do you contine the CIRCLE are calculation:\t")
            if repeat=="no":
                print("---------------------------------------------------- ")
                break
    elif choice==3:
        while True:
            length=int(input("ENTER THE LENGHT OF THE RECTANGLE\t"))
            bredth=int(input("ENTER THE BREDTH OF THE RECATNGLE\t"))
            area=length*bredth
            print("THE AREA OF THE RECTANGL IS\t",area)
            repeat=input("Do you contine the RECTANGLE are calculation:\t")
            if repeat=="no":
                print("---------------------------------------------------- ")
                break
    elif choice==4:
        while True:
            base=int(input("ENTER THE BASE OF THE TRIANGLE\t"))
            height=int(input("ENTER THE HEIGHT OF THE TRIANGLE\t"))
            area=0.5*height*base
            print("THE AREA OF THE TRIANGLE IS ",area)
            repeat=input("Do you contine the TRIANGLE are calculation:\t")
            if repeat=="no":
                print("---------------------------------------------------- ")
                break
    else:
        print("invalid choice")
    repeatt=input("Do you want the menu agian?")
    if repeatt=="no":
        print("THANK YOU ")
        break
print("----------------------------------calculation end here-----------------------------------------")
