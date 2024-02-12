from PIL import Image, ImageDraw
import numpy as np
import cv2

## 1. Verify image

def check_image_happinnes(image) :
    """
    Checks if the colors of a PIL image give a "happy" feeling by evaluating its average brightness.
    Assumes images in RGBA format are input, and converts them for OpenCV processing.
    """

    # Convert PIL image to OpenCV format
    open_cv_image = np.array(image)

    # Since input images are in RGBA and OpenCV uses BGR, we discard the Alpha channel and reorder RGB to BGR
    open_cv_image = open_cv_image[:, :, :-1][:, :, ::-1]

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2HSV)

    # Calculate the average brightness of the image
    average_value = np.mean(hsv_image[:, :, 2])

    # Assuming the midpoint of the brightness scale (0-255) as the threshold
    return average_value > 127


def verify_image(img_path) :
    try:
        # Check if the image is a PNG file
        if not img_path.endswith('.png'):
            return False, "Your image does not meet the criteria : Image is not in PNG format!"

        # Load image
        image = Image.open(img_path)
        image = image.convert("RGBA")

        # Check size
        if image.size != (512, 512):
            return False, "Your image does not meet the criteria : Image size is not 512x512!"

        # Create a circular mask
        mask = Image.new('L', (512, 512), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + mask.size, fill=255)

        # Apply mask and check if any non-transparent pixel is outside the circle
        masked_image = Image.composite(image, Image.new('RGBA', image.size, (0, 0, 0, 0)), mask)
        if masked_image.getbbox() is None :
            return False, "Your image does not meet the criteria : Non-transparent pixels are outside the circle!"

        # Check if thr coulours of the image give a happy feeling
        if not check_image_happinnes(image) :
            return False, "Your image does not meet the criteria : The colours of the badge do not give a 'happy' feeling"

        return True, "Your image meets all the criteria"

    except Exception as e :
        return False, f"Error processing image : {e}"

## 2. Convert image

def convert_image(input_path, output_path):
    try:
        # Load and convert image
        image = Image.open(input_path)
        image = image.resize((512, 512))
        image = image.convert("RGBA")

        # Apply circular mask
        mask = Image.new('L', (512, 512), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + mask.size, fill=255)
        final_image = Image.composite(image, Image.new('RGBA', image.size, (0, 0, 0, 0)), mask)

        # Save converted image
        final_image.save(output_path, "PNG")
        return True, "Your image is converted sucessfully"
    except Exception as e :
        return False, f"Error converting image: {e}"

## 3. Example usage
verify_result, verify_msg = verify_image("avatar.png")
print(verify_msg)

convert_result, convert_msg = convert_image("avatar.png", "result.png")
print(convert_msg)

verify_result2, verify_msg2 = verify_image("result.png")
print(verify_msg2)
