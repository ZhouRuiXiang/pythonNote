import functools


def log(month, day):
	def decorator(func):
		# 将被装饰函数的特殊属性__name__改为其本身，而非wrapper
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			print("%s月%s日，函数%s被调用了" % (month ,day, func.__name__))
			return func(*args, **kwargs)
		return wrapper
	return decorator


@log(9, 18)
def add(num1, num2):
	print(num1, num2)
	return num2 + num1








if __name__ == '__main__':
	print(add(1, 2))
	print(add.__name__)





