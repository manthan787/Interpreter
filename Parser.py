from Token import TokenType
from Token import Token


class Parser:


	def __init__(self, text):
		""" text to be parsed """
		self.text = text
		""" the pointer pointing at a characeter in the given text """
		self.pointer = 0	
		""" most recently identified token """			 
		self.current_token = None
	

	def parse(self):
		"""	
			Parses the given text
			1) Identifies the tokens
			2) Constructs an expression
			3) Solves it
		"""
		expression = self.construct_expression()
				




def test():
	parser = Parser("3 + 5")
	print parser.parse()


if __name__ == '__main__':
	test()

