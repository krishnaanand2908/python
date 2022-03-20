
name = input("Your full name: ")

sex = input("Your Sex[M]/[F]: ")
    
age = int(input("Age(in numbers):"))

colour = input("You favourite colour:")
    
email = input("Your Email:")

mname = input('What is the name of your mother? =>')

fname = input('What is the name of your father? =>')

if sex == "F":
    a = input("What's your husband's name")
    
elif sex == "M":
    b = input("What's your wifes name?")
    
else:
    c = input("What's your partner's name?")
    
siblings = int(input("How many siblings do you have?"))

if siblings == 0:
     d = input("No problem. Can I be your sibling?[YES/NO]")
     
else:
    d = input("Nice, will you be my friend? [YES/NO]")

if sex == 'M':
    print('Nice to meet you Mr.', name)
    
elif sex == 'F':
    print('Nice to meet you Miss.', name)
    
else:
    print('Nice to meet respected', name)

print("So you are", age, 'years old.')

print("You like", colour, "colour.")

print("Hence,", mname, "is your mother and", fname, "is your father.")

if sex == "F":
    print("It seems that Mr.", a, "is your husband")
    
elif sex == "M":
    print("It seems that Mrs.", b, "is your wife." )
    
else:
    print("It seems that your partner's name is", c, ".")
    
if d == "YES":
    print("Hello my buddy!")
    
elif d == "NO":
    print("No problem... :(")
    
else:
    print("WHAT?")
    
if d == "YES":
    print("Hello my new friend. Am I your sibling? You knows this very well.")
    
elif d == "NO":
    print("OKAY... BUt am I your sibling? I think you knows this... :(")
    
else:
    print("WHAT!?")
    
    

    


print("Dont worry, we will meet again soon. I will send an email on", email)

    
