from Parser import Parser

class Interpreter:

	def __init__(self, text):
		self.parser = Parser(text)


	def interpret(self):
		return self.parser.parse()


if __name__ == '__main__':
	intp = Interpreter('3 + 5')
	print intp.interpret()
