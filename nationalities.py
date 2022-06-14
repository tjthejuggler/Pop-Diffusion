nationalities = ["Afghan","Algerian","Angolan","Argentine","Austrian","Australian","Bangladeshi","Belarusian","Belgian","Bolivian","Bosnian/Herzegovinian","Brazilian","British","Bulgarian","Cambodian","Cameroonian","Canadian","Central African","Chadian","Chinese","Colombian","Costa Rican","Croatian","Czech","Congolese","Danish","Ecuadorian","Egyptian","Salvadoran","English","Estonian","Ethiopian","Finnish","French","German","Ghanaian","Greek","Guatemalan","Dutch","Honduran","Hungarian","Icelandic","Indian","Indonesian","Iranian","Iraqi","Irish","Israeli","Italian","Ivorian","Jamaican","Japanese","Jordanian","Kazakh","Kenyan","Lao","Latvian","Libyan","Lithuanian","Malagasy","Malaysian","Malian","Mauritanian","Mexican","Moroccan","Namibian","New Zealand","Nicaraguan","Nigerien","Nigerian","Norwegian","Omani","Pakistani","Panamanian","Paraguayan","Peruvian","Philippine","Polish","Portuguese","Congolese","Romanian","Russian","Saudi, Saudi Arabian","Scottish","Senegalese","Serbian","Singaporean","Slovak","Somalian","South African","Spanish","Sudanese","Swedish","Swiss","Syrian","Thai","Tunisian","Turkish","Turkmen","Ukranian","Emirati","American","Uruguayan","Vietnamese","Welsh","Zambian","Zimbabwea"]

frames_skip_steps_input = ""
text_prompts = {}
for frame in range(len(nationalities) * 4):
    age = frame//4
    nationality = nationalities[age]
    type = 'senior'
    if age < 5:
        type = 'baby'
    elif age < 12:
        type = 'child'
    elif age < 19:
        type = 'teenager'
    elif age < 55:
        type = 'adult'
    elif age < 65:
        type = 'elderly person'
    
    text_prompts[frame] = ["Beautiful detailed portrait of a "+str(age)+" day old "+nationality+" "+type+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation:4",
    "text:-2", "glasses:-1", "color:1" ]
    #frames_skip_steps_input = "1: (85), 50: (65), 100: (85)" #@param{type: 'string'}
    if frame > 0:
        if frame%4 == 0:
            frames_skip_steps_input += str(frame)+":(40),"
        elif frame%4 == 1:
            frames_skip_steps_input += str(frame)+":(60),"
        elif frame%4 == 3:
            frames_skip_steps_input += str(frame)+":(80),"

frames_skip_steps_input = frames_skip_steps_input[:-1]
frames_skip_steps = absolute_key_frame_multiplier(frames_skip_steps_input)
