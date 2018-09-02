import shareddata as globl
import system as system
import registers as registers
import call as caller
import execution as execution

string_letters = {
	0:" ",
	1:"a",
	2:"b",
	3:"c",
	4:"d",
	5:"e",
	6:"f",
	7:"g",
	8:"h",
	9:"i",
	10:"j",
	11:"k",
	12:"l",
	13:"m",
	14:"n",
	15:"o",
	16:"p",
	17:"q",
	18:"r",
	19:"s",
	20:"t",
	21:"u",
	22:"v",
	23:"w",
	24:"x",
	25:"y",
	26:"z",
	27:":",
	28:"1",
	29:".",
	30:"0"
}

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
	
def mov(params):
	frm = [params[1], params[2], params]
	to = [params[3], params[4]]
	
	frm = decode(frm)
	# print(frm)
	# print(to)
	decodeTo(to, frm)

def movs(params):
	frm = [params[1], params[2], params]
	legnth = int(params[2], 2)
	i = 0
	ret = ""
	while i < legnth:
		ret += string_letters[int(frm[2][3+i], 2)]
		i+=1
	frm = ret
	
	to = [params[3 + legnth], params[4 + legnth]]
	decodeTo(to,frm)

def add(params):
	v1 = [params[1], params[2], params]
	v2 = [params[3], params[4], params]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 + v2
	
	decodeTo(to, val_sum)

def sub(params):
	v1 = [params[1], params[2], params]
	v2 = [params[3], params[4], params]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 - v2
	
	decodeTo(to, val_sum)

def mul(params):
	v1 = [params[1], params[2], params]
	v2 = [params[3], params[4], params]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 * v2
	
	decodeTo(to, val_sum)

def div(params):
	v1 = [params[1], params[2], params]
	v2 = [params[3], params[4], params]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 / v2
	
	decodeTo(to, val_sum)

def ret(params):
	value = [params[1], params[2]]
	decodeTo(["00000101", "00000001"], decode(value))

def call(params):
	callid = [params[1], params[2], params]
	callid = decode(callid)
	caller.call(callid)

def paus(params):
	ins = [params[1], params[2], params]
	ins = decode(ins)
	if ins == 0:
		input()
	if ins == 1:
		registers.extended[0] = input()

def load(params):
	if params[1] == "00000011":
		globl.rom = system.loadRom()
	else:
		system.coredump()
		exit(1)

