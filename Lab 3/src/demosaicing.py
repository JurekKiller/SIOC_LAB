import numpy as np
from numpy.typing import NDArray
from src.convlotuion import apply_convolution

def uniwersal_demosaic(image: NDArray, filter_set: dict[str, NDArray]) -> NDArray:
    
    if image.ndim != 3 or image.shape[2] != 3: 
        raise ValueError("Input image must be a 3D array with 3 color channels (RGB).")

    if not all(channel in filter_set for channel in ['red', 'green', 'blue']):
        raise ValueError("Filter set must contain 'red', 'green', and 'blue' filters.")

    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]

    R_interp = apply_convolution(R, filter_set['red'], padding=0)
    G_interp = apply_convolution(G, filter_set['green'], padding=0)
    B_interp = apply_convolution(B, filter_set['blue'], padding=0)

    demosaiced_image = np.stack([R_interp, G_interp, B_interp], axis=-1)
    return demosaiced_image
