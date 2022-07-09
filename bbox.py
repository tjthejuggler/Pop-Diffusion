from PIL import Image, ImageDraw, ImageFont

# Image
canvas_width = 200
canvas_height = 200
img_center = (canvas_width/2, canvas_height/2)
img = Image.new('RGB', (canvas_width, canvas_height), (0, 0, 0))

# Drawing
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', 55)
draw.text(img_center, 'Text', (255, 255, 255), font=font, anchor='mm')
draw.rectangle((img.getbbox()[0]-10,img.getbbox()[1]-10,img.getbbox()[2]+10,img.getbbox()[3]+10), fill ="red")
draw.text(img_center, 'Text', (255, 255, 255), font=font, anchor='mm')

#draw = ImageDraw.Draw(img)
img.show()

print('Text at: ', img.getbbox())