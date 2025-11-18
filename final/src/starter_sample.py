#%%
# %pip install openimages
# 
# %%
# Download Open Images subset
import os
from dataset_utils import download_openimages_subset, preview_imagefolder

output = download_openimages_subset(
    classes=["Dog", "Cat"],
    max_samples=400,
    export_dir=f"..{os.sep}data{os.sep}bigdata{os.sep}open_images_subset"
)

preview_imagefolder(output)
print("Download Done.")



#%%


