check_str = [[16456,2084555,35840,1175260,35844,1175356],
[36136,1174975,36146,1174975,1100038,1101183],
[999589,1011623,1010086,1011135,76218,1043903],
[1106904,1114107,24961,2097151,999590,1011631],
[999572,1011639,1000582,1011639,1009922,1011199],
[35073,1175039,16392,2084719,16384,2094716]];

check_flag = [115,86,127,18,22,106]
for i in xrange(0,6):
	x = list(' '*4)
	for x[0] in xrange(32,128):
		for x[1] in xrange(32,128):
			a = int(bin(x[0])[2:])&int(bin(x[1])[2:])
			b = int(bin(x[0])[2:])|int(bin(x[1])[2:])
			if a == check_str[i][0]:
				if b == check_str[i][1]:
					for x[2] in xrange(32,128):
						a = int(bin(x[1])[2:])&int(bin(x[2])[2:])
						b = int(bin(x[1])[2:])|int(bin(x[2])[2:])
						if a == check_str[i][2]:
							if b == check_str[i][3]:
								for x[3] in xrange(32,128):
									a = int(bin(x[2])[2:])&int(bin(x[3])[2:])
									b = int(bin(x[2])[2:])|int(bin(x[3])[2:])
									if a == check_str[i][4]:
										if b == check_str[i][5]:
											s = 0
											s = x[0]
											for j in xrange(len(x)-1):
												s ^= x[j+1]
											print "Result %d :" %(i)
											if s == check_flag[i]:
												for j in x:
													print str(chr(j))