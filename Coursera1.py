name = input("Enter file:")
if len(name) < 1:	# Enter만 누르면 file name을 'mbox-short.txt'로 해줌 (Default)
    name = "mbox-short.txt"
handle = open(name)

b = []

for line in handle :
    if line.startswith('From ') :
        a = line.split()
        b.append(a[1])
        
x = dict()

for words in b :
	x[words] = x.get(words,0) + 1
        
bigcount = None
bigword = None

for k,v in x.items() :
	if bigcount is None or v > bigcount :
		bigword = k
		bigcount = v
        
print(bigword, bigcount)