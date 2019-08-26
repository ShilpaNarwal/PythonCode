# Python code to merge dict using update() method 
def Merge(dict1, dict2): 
    for x in dict2:
        if x in dict1:
            if isinstance(dict2[x], list):
                dict1[x].extend(dict2[x])
            else:
                dict1[x]=dict2[x]
        else:
            dict1[x]=dict2[x]

      

dict1 = {'a':1, 'b':2, 'd':4, 'e':[5,6,8]} 
dict2 = {'c':3, 'd':11, 'e':[9,10]}
  

Merge(dict1, dict2)
print(dict1)
  