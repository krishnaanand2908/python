game = input("Which digital multiplayer game you frequently play? I frequently plays ")
print("Wow! What a coincedience! I also plays", game, ".")

name = input("What's your in-game name? ")
print(
    "Okay...So your in-game name is",
    name,
    ". I am going to send you the friend request.",
)

friend = input(
    "My in-game name is Mr.Python. Can you plz accept my friend request in that game?"
)


if friend == "yes":
    print("Thank you very much for this.")
else:
    print("Ok no problem.")
