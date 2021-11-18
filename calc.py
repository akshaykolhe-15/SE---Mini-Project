# CALCULATOR WITH VARIOUS FUNCTIONALITIES (SCIENTIFIC CALCULATOR).

# 111903012 - Akshay Kolhe
# 111903016 - Aniket Mohod

# Basic functionalities.
def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y

# Advance functionalities.    
def fibonacci(n):
    # n shows the position of fibonacci number
    
    if n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
def fact(n):
	fact = 1
	if len(str(n))<10:
		for i in range(2,n+1):
			fact = fact * i
	return fact

# Number conversion.
def bin_to_dec(bin_num):
    """convert binNum to Decimal Number."""
    dec_num = 0
    power = 0
    while bin_num > 0:
        dec_num += 2 ** power * (bin_num % 10)
        bin_num //= 10
        power += 1
    return dec_num
    
def dec_to_binary(number):
	"""convert Decimal to binNum Number."""
	binary = ''
	if number == 0:
		return '0'
	while number >= 1:
		if number % 2 == 0:
			binary += '0'
			number /= 2
		else:
			binary += '1'
			number =(number- 1)/2
	return binary[::-1]	

def hex_to_dec(number):
	"""convert HexaDecimal to Decimal Number."""
	dec = 0
	n = len(str(number))
	for i in str(number):
		if i == 'A' or i == 'a':
			i = 10
		elif i == 'B' or i == 'b':
			i = 11
		elif i == 'C' or i == 'c':
			i = 12
		elif i == 'D' or i == 'd':
			i = 13
		elif i == 'E' or i == 'e':
			i = 14
		elif i == 'F' or i == 'f':
			i = 15
		dec += int(i)*16**(n-1)
		n -= 1
	return dec   

def oct_to_dec(number):
	"""convert Octal to Decimal Number."""
	dec = 0
	n = len(str(number))
	for i in str(number):
		dec += int(i)*8**(n-1)
		n -= 1
	return dec
	

	   

