'''reinforcement learning agent'''

from config import *

class Agent:
    '''agent class that moves in the 2D world'''
    def __init__(self, initPos, world):
        '''2D position of the agent'''
        self.pos = py_copy.deepcopy(initPos)
        '''the world this agent lives in'''
        self.world = world
        self.cum_reward = 0

    def move(self, action):
        # always move forward
        self.pos[COL] += SPEED_AGENT
        if (action == DOWN):self.pos[ROW] +=1
        if (action == UP):self.pos[ROW] -=1
        if (self.pos[ROW] >= self.world.rows):self.pos[ROW] = self.world.rows - 1;        
        if (self.pos[ROW] < 0):self.pos[ROW] = 0;

    def draw(self, isnew, color = 'red'):
        '''if object is new draw a new object'''
        if (isnew == True):
            self.picCenter = cg.Point((self.pos[COL] + 0.5) * CELL_SIZE, (self.pos[ROW] + 0.5) * CELL_SIZE)
            self.agentPic = cg.Circle(self.picCenter, CELL_SIZE/4)
            self.agentPic.setFill(color)
            self.agentPic.draw(self.world.window)
        else:
            dx = -self.agentPic.getCenter().getX() + (self.pos[COL] + 0.5) * CELL_SIZE
            dy = -self.agentPic.getCenter().getY() + (self.pos[ROW] + 0.5) * CELL_SIZE
            self.agentPic.move(dx,dy)

if __name__ == '__main__':
    main()


##Predator class
#class Predator:
#    '''predator class that moves in the 2D world'''
#    def __init__(self, initPos, world):
#        '''2D position of the predator'''
#        self.pos = py_copy.deepcopy(initPos)
#        '''the world this agent lives in'''
#        self.world = world
#
# 
#    def move(self, action):
#        if (action == UP):self.pos[0] -=1
#        if (action == DOWN):self.pos[0] +=1
#        if (action == LEFT):self.pos[1] -=1
#        if (action == RIGHT):self.pos[1] +=1
#        if (self.pos[0] >= self.world.rows):self.pos[0] = self.world.rows - 1;
#        if (self.pos[0] < 0):self.pos[0] = 0;
#        if (self.pos[1] >= self.world.columns):self.pos[1] = self.world.columns - 1;        
#        if (self.pos[1] < 0):self.pos[1] = 0;
#
#    def drawSelf(self, isnew, color = 'black'):
#        '''if object is new draw a new object'''
#        if (isnew == True):
#            self.picCenter = cg.Point((self.pos[COL] + 0.5) * CELL_SIZE, (self.pos[ROW] + 0.5) * CELL_SIZE)
#            self.agentPic = cg.Circle(self.picCenter, CELL_SIZE/4)
#            self.agentPic.setFill(color)
#            self.agentPic.draw(self.world.window)
#        else:
#            dx = -self.agentPic.getCenter().getX() + (self.pos[COL] + 0.5) * CELL_SIZE
#            dy = -self.agentPic.getCenter().getY() + (self.pos[ROW] + 0.5) * CELL_SIZE
#            self.agentPic.move(dx,dy)
#    
#    #Predator always tries to select action to approach agent
#    def chase(self, agentPos, pChase):
#        diffRow = -self.pos[ROW] + agentPos[ROW]
#        diffCol = -self.pos[COL] + agentPos[COL]
#
#        if (random.random() > pChase):
#            action = random.choice(range(NUM_ACT))
#            return action
#        elif (diffRow == 0 and diffCol == 0):
#            action = random.choice(range(NUM_ACT))
#        elif (diffCol == 0):
#            if (diffRow > 0):#agent is below the predator   
#                action = DOWN
#            elif (diffRow < 0):#agent is above of the predator
#                action = UP
#        elif (diffRow == 0):
#            if (diffCol > 0):#agent is on right of the predator
#                action = RIGHT
#            elif (diffCol < 0):#agent is on left of the predator
#                action = LEFT
#        else:# (diffRow != 0 and diffCol != 0):
#            if (random.random() >= 0.5):#listen to row
#                if (diffRow > 0):#agent is below of the predator   
#                    action = DOWN
#                elif (diffRow < 0):#agent is above the predator
#                    action = UP
#            else:#listen to column
#                if (diffCol > 0):#agent is on right of the predator
#                    action = RIGHT
#                elif (diffCol < 0):#agent is on left of the predator
#                    action = LEFT
#     
#        return action


