import random
rand_numb = random.randrange(1000,9999)

def check_numb (checked_numb, numb):
	checked_numb_str = str(checked_numb)
	numb_str = str(numb)
	eieren = 0
	kippen = 0
	for index, char in enumerate(checked_numb_str):
		if char == numb_str[index]:
			kippen += 1
	correct_char = str(rand_numb)
	for index, char in enumerate(checked_numb_str):
		if char in numb_str and char in correct_char:
			eieren += 1
			correct_char = correct_char[:index] + correct_char[index+1:]
	eieren = eieren - kippen
	if eieren < 0:
			eieren = 0
	return [kippen, eieren]

def showResult(result_arr):
	if result_arr[0] > 1 or result_arr[0] == 0:
		if result_arr[1] > 1 or result_arr [1] == 0:
			print(str(result_arr[0])+' kippen en '+str(result_arr[1])+' eikes')
		else:
			print(str(result_arr[0])+' kippen en '+str(result_arr[1])+' ei')
	else:
		if result_arr[1] > 1 or result_arr[1] == 0:
			print(str(result_arr[0])+' kip en '+str(result_arr[1])+' eikes')
		else:
			print(str(result_arr[0])+' kip en '+str(result_arr[1])+' ei')

right_numb = False
counter = 0

while not right_numb:
	given_numb = input('Geef een nummer: ')
	counter += 1
	if rand_numb == right_numb:
		print('Juist geraden proficiat je hebt er maar '+ str(counter)+' keer over gedaan hiep hiep hoera!')
	else: 
		verder_raden = check_numb(rand_numb, given_numb)
		showResult(verder_raden)