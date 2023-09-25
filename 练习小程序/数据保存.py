#2020年12月10日20:24:53
import json
numbers=[1,3,5,7,9,11]
filename='numbers.jason'
with open(filename,'a') as f:
    json.dump(str(numbers)+'\n',f)
