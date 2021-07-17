print ("How many live cables must I avoid?")
number = int(input(":"))
cables = 0

while (cables < number):
  cables = cables + 1
  print ("Avoiding...Done!",end=" avoided")
  
print (" All live cables have been avoided")