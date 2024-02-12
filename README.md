# Tech Assessment

We want to allow users to upload a personalized badge, encapsulated within a circle, that not only meets certain technical criteria but is also crafted to convey a feeling of happiness and positivity.

## Author : MANSSOURI OUSSAMA

## Features

- **Image Format Verification**: Checks if the input image is in PNG format.
- **Image Size Verification**: Validates that the image's dimensions are exactly 512x512 pixels.
- **Shape Verification**: Ensures that non-transparent pixels are within a predefined circular area.
- **Color Brightness Check**: Analyzes the image to determine if the colors are bright enough to give a "happy" feeling, based on average brightness.

## Implementation

The system is implemented in Python, utilizing the Pillow (PIL) library for basic image manipulation (e.g., loading images, converting formats, and applying masks) and OpenCV for more advanced image processing tasks (e.g., color space conversion and brightness analysis).

### Key Functions

- `check_image_happiness(image)`: Analyzes the image's color brightness to assess if it gives a "happy" feeling.
- `verify_image(img_path)`: Verify the image's format, size, shape, and color brightness

### Usage 
```
result, message = verify_image("path/to/image.png")
print(message)

result, message = convert_image("path/to/init_image.png", "path/to/result_image.png")
print(message)
```