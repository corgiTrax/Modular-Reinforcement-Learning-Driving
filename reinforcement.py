'''modular reinforcement learning'''

from config import *
import agent

def calc_dists(moduleType, agentPos, objPos, maze):
    '''for a module instance, for each action, calculate the 'd' variable in log likelihood function'''
    dists = [] 
    for act in ACTIONS:
        #suppose the agent really takes the current action act
        testAgent = agent.Agent(agentPos, maze)
        testAgent.move(act)
        #calc number of steps away from the object
        if moduleType == CAR: # car will move 1 step further at next step
            dist = abs(testAgent.pos[ROW] - objPos[ROW]) + abs(testAgent.pos[COL] - (objPos[COL] + SPEED_OTHER))
        else:
            dist = abs(testAgent.pos[ROW] - objPos[ROW]) + abs(testAgent.pos[COL] - objPos[COL])
        dists.append(dist)
        del testAgent

    return dists

def calc_Qvalues(moduleType, moduleClass, agentPos, maze):
    '''given module class, agent position and instances' positions, calculate Q values'''
    ''' return dimension is #instnces * #actions'''
    Qvalues = []

    for inst in moduleClass.insts:
        inst_Qvalue = []
        for act in ACTIONS:
            #suppose the agent really takes the current action act
            testAgent = agent.Agent(agentPos, maze)
            testAgent.move(act)
            #calc number of steps away from the inst
            if moduleType == CAR: # car will move 1 step further at next step
                dist = abs(testAgent.pos[ROW] - inst[ROW]) + abs(testAgent.pos[COL] - (inst[COL] + SPEED_OTHER))
            else:
                dist = abs(testAgent.pos[ROW] - inst[ROW]) + abs(testAgent.pos[COL] - inst[COL])
            Q = moduleClass.weight * moduleClass.unit_reward * (moduleClass.gamma ** dist)
            inst_Qvalue.append(Q)

            del testAgent

        Qvalues.append(inst_Qvalue)

    return Qvalues


def sumQ(Qvalues):
   '''given an array of Qvalues, perform sumQ algorithm'''
   sumed_Q = numpy.zeros(len(ACTIONS))
   for i in range(len(sumed_Q)):
       for j in range(len(Qvalues)):
           sumed_Q[i] += Qvalues[j][i]

   return sumed_Q


def softmax_act(Qvalues):
    '''Input: a vector of weights of actions
    Return: an action according to its softmax probability'''
    weights = py_copy.deepcopy(Qvalues)
    num_actions = len(weights)

    #map to exponential
    for i in range(num_actions):
        weights[i] = math.exp(ETA * weights[i]) #note that this is softmax with temperature parameter eta

    #normalize, get probability for each action
    total_weight = 0
    for i in range(num_actions):
        total_weight += weights[i]
    for i in range(num_actions):
        weights[i] = weights[i] / total_weight

    #calc cumulative probability
    cum_prob = numpy.zeros(num_actions + 1)
    cum_prob[0] = 0
    for i in range(num_actions):
        cum_prob[i+1] = cum_prob[i] + weights[i]

    #random seed
    seed = random.random()
    for i in range(num_actions):
        if (seed >= cum_prob[i] and seed < cum_prob[i+1]):
            action = i

    return action


if __name__ == '__main__':
    main()

