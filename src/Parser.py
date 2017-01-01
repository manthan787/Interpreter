from Token import TokenType
from Token import Token, get_operator_type
from Expression import SimpleExpression


class Parser:


	def __init__(self, text):
		""" text to be parsed """
		self.text = text
		""" the pointer pointing at a character in the given text """
		self.pointer = 0


	def parse(self):
		"""	
			Parses the given text
			1) Identifies the tokens
			2) Constructs an expression
			3) Solves it
		"""
		expression = self.construct_expression()
		return expression.solve()


	def construct_expression(self):
		"""
			Parse the given text to construct an expression
		"""		
		operand1, operator, operand2 = self.get_tokens()
		return SimpleExpression(operand1, operator, operand2)


	def get_tokens(self):
		"""
			Get tokens from the expected INTEGER OPERATOR INTEGER
			patterns of expressions
		"""
		operand1 = self.get_next_token()		
		self.verify(operand1, [TokenType.INTEGER])

		operator = self.get_next_token()		
		self.verify(operator, [TokenType.PLUS, TokenType.MUL, TokenType.DIV, TokenType.MINUS])

		operand2 = self.get_next_token()		
		self.verify(operand2, [TokenType.INTEGER])

		return operand1, operator, operand2


	def get_next_token(self):
		current_char = self.get_next_char()		
		
		int_buffer = ''
		while current_char is not None and current_char.isdigit():
			int_buffer += current_char			
			current_char = self.get_next_char()

		if len(int_buffer) > 0:
			self.pointer -= 1		
			return Token(TokenType.INTEGER, int(int_buffer))	

		if self.isoperator(current_char):			
			return Token(get_operator_type(current_char), current_char)

		raise Exception("Invalid Syntax")


	def isoperator(self, char):
		"""
		Return true if the given character is a supported operator
		"""		
		return char in TokenType.OPERATOR_TYPE_MAPPINGS
	

	def get_next_char(self):
		"""
			Get the next character in the text
		"""		
		if self.pointer > len(self.text) - 1:
			return None

		current_char = self.text[self.pointer]		
		self.pointer += 1
		if current_char == ' ':
			current_char = self.get_next_char()	
					
		return current_char


	def verify(self, token, types):
		"""
			Verify whether the token is of the expected type
		"""	
		if token.type not in types:
			raise Exception("Unexpected Token")


def test():
	parser = Parser("33 + 5")
	print parser.parse()
	parser = Parser("33 - 5")
	print parser.parse()
	parser = Parser("33 * 5")
	print parser.parse()
	parser = Parser("30 / 5")
	print parser.parse()


if __name__ == '__main__':
	test()

