import os
import sys
import registers as registers

sys.path.append(os.getcwd() + "/devices")

def call(callid):
	calls[str(callid)].call(registers.general, registers.extended)
	

try:
	from a.src import __main__ as m1
except:
	m1 = ""

try:
	from b.src import __main__ as m2
except:
	m2 = ""

try:
	from c.src import __main__ as m3
except:
	m3 = ""

try:
	from d.src import __main__ as m4
except:
	m4 = ""

try:
	from e.src import __main__ as m5
except:
	m5 = ""

try:
	from f.src import __main__ as m6
except:
	m6 = ""

try:
	from g.src import __main__ as m7
except:
	m7 = ""

try:
	from h.src import __main__ as m8
except:
	m8 = ""

try:
	from i.src import __main__ as m9
except:
	m9 = ""

try:
	from j.src import __main__ as m10
except:
	m10 = ""

calls = {
	"1":m1,
	"2":m2,
	"3":m3,
	"4":m4,
	"5":m5,
	"6":m6,
	"7":m7,
	"8":m8,
	"9":m9,
	"10":m10
}

