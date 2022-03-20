print("SURVEY TEST 2")

name = input("Your Name:")

age = int(input("What's your age? =>"))

sex = input("Your sex[M/F]:")

mrd = input("Are you marrid(M) or Unmarrid(U)? =>")

ride = input("Your favourite mode of transport [NOTE: The name of your ride should be in one word and the first letter must be capital. For walk you can use Foot.]:")

agroup = input("What's your age group? for Baby= B, for Child= C, for Teenage= T, for pre- adult= P, for Adult=A and for Old age= O. =>")

bgroup = input("Your Blood Group:")

if sex == 'M':
    if mrd == "M":
        print("Nice to meet you Mr.", name, ".")
        
    else:
        print("Nice to meet you respected", name, ".")
        
elif sex == 'F':
    if mrd == "M":
        print("Nice to meet you Mrs.", name, ".")
        
    else:
        print("Nice to meet you respected", name, ".")
        
elif sex == 'F':
    if mrd == "U":
        print("Nice to meet you Miss.", name, ".")
        
    else:
        print("Nice to meet you respected", name, ".")
        
else:
    print("I didn't understand your name.")
        
print("It seems that you are", age, "years old.")

if ride == "Cycle":
    print("Cycling is good for health :)")
    
elif ride == "Bike":
    print("Okay, but bike increases air pollution and it also causes noise pollution ;)")
    
elif ride == "Scooty":
    print("My mother also uses scooty and she have issues in breathing and joint pain :(")
    
elif ride == "Foot":
    print("Walking is good for health |:)")
    
else:
    print("hmmm, so you like", ride, "as a mean of transport.")
    
if agroup =="B":
    print("SO CUTE (:O")

elif agroup == "C":
    print("Hi Kid")
    
elif agroup == "T":
    if sex == "M":
        print("Hi bro!")
        
    else:
        print("Hi sis!")
    
    
elif agroup == "P":
    print("You are older than me :(")
    
elif agroup == "A":
    if sex == "M":
        print("I am a good kid Sir.")
        
    else:
        print("I am a good kid Mam.")
        
else:
    print("Live a happy old age :)")
    
print("You are", bgroup, "and I am O+")

print("I HOPE YOU LIKE THIS SURVEY :)")     

        

    
    
      