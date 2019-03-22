import numpy as np

def image_center_crop(img):
    """
    Single image center-cropper
    _____________________________________________________________
    Takes a 3D image with shape (h, w, c) as np.array and 
    returns a centered image with shape (min(h, w), min(h, w), c)
    """
    
    edge = np.min(img.shape[:2])

    h, w, c = img.shape
    
    cropped_img = img[int(h/2 - edge/2):int(h/2 + edge/2), int(w/2 - edge/2):int(w/2 + edge/2 ), :]
    
    return cropped_img
