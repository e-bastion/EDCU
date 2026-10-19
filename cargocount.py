import json, os


def listing():
	comparitor1 = []
	for k, v in comparitor.items():
		if deductor[k] != 0:
			newkey1 = k[0:3].lower()
			while newkey1 in comparitor1:
				newkey1 += "+"
			comparitor1.append(newkey1)
			print(f"({newkey1}) {v}: {deductor[k]}")
	print("")


while 1:
	capacity_input = input("cargo capacity: ")
	try:
		capacity_input = int(capacity_input)
		break
	except ValueError:
		os.system("cls")
		print("wrong value, try again")

capacity_flag = 1
with open("cargo.json", "r") as file:
	data = json.load(file)
	comparitor0 = {}
	for k in data:
		newkey0 = k[0:3].lower()
		if newkey0 == "t3 ":
			newkey0 = "t3"
		if "Secondary" in k:
			newkey0 += "2"
		while newkey0 in comparitor0:
			newkey0 += "+"
		comparitor0[newkey0] = k
		total_weight = sum(data[k].values())
		print(f"({newkey0}) {k}: {total_weight}")
	while 1:
		goal = input("\nproject: ")
		#
		if goal in comparitor0:
			goal = comparitor0[goal]
			break
		else:
			print("no such project")

	os.system("cls")
	comparitor = {}
	deductor = {}

	for k1 in data[goal]:
		newkey = k1[0:3].lower()
		comparitor[newkey] = k1
		deductor[newkey] = data[goal][k1]
	listing()
	print(f"selected goal - {goal}")
	while 1:
		if capacity_flag == 1:
			capacity = capacity_input
		query = input(f"delivering {capacity}: ")
		if query == "exit":
			break
		os.system("cls")
		if query in deductor:
			if deductor[query] >= capacity:
				deductor[query] -= capacity
				listing()
				print(f"delivered {capacity} {comparitor[query]}, {deductor[query]} remaining")
				capacity_flag = 1
			else:
				capacity -= deductor[query]
				if deductor[query] == 0:
					listing()
					print("already at zero you drunk fuck")
				else:
					deductor[query] = 0
					listing()
					print(f"filled {comparitor[query]}, enter next commodity or (r) to reset capacity")
				capacity_flag = 0
		else:
			listing()
			if query == "r":
				print("capacity has been reset")
				capacity_flag = 1
			else:
				print("wrong query, try again or (r) to reset capacity")
		if all(value == 0 for value in deductor.values()):
			os.system("cls")
			print(f"congratulations on finishing the {goal}!\npress any key to exit")
			input()
			break
