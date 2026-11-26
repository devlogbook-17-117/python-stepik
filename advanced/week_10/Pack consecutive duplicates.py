# Group consecutive identical elements into sublists

n = input().split()  # read space-separated elements as a list
result = []

for elem in n:
    # if elem matches the last group, add it to that group
    if result and elem == result[-1][-1]:
        result[-1].append(elem)
    else:
        # otherwise, start a new group
        result.append([elem])


print(result)