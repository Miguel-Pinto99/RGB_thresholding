import cv2
import easygui


class Get_Data:
    def __init__(self):
        self.image2d = None
        self.initialized = False
        self.frame_2d = None
        self.camera = None

    def get_image_Picture(self, mode):
        """
        This function retrieves an image file for processing.
        :return: the image that was captured or loaded based on the condition of whether the program has been initialized or
        not.
        """

        initialized = self.initialized

        if not initialized:
            path_filename = easygui.fileopenbox(
                title="Select image file",
                default="*.png",
                filetypes=["*.png", "*.jpg", "*.bmp"],
            )

            if path_filename:
                self.initialized = True
                self.image2d = cv2.imread(path_filename, cv2.IMREAD_COLOR)
            else:
                raise ValueError("No file selected")

        image = self.image2d
        if mode == "HSV":
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return image

    def get_image_WebCam(self, mode):
        """
        This function captures images from a webcam, converts them to HSV color space if specified, processes the images,
        displays them, and allows for keyboard interactions.

        :param mode: The `mode` parameter in the `get_image_WebCam` function is used to specify the color space conversion
        mode for the captured image. It can take on the value of 'HSV' to convert the image from BGR to HSV color space
        """

        image2d = self.image2d
        initialized = self.initialized

        if not initialized:
            image2d = cv2.VideoCapture(0)
            self.initialized = True
            self.image2d = image2d

        _, image = image2d.read()
        if mode == "HSV":
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return image
