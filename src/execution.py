import shareddata as globl
import system as system
import registers as registers

def mov(params):
	frm = [params[1], params[2]]
	to = [params[3], params[4]]
	
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
	else:
		system.coredump()
		exit(1)
	
	# check type of to and store frm in location
	if to[0] == "00000010":
		registers.general[int(to[1], 2)] = frm
	elif to[0] == "00000101":
		registers.extended[int(to[1], 2)] = frm
	else:
		system.coredump()
		exit(1)

def add():
	print("add")

def sub():
	print("sub")

def mul():
	print("mul")

def div():
	print("div")

def ret():
	print("ret")

def call():
	print("call")

def jmpf():
	print("jmpf")

def jmpb():
	print("jmpb")

def jmp():
	print("jmp")

execute = {
	"10000001":mov,
	"10000010":add,
	"10000011":sub,
	"10000100":mul,
	"10000101":div,
	"10000110":ret,
	"10000111":call,
	"10001000":jmpf,
	"10001001":jmpb,
	"10001011":jmp
}

def run(code):
	i = 0
	for instruction in code:
		if instruction in execute:
			execute[instruction](code[i:])
		i+=1