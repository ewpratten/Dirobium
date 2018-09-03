import shareddata as globl
import encodedecode as ed

# Compare
def comp(params):
	v1 = ed.decode([params[1], params[2], params])
	v2 = ed.decode([params[3], params[4], params])
	
	if v1 != v2:
		if globl.mode == globl.modes.bootloader:
			globl.bootl += 1
		elif globl.mode == globl.modes.rom:
			globl.roml +=1
	else:
		if globl.mode == globl.modes.bootloader:
			globl.bootl += 7
		elif globl.mode == globl.modes.rom:
			globl.roml +=7

# Less or equal
def lte(params):
	v1 = ed.decode([params[1], params[2], params])
	v2 = ed.decode([params[3], params[4], params])
	
	if not v1 <= v2:
		if globl.mode == globl.modes.bootloader:
			globl.bootl += 1
		elif globl.mode == globl.modes.rom:
			globl.roml +=1

# Greater or equal
def gte(params):
	v1 = ed.decode([params[1], params[2], params])
	v2 = ed.decode([params[3], params[4], params])
	
	if not v1 >= v2:
		if globl.mode == globl.modes.bootloader:
			globl.bootl += 1
		elif globl.mode == globl.modes.rom:
			globl.roml +=1