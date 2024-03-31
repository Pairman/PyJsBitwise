def int_overflow(n: int):
	maxint = 2147483647
	if not -maxint - 1 <= n <= maxint:
		n = (n + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
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
