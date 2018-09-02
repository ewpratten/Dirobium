import encodedecode as ed
import registers as registers
import execution as execution
import shareddata as globl


def jmpf(params):
	distance = [params[1], params[2], params]
	distance = ed.decode(distance)
	if globl.mode == globl.modes.bootloader:
		globl.bootl += distance
	elif globl.mode == globl.modes.rom:
		globl.roml += distance

def jmpb(params):
	distance = [params[1], params[2], params]
	distance = ed.decode(distance)
	if globl.mode == globl.modes.bootloader:
		globl.bootl -= distance
	elif globl.mode == globl.modes.rom:
		globl.roml -= distance

def jmp(params):
	if params[1] == "00000011" and len(params) >= 2 and ed.decode([params[2], params[3], params]) == 0:
		globl.mode = globl.modes.rom
		execution.run(globl.rom)