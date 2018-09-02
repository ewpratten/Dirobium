def decode(frm):
	#check type of frm and turn back to int
	if frm[0] == "00000001":
		frm = int(frm[1], 2)
	elif frm[0] == "000000010":
		frm = registers.general[int(frm[1], 2)]
	elif frm[0] == "00000011":
		print("rom")
	elif frm[0] == "00000100":
		print("boot")
	elif frm[0] == "00000101":
		frm = registers.extended[int(frm[1], 2)]
	elif frm[2][1] == "00000110":
		legnth = int(frm[2][2], 2)
		i = 0
		ret = ""
		while i < legnth:
			ret += string_letters[int(frm[2][3+i], 2)]
			i+=1
		frm = ret
		# print(frm)
	else:
		system.coredump()
		exit(1)
	return frm

def decodeTo(to, data):
	# check type of to and store data in location
	if to[0] == "00000010":
		registers.general[int(to[1], 2)] = data
	elif to[0] == "00000101":
		registers.extended[int(to[1], 2)] = data
	else:
		system.coredump()
		exit(1)