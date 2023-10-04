from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """uses the load image function and prints the zoomed image
after slicing"""
    image = ft_load("animal.jpeg")
    print(image)
    zoom_image = image[:400, 400:800, :1]
    print("New shape after slicing: ", zoom_image.shape, end=' ')
    print("or", zoom_image.shape[:2])
    print(zoom_image)
    plt.imshow(zoom_image, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
