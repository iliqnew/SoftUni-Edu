ints = input().split(", ")
beggars_count = int(input())
print([sum([int(ints[ind]) for ind in range(i-1, len(ints), beggars_count)]) for i in range(1, beggars_count+1)])
