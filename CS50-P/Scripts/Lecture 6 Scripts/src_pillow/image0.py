from PIL import Image

#open and close file
def main():
    img = Image.open("in.jpeg")
    img.close()


main()
