import shareddata as globl

def mov(params):
	frm = [params[1], params[2]]
	to = [params[3], params[4]]
	print(frm)
	print(to)

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