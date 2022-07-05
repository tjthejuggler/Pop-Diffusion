def calculate_number_of_frames_from_interpolation(interpolation_number):
    return (2 ** (interpolation_number) - 1)

for i in range (5):
    print(calculate_number_of_frames_from_interpolation(i))