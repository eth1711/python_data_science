from PIL import Image
import numpy as np


def ft_load(path: str) -> int:
    """opens image using the pillow package, converts
it into array and returns image"""
    assert type(path) is str, "not str"
    image = Image.open(path)
    image = np.asarray(image)
    print("The shape of image is: ", image.shape)
    return image
