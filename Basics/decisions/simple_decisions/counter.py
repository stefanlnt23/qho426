print (" Please enter the first whole number: ")
 
first_number = int(input())

print (" Please enter the second whole number: ")

second_number= int(input())

print ("Please enter the third whole number:")

third_number = int(input()) 

even_number = 0
odd_number = 0

if (first_number %2 ==0):
  even_number = even_number +1
else:
  odd_number =  odd_number +1

if (second_number %2 ==0):
  even_number =  even_number +1
else:
  odd_number = odd_number +1

  if (third_number % 2 ==0):
    even_number = even_number + 1
  else:
    odd_number=odd_number +1
print (" there were", even_number ,"even numbers and  ", odd_number , " odd numbers ")