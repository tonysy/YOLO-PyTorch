#
# @Author: Songyang Zhang 
# @Date: 2019-03-18 01:10:16 
# @Last Modified by:   Songyang Zhang 
# @Last Modified time: 2019-03-18 01:10:16 
#
import torch
import torch.nn as nn

class YOLODetector(object):
    """
    "You Only Look Once" One-stage Object Detector

    """
    def __init__(self, cfg):
        super(YOLODetector, self).__init__()
        self.cfg = cfg

    def _build_model(self, cfg):

        self.model = 

    def _build_dataloader(self):
        
        self.train_loader = 
        self.test_loader = 

    def _build_optimizer(self):
        pass

    def _build_plotter(self):
        pass

    def _build_meters(self):
        pass

    def _reset_meters(self):
        pass

    def train(self):
        """
        train function for the detector
        """
        for iter_id in range(self.cfg.train.start_iters,
                        self.cfg.train.start_iters+self.cfg.train.total_iters):
            # Set the model into training mode
            self.model.train()

            iter_start_time = time.time()

            # Execute the forward process 
            self._forward(self.train_loader, is_training=True)

            _log_str = 'Train\t Iter:{}/{} Loss:{:.6f} '