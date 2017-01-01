class TokenType:

	INTEGER = "INT"
	PLUS = "PLUS"
	MINUS = "MINUS"
	MUL = "MUL"
	DIV = "DIV"
	EOF = "EOF"

	OPERATOR_TYPE_MAPPINGS = {'+': PLUS,
							  '-': MINUS,
							  '*': MUL,
							  '/': DIV}


class Token:

	def __init__(self, type, value):
		self.type = type
		self.value = value


	def __str__(self):
		return "Token({},{})".format(self.type, self.value)


# Module methods
def get_operator_type(op):
	"""
		Returns the TokenType of the given operator character
		op: A character depicting an operator

		Returns: The type value for the given operator
	"""
	return TokenType.OPERATOR_TYPE_MAPPINGS[op]