import functools
def my_decorator(func):

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print("start")
		result = func(*args, **kwargs)
		print("end")
		return result
	return wrapper 

@mydecorator
def dosome(x):
	return x+5
res = dosome(5)
print(res)
