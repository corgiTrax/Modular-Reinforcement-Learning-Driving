'''inverse reinforcement learning algorithm'''
from scipy.optimize import differential_evolution, fmin_tnc, fmin_l_bfgs_b, minimize
import random
import numpy
import copy as py_copy
import math
import sys
import time

NUM_ACT = 4
NUM_MODULE = 10

class observed_inst():
    '''observed data from agent
    look at log likelihood function, at time t, for module instance m of module class n
    we need to record time t, module class n (obstacle or prize), chosen action a, discount factor power d(a), and d(-a)
    a sample is of the form [trial, t, n(0-prize, 1-obstacle], a, [d(Up, Down, Left, Right)]]'''
    def __init__(self, stepCount, module_class, unit_r, chosen_action, ds):
        self.stepCount = stepCount
        self.module_class = module_class
        self.unit_r = unit_r
        self.chosen_action = chosen_action
        self.ds = py_copy.deepcopy(ds) #array of length |ACTIONS|
    
    def record(self, data_file):
        '''write data to file'''
        data_file.write(str(self.module_class) + ',' \
                        + str(self.unit_r) + ','\
                        + str(self.chosen_action) + ',' \
                        + str(self.ds[0]) + ',' + str(self.ds[1]) + ',' + str(self.ds[2]) + ',' + str(self.ds[3]) )
   
    def __str__(self):
        return "[Step:{}, ModuleClassID:{}, UnitReward:{}, Action:{}, Dists: {}]".format \
                (self.stepCount, self.module_class, self.unit_r, self.chosen_action, self.ds)        

class inverse_rl:
    def __init__(self, data_file, sparse):
        self.data_file = data_file
        self.sparse = sparse
        if self.sparse == True:
            print("sparse version")
        else:
            print("non sparse version")
    def construct_obj(self, x):
        # construct objective function
        data_file = open(self.data_file,'r')
        logl = 0
        
        # each line is a step of execution
        for line in data_file:
            data = line.split()
            
            insts = []
            # each inst 
            for inst in data:
                inst_data = inst.split(',')
                mc_id = int(inst_data[0])
                unit_r = int(inst_data[1])
                act = int(inst_data[2])
                ds = []
                for i in range(NUM_ACT):
                    ds.append(int(inst_data[i + 3]))        
                
                # the w*r*(gamma**d) term 
                terms = []
                # for each action:
                for d in ds:
                    term = x[mc_id * 2] * unit_r * (x[mc_id * 2 + 1]**d)
                    terms.append(py_copy.deepcopy(term))
                insts.append(py_copy.deepcopy(terms))
            
            # first term in loglikelihood function
            first_term = 0 
            for inst in insts:
                first_term += inst[act]
            
            # second term
            second_term = 0
            for a in range(NUM_ACT):
                temp = 1
                for inst in insts:
                    temp = temp * math.exp(inst[a]) 
                second_term += py_copy.deepcopy(temp)
            second_term = math.log(second_term) 
            
            logl = logl + py_copy.deepcopy(first_term) - py_copy.deepcopy(second_term)
        
        # l1 norm on w
        if self.sparse:
            delta = 1
            for i in range(NUM_MODULE): 
                logl = logl - delta * x[i * 2]

        data_file.close()
        obj = -logl
        print("objective function constructed, one iter completed >>>")
        return obj

#    def callbackF(self,Xi):
#        print '{0:4d}   {1: 3.2f}   {2: 3.2f}   {3: 3.2f}   {4: 3.2f}   {5: 3.2f}'.format(Xi[0], Xi[1], Xi[2], Xi[3], Xi[4], Xi[5])

    def optimize(self):
        # differential evolution
        # two modules the variables are x[0] = w0, x[1] = gamma0, x[2] = w1, x[3] = gamma1...
        x0 = []
        bound = []
        for i in range(NUM_MODULE):
            x0.append(10)
            x0.append(0.5)
            bound.append((0,20))
            bound.append((0,0.9))
        #print(x0)
        #print(bound)
        #print("begin minimization algorithm >>>")
        #return differential_evolution(self.construct_obj, bounds)
        return minimize(self.construct_obj, x0, method = 'SLSQP', bounds = bound)

if __name__ == '__main__':
    test = inverse_rl(sys.argv[1], int(sys.argv[2]))
    test.optimize()
 
