import struct


def uint1(stream):
	#ord("a") - returns Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. For example, ord('a') returns the integer 97, ord(u'\u2020') returns 8224
	#read-'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'.
	#stream.read(2) reads the first 2 elements from the file, and points to the next element for the next read
	#struct.unpack('H' --H 
	#H	unsigned short	integer	2
	#I	unsigned int	integer	4
	#Q	unsigned long long	integer	8
	#stream.read(32)[::-1] - reads the first 32 units, but in reverse order.
	#stream.read(32)[::-2] - reads the first 32 units skips alternate ones, but starting in reverse order.
	#example, a file test.dat has the folloing 2 lines:
	#abcdefg
	#hijklmn
	#>>>  with open('test.dat') as blockfile: 
	# ...     print(blockfile.read(20)[::-1])
	# ... 
	# nmlkjih
	# gfedcba
	# >>> with open('test.dat') as blockfile: 
	# ...     print(blockfile.read(20)[::-2])
	# ... 
	# nljhgeca
	#f.tell() returns an integer giving the file object’s current position in the file, measured in bytes from the beginning of the file. To change the file object’s position, use f.seek(offset, from_what). The position is computed from adding offset to a reference point; the reference point is selected by the from_what argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.


	return ord(stream.read(1))

def uint2(stream):
	return struct.unpack('H', stream.read(2))[0]

def uint4(stream):
	return struct.unpack('I', stream.read(4))[0]

def uint8(stream):
	return struct.unpack('Q', stream.read(8))[0]

def hash32(stream):
	return stream.read(32)[::-1]

def time(stream):
	time = uint4(stream)
	return time

def varint(stream):
	size = uint1(stream)

	if size < 0xfd:
		return size
	if size == 0xfd:
		return uint2(stream)
	if size == 0xfe:
		return uint4(stream)
	if size == 0xff:
		return uint8(stream)
	return -1

def hashStr(bytebuffer):
	return ''.join(('%02x'%ord(a)) for a in bytebuffer)

