# Coursera HW
# E-mail Data에서 시간 Data 추적 후 각 '시간'별 E-mail 횟수 출력

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

x = dict()
lst = []

for lines in handle :
    if lines.startswith('From ') :
        words = lines.split()
        time = words[5]
        date = time.split(':')
	lst.append(date[0])

for counts in lst :
    x[counts] = x.get(counts,0) + 1


for k,v in sorted(x.items()) :
    print(k,v)