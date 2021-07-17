print ("What type of adventure should I have?")

type_adventure =  input ()

if ((type_adventure == "scary") or ( type_adventure == "short")):
  print (" Entering the dark forest !")
elif (( type_adventure == "safe") or (type_adventure == "long")):
  print (" Taking the safe route !")
else:
  print (" Not sure wich route to take!")
  