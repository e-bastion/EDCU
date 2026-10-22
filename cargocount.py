import json, os


def listing():
	for k, v in deductor.items():
		if v != 0:
			print(f"({k}) {comparitor[k]}: {v}")
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
error_list = []
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
		goal = input("\nprojects separated by space: ")
		goal_list = goal.split()
		goal_total = []
		for project in goal_list:
			if project in comparitor0:
				goal_total.append(project)
				print(f"added {project}")
			else:
				error_list.append(project)
				print(f"no project named {project}")
		break

	os.system("cls")
	comparitor = {}
	deductor = {}
	# i hate this part so much
	inverted_comparitor = {}
	project_list = []

	for project1 in goal_total:
		full_name = comparitor0[project1]
		project_list.append(full_name)

		for k1 in data[full_name]:
			if k1 in inverted_comparitor:

				deductor[inverted_comparitor[k1]] += data[full_name][k1]
			else:
				newkey = k1[0:3].lower()
				if newkey in comparitor.keys():
					while newkey in comparitor:
						newkey += "+"

				comparitor[newkey] = k1
				inverted_comparitor[k1] = newkey
				deductor[newkey] = data[full_name][k1]

listing()
prettyprint = ", ".join(project_list)
print(f"selected goals - {prettyprint}")
if error_list:
	print(f"{error_list} failed to recognize as projects")
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
				print(f"{comparitor[query]} is already filled, try again")
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
