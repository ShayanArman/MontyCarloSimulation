import random as r

DATA_SET_SIZE = 100

# Cow starts in the center, eats the grass
# 20 minutes later, it moves to another square:
# If that square hasn't been eaten, you eat the grass
# If it has been eaten, you don't eat the grass

def letBernaRoam(Matrix, start_position):
	position = start_position
	Matrix[position[0]][position[1]] = 0 # A block of 1 eats the grass
	total_grass_eaten = 1.00
	cycles_count = 0
	matrix_width = len(Matrix)
	percentage_eaten = 100.0 * total_grass_eaten / (matrix_width**2.0)
	while(percentage_eaten < 50):
		cycles_count += 1
		#newPosition
		position = getNextPosition(Matrix, position)
		#Eat the grass
		grass_avail = Matrix[position[0]][position[1]]
		
		if grass_avail: # if there is still grass, then remove the grass
			Matrix[position[0]][position[1]] = 0
			total_grass_eaten += 1
			percentage_eaten = 100.0 * total_grass_eaten / (matrix_width**2.0)
	return (cycles_count)/3.0

def letBernaDie(Matrix, start_position):
	starvation_period = 24*3
	total_time_to_die = 0
	rest_periods = 0
	position = start_position
	Matrix[position[0]][position[1]] = 0 # A block of 1 eats the grass
	matrix_length = len(Matrix)
	while(rest_periods != starvation_period):
		total_time_to_die += 1
		#newPosition
		position = getNextPosition(Matrix, position)
		#Eat the grass
		grass_avail = Matrix[position[0]][position[1]]
		
		if(grass_avail):
			rest_periods = 0
		else:
			rest_periods += 1

		if grass_avail: # if there is still grass, then remove the grass
			Matrix[position[0]][position[1]] = 0
	return (total_time_to_die)/3.0

def bernaStats(set_range):
	grass_eaten_sum = 0
	for x in xrange(set_range):
		Matrix = [[1 for x in xrange(11)] for x in xrange(11)]
		grass_eaten_sum += letBernaRoam(Matrix, [5,5])
	return grass_eaten_sum / set_range

def timeToDeath(set_range):
	time_to_death = 0
	for x in xrange(set_range):
		Matrix = [[1 for x in xrange(11)] for x in xrange(11)]
		time_to_death += letBernaDie(Matrix, [5,5])
	return time_to_death / set_range

def randFromWeightedChoices(choices):
   total = sum(w for c, w in choices.iteritems())
   uni = r.uniform(0, total)
   upto = 0
   for c, w in choices.iteritems():
      if upto + w >= uni:
         return c
      upto += w
   assert False, "Shouldn't get here"	

def findWeightedChoice(Matrix, current_position, choice_set):
	choice_weight_dict = {}
	for choice in choice_set:
		new_pos = nextPos(current_position, choice)
		# Available grass space gets higher weight
		choice_weight_dict[choice] = Matrix[new_pos[0]][new_pos[1]] + 1
	return randFromWeightedChoices(choice_weight_dict)

def getNextPosition(Matrix, current_position):
	if not isEdge(current_position):
		next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [x for x in xrange(8)]))

	else:
		if not isCorner(current_position):
			# Current position of Bernadette is on the outer wall of the pen
			#TOP 
			if(current_position[0] == 0):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [2,3,4,5,6]))
			#LEFT
			elif(current_position[1] == 0):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [0,1,2,3,4]))
			#RIGHT
			elif(current_position[1] == 10):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [0,4,5,6,7]))
			#BOTTOM
			elif(current_position[0] == 10):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [0,1,2,6,7]))
		else:
			# Do corner stuff
			#TOP_LEFT
			if(current_position == [0,0]):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [2,3,4]))
			#TOP_RIGHT
			elif(current_position == [0,10]):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [4,5,6]))
			#BOTTOM_LEFT
			elif(current_position == [10,0]):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [0,1,2]))
			#BOTTOM_RIGHT
			elif(current_position == [10,10]):
				next_position = nextPos(current_position,findWeightedChoice(Matrix, current_position, [0,6,7]))
	return next_position

def nextPos(pos,num):
	new_position = pos[:]
	if(num==0): # Bernadette move up
		new_position[0] -= 1
	elif(num==1): # Bernadette move top right
		new_position[0] -= 1
		new_position[1] += 1
	elif(num==2): # Bernadette move right
		new_position[1] += 1
	elif(num==3): # Bernadette move bottom right
		new_position[0] += 1
		new_position[1] += 1
	elif(num==4): # Move down
		new_position[0] += 1
	elif(num==5): # Move bottom left
		new_position[0] += 1
		new_position[1] -= 1
	elif(num==6): # Move left
		new_position[1] -= 1
	elif(num==7): # Move top left
		new_position[0] -= 1
		new_position[1] -= 1
	return new_position # ToDO: incorporate default movement

def isEdge(pos):
	if(abs(pos[0]-5)==5 or abs(pos[1]-5)==5):
		return True
	else:
		return False

def isCorner(pos): # ToDo: Easier way to find corner?
	posSum = pos[0]+pos[1]
	if(posSum==20 or posSum == 0 or pos ==[10,0] or pos == [0,10]):
		return True
	else:
		return False 