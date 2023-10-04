import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


def main():
    """loads the image using the load function,
prints the zoomed image after slicing, transposes the image,
and outputs the transposed image"""
    image = ft_load("animal.jpeg")
    cut_image = image[:500, 300:800, :1]
    print("The shape of the image is:", cut_image.shape, end=' ')
    print("or", cut_image.shape[:2])
    print(cut_image)
    rot_cut_image = [cut_image[:, i, 0] for i in range(450)]
    rot_cut_image = np.array(rot_cut_image)
    print("New shape after Transpose: ", rot_cut_image.shape[:2])
    print(rot_cut_image)
    plt.imshow(rot_cut_image, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
