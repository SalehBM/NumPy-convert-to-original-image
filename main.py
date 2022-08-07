import numpy as np
from IPython.display import display
from PIL import Image

img = Image.open('image.png')

img_array = np.array(img)

mask = np.full(img_array.shape, 255)

color_img = np.subtract(mask, img_array).astype(img_array.dtype)

Image.save("new_img.png")
