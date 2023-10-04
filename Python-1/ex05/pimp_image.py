import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """function that inverts the color of the image"""
    inverted_image = 255 - array
    plt.imshow(inverted_image)
    plt.show()
    return inverted_image


def ft_red(array):
    """function that makes the color of the image red"""
    red_image = array[:, :] * [1, 0, 0]
    plt.imshow(red_image)
    plt.show()
    return red_image


def ft_green(array):
    """function that makes the color of the image green"""
    green_image = array.copy()
    green_image[:, :, 0] = 0
    green_image[:, :, 2] = 0
    plt.imshow(green_image)
    plt.show()
    return green_image


def ft_blue(array):
    """function that makes the color of the image blue"""
    blue_image = array.copy()
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0
    plt.imshow(blue_image)
    plt.show()
    return blue_image


def ft_grey(array):
    """function that makes the color of the image grey"""
    grey_image = array.copy()
    grey_image = np.mean(grey_image, axis=2)
    plt.imshow(grey_image, cmap='gray')
    plt.show()
    return grey_image
