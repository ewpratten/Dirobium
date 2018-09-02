import instructions as ins
import pushandpop as pnp
import system as system
import shareddata as globl
import jump as jmp

# Map all valid instructin opcodes to a function
execute = {
	"10000001":ins.mov,
	"10000010":ins.add,
	"10000011":ins.sub,
	"10000100":ins.mul,
	"10000101":ins.div,
	"10000110":ins.ret,
	"10000111":ins.call,
	"10001000":jmp.jmpf,
	"10001001":jmp.jmpb,
	"10001011":jmp.jmp,
	"10001100":ins.paus,
	"10001101":ins.load,
	"10001110":system.coredump,
	"10001111":ins.movs,
	"10010000":pnp.push,
	"10010001":pnp.pop
}

# loop through code and run instructions
def run(code):
	if code == globl.bootloader:
		while globl.bootl < len(globl.bootloader):
			if globl.bootloader[globl.bootl] in execute:
				execute[globl.bootloader[globl.bootl]](code[globl.bootl:])
			globl.bootl += 1
		
	elif code == globl.rom:
		while globl.roml < len(globl.rom):
			if globl.rom[globl.roml] in execute:
				execute[globl.rom[globl.roml]](code[globl.roml:])
			globl.roml += 1
	# else:
	# 	i = 0
	# 	for instruction in code:
	# 		if instruction in execute:
	# 			# if instruction == "10001110":
	# 			# 	system.coredump()
	# 			# print(instruction)
	# 			execute[instruction](code[i:])
	# 		i+=1