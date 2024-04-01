def int_overflow(n):
	"""Overlow behavior of signed int32 type.
 	:param n: Number to be owerflowed. Int.
  	:return: The overflowed number. Int.
 	"""
	return (n + 0x80000000) & 0xFFFFFFFF - 0x80000000

def lshift(n, i):
	"""JavaScript-flavored bitwise shift left (<<).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = (type(n) is float and int(n) & 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n << j) or n >> j)

def rshift(n, i):
	"""JavaScript-flavored bitwise shift right (>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = (type(n) is float and int(n) & 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n >> j) or n << j)

def urshift(n, i):
	"""JavaScript-flavored bitwise unsigned shift right (>>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = (type(n) is float and int(n) & 0xFFFFFFFF) or n
	n &= (n < 0 and 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return abs(int_overflow((i >= 0 and n >> j) or n << j))
