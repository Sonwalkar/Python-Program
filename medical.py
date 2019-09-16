print("\n------------------simple medical expert------------------\n")


def check_disease():
	flag1 = 0
	flag2 = 0
	flag3 = 0
	cancer = 0
	fever = 0
	cold = 0
	cancer_symptoms = ['hair loss', 'weight loss', 'blood vomit', 'blood-tinged saliva']
	fever_symptoms = ['shaking', 'cold', 'cough', 'chills']
	cold_symptoms = ['headache', 'runny_nose', 'sneezing', 'sore_throat']

	for i in cancer_symptoms:
		dummy_input = str(input("do you have " + i + "  Y/N "))
		if dummy_input.upper() == 'Y':
			cancer = cancer + 1
		print("\n")
	for i in fever_symptoms:
		dummy_input = str(input("do you have " + i + "  Y/N "))
		if dummy_input.upper() == 'Y':
			fever = fever + 1
		print("\n")
	for i in cold_symptoms:
		dummy_input = str(input("do you have " + i + "  Y/N "))
		if dummy_input.upper() == 'Y':
			cold = cold + 1
		print("\n")
	if cancer == 0 and fever == 0 and cold == 0:
		print("You are healthy")
	elif cancer == fever == cold:
		print("You have Cancer, Fever and Cold")
		flag3 = flag2 = flag1 = 1
	else:	
		print("You have", end="")
		if cancer >= 3:
			print(" Cancer", end="")
			flag1 = 1
		if fever >= 3:
			print(" Fever", end="")
			flag2 = 1
		if cold >= 3:
			print(" cold", end="")
			flag3 = 1
	if flag1 == 1:
		print("Advices and Suggestions for Cancer\n1: Tylenol\n2: Panadol\n3: Nasal spray\nPlease weare warm cloths because")
	if flag2 == 1:
		print("Advices and Suggestions for Fever\n 1: Tylenol \n2:Nasal spray \nnPlease weare warm cloths because")
	if flag3 == 1:
		print("Advices and Suggestions for Cold\n 1: 1: Chloramphenicol\n 2: Amoxicillin\n3: Ciprofloxacin\n4: Azithromycin\nPlease do complete bed rest and take soft diet because")


check_disease()
