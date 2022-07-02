import re
absolute_frame_multiplier = 2

def absolute_key_frame_multiplier(original_string):
    #if there is no colon in the string, return the original string
    if not re.search(':', original_string):
        return original_string
    #if original_string doesn't include decimals
    if not re.search('\.', original_string):
        multiplied_string = re.sub(r'\d+', lambda x: str(int(x.group(0)) * absolute_frame_multiplier), original_string)
        print('mult',multiplied_string)
        #divide all numbers in parentheses by absolute_frame_multiplier
        # this brings them back to the original number since we only want to change frame numbers
        return re.sub(r'\((\d+)\)', lambda x: '(' + str(int(x.group(1)) // absolute_frame_multiplier) + ')', multiplied_string)
    else:
        #get all non-float numbers in the string
        non_floats = re.compile("(?<![\.\d])[0-9]+(?![\.\d])")
        #sub all non-floats with themselves times absolute_frame_multiplier
        return re.sub(non_floats, lambda x: str(int(x.group(0)) * absolute_frame_multiplier), original_string)

print("4: (1) ->", absolute_key_frame_multiplier("4: (1)"))