def f(x):
	return x ** 3 + 8

def main():
	x = 9
	y = f(x)
	print(y)
	if int(y) > 27:
		print("YAY!")
if __name__=="__main__":
	main()