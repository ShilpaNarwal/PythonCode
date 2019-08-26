# Python code to merge dict using update() method 
def Merge(dict1, dict2): 
    for x in dict2:
        if x in dict1:
            if isinstance(dict2[x], dict):
                Merge(dict1[x],dict2[x])
            elif isinstance(dict2[x], list):
                dict1[x].extend(dict2[x])
            else:
                dict1[x]=dict2[x]
        else:
            dict1[x]=dict2[x]

      

dict1 = {'a': 1, 'b': {'c': 3, 'd': [4, 5, 6]}, 'f': 7}  
dict2 = {'a': 1, 'c': 9, 'b': {'d': [8]}}
  

Merge(dict1, dict2)
print(dict1)
  