import os
import pathlib
import shutil
import numpy as np
import pandas as pd
import random
import config

random.seed(10)

# "./data/train"
def split_train_valid_set(image_dir, output_path):
    """
    Split data into trains set and validation set
    Output is 2 csv files which contain list of image names
    """
    files = np.array([f for f in image_dir.glob("*.png")])

    # shuffle index
    indices = np.random.permutation(len(files))
    # split train (80%) and valid set (20%)
    train_idx, valid_idx = indices[:int(len(files)*0.8)], indices[int(len(files)*0.8):]
    train_set, valid_set = files[train_idx], files[valid_idx]

    # store list images of dataset
    train_imgs = [i.name for i in train_set]
    valid_imgs = [i.name for i in valid_set]
    pd.DataFrame(train_imgs, columns=["filenames"]).to_csv(output_path/"train_set_images.csv", index=False)
    pd.DataFrame(valid_imgs, columns=["filenames"]).to_csv(output_path/"valid_set_images.csv", index=False)

    return train_set, valid_set

def create_image_foler(img_paths,output_dir):
    """
    Create image folder and copy image into this folder
    """
    if os.path.isdir(output_dir):
        # remove folder if exist
        shutil.rmtree(output_dir)
    # create new folder
    os.mkdir(output_dir) 
    for img_path in img_paths:
        print(f"Copying {img_path}...")
        shutil.copy(img_path, output_dir/img_path.name)

if __name__ == "__main__":
    train_imgs, valid_imgs = split_train_valid_set(config.image_dir, config.image_dir.parent.parent)
    create_image_foler(train_imgs, config.train_folder)
    create_image_foler(valid_imgs, config.valid_folder)

    