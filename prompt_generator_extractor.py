from requests import get
import os
import json
dir = os.path.dirname(os.path.realpath("_file_"))
print(dir)
dir = '/content/drive/MyDrive/Colab Notebooks'
filename = get('http://172.28.0.2:9000/api/sessions').json()[0]['name']
print(dir +'/' + filename)
with open(dir +'/' + filename, 'r') as f:
    s = f.read()
    print(s)
json_file=open(dir +'/' + filename)
data = json.load(json_file)
full_source_code_list= data["cells"][0]["source"]
prompt_generator_list=[]
should_append_string_to_prompt_generator_list=False
for string in full_source_code_list:
  if '#this comment is used to indicate the end of prompt creation DONT CHANGE!!!!' in string:
    break
  if should_append_string_to_prompt_generator_list:
      prompt_generator_list.append(string)
  elif '#this comment is used to indicate the beginning of prompt creation DONT CHANGE!!!!' in string:
      should_append_string_to_prompt_generator_list=True
print(prompt_generator_list)
with open(batch_name+"_prompt_generator.txt", "w") as output:
    output.writelines(prompt_generator_list)
    output.close()
if not os.path.exists("all_prompt_generator.txt"):
 f=open("all_prompt_generator.txt","w")
with open("all_prompt_generator.txt", "r") as output:
    f=output.read()
all_data_to_write = f + "\n"
all_data_to_write += "-----------\n"
all_data_to_write+=batch_name+"\n"
for line in prompt_generator_list:
  all_data_to_write += line
with open("all_prompt_generator.txt", "w") as output:
   output.write(all_data_to_write)