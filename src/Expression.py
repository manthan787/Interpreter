import operator

class SimpleExpression:

	def __init__(self, operand1, operator, operand2):
		"""
			Here operands are INT tokens 
			and operator is a token one of [+, -, *, /]
		"""
		self.operand1 = operand1
		self.operator = operator
		self.operand2 = operand2


	def solve(self):
		operator_mappings = {'PLUS': operator.add, 
							 'MINUS': operator.sub,
							 'MUL': operator.mul,
							 'DIV': operator.div}

		return operator_mappings[self.operator.type](self.operand1.value, self.operand2.value)


def test():
	from Token import Token
	expr = SimpleExpression(Token('INT', 32), Token('PLUS', '+'), Token('INT', 12))
	print expr.solve()
	expr = SimpleExpression(Token('INT', 32), Token('MINUS', '-'), Token('INT', 12))
	print expr.solve()
	expr = SimpleExpression(Token('INT', 32), Token('MUL', '*'), Token('INT', 12))
	print expr.solve()
	expr = SimpleExpression(Token('INT', 32), Token('DIV', '/'), Token('INT', 12))
	print expr.solve()


if __name__ == '__main__':
	test()