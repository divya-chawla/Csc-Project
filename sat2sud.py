#Dryden Linden V00849440 Aug 3 2018 
 
def sat2sud ():
  input = sys.argv
  try: 
	  file = open(input[1],'r')
	  input = file.read().split(' ')
	  file.close()
  except:
	  print("error opening txt file.")
  Matrix = [[0 for z in range(9)] for y in range(9)] 
  
  for line in input:
    if line.find('-', 0) != -1: 
    else  
      Matrix[line[0] -1][line[1] -1] = line[2]
   
  for c < 9:
    for q<9:
      s = s + str(Matrix[q][c])
    s = s + "/n"
    
  print(s)
