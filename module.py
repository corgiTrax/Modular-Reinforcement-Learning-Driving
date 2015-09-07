'''moduleClass'''
'''note that in order to ensure module independence, we have a 'transparent' world: different instance can exist on the same grid'''

from config import *

class moduleClass:
    def __init__(self, classID, world, collectable = True,  weight = 1, unit_reward = 1, gamma = 0.9, num_inst = 5, random_gen = True):
        self.classID = classID
        self.world = world
        self.collectable = collectable
        self.insts = []
        if (not random_gen):
            self.weight = weight
            self.unit_reward = unit_reward 
            self.gamma = gamma
            self.num_inst = num_inst
            self.collectable = collectable
        else: # randomly generate a module
            self.weight = random.randint(1,20) # 1<= N <=100, may be too large
            self.unit_reward = random.choice([1,-1])
            self.num_inst = random.randint(1, 10)

            if self.unit_reward == 1: # rewarding objects must be collected
                self.collectable = True
                self.gamma = round(random.uniform(0.5, 0.8), 2) 
            else:
                self.collectable = random.choice([True,False])
                self.gamma = round(random.uniform(0.1,0.4), 2)

        # construct a list of module instances that belong to the same module class

    def place_inst(self, moduleType, agentPos):
        if moduleType == CAR: # cars
            for i in range(self.num_inst):
                new_car = [random.randint(0, self.world.rows - 1), random.randint(0, self.world.columns - 1)]
                self.insts.append(new_car)
        elif moduleType == ROAD: # offroad
            for i in range(self.world.columns):
                self.insts.append([0,i]) #top offroad
                self.insts.append([self.world.rows - 1,i]) #bottom offroad
        elif moduleType == TARGET: # target
            self.insts.append([random.randint(0, self.world.rows - 1), agentPos[COL] + 10])
#        for i in range(self.num_inst):
#            # place instances randomly in the maze
#            new_inst = [random.randint(0, self.world.rows - 1), random.randint(0, self.world.columns - 1)]
#            self.insts.append(new_inst)

    def calc_reward_update_inst(self, moduleType, agentPos):
        cur_reward = 0
        if moduleType == CAR: # cars
            for car in self.insts:
                car[COL] += SPEED_OTHER
                if car[COL] >= self.world.columns - 1: car[COL] = 0 # move back to start line
            if agentPos in self.insts: # hit a car
                if DRAW: print("hit a car")
                cur_reward = self.unit_reward * self.weight
        elif moduleType == ROAD: # offroad
            if agentPos in self.insts: # drive offroad
                if DRAW: print("drive offroad")
                cur_reward = self.unit_reward * self.weight
        elif moduleType == TARGET: # target
            if agentPos == self.insts[0]: #if hit the target
                if DRAW: print("get a target")
                self.insts = []
                self.insts.append([random.randint(0, self.world.rows - 1), agentPos[COL] + 10])
                cur_reward = self.unit_reward * self.weight
            elif agentPos[COL] >= self.insts[0][COL]: # if pass the target
                self.insts = []
                self.insts.append([random.randint(0, self.world.rows - 1), agentPos[COL] + 10])
        return cur_reward

    def draw(self, isNew):
        if isNew: # if this is the first time calling draw
            self.color = cg.COLORLIST[self.classID]
            self.window = self.world.window
            self.inst_pics = []
            for inst in self.insts:
                if self.unit_reward == 1: # this is some good stuff
                    pic = cg.Circle(cg.Point((inst[COL] + 0.5) * CELL_SIZE, (inst[ROW] + 0.5) * CELL_SIZE), CELL_SIZE/6)
                else: # this is something agent want to avoid
                    topLeftPt = cg.Point(inst[COL] * CELL_SIZE, inst[ROW] * CELL_SIZE)
                    bottomRightPt = cg.Point((inst[COL] + 1) * CELL_SIZE, (inst[ROW] + 1) * CELL_SIZE)
                    pic = cg.Rectangle(topLeftPt,bottomRightPt)
                pic.setFill(self.color)
                pic.draw(self.window)
                self.inst_pics.append(pic)
        else:
            if self.collectable:
                for pic in self.inst_pics:
                    pic.undraw()
                self.inst_pics = []
                for inst in self.insts:
                    if self.unit_reward == 1: # this is some good stuff
                        pic = cg.Circle(cg.Point((inst[COL] + 0.5) * CELL_SIZE, (inst[ROW] + 0.5) * CELL_SIZE), CELL_SIZE/6)
                    else: # this is something agent want to avoid
                        topLeftPt = cg.Point(inst[COL] * CELL_SIZE, inst[ROW] * CELL_SIZE)
                        bottomRightPt = cg.Point((inst[COL] + 1) * CELL_SIZE, (inst[ROW] + 1) * CELL_SIZE)
                        pic = cg.Rectangle(topLeftPt,bottomRightPt)
                    pic.setFill(self.color)
                    pic.draw(self.window)
                    self.inst_pics.append(pic)
            #else: if instances are not collectable, then do not need to redraw anything

            

if __name__ == '__main__':
    main()


