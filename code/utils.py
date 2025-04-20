import os

import torch
from torch.utils.data import Dataset
from PIL import Image
from datetime import datetime



class CustomDataset(Dataset):
    def __init__(self, df_data, img_dir, transform=None, N_LABELS=10, with_label=True):
        """
        Create dataset for model
        Input:
        df_data: df contain image names and tagets
        img_dir: image folder directory
        transform: transform pipeline
        """
        self.data = df_data
        self.data_dir = img_dir
        self.transform = transform
        self.nb_labels = N_LABELS
        self.with_label = with_label

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        if self.with_label:
            img_name, labels = self.data.iloc[idx,:]
            img_path = self.data_dir/img_name
            # image to tensor
            image = Image.open(img_path)
            image = self.transform(image)
            # hot encoder target
            labels = list(map(int, labels.split(' ')))
            target = torch.zeros(self.nb_labels)
            target[labels] = 1.
            return image, target, img_name
        else:
            img_name = self.data.iloc[idx,0]
            img_path = self.data_dir/img_name
            image = Image.open(img_path)
            image = self.transform(image)
            return image, img_name

        
        

def create_save_dir(model_dir, model_name):
    string_name = datetime.now().strftime("_%m%d")
    output_dir = model_dir/(model_name+string_name)
    if not(os.path.isdir(output_dir)):
        os.mkdir(output_dir)
        os.mkdir(output_dir/'runs')
    return output_dir    

def save_checkpoint(state, output_dir, epoch): 
    f_path = output_dir/ f'checkpoint_{epoch}.pt'
    torch.save(state, f_path)

def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = checkpoint['model']
    model.load_state_dict(checkpoint['state_dict'])
    for parameter in model.parameters():
        parameter.requires_grad = False
    model.eval()
    return model