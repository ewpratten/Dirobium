import registers as registers
import shareddata as globl

def setRORegisters():
	registers.read_only[0] = int(len(registers.stack)) # Stack size
	registers.read_only[1] = 0 if globl.mode == globl.modes.bootloader else 1
	registers.read_only[2] = int(globl.bootl)
	registers.read_only[3] = int(globl.roml)

def loadBootloader():
	raw = open("./bootloader.rom").read().strip()
	return [raw[i:i+8] for i in range(0, len(raw), 8)]


def loadRom():
	raw = open("./main.rom").read().strip()
	return [raw[i:i+8] for i in range(0, len(raw), 8)]

def coredump(inp=None):
	print("-- Core Dump --")
	print("General Registers: " + str(registers.general))
	print("Extended Registers: " + str(registers.extended))
	print("Read Only Registers: " + str(registers.read_only))
	print("Stack: " + str(registers.stack))
	# exit(1)
	# print("-- End Core Dump --")