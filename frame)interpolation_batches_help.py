if should_interpolate:
  #@markdown # 3. Interpolate!
  #@markdown Results will be saved in a subdirectory of `frames_dir` named "interpolated_frames"

  from loguru import logger
  
  number_of_images_to_be_interpolated = len(os.listdir(f"{frames_dir}"))
  number_of_images_to_be_interpolated_per_batch = number_of_interpolations_per_batch // number_of_interpolations
  #use shutil to copy every image in {frames_dir} to {frames_dir}/waiting_for_interpolation {frames_dir}
  


  isExist = os.path.exists(f"{frames_dir}/waiting_for_interpolation")
  if not isExist:
    os.makedirs(f"{frames_dir}/waiting_for_interpolation")
  


  for file in os.listdir(f"{frames_dir}"):
    if file.endswith(".png"):
      shutil.copy(f"{frames_dir}/{file}", f"{frames_dir}/waiting_for_interpolation")
         
    

  #make a folder called 'this_interpolation_batch'
  !mkdir -p {frames_dir}/interpolated_frames/this_interpolation_batch 
  #while there are still files in {frames_dir}/waiting_for_interpolation
  while len(os.listdir(f"{frames_dir}/waiting_for_interpolation")) > 0:
    isExist = os.path.exists(f"{frames_dir}/waiting_for_interpolation/this_interpolation_batch")
    if not isExist:
      os.makedirs(f"{frames_dir}/waiting_for_interpolation/this_interpolation_batch")
    #move the first {number_of_images_to_be_interpolated_per_batch} files from {frames_dir}/waiting_for_interpolation to {frames_dir}/interpolated_frames/this_interpolation_batch
    for i in range(number_of_images_to_be_interpolated_per_batch):
      if len(os.listdir(f"{frames_dir}/waiting_for_interpolation")) > 0:
        file = os.listdir(f"{frames_dir}/waiting_for_interpolation")[1]
        shutil.move(f"{frames_dir}/waiting_for_interpolation/{file}", f"{frames_dir}/interpolated_frames/this_interpolation_batch/{file}")

    logger.info("Beginning interpolation...")
  
    !python -m frame_interpolation.eval.interpolator_cli \
        --model_path ./saved_model \
        --pattern f"{frames_dir}/interpolated_frames/this_interpolation_batch \
        --fps {output_video_fps} \
        --times_to_interpolate {number_of_interpolations}

    cmd = [
        'python',
        '-m',
        'frame_interpolation.eval.interpolator_cli',
        '--model_path',
        '--pattern',
        f'{frames_dir}/interpolated_frames/this_interpolation_batch',
        '--fps',
        str(output_video_fps),
        '--times_to_interpolate',
        str(number_of_interpolations),
    ]

    process = subprocess.Popen(cmd, cwd=f'{gdrive_mountpoint}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    logger.info("Interpolation comlpete.")

    #remove all files from {frames_dir}/interpolated_frames/this_interpolation_batch
    shutil.rmtree(f"{frames_dir}/waiting_for_interpolation/this_interpolation_batch")


  # if output_video:
  #   !python -m frame_interpolation.eval.interpolator_cli \
  #       --model_path ./saved_model \
  #       --pattern {frames_dir} \
  #       --fps {output_video_fps} \
  #       --times_to_interpolate {number_of_interpolations} \
  #       --output_video
        

  # else:
  #     !python -m frame_interpolation.eval.interpolator_cli \
  #       --model_path ./saved_model \
  #       --pattern {frames_dir} \

  #logger.info("Interpolation comlpete.")