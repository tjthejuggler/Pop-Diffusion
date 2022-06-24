import json

json_file=open('sample_text_prompt_dict.txt')
text_prompts = json.load(json_file)
# combine each text_prompts value into a single string seperated by spaces
#print(text_prompts)
def get_unique_text_prompts(original_dict):
    
    def find_largest_common_substring(arr):
        list_length = len(arr)
        reference_item = arr[0]
        reference_item_length = len(reference_item) 
        res = ""
        for i in range(reference_item_length):
            for j in range(i + 1, reference_item_length + 1):
                stem = reference_item[i:j]
                k = 1
                for k in range(1, list_length):
                    if stem not in arr[k]:
                        break
                if (k + 1 == list_length and len(res) < len(stem)):
                    res = stem 
        return res

    unique_text_prompts = {}
    for prompt in original_dict:
        original_dict[prompt] = ' '.join(original_dict[prompt])
    for i in range(2):
        text_prompts_list = list(original_dict.values())
        largest_common = find_largest_common_substring(text_prompts_list)
        for frame in original_dict:
            unique_text_prompts[frame] = original_dict[frame].replace(largest_common, '')
        original_dict = unique_text_prompts.copy()

    return unique_text_prompts

print(get_unique_text_prompts(text_prompts))





 


#print(text_prompts)




# get all the words that every string has in common
# remove these common words from the value strings
# the final dictionary should just have the words that are unique to each value
# the function that does this should be hooked up to 'get_unique_text_prompts()' in the 'make the video' cell