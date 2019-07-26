def image2vector(image):
    """ Input image to receive a vector output of the image in the form of (something, 1)"""
    return image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)
