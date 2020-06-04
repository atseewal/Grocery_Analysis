#%% Libraries
import cv2
import pytesseract
import os


#%% Pictures location
receipt_directory = 'C:/Users/Drew/Desktop/Grocery_Analysis/temp/'


#%% Output Dict
raw_output = {}


#%% Loop over images in directory
for file in os.listdir(receipt_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        img_string = pytesseract.image_to_string(receipt_directory + filename)
        raw_output[filename] = img_string

#%% Associate Savings with the correct row

# Create an index column
# Filter out anything with Kroger savings to a new df
# subtract 1 from the new df index column
# join to original df to get savings, keep only items, no savings