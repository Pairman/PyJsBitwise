def int_overflow(n: int):
	"""Overlow behavior of signed int32 type.
 	:param n: Number to be owerflowed.
  	:return: The overflowed number.
 	"""
	if not -0x80000000 <= n <= 0x7FFFFFFF:
		n = (n + 0x80000000) % (2 * 0x80000000) - 0x80000000
	return n

def lshift(n: int | float, i: int):
	if type(n) is float:
		n = int(n) & 0xFFFFFFFF
	i &= 0x1F
	return int_overflow(n << i if i >= 0 else n >> -i)

def rshift(n: int | float, i: int):
	if type(n) is float:
		n = int(n) & 0xFFFFFFFF
	i &= 0x1F
	return int_overflow(n >> i if i >= 0 else n << -i)

def urshift(n: int | float, i: int):
	if type(n) is float:
		n = int(n) & 0xFFFFFFFF
	if n < 0:
		n &= 0xFFFFFFFF
	i &= 0x1F
	return int_overflow(n >> i) if i >= 0 else -int_overflow(n << -i)
