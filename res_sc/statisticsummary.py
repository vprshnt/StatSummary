from PIL import Image
import numpy as np
from scipy import stats

image = Image.open('54816.jpg')

gray_image=image.convert('L')

pixel_values = np.array(gray_image)

mean_value=np.mean(pixel_values)
median_value=np.median(pixel_values)
mode_value=stats.mode(pixel_values,axis=None)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")