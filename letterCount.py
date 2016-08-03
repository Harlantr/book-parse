import operator
import time

start = time.time()
 
doc = open('letterCount.txt', 'r')
txt = filter(lambda x: x.isalpha(), doc.read().lower())
test
dic = {}
for c in txt:
	if not c in dic:
		dic[c] = 1
	else:
		dic[c] += 1

sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)

results_file = open('letterCountResults.txt', 'w')
result = ''
for key, value in sorted_dic:
	result += key + ': ' + str(value) + '\n'
results_file.write(result)

end = time.time()
print (end - start)