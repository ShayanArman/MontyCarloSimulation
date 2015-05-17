from Clarabelle import clarabelle
set_range = 100
while(set_range < 105000 ):
	print str(set_range) + ", " + str(clarabelle.claraStats(set_range))
	set_range *= 2