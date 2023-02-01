print("Welcome Deborah")
answer_1 = input("Do you choose the red door or the white door?>")
if answer_1 == "Red":
  print("You've been eaten by a monster. The End.")
elif answer_1 == "White":
  print("Congratulations you've moved on to the next stage")
  answer_2 = input("You've found a red door and a white door, which way to go now? ")
  if answer_2 == "White":
    print("You've been eaten by a monster. The End.")
  elif answer_2 == "Red":
    print("You've found a chest of treasure. Enjoy your victory.")
  else:
   print("Choose a valid option")
else:
  print("Choose a valid option")
