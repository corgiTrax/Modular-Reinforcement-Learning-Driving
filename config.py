'''config file'''

import random
import numpy
import copy as py_copy
import graphics as cg
import math
import sys

#State index
ROW = 0
COL = 1

#Actions for agent
VISUAL_RANGE = 10 # columns
SPEED_AGENT = 2
SPEED_OTHER = 1
NUM_ACT = 3
UP = 0; STAY = 1; DOWN = 2
ACTIONS = [UP,STAY,DOWN]

'''ModuleClass.py, flag for decideAct function'''
SOFTMAX_ACTION = True
ETA = 1
'''ModuleClass.py, flags for vote function'''
SUMQ = True
VOTE = False
SELECT = False

'''Test world'''
#Test Maze size
MAZE_ROW = 5
MAZE_COL = 20

#test trial numbers
MAX_STEP = MAZE_COL / SPEED_AGENT
MAX_TRIAL = 300
DRAW = False
MOUSE = False

'''Module Classes and Instances'''
NUM_MODULE_CLASS = 3
RAND_MODULE = False
MAX_INST = 100

'''test module setup'''
CAR = 0
ROAD = 1
TARGET = 2
# module0: avoid cars; 
# module1: avoid offroad
# module2: go to target
COLLECTABLES= [True, False, True]
UNIT_REWARDS = [1,-1,1]
WEIGHTS = [5,2,10]
GAMMAS = [0.4, 0.1, 0.9]
NUM_INSTS = [MAZE_ROW*MAZE_COL/10,MAZE_COL * 2,1]
RAND_GENS = [False,False,False]

'''IRL stuff'''
RECORDING = True

'''Graphic visualization'''
#Maze cell size in pixel, everything else depends on this
CELL_SIZE = 12

