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

def CNFpos(x, y, z):
	sa = ""
	for p in range(10):
		if(p > 0):
					for i in range(p+1, 10):
						sa = sa +"-"+str(x+1)+str(y+1)+str(p)+" -"+str(x+1)+str(y+1)+str(i)+" 0\n"
	return(sa);	

def CNFrow(x, y, value):
	sr = ""
	for t in range(1,10):
		if(t != y+1):
			sr = sr + "-"+str(x+1)+str(y+1)+str(value)+" -"+str(x+1)+str(t)+str(value)+" 0\n"

	return sr
def CNFcol(x, y, value):
	sc = ""
	for c in range(1,10):
		if(c != x+1):
			sc = sc + "-"+str(x+1)+str(y+1)+str(value)+" -"+str(c)+str(y+1)+str(value)+" 0\n"

	return sc
def CNFbox(x, y, value):	
	if(x < 3):
		if(y < 3):
			return(grid1(1,4,1,4,x,y, value))
		if(y < 6):
			return(grid1(1,4,4,7,x,y, value))
		else:
			return(grid1(1,4,7,10,x,y, value))
	if(x < 6):
		if(y < 3):
			return(grid1(4,7,1,4,x,y, value))
		if(y < 6):
			return(grid1(4,7,4,7,x,y, value))
		else:
			return(grid1(4,7,7,10,x,y, value))
	else:
		if(y < 3):
			return(grid1(7,10,1,4,x,y, value))
		if(y < 6):
			return(grid1(7,10,4,7,x,y, value))
		else:
			return(grid1(7,10,7,10,x,y, value))
	return
def grid1(s1,f1,s2,f2,x,y,value):
	sg = ""
	for i in range(s1,f1):
		for j in range(s2,f2):
			if(i != x+1 and j != y+1):
				sg = sg+ "-"+str(x+1)+str(y+1)+str(value)+" -"+str(i)+str(j)+str(value)+" 0\n"
	return sg

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
count = 0
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

else:
	lines = re.findall('.........?', x[0])

puzzle = [[[ 1 for col in range(10)]for col in range(10)]for col in range(10)]
def sud2sat():
	count = 0
	for x in range(9):
		number = re.findall('.', lines[x])
		for y in range(9):
			if(check(number[y])):
				i = int(number[y])
				puzzle[x][y][0] = i;
				mark(i,x,y)
			else:
				count = count + 1
				puzzle[x][y][0] = 0;

	try:
		file = open('CNF.txt', 'w')
		file.write("p cnf 17577 729 \n") 
		
	except:
		print("error opening txt file.")
	for x in range(9):
		for y in range(9):
			so = ""
			for z in range(10):
				if(z == 0 and puzzle[x][y][z] != 0):
					so = str(x+1)+str(y+1)+str(puzzle[x][y][z])
					so = so + " 0\n"
					count = count + 1
					break;
				elif(z == 9): 
					if(puzzle[x][y][z] == 1):
						so = so + str((x+1))+str(y+1)+str(z)
						so = so + " 0\n"
					else:
						so = so +str(x+1)+str(y+1)+str(z)
						so = so + " 0\n"
				elif(z > 0): 
					if(puzzle[x][y][z] == 1):
						so = so + str((x+1))+str(y+1)+str(z)
						so = so + " "
					else:
						so = so + str(x+1)+str(y+1)+str(z)
						so = so + " "
			file.write(so)
			file.write(CNFpos(x,y,z))

## write now it says it can be 1 or 2 or 3 .. etc now I need to say that
## for each row, column and box, if its 111 then nothing in row box or column can be
## if its 112 nothing in that row, box, or columns could be etc.
			for p in range(10):
				if(p > 0 ):
					file.write(CNFrow(x,y,p))
					# mark all things in xyp row can't be p
					file.write(CNFcol(x,y,p))
					# mark all things in xyp col can't be p
					file.write(CNFbox(x,y,p))
					# mark all things in xyp box can't be p

	
	file.close()
	cmd = 'minisat CNF.txt SatOutput.txt'
	os.system(cmd)
sud2sat()
