import pydicom
import matplotlib.pyplot as plt

# Spécifiez le chemin de votre image DICOM
image_path = 'chemin/vers/votre/image.dcm'

# Lisez l'image DICOM
ds = pydicom.dcmread(image_path)

# Affichez l'image
plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
plt.axis('off')  # Masquez les axes
plt.show()
