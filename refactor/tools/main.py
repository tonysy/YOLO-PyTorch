#
# @Author: Songyang Zhang 
# @Date: 2019-03-18 00:52:25 
# @Last Modified by:   Songyang Zhang 
# @Last Modified time: 2019-03-18 00:52:25 
#

from easydict import EasyDict as edict 
from sacred import Experiment
from distutils.version import LooseVersion

import logging
import pprint

import torch

from configs.logging_dictconfig import create_logger
from lib.utils import random_init
from lib.detector import YOLODetector
ex = Experiment()


@ex.command
def train(_run, _rnd, _seed):

    # Fix the seed for reproduction
    random_init(_seed)
    # create logger
    ex.logger = create_logger()
    # create config edict
    cfg = edict(_run.config)

    yolo_detector = 

