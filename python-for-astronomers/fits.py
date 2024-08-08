import os

import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import astropy_mpl_style

plt.style.use(astropy_mpl_style)

# http://data.astropy.org/tutorials/FITS-images/HorseHead.fits
image_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "HorseHead.fits")

# hdu_list = fits.open(image_file)
# hdu_list.info()
# image_data = hdu_list[0].data
# print(type(image_data))
# print(image_data.shape)
# hdu_list.close()

image_data = fits.getdata(image_file)
# print(type(image_data))
# print(image_data.shape)

plt.imshow(image_data, cmap="gray")
plt.colorbar()
