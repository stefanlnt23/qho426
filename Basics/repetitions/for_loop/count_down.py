print ("How far are we from the cave?")

distance = int(input(":"))


print()


for count in range (distance,0, -1,):
  print (count,"steps remaining")

print (" We have reached the cave boss man")


#range(1, 10, 1) produces the following list of numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9 (natural numbers)



#range(1, 10, 2) produces the following list of numbers: 1, 3, 5, 7, 9 (odd numbers)



#range(0, 10, 2) produces the following list of numbers: 0, 2, 4, 6, 8 (even numbers)