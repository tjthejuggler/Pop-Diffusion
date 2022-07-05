zoom_input = "0: (0.998),"#@param {type:"string"}
for i in range(3000):
  if i > 0:
    j = i % 240
    
    if j == 0:
        if (i//240) % 2 == 0:
            zoom_input += str(i-1)+": (0.998),"+str(i)+": (1.002),"
        else:
            zoom_input += str(i-1)+": (1.002),"+str(i)+": (0.998),"

print(zoom_input)