import argparse
from rectification import rectification
import pytesseract
import cv2

from template_matching import template_matching

parser = argparse.ArgumentParser(description='Locating bounding box in the image')
parser.add_argument('file', type=str,
                    help='path to file')
args = parser.parse_args()


if __name__ == "__main__":
    # step 1:
    # straighten image and crop paper
    # returns path to rectified image
    crop_img_path = rectification(args.file)
    
    # step 2:
    # get address through template matching
    cropped = cv2.imread(crop_img_path)
    print(pytesseract.image_to_string(cropped))
    
    correct_bottom, correct_top, address = template_matching(cropped)
    print(address)