#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem56.py
#  
#  Copyright 2017 Robert <Robert@DESKTOP-UG02M0H>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def a_tothe_b(a, b):
	return a ** b

def sum_of_digits(x):
	string_representation = str(x)
	sum = 0
	for digit in string_representation:
		sum+=int(digit)
	return sum

def main(args):
	maxsum = 0
	for a in range(100):
		for b in range(100):
			print(str(a) + ' to the ' + str(b))
			ab = a_tothe_b(a,b)
			sumofdigits = sum_of_digits(ab)
			if sumofdigits > maxsum:
				maxsum = sumofdigits
	print(maxsum)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
