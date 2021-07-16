#for number in range(1, 10):
 #   if(number % 2 != 0): 
  #      print(number)





# THE RESULTS WILL BE :
# 1,3,5,7,9- 2 IN 1 CANNOT BE POSSIBLE AS THE %2 IS BIGGER THAN 1, 3 % 2 WILL GIVE A REMAINDER OF 1 SO NUMBER IS NOT EQUAL TO 0 LIKE WANTED IN THE ECUATION ETC..

number = int(input (" Please enter a whole number: "))
if (number % 2 !=0):
  print (" Your number is odd")
else:
  print ("Your number", number," is whole! good job!")