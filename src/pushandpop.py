import encodedecode as ed
import registers as registers

def push(params):
	frm = [params[1], params[2], params]
	
	frm = ed.decode(frm)
	# print(frm)
	registers.stack.append(frm)

def pop(params):
	frm = [params[1], params[2], params]
	to = [params[3], params[4]]
	
	frm = ed.decode(frm)
	frm = registers.stack.pop(frm)
	ed.decodeTo(to, frm)