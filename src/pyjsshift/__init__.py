from typing import overload

def int_overflow(n: int):
	"""Overlow behavior of signed int32 type.
 	:param n: Number to be owerflowed. Int.
  	:return: The overflowed number. Int.
 	"""
	return (n + 0x80000000) & 0xFFFFFFFF - 0x80000000

@overload
def lshift(n: int, i: int):
	"""JavaScript-flavored bitwise shift left (<<).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n << j) or n >> j)

@overload
def lshift(n: float, i: int):
	"""JavaScript-flavored bitwise shift left (<<).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = int(n) & 0xFFFFFFFF
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n << j) or n >> j)

@overload
def rshift(n: int, i: int):
	"""JavaScript-flavored bitwise shift right (>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n >> j) or n << -j)

@overload
def rshift(n: float, i: int):
	"""JavaScript-flavored bitwise shift right (>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = int(n) & 0xFFFFFFFF
	i &= 0x1F
	j = abs(i)
	return int_overflow((i >= 0 and n >> j) or n << -j)

@overload
def urshift(n: int, i: int):
	"""JavaScript-flavored bitwise unsigned shift right (>>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n &= (n < 0 and 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return int_overflow(n >> j) if i >= 0 else -int_overflow(n << j)

@overload
def urshift(n: float, i: int):
	"""JavaScript-flavored bitwise unsigned shift right (>>>).
 	:param n: Number to be owerflowed. Int or float.
 	:param i: Number of bits to shift by. Int.
  	:return: The shifted number. Int.
 	"""
	n = int(n) & 0xFFFFFFFF
	n &= (n < 0 and 0xFFFFFFFF) or n
	i &= 0x1F
	j = abs(i)
	return int_overflow(n >> j) if i >= 0 else -int_overflow(n << j)
