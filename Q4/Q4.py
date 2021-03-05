Input = input("Input:")
stack=[]
def singleNumber(Input):
        
        hash_table = {}
        for i in Input:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
        
print(f'Output:{singleNumber(Input)}')
