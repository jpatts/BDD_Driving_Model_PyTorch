# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 02:09:57 2018

@author: AUSTIN
"""
from collections import defaultdict
import numpy as np

def segmentation_color(pred):
    color = {
        0:[128, 64, 128], 1:[244, 35,232], 2:[ 70, 70, 70],
        3:[102, 102,156], 4:[190,153,153], 5:[153,153,153],
        6:[250, 170, 30], 7:[220,220,  0], 8:[107,142, 35],
        9:[152,251, 152], 10:[70,130,180], 11:[220, 20,60],
        12:[255,  0,  0], 13:[0, 0,  142], 14:[0,  0,  70],
        15:[0, 60,  100], 16:[0, 80, 100], 17:[0,  0, 230],
        18:[119, 11, 32]
    }
    color = defaultdict(lambda: [0,0,0], color)
    shape = pred.shape
    pred = pred.ravel()
    pred = np.asarray([color[i] for i in pred])
    pred = pred.reshape(shape[0],shape[1],shape[2],3)
    return pred.astype(np.uint8)
    