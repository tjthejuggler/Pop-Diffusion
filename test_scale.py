def determine_zoom_scale(box_width, box_height, image_width, image_height, num_iterations):
  if image_width/box_width > image_height/box_height:
    small_number = box_width
    large_number = image_width
  else:
      small_number = box_height
      large_number = image_height 
  percent_increase = (large_number / small_number) ** (1/num_iterations)
  return percent_increase

print(determine_zoom_scale(150, 170, 600, 600, 30))