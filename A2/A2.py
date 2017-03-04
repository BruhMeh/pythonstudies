import re

#path = "regex_sum_42.txt"
path = "regex_sum_349429.txt"
fh = open(path)
total = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) == 0 : continue
    total += sum (int(number) for number in numbers)
print(total)
