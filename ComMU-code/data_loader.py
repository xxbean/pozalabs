# -*- coding: utf-8 -*-
"""data_loader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15x18CPgAyOzvyAvaMx3D47HO16T-DJ7p
"""

class Commu(Dataset):
    def __init__(self, meta_npy, midi_npy,seq_len):
        self.meta_npy = meta_npy
        self.midi_npy = midi_npy
        self.seq_len = seq_len
        self.label_npy = np.zeros_like(self.meta_npy)
        for i in range(11):
            self.label_npy[:,i] = np.array(list(map(meta_list[i],meta_npy[:,i])))

    def __len__(self):
        return len(self.meta_npy)

    def __getitem__(self, idx):
        label = self.label_npy[idx]
        midi = np.zeros((1,self.seq_len))
        midi_real = self.midi_npy[idx][:self.seq_len]
        midi[:,:len(midi_real)] = midi_real
        midi = torch.tensor(midi.tolist(),dtype=torch.float)
        label = torch.tensor(label.tolist(),dtype=torch.float)
        return midi,label