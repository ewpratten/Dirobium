import system as system
import shareddata as globl
import execution as execution

# initalize computer
globl.bootloader = system.loadBootloader()	#load bootloader code
globl.mode = globl.modes.bootloader	#set current mode to bootloader

execution.run(globl.bootloader)

# system.coredump()
