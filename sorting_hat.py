#Sorting hat quiz!

#Initialize variables
gryffindor = 0 
ravenclaw = 0
hufflepuff = 0
slytherin = 0 

#Introduction message
print("Welcome to the sorting hat quiz!🪄")

#Question 1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer_1 = int(input("Answer: "))
print(" ")

if answer_1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer_1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong input.")
print(" ")

#Question 2
print("Q2) When I'm dead, I want people to remember me")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer_2 = int(input("Answer: "))
print(" ")

if answer_2 == 1:
  hufflepuff += 2
elif answer_2 == 2:
  slytherin += 2
elif answer_2 == 3:
  ravenclaw +=2
elif answer_2 == 4:
  gryffindor += 2
else: 
  print("Wrong input.")
print(" ")

#Question 3
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer_3 = int(input("Answer: "))
print("")

if answer_3 == 1:
  slytherin += 4
elif answer_3 == 2: 
  hufflepuff += 4
elif answer_3 == 3:
  ravenclaw += 4
elif answer_3 == 4:
  gryffindor += 4
else: 
  print("Wrong input.")
print(" ")

#Question 4
print("4) You discover a student is being unfairly blamed for something you know")
print("they didn't do. What do you do?")
print("1) Speak up immediately, even if it gets you in trouble")
print("2) Gather evidence and figure out exactly what happened first")
print("3) Make sure the student knows you'll support them")
print("4) Find the most effective way to expose who actually did it")
answer_4 = int(input("Answer: "))
print(" ")

if answer_4 == 1:
  hufflepuff += 7
elif answer_4 == 2:
  ravenclaw += 7
elif answer_4 == 3:
  slytherin += 7
elif answer_4 == 4:
  gryffindor += 7
else:
 print("Wrong input.")
print("")


#Scoreboard
print("〜˚₊‧꒰ა scoreboard ໒꒱ ‧₊˚〜")
print(f"Slytherin: {slytherin}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Gryffindor: {gryffindor}" )
print(" ")


#Bonus: Print the house with the most points
print("╔═══.·:·.☽✧ ✦ ✧☾.·:·.═══╗")
print("      ☆Scoreboard☆")
if hufflepuff >= 7:
  print("Your house is Hufflepuff! 🦡")
elif ravenclaw >= 7:
  print("Your house is Ravenclaw! 🐦‍⬛")
elif gryffindor >= 7:
  print("Your house is Gryffindor! 🦁")
elif slytherin >= 7:
  print("Your house is Slytherin! 🐍")
print("╚═══.·:·.☽✧ ✦ ✧☾.·:·. ═══╝")