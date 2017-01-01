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
	
