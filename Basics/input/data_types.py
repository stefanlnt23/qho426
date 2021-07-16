import time
name = input(" What is your name Boss Man?:")
print (" Hello",name)
age = int(input (" What is your age "+ name+"  :"))

print ("....ok if your are", age," old")
time.sleep(1)
heigh = float(input (" How tall are you in meters? : "))
weight = float(input (" How much do you weigh in kg ? :"))
heigh_square = int(heigh * heigh) 
bmi = int(weight / heigh_square)

print (" You are "+ str(age)+" years old and your BMI is "+str(bmi))

if (bmi>26):
  print (" You are overweighted! try lose some!")
elif (bmi<19):
  print (" You are underweighted ! Get some food boss man!")

else:
  print (" You are healty af!")
