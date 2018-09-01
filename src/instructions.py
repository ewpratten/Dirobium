import shareddata as globl
import system as system
import registers as registers
import call as caller
import execution as execution

def decode(frm):
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
	return frm

def decodeTo(to, data):
	# check type of to and store data in location
	if to[0] == "00000010":
		registers.general[int(to[1], 2)] = data
	elif to[0] == "00000101":
		registers.extended[int(to[1], 2)] = data
	else:
		system.coredump()
		exit(1)
	
def mov(params):
	frm = [params[1], params[2]]
	to = [params[3], params[4]]
	
	frm = decode(frm)
	decodeTo(to, frm)
	
	

def add(params):
	v1 = [params[1], params[2]]
	v2 = [params[3], params[4]]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 + v2
	
	decodeTo(to, val_sum)

def sub(params):
	v1 = [params[1], params[2]]
	v2 = [params[3], params[4]]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 - v2
	
	decodeTo(to, val_sum)

def mul(params):
	v1 = [params[1], params[2]]
	v2 = [params[3], params[4]]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 * v2
	
	decodeTo(to, val_sum)

def div(params):
	v1 = [params[1], params[2]]
	v2 = [params[3], params[4]]
	to = [params[5], params[6]]
	
	v1 = decode(v1)
	v2 = decode(v2)
	
	val_sum = v1 / v2
	
	decodeTo(to, val_sum)

def ret(params):
	value = [params[1], params[2]]
	decodeTo(["00000101", "00000001"], decode(value))

def call(params):
	callid = [params[1], params[2]]
	callid = decode(callid)
	caller.call(callid)

def jmpf(params):
	print("jmpf")

def jmpb(params):
	print("jmpb")

def jmp(params):
	if params[1] == "00000011" and len(params) >= 2 and decode([params[2], params[3]]) == 0:
		globl.mode = globl.modes.rom
		execution.run(globl.rom)
		

def paus(params):
	ins = [params[1], params[2]]
	ins = decode(ins)
	if ins == 0:
		input()
	if ins == 1:
		registers.extended[0] = input()

def load(params):
	if params[1] == "00000011":
		globl.rom = system.loadRom()
	else:
		system.coredump()
		exit(1)
	