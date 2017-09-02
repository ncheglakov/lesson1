def get_summ(one, two, delimeter=' '):
	return str(one).upper() + delimeter + str(two).upper()


print(get_summ(2, 2))
print(get_summ('Hello', 'world!'))
print(get_summ('Hello', 2))
print(get_summ('Hello', 'World', delimeter=' & '))

