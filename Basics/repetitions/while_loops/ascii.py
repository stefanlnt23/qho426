print ("How many bars should be charged?")
response = int (input (":"))
slave = 0
while (slave < response):
  slave = slave +1
  print ("Charging:","█"*slave,"\t")
print (" Battery fully charged")
