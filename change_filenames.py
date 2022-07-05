import os

directory = '/home/lunkwill/Downloads/famous_people_bubbles4interp'
#loop through every png file in the directory
for filename in os.listdir(directory):
    #if the file is a png file
    if filename.endswith(".png"):
        if 'fuck' in filename:
            new_filename = filename.replace('fuck','')
            os.rename(directory+'/'+filename, directory+'/'+new_filename)
        # #get the number out of the filename
        # number = filename.split('_')[-1].split('.')[0]
        # #convert the number to an integer
        # number = int(number)
        # if number > 41:
        #     new_number = number - 6
        #     #replace the number in filename with the new number
        #     new_filename = filename.replace(str(number), str(new_number))
        #     #change the filename in the directory
        #     os.rename(directory + '/' + filename, directory + '/' + 'fuck'+ new_filename)
