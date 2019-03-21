import numpy as np

def image_center_crop(img):
    """
    Single image center-cropper
    """
    
    edge = np.min(img.shape[:2])
    cropped_img = img[0:edge, 0:edge, :]
    
    return cropped_img
