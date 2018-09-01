import instructions as ins
import system as system

execute = {
	"10000001":ins.mov,
	"10000010":ins.add,
	"10000011":ins.sub,
	"10000100":ins.mul,
	"10000101":ins.div,
	"10000110":ins.ret,
	"10000111":ins.call,
	"10001000":ins.jmpf,
	"10001001":ins.jmpb,
	"10001011":ins.jmp,
	"10001100":ins.paus,
	"10001101":ins.load,
	"10001110":system.coredump
}

def run(code):
	i = 0
	for instruction in code:
		if instruction in execute:
			# print(instruction)
			execute[instruction](code[i:])
		i+=1