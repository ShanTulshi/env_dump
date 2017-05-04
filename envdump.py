import json

def dump(f, d=globals()):
	if(type(f) is str):
		f = open(f, 'w')
	if(type(f) is file):
		json.dump(d, f)
	else:
		raise ValueError('first parameter to dump has to be a file or a filename!')

def read(f):
	if(type(f) is str):
		f = open(f)
	if(type(f) is file):
		return json.loads(f.read())
	else:
		raise ValueError('first parameter to read has to be a file or a filename!')

