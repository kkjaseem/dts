def intersect(lst1, lst2): 
	return list(set(lst1) & set(lst2)) 

lst1 = [1,2,2,1] 
lst2 = [2,2] 
print(intersect(lst1, lst2))