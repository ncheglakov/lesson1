
def get_answer(question):
	return {
		"привет": "И тебе привет!",
		"как дела": "Лучше всех", "пока": "Увидимся"
	}.get(question, 'я не знаю')

print(get_answer(input()))


