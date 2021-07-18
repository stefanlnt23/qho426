
print("What level of brightness is required?","\n" * 1)


level = int(input(">>>:"))


for variable in range (1,level,2):
  print ("Beep's brightness level:","*" * variable )
  print ("Bop's brightness level: ", "*" * variable,"\n" * 2 )


print (" Adjustment completed")