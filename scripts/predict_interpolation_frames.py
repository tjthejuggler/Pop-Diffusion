def predict_number_of_interpolation_frames(frame_number,interpolation_number):
    for i in range(interpolation_number):
        prediction_number=(frame_number)*2-1
        frame_number=prediction_number
    return prediction_number

print(predict_number_of_interpolation_frames(290,4))