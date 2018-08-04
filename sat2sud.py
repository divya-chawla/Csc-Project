import re
import sys
import os

def sat2sud (bubble):
  try: 
    file = open(bubble[1],'r')
    intake = file.read()
    intake = intake[3:]
    file.close()
  except:
    print("error opening txt file.")
  Matrix = [[0 for z in range(9)] for y in range(9)] 
  
  for line in intake.split(" "):
    if(int(line) == 0):
      break
    if (line.find('-', 0) == -1): 
      Matrix[int(line[0])-1][int(line[1]) -1] = int(line[2])
  s = ""   
  for c in range(9):
    for q in range (9):
      s = s + str(Matrix[q][c])
    s = s + "\n"
    
  print(s)

bubble = sys.argv
sat2sud(bubble)
