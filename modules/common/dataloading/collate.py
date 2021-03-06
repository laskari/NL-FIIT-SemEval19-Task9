import numpy as np
import torch


def collate_fn_cf(data):
    samples, labels, lengths = zip(*data)
    labels = torch.LongTensor(labels)
    lengths = torch.LongTensor(lengths)

    if isinstance(samples[0], np.ndarray):
        samples = torch.LongTensor(samples)
    elif isinstance(samples[0], tuple):
        samples = samples

    return samples, labels, lengths
