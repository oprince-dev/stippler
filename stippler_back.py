from PIL import Image, ImageDraw
import numpy as np

# background mid grey
# white gets largest radius and magneticism
# circles creator class
# itterate over brightness values
# brightness/255 -> 0 -> 1
# radius_factor


def main():
    def load_image():
        img = Image.open('./portrait2.jpg', mode="r").convert("L")
        return img

    def read(img):
        arr = np.array(img)
        # arr[arr <= 25] = 0
        return arr

    def create_canvas(img):
        w = img.width
        h = img.height
        background = ImageDraw.Draw(img)
        background.rectangle((0, 0, w, h), fill=(25), outline=(25))

#    def create_circles(img, arr):
#        circles = ImageDraw.Draw(img)
#        w = img.width
#        h = img.height
#        d = 20
#        cw = w / 10.0
#        ch = h / 10.0
        # hc = round((img.width) / 10) + 1

#       Need to obtain value -> calculate radius -> use radius to find next pixel in array

#        for y in range(int(ch)):
#            if y % 2 == 0:
#                for x in range(int(cw)):
#                    if x % 2 == 0:
#                        index = x + y * w
#                        value = int(arr[y*10, x*10])
#                        print(str(x) + " " + str(y) + " " + str(value))
#                        if value > 0:
#                            circles.ellipse((x*10, y*10, x*10+d, y*10+d),
#                                            fill=(value), outline=(value))
        # circles.ellipse((x*5, y*5, (x*5)+r, (y*5)+r), fill=(255), outline=(255))
#                else:
# s                    pass

        # for x in np.nditer(arr):
        # if x != 0:
        # new_dot = Dot(x)
        # new_dot.radius_calculate()
        # new_dot.create_dot()

    class Dot(object):
        def __init__(self, value):
            self.value = value

        def radius_calculate(self):
            self.factor = round((self.value / 255), 2)

        # def create_dot(self):

    img = load_image()
    arr = read(img)
    create_canvas(img)
    #create_circles(img, arr)


if __name__ == "__main__":
    main()
