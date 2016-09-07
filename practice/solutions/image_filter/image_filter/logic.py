"""image_filter Logic."""
from PIL import ImageFilter
from PIL import ImageOps


BLUR_FILTER = ImageFilter.GaussianBlur(2)


def filter_gray(in_image):
    """Convert a PIL image to grayscale."""
    return in_image.convert('L')


def filter_blur(in_image):
    """Blur a PIL image slightly."""
    return in_image.filter(BLUR_FILTER)


def filter_invert(in_image):
    """Invert the colors of a PIL image."""
    return ImageOps.invert(in_image)
