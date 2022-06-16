# [16]*200+[12]*200+[10]*200+[4]*200+[1]*200
# [0]*200+[0]*200+[6]*200+[8]*200+[4]*200
# 10
# [0.2]*400+[0]*800

text_prompts = {}

evolutions = [
"single celled organism",
"virus",
"fungus",
"clam",
"shrimp",
"octopus",
"scorpion",
"spider",
"crab",
"rat",
"lemur",
"monkey",
"orangutan",
"gorrilla",
"chimpanzee",
"bonobo",
"neanderthal",
"human",
"humanoid robot"
]

for i in range(1, len(evolutions) * 30):
    if i == 0:
        text_prompts[i] = ["Beautiful detailed picture of earth by Nick Silva, Jim Burns, Noah Bradley, Symmetrical composition with people centered, colorized, trending on artstation:4", "text:-2", "glasses:-1", "color:1"],  

    elif (i%25 == 0):
        j = i / 25
        text_prompts[j-1] = [
            "Beautiful detailed portrait of a hyperrealistic "+evolutions[j]+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, greyscale:4",
            "text:-2",
            "glasses:-1"
        ]
