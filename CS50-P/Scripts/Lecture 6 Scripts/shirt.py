"""
GOALS:
- implement a program that expects exactly two command-line arguments
    - in sys.argv[1], the name of an image file to read as input
    - in sys.argv[2], the name of an image file to save as output
- the program should overlay shirt.png on the input file after resizing and cropping the input to be the same size
- save result as output
"""

import os
import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("ERROR: Missing pathway for output")
    elif len(sys.argv) > 3:
        sys.exit("ERROR: Too many arguments")

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    input_ext = os.path.splitext(inputfile)[1]
    output_ext = os.path.splitext(outputfile)[1]

    
    try:
        if input_ext.lower() not in [".jpeg", ".jpg", ".png"]:
            sys.exit("ERROR: Must enter .jpeg, .jpg, or .png file as argument.")
        if output_ext != input_ext:
            sys.exit("ERROR: Must enter output file type asme as input file type.")
        else:
            with Image.open("shirt.png") as shirt_img, Image.open(inputfile) as input_img:
                #find shirt size to make input fit
                shirt_size = shirt_img.size

                fitted_image = ImageOps.fit(input_img, shirt_size)

                #paste shirt on top of input image
                fitted_image.paste(shirt_img, (0,0), shirt_img)
            
                fitted_image.save(outputfile)
    except FileNotFoundError:
        sys.exit("ERROR: file not found")

main()

