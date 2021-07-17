import time
print ("How many live cables must I avoid?")
number = int(input(":"))
cables = 0

while (cables < number):
  cables = cables + 1
  time.sleep(1)
  print ("Avoiding...Done!",cables, end=" Cable avoided" "\n")
  
print (" All live cables have been avoided")