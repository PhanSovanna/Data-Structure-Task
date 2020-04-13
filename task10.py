import collections

n = int(input())
arr = []
for i in range(0, n):
    person, sport = input().split(" ")
    arr.append({'person':person,'sport': sport})

new_arr = [dict(t) for t in {tuple(d.items()) for d in arr}]
unique_counts = collections.Counter(e['sport'] for e in new_arr)

print(list(unique_counts.keys())[0])
print(unique_counts['football'])