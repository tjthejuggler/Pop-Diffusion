import re
absolute_multiplier = 5

def absolute_key_frame_multiplier(original_string):
    #if there is no colon in the string, return the original string
    if not re.search(':', original_string):
        return original_string
    #if original_string doesn't include decimals
    if not re.search('\.', original_string):
        multiplied_string = re.sub(r'\d+', lambda x: str(int(x.group(0)) * absolute_multiplier), original_string)
        #print('mult',multiplied_string)
    #divide all numbers in parentheses by absolute_multiplier
        return re.sub(r'\((\d+)\)', lambda x: '(' + str(int(x.group(1)) // absolute_multiplier) + ')', multiplied_string)
    else:
        #get all non-float numbers in the string
        non_floats = re.compile("(?<![\.\d])[0-9]+(?![\.\d])")
        #sub all non-floats with themselves times absolute_multiplier
        return re.sub(non_floats, lambda x: str(int(x.group(0)) * absolute_multiplier), original_string)

print(absolute_key_frame_multiplier("2"))
print(absolute_key_frame_multiplier("0.2"))
print(absolute_key_frame_multiplier("0:(0.0),2:(1.0),12:(0.4)"))
print(absolute_key_frame_multiplier("0:(10),2:(99),12:(55)"))


#a sample dict with integer keys
d = {1: 'one', 2: 'two', 3: 'three'}
#get the value of the highest key that is less than 3
print(d.get(max(k for k in d if k < 3)))





