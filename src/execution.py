import instructions as ins

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
	"10001011":ins.jmp
}

def run(code):
	i = 0
	for instruction in code:
		if instruction in execute:
			execute[instruction](code[i:])
		i+=1