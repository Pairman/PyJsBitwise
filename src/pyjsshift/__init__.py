def int_overflow(n):
	"""Overlow behavior of signed 32-bit integer.
 	:param n: Number to be owerflowed. Int.
  	:return: The overflowed number. Int.
 	"""
	return (n + 0x80000000) % 0x100000000 - 0x80000000

def lshift(n, i):
	"""JavaScript-flavored bitwise shift left (<<).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = int(n) & 0xFFFFFFFF
	i = int(i) & 0x1F
	return int_overflow(n << i if i >= 0 else n >> -i)

def rshift(n, i):
	"""JavaScript-flavored bitwise shift right (>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = (int(n) & 0xFFFFFFFF) if type(n) is float else int_overflow(n)
	i = int(i) & 0x1F
	return int_overflow(n >> i if i >= 0 else n << -i)

def urshift(n, i):
	"""JavaScript-flavored bitwise unsigned shift right (>>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = int(n) & 0xFFFFFFFF
	i = int(i) & 0x1F
	return (n >> i if i >= 0 else -n << -i) & 0xffffffff
