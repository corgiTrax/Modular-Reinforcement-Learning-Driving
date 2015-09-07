'''config file'''

import random
import numpy
import copy as py_copy
import graphics as cg
import math
import sys

'''discretized Stanford Abeel&Ng driving domain'''

'''Speed per frame, 1Hz'''
SPEED_AGENT = 2
SPEED_OTHER = 1


'''ACTIONS'''
NUM_ACT = 3
LEFT = 0
STAY = 1
RIGHT = 2

'''Lane'''
LN_W = 1.5
LN_L = 3000
NUM_LN = 5


'''modules'''
# 1. avoid other cars (AC)
COLLISION_RADIUS = 1 #meters
REWARD_AC = -100
GAMMA_AC = 0.1

# 2. stay on road (SR)
# if drive off road will continuously receive small penalty
REWARD_SR = -1
GAMMA_AC = 0.1

# 3. drive to target destinations
REWARD_TG = 10
GAMMA_TG = 0.9


#'''Car'''
#CAR_W = 1
#CAR_L = 3
#
#'''Speed per frame; 50Hz'''
#SPEED_L = 0.6 
#SPEED_M = 0.5 # 25m/s, 56mph
#SPEED_R = 0.4
#SPEED_LIMIT_MAX = 0.626 #70mph
#SPEED_LIMIT_MIN = 0.4
#
#'''Lane'''
#LANE_L = 2000
#LANE_W = 1.5
#NUM_LANES = 3
#
#
#'''Action: acceleration and turning'''
#MAX_ACC = 0.06 # maximum acceleration
#
#'''Modules reward rules'''
## follow current lane (LF)
## state: rel position to current lane 
## reward:
#
## move forward to target point (MF)
#
## avoid cars (AC)
#
## traffic light (TL)
#
## speed control (SC)
## state: current speed
## reward: if > max or < min get fine
#REWARD_SC = -10
#GAMMA_SC = 0.9
