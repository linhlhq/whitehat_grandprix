def xor(a,b):
	return int('0x'+a.encode('hex'),16) ^ int('0x'+b.encode('hex'),16)
def check_flag(a):
	s = ord(a[0])
	for i in xrange(len(a)-1):
		s ^= ord(a[i+1])
		pass
	return s
def check_str(a):
	ret =list()
	for i in xrange(len(a)-1):
		x = ord(a[i])
		y = ord(a[i+1])
		ret.append(int(bin(x)[2:])&int(bin(y)[2:]))
		ret.append(int(bin(x)[2:])|int(bin(y)[2:]))
		pass
	return ret

f = open('flag.txt','r')
fl = f.read();
f.close()
c = 0
flag = list()
s = ''
for char in fl:
	if ord(char) == 10:
		c = c+1
		flag.append(s)
		s = ''
	else:
		s = s + char
if c != 5:
	print 'Oops!!!'
	exit()
flag.append(fl[len(fl)-4:])
print flag

xo = list()
#flag = map(int, flag)
for i in range(len(flag) - 1):
	#print 1
	xo.append(xor(flag[i],flag[i+1]))
print xo
if xo[0] == 794515979:
	if xo[1] == 694958164:
		if xo[2] == 925239669:
			if xo[3] == 657915924:
				if xo[4] == 1680414502:
					print 'Look good!'
cf = list()
for i in xrange(len(flag)):
	cf.append(check_flag(flag[i]))
	pass
if cf[0] == 115:
	if cf[1] == 86:
		if cf[2] == 127:
			if cf[3] == 18:
				if cf[4] == 22:
					if cf[5] == 106:
						print 'Good, but not done!'
p1 = check_str(flag[0])
if p1[0] == 16456:
	if p1[1] == 2084555:
		if p1[2] == 35840:
			if p1[3] == 1175260:
				if p1[4] == 35844:
					if p1[5] == 1175356:
						print "ok1"

p2 = check_str(flag[1])
if p2[0] == 36136:
	if p2[1] == 1174975:
		if p2[2] == 36146:
			if p2[3] == 1174975:
				if p2[4] == 1100038:
					if p2[5] == 1101183:
						print "ok2"

p3 = check_str(flag[2])
if p3[0] == 999589:
	if p3[1] == 1011623:
		if p3[2] == 1010086:
			if p3[3] == 1011135:
				if p3[4] == 76218:
					if p3[5] == 1043903:
						print "ok3"

p4 = check_str(flag[3])
if p4[0] == 1106904:
	if p4[1] == 1114107:
		if p4[2] == 24961:
			if p4[3] == 2097151:
				if p4[4] == 999590:
					if p4[5] == 1011631:
						print "ok4"

p5 = check_str(flag[4])
if p5[0] == 999572:
	if p5[1] == 1011639:
		if p5[2] == 1000582:
			if p5[3] == 1011639:
				if p5[4] == 1009922:
					if p5[5] == 1011199:
						print "ok5"
p6 = check_str(flag[5])
if p6[0] == 35073:
	if p6[1] == 1175039:
		if p6[2] == 16392:
			if p6[3] == 2084719:
				if p6[4] == 16384:
					if p6[5] == 2094716:
						print "ok6"