def intersect(lst1, lst2): 
	return list(set(lst1) & set(lst2)) 

lst1 = [4,9,5] 
lst2 = [9,4,9,8,4] 
print(intersect(lst1, lst2))