from src.Interpreter import Interpreter

if __name__ == '__main__':
	while True:
		expr = raw_input("Interpreter> ")
		intp = Interpreter(expr)
		print intp.interpret()
		