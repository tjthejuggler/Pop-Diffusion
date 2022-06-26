
#increase x by 1% until it reaches y
from cgitb import small
small_box = [50,60]
big_box = [200,400]

def find_number_of_frames_to_reach_goal(x,y):
    number_of_frames_to_reach_goal = 0
    while x < y:    
        x = x + (x * 0.02)
        number_of_frames_to_reach_goal = number_of_frames_to_reach_goal + 1
        print(number_of_frames_to_reach_goal)
    return number_of_frames_to_reach_goal

num_frames = min(find_number_of_frames_to_reach_goal(small_box[0],big_box[0]),find_number_of_frames_to_reach_goal(small_box[1],big_box[1]))
print(num_frames)
#if we increase the small box by 1% every frame, figure out which frame it will be at the big box
