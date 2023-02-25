while True:
    print("enter the y for yes and N for NO")
    c=input().strip()
    if c=="y":
        print("enter the x,y,M values for y th part of x of weekly income is M")
        M=int(input("enter M value : "))
        x=int(input("enter X value : "))
        y=int(input("enter y value : "))
        print("enter the Z value for zth part of weeklyincome you need ")
        z=int(input("enter z value : "))
        weeklyincome=(M*y)/x
        zthpartofweki=weeklyincome/z
        print("zth part of weeklyincome is",zthpartofweki)
    elif c=="n":
        break
