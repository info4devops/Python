# Mathematical Operations for set
s1={10,20,30,40}
s2={11,20,33,40}

# Union: print all the elements present in both sets
result = s1.union(s2) # use s1|s2 as well
print(f'Union result(s1|s2):{result}')

# intersection: print common elements
result = s1.intersection(s2) # use s1&s2 as well:
print(f'intersection result(s1&s2):{result}')

# difference: print different elements in set
# s1.difference(s2) = returns elements present in s1 but not in s2
# s2.difference(s1) = returns elements present in s2 but not in s1

result = s1.difference(s2) # use s1&s2 as well:
print(f'difference result(s1-s2):{result}')

# symmetric_difference: print different elements in set
# s1.symmetric_difference(s2) = returns elements present in s1 OR s2 but not in both
# s2.symmetric_difference(s1) = returns elements present in s2 OR s1 but not in both

result = s1.symmetric_difference(s2) # use s1&s2 as well:
print(f'symmetric_difference result(s1^s2):{result}')