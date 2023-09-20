import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image

# Step 1: Load and convert the image to grayscale
image = Image.open("../../image_data/WhiteDiamond2019.tif").convert('L')
image = np.array(image)

# Step 2: Compute the gradient of the image in the x and y directions
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

ix = ndimage.convolve(image, sobel_x, mode='reflect')
iy = ndimage.convolve(image, sobel_y, mode='reflect')

# Step 3: Compute elements of the structure tensor
i_xx = ix ** 2
i_yy = iy ** 2
i_xy = ix * iy

# Step 4: Apply Gaussian filter to each of these images
gaussian_window_size = 5
i_xx = gaussian_filter(i_xx, gaussian_window_size)
i_yy = gaussian_filter(i_yy, gaussian_window_size)
i_xy = gaussian_filter(i_xy, gaussian_window_size)

# Step 5: Compute the response function R
k = 0.04
det = (i_xx * i_yy) - (i_xy ** 2)
trace = i_xx + i_yy
response = det - k * (trace ** 2)

# Step 6: Perform non-maximum suppression
local_maxima = ndimage.maximum_filter(response, size=5) == response

# Apply a threshold to keep only strong corners
threshold = 0.1 * response.max()
corners = (response > threshold) & local_maxima

# Show the image and the detected corners
plt.imshow(image, cmap='gray')
plt.plot(np.nonzero(corners)[1], np.nonzero(corners)[0], 'ro')
plt.show()
