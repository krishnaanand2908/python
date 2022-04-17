while(True):
    num1 = int(input("Enter first number:\n"))
    num2 = int(input("Enter second number:\n"))

    if num1 > num2:
        num1, num2 = num2, num1
    for i in range(num1, num1+1):
        if num1%i == 0 and num2%i == 0:
            hcf = i

    print("The HCF of", num1, "and", num2, "is", hcf)
    
    continue