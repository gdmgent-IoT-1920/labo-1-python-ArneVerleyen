namen = open ("./namen.txt","r")
d = dict()
arr = []
for line in namen: 
	line = line.strip()
	line = line.lower()
	arr.append(line)
print(arr)

for naam in arr:
	aantal = arr.count(naam)
	d[naam] = aantal
print(d)

	

