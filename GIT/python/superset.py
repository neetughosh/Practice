# Enter your code here. Read input from STDIN. Print output to STDOUT
superset = set(input().split())
nbr_of_subset = int(input())

status = "True"
for i in range(nbr_of_subset):
    sets = set(input().split())
    
    if not(superset.issuperset(sets) and len(sets) < len(superset)): 
        status = "False"
        break
print(status)    