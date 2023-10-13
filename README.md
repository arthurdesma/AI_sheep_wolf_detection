# Project Overview

This project encompasses a range of functionalities related to image and video processing, particularly focusing on the detection and classification of certain animals in images.

## Content

### 1. Image Classification (`ia_v1.py` & `IA.ipynb`)
- Utilizes the VGG16 model from TensorFlow's Keras library for image classification.
- Specifically, detects animals such as 'coyote', 'timber_wolf', 'white_wolf', 'red_wolf', and 'Irish_wolfhound'.

### 2. Video Processing (`video.ipynb`)
- Splits videos into frames at specified intervals.
- Useful for extracting images from video footage for further analysis.

## Dependencies

To set up the project, you'll need the following dependencies:

```bash
pip install tensorflow keras opencv-python Pillow
```


## Usage
### Image Classification

Use the `classify_image(image_path)` function, providing the path to your image. The function will return whether one of the specified animals is detected and its associated probability.


### Video Processing
To process videos and extract frames at specified intervals, follow these steps:

1. Use the `decouper_video` function.
2. Provide the `video_path` which is the path to your video.
3. Specify the `output_folder` which is the directory where you want the extracted frames to be saved.
4. Set the `interval` which is the time interval (in seconds) between frames that should be saved.

Example:
```python
video_path = "path_to_your_video.mp4"
output_folder = "desired_output_directory"
interval = 1  # Extracts a frame every 1 second
decouper_video(video_path, output_folder, interval)
```
