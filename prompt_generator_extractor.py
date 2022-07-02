import os 
project_name="fifth_file"
my_list=['apple','beginning','heloo','sanada hello','ending']
new_list=[]
should_append_string_to_new_list=False
for string in my_list:
  if string=='ending':
    break
  if should_append_string_to_new_list:
      new_list.append(string)
  elif string=='beginning':
      should_append_string_to_new_list=True
print(new_list)
with open(project_name+"_prompt_generator.txt", "w") as output:
    output.writelines(new_list)
    output.close()
if not os.path.exists("all_prompt_generator.txt"):
 f=open("all_prompt_generator.txt","w")
with open("all_prompt_generator.txt", "r") as output:
    f=output.read()
all_data_to_write = f + "\n"
all_data_to_write += "-----------\n"
all_data_to_write+=project_name+"\n"
for line in new_list:
  all_data_to_write += line
with open("all_prompt_generator.txt", "w") as output:
   output.write(all_data_to_write)