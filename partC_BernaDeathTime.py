from Bernadette import bernadette

set_range = 100
while(set_range < 105000 ):
	print str(set_range) + ", " + str(bernadette.timeToDeath(set_range))
	set_range *= 2