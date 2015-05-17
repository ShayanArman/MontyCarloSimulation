import random as r

DATA_SET_SIZE = 100

# Cow starts in the center, eats the grass
# 20 minutes later, it moves to another square:
# If that square hasn't been eaten, you eat the grass
# If it has been eaten, cow doesn't eat the grass
def letClaraRoam(Matrix, start_position):
	position = start_position
	Matrix[position[0]][position[1]] = 0 # A block of 1 eats the grass
	total_grass_eaten = 1
	matrix_length = len(Matrix)
	for x in xrange(144):
		#newPosition
		position = getNextPosition(position)
		#Eat the grass
		grass_avail = Matrix[position[0]][position[1]]
		
		if grass_avail: # if there is still grass, then remove the grass
			Matrix[position[0]][position[1]] = 0
			total_grass_eaten += 1
	return 100 * total_grass_eaten / (matrix_length**2.0)

def letClaraDie(Matrix, start_position):
	starvation_period = 24*3
	total_time_to_die = 0
	rest_periods = 0
	position = start_position
	Matrix[position[0]][position[1]] = 0 # A block of 1 eats the grass
	matrix_length = len(Matrix)
	while(rest_periods != starvation_period):
		total_time_to_die += 1
		#newPosition
		position = getNextPosition(position)
		#Eat the grass
		grass_avail = Matrix[position[0]][position[1]]
		
		if(grass_avail):
			rest_periods = 0
		else:
			rest_periods += 1

		if grass_avail: # if there is still grass, then remove the grass
			Matrix[position[0]][position[1]] = 0
	return (total_time_to_die)/3.0

def claraStats(set_range):
	grass_eaten_sum = 0
	for x in xrange(set_range):
		Matrix = [[1 for x in xrange(11)] for x in xrange(11)]
		grass_eaten_sum += letClaraRoam(Matrix, [5,5])
	return grass_eaten_sum / set_range

def timeToDeath(set_range):
	time_to_death = 0
	for x in xrange(set_range):
		Matrix = [[1 for x in xrange(11)] for x in xrange(11)]
		time_to_death += letClaraDie(Matrix, [5,5])
	return time_to_death / set_range		

def getNextPosition(current_position):
	if not isEdge(current_position):
		next_position = nextPos(current_position,r.randrange(8))
	else:
		if not isCorner(current_position):
			# Current position of Clarabelle is on the outer wall of the pen
			# TODO: # Change r.choice to r.random
			#TOP 
			if(current_position[0] == 0):
				next_position = nextPos(current_position,r.choice([2,3,4,5,6]))
			#LEFT
			elif(current_position[1] == 0):
				next_position = nextPos(current_position,r.choice([0,1,2,3,4]))
			#RIGHT
			elif(current_position[1] == 10):
				next_position = nextPos(current_position,r.choice([0,4,5,6,7]))
			#BOTTOM
			elif(current_position[0] == 10):
				next_position = nextPos(current_position,r.choice([0,1,2,6,7]))
		else:
			# Do corner stuff
			#TOP_LEFT
			if(current_position == [0,0]):
				next_position = nextPos(current_position,r.choice([2,3,4]))
			#TOP_RIGHT
			elif(current_position == [0,10]):
				next_position = nextPos(current_position,r.choice([4,5,6]))
			#BOTTOM_LEFT
			elif(current_position == [10,0]):
				next_position = nextPos(current_position,r.choice([0,1,2]))
			#BOTTOM_RIGHT
			elif(current_position == [10,10]):
				next_position = nextPos(current_position,r.choice([0,6,7]))
	return next_position

def nextPos(pos,num):
	if(num==0): # Clarabelle move up
		pos[0] -= 1
	elif(num==1): # Clarabelle move top right
		pos[0] -= 1
		pos[1] += 1
	elif(num==2): # Clarabelle move right
		pos[1] += 1
	elif(num==3): # Clarabelle move bottom right
		pos[0] += 1
		pos[1] += 1
	elif(num==4): # Clarabelle move down
		pos[0] += 1
	elif(num==5): # Clarabelle move bottom left
		pos[0] += 1
		pos[1] -= 1
	elif(num==6): # Clarabelle move left
		pos[1] -= 1
	elif(num==7): # Clarabelle move top left
		pos[0] -= 1
		pos[1] -= 1
	return pos

def isEdge(pos):
	if(abs(pos[0]-5)==5 or abs(pos[1]-5)==5):
		return True
	else:
		return False

def isCorner(pos):
	posSum = pos[0]+pos[1]
	if(posSum==20 or posSum == 0 or pos ==[10,0] or pos == [0,10]):
		return True
	else:
		return False