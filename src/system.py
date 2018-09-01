import registers as registers

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
	
	# print("-- End Core Dump --")