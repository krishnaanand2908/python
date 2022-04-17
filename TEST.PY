def getdate():
    import datetime
    return datetime.datetime.now()
n=int(input("Enter your choice 1 for siddhartha 2 for kavita and 3 for abhishek\n"))
if n==1 :
    print("You have selected siddhartha\n")
    k=input("Enter 'a' for Exercise And 'b' for Diet\n")
    if k=='a':
        print("You have chosen Exercise\n")
        with open("sid.txt","w") as f:
            t=input("What you have done in exercise\n")
            hour = str(datetime.datetime.now().hour)
            min = str(datetime.datetime.now().minute)
            print(f.write(t))
            print(f.write(hour))
            print(f.write(":"))
            print(f.write(min))

