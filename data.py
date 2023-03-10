# -*- coding: utf-8 -*-
"""data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yuzJfFsT4aaiAMCT0tC-4ZCej6MG74_J
"""

from model.multi_scale_ori import *
from meta_label import *
import torch
import numpy as np
from torchsummary import summary
import torch.optim as optim
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import tqdm
import torch.nn.functional as F
import sys
import glob

raw_train = glob.glob("./ComMU-code/dataset/commu_midi/train/raw/**")
raw_val = glob.glob("./ComMU-code/dataset/commu_midi/val/raw/**")
train_meta_npy_ = np.load("./ComMU-code/dataset/commu_midi/output_npy_/input_train.npy", allow_pickle=True)
train_midi_npy_ = np.load("./ComMU-code/dataset/commu_midi/output_npy_/target_train.npy", allow_pickle=True)
val_meta_npy_ = np.load("./ComMU-code/dataset/commu_midi/output_npy_/input_val.npy", allow_pickle=True)
val_midi_npy_ = np.load("./ComMU-code/dataset/commu_midi/output_npy_/target_val.npy", allow_pickle=True)

real_data = Commu(train_meta_npy_, train_midi_npy_,512)
real_loader = DataLoader(real_data, batch_size=256, shuffle=True)
val_data = Commu(val_meta_npy_, val_midi_npy_,512)
val_loader = DataLoader(val_data, batch_size=256, shuffle=True)

test_batch = next(iter(real_loader))[0]
test_target = next(iter(real_loader))[1]