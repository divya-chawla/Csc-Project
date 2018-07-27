import sys
import os
import re

def grid(s,x,t, y, value):
	for i in range(s,x):
		for j in range(t,y):
			puzzle[i][j][value] = 0

def mark(value, x, y):
	for k in range(9):
		puzzle[x][k][value] = 0
		puzzle[k][y][value] = 0
	if(x < 3):
		if(y < 3):
			grid(0,3,0,3, value)
		if(y < 6):
			grid(0,3,3,6, value)
		else:
			grid(0,3,6,9, value)
	if(x < 6):
		if(y < 3):
			grid(3,6,0,3, value)
		if(y < 6):
			grid(3,6,3,6, value)
		else:
			grid(3,6,6,9, value)
	else:
		if(y < 3):
			grid(6,9,0,3, value)
		if(y < 6):
			grid(6,9,3,6, value)
		else:
			grid(6,9,6,9, value)

def check(str):
	if str == '0':
		return False
	if str == '*':
		return False
	if str == '.':
		return False
	if str == '?':
		return False
	return True


x = sys.argv
try: 
		file = open(x[1],'r')
		x = file.read().split('\n')
		file.close()
except:
		print("error opening txt file.")

if(len(x[0]) == 0):
	print("No Input Provided.")
	exit()

if(len(x) == 9):
	lines = x
	print lines

else:
	lines = re.findall('.........?', x[0])

puzzle = [[[ 1 for col in range(10)]for col in range(10)]for col in range(10)]
def sud2sat():
	for x in range(9):
		number = re.findall('.', lines[x])
		for y in range(9):
			if(check(number[y])):
				i = int(number[y])
				puzzle[x][y][0] = i;
				mark(i,x,y)
			else:
				puzzle[x][y][0] = 0;

	try:
		file = open('CNF.txt', 'w')
		file.write("p cnf 9 81 \n") 
		
	except:
		print("error opening txt file.")
	for x in range(9):
		for y in range(9):
			so = ""
			for z in range(10):
				if(z == 0 and puzzle[x][y][z] != 0):
					so = str(puzzle[x][y][z])
					so = so + " 0\n"
					break;
				elif(z == 9): 
					if(puzzle[x][y][z] == 1):
						so = so + str(-z)
						so = so + " 0\n"
					else:
						so = so + str(z)
						so = so + " 0\n"
				elif(z > 0): 
					if(puzzle[x][y][z] == 1):
						so = so + str(-z)
						so = so + " "
					else:
						so = so + str(z)
						so = so + " "
			file.write(so)		
	file.close()
	cmd = './minisat CNF.txt SatOutput.txt'
	os.system(cmd)
sud2sat()
