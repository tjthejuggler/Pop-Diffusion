from pickle import HIGHEST_PROTOCOL


text_prompts= {
        0: [
            "girl detailed portrait of an adorable egyptian baby girl by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:4",
            "text:-2",
            "glasses:-1",
            "color:1"
        ],
        1: [
            "DÜNYA DÖNÜYOR detailed portrait of an adorable egyptian baby girl by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:4",
            "text:-2",
            "glasses:-1",
            "color:1"
        ],
        2: [
            "guy det trending on artstation, colorized:2",
            "text:-2",
            "glasses:-1",
            "color:1"
        ]
    }
print(text_prompts)

# looop through each item in the dictionary
# you get the sum of the weights of the items in the list

#loop through each item in the dictionary
for key, value in text_prompts.items():
    #loop through each item in the list
    sum_number=0
    for item in value:
        #split the item into a list
        item_list = item.split(":")
        #get the weight of the item
        weight = int(item_list[1])
        #add the weight to the sum
        sum_number += weight
    if sum_number == 0:
        new_first_weight=int(value[0].split(":")[1])+1
        value[0] = value[0].split(":")[0] + ":" + str(new_first_weight)
    print(sum_number)
    #if the sum is equal to 0, then make the first item HIGHEr

 
    #reset the sum to 0
    # sum = 0
    #loop through each item in the list

print(text_prompts)