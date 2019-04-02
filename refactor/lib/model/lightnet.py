#
# @Author: Songyang Zhang 
# @Date: 2019-03-18 09:57:13 
# @Last Modified by:   Songyang Zhang 
# @Last Modified time: 2019-03-18 09:57:13 
#

import torch
import torch.nn as nn

__all__ = ['LightNet']

class LightNet(nn.Module):
    """
    Abstraction Layer on the top of :class:`pytorch:torch.nn.Module`
    """

    def __init__(self):
        super(LightNet, self).__init__()

        self.layers = None
        