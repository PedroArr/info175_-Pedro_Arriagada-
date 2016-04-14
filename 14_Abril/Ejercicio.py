#-*- config: utf-8 -*-
#funcion recursiva que calcule el n-esimo elemento de fibonacci

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n > 1:
		return fib(n-1)+fib(n-2)