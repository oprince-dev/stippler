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
        return arr

    def create_artboard(img):
        w = img.width
        h = img.height
        background = ImageDraw.Draw(img)
        background.rectangle((0, 0, w, h), fill=(25), outline=(25))
        canvas = ImageDraw.Draw(img)
        return canvas

    def init_dot_creation(arr, img, canvas):
        print(canvas)
        canvas.show()
        thresh = 10
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                value = arr[y, x]
                dot = Dot(value, x, y, thresh)
                dot.find_diameter()
                dot.place_dot(canvas)

        # def value_iterate(arr):
        #    thresh = 10
        #    buffer = []
        #    for i in np.nditer(arr):
        #        if i <= thresh or buffer:
        #            if buffer:
        #                buffer.pop()
        #                continue
        #            else:
        #                continue
        #        else:
        #            print("found dot")
        #            dot = Dot(i)
        #            dot.diameter_calculate(thresh)
        #            print("adding " + str(dot.diameter) + " to the buffer")
        #            dot.diameter = 10
        #            for _ in range(dot.diameter):
        #                buffer.append(True)
        #            print(buffer)
        #            dot.create_dot()

    class Dot(object):
        def __init__(self, value, x, y, thresh):
            self.value = value
            self.x = x
            self.y = y
            self.thresh = thresh

        def find_diameter(self):
            self.diameter = int(round((self.value / self.thresh)))

        def place_dot(self, canvas):
            canvas.ellipse((self.x, self.y, (self.x + 10), (self.y +
                                                            10)), fill=(int(self.value)), outline=(int(self.value)))
            return canvas

    img = load_image()
    arr = read(img)
    canvas = create_artboard(img)
    test = init_dot_creation(arr, img, canvas)


if __name__ == "__main__":
    main()
