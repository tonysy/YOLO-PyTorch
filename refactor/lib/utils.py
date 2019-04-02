#
# @Author: Songyang Zhang 
# @Date: 2019-03-18 00:59:36 
# @Last Modified by:   Songyang Zhang 
# @Last Modified time: 2019-03-18 00:59:36 
#
import torch
import numpy as np 
import random


def random_init(seed=0):
    """Set the seed for the random for torch and random package
    Args:
        seed: random seed
    """
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)

    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

