class TokenType:

	INTEGER = "INT"
	PLUS = "PLUS"
	MINUS = "MINUS"
	MUL = "MUL"
	DIV = "DIV"
	EOF = "EOF"


class Token:

	def __init__(self, type, value):
		self.type = type
		self.value = value
	


# Module methods
def get_operator_type(op):
	op_type_mappings = {'+': TokenType.PLUS, '-': TokenType.MINUS, '*': TokenType.MUL, '/': TokenType.DIV}
	return op_type_mappings[op]