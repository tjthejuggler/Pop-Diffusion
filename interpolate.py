import os

number_of_interpolated_frames = 0
if os.path.exists("../Pop-Diffusion"):
    number_of_interpolated_frames=len(os.listdir("../Pop-Diffusion"))
    print('real_frame_number', number_of_interpolated_frames)