directory = '/content/drive/MyDrive/AI/Object_Detection/request'

#if directory does not exist, create it
if not os.path.exists(directory):
    os.makedirs(directory)

#while directory is empty
while len(os.listdir(directory)) == 0:
    time.sleep(1)
#get the name of the file in the directory
file_name = os.listdir(directory)[0]
download_and_resize_image(f'/content/drive/MyDrive/AI/Object_Detection/request/{file_name}', 1280, 856, True)