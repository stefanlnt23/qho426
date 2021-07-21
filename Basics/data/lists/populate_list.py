
def directions():
  directions =["Move Forward","Move backwards","Turn Left","Turn Right"]
  return directions

  

def menu():
  print ("Please select a direction")
  direction = directions()
  i = 0 
  for something in direction:
    print (f"{i}:{something}")
    i +=1
  response = int(input())
  if response >3 or response <0:
    return "wrong direction provided!"
  else:
    return direction [response]
def run ():
  route = list()
  print (" Working out escape route...")
  for i in range(5):
    route.append(menu())
  print (f"Escape route: {route}")


run()
