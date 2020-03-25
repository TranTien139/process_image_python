import cv2
import time
from PIL import Image


def resize_image(id):
    img = cv2.imread('./image/' + str(id) + '.png', cv2.IMREAD_UNCHANGED)
    width = 750
    height = (width / img.shape[1]) * img.shape[0]
    dim = (width, int(height))
    print(dim, "dim")
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite('./images/' + str(id) + '.png', resized)
    print('success: ', id)


for i in range(1, 262):
    resize_image(i)
    time.sleep(2)




