def int_overflow(n: int):
	"""Overlow behavior of signed int32 type.
 	:param n: Number to be owerflowed.
  	:return: The overflowed number.
 	"""
	return (n + 0x80000000) & 0xFFFFFFFF - 0x80000000

def lshift(n: int | float, i: int):
	"""JavaScript-flavored bitwise shift left (<<).
 	:param n: Number to be shifted.
 	:param i: Number of bits to shift by.
  	:return: The shifted number.
 	"""
	n = (type(n) is float and int(n) & 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n << j) or n >> j)

def rshift(n: int | float, i: int):
	"""JavaScript-flavored bitwise shift right (>>).
 	:param n: Number to be shifted.
 	:param i: Number of bits to shift by.
  	:return: The shifted number.
 	"""
	n = (type(n) is float and int(n) & 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n >> j) or n << -j)

def urshift(n: int | float, i: int):
	"""JavaScript-flavored bitwise unsigned shift right (>>>).
 	:param n: Number to be shifted.
 	:param i: Number of bits to shift by.
  	:return: The shifted number.
 	"""
	n = (type(n) is float and int(n) & 0xFFFFFFFF) or n
	n &= (n < 0 and 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return int_overflow(n >> j) if i >= 0 else -int_overflow(n << j)
