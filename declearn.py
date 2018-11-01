# A decorator is nothing more than a callable object that takes a function as an input parameter

def succ(x):
	return x+1

shenxu=succ
print(shenxu(10))
print(succ(10))

del succ
print(shenxu(10))

# defining function inside of a function

def f():
	def g():
		print("Hi,it's me 'g'")
		print("Thanks for calling me")
	print("This is the function 'f'")
	print("I am calling 'g' now:")
	g()
f()

# function as parameters

def g():
	print("Hi,it's me 'g'")
	print("Thanks for calling me.")

def f(func):
	print("Hi,it's me 'f'")
	print("I will call function now.")
	func()
	print("function's real name is "+func.__name__)


f(g)


def our_decorator(func):
	def function_wrapper(x):
		print("Before calling " + func.__name__)
		func(x)
		print("After calling "+ func.__name__)
	return function_wrapper

def foo(x):
	print("Hi, foo has been called with "+str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)


def our_decorator(func):
	def function_wrapper(x):
		print("Before calling " + func.__name__)
		res = func(x)
		print(res)
		print("After calling" + func.__name__)
	return function_wrapper

@our_decorator
def succ(n):
	return n+1

succ(10)


