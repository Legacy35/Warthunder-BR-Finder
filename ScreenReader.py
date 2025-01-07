import pygetwindow as gw
import pyautogui
from PIL import Image
import easyocr

def capture_application_screenshot(app_name, output_file):
    try:
        # Find the application window by its title
        windows = gw.getWindowsWithTitle(app_name)
        if not windows:
            raise Exception(f"No application with title '{app_name}' found.")

        # Assume the first matching window is the desired one
        app_window = windows[0]

        # Get the application window's position and size
        left, top, width, height = app_window.left, app_window.top, app_window.width, app_window.height

        # Capture the screenshot of the specified region
        screenshot = pyautogui.screenshot(region=(left, top, width, height))

        # Save the screenshot
        screenshot.save(output_file)

    except Exception as e:
        print(f"Error: {e}")

def get_list_of_friendly_planes_from_screenshot(image_path,roi):
     try:
        print("test")
        # Initialize the EasyOCR reader (use 'en' for English)
        reader = easyocr.Reader(['en'])

        # Open the image
        img = Image.open(image_path)

        # Crop the image to the ROI if provided
        if roi:
            x, y, width, height = roi
            img = img.crop((x, y, x + width, y + height))

        # Convert the cropped image to a format EasyOCR can process
        img.save("temp_image_for_ocr.png")  # Save temporarily for EasyOCR processing

        # Perform OCR using EasyOCR
        results = reader.readtext("temp_image_for_ocr.png")

        # Extract and return the detected text
        names = [text for _, text, _ in results]
        print(names)
        return names

     except Exception as e:
        print(f"Error: {e}")
        return []


import cv2

def is_matching_progress_bar(base_image_path, template_image_path, roi, threshold=0.8):
    # Open the image
    img = Image.open(base_image_path)
    # Crop the image to the ROI if provided
    if roi:
        x, y, width, height = roi
        img = img.crop((x, y, x + width, y + height))

    # Convert the cropped image to a format EasyOCR can process
    img.save("temp_image_for_ocr_bar.png")  # Save temporarily for EasyOCR processing
    # Load the base image and template
    base_image = cv2.imread(base_image_path, cv2.IMREAD_GRAYSCALE)
    template = cv2.imread(template_image_path, cv2.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv2.matchTemplate(base_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match is above the threshold
    return max_val >= threshold