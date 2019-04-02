#
# @Author: Songyang Zhang 
# @Date: 2019-03-18 11:22:37 
# @Last Modified by:   Songyang Zhang 
# @Last Modified time: 2019-03-18 11:22:37 
#

from collections import OrderedDict, Iterable

import torch
import torch.nn as nn

class YOLOV2(nn.Module):
    """
    YOLO V2 Network Structure

    Args:

    Return:

    """
    def __init__(self,num_classes=20, conf_thresh=0.25,
                        nms_thresh=0.5, input_channels=3,
                        anchors=[(1.3221, 1.73145), (3.19275, 4.00944), 
                                 (5.05587, 8.09892), (9.47112, 4.84053), 
                                 (11.2364, 10.0071)]):
        super(YOLOV2, self).__init__()

        if not isinstance(anchors, Iterable) and not isinstance(anchors[0], Iterable):
            raise TypeError('Anchors need to be a 2D list of numbers')

        self.num_classes = num_classes
        self.anchors = anchors
        self.stride = 32 # input_dim/output_dim

        # Network Architecture
        layer_list = [
            # Sequence 0: input = image tensor
            OrderedDict([
                
            ])
        ]