print("******AREA CALCULATOR*******")
print(""" PRESS 1 TO GET THE AREA OF THE SQUARE
      PRESS 2 TO GET THE AREA OF THE CIRCLE
      PRESS 3 TO GET THE AREA OF THE RECTANGLE
      PRESS 4 TO GET THE AREA OF REACTANGLE""")
print("-------------------------------------------------------------------------------------------------")
choice=int(input("ENTER YOUR CHOICE FROM 1-4\n"))
if choice==1:
    side=int(input("ENTER THE SQUARE'S SIDE VALUE\t"))
    area=side*side
    print("THE AREA OF THE SQURE is ",area)
elif choice==2:
    radious=int(input("ENTER THE RADIOUS OF THE CIRCLE\t"))
    area=(22/7)*radious**2
    print("THE AREA OF THE CIRCLE IS",area)
elif choice==3:
    length=int(input("ENTER THE LENGHT OF THE RECTANGLE\t"))
    bredth=int(input("ENTER THE BREDTH OF THE RECATNGLE\t"))
    area=length*bredth
    print("THE AREA OF THE RECTANGL IS\t",area)
elif choice==4:
    base=int(input("ENTER THE BASE OF THE TRIANGLE\t"))
    height=int(input("ENTER THE HEIGHT OF THE TRIANGLE\t"))
    area=0.5*height*base
    print("THE AREA OF THE TRIANGLE IS ",area)
else:
    print("invalid choice")
    
print("----------------------------------calculation end here-----------------------------------------")