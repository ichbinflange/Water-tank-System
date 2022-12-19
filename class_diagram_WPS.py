import sys 
class Pump:
    def __init__(self, temperature, pressure, speed,status):
        self.temperature = temperature
        self.pressure = pressure
        self.speed = speed
        self.status = status
    def startPump(self):
        return "Pump started"
    def stopPump(self):
        return "Pump stopped"
    def pumpStatus(self):
        updated_status = self.status
        print(updated_status)
        return updated_status


class Valve:
    def __init__(self, ValveStatus=False):
        self.ValveStatus = ValveStatus
    def openValve(self):
        return "Valve opened"
    def closeValve(self):
        return "Valve closed"

class Tank:
    def __init__(self, volume, flow, level):
        self.volume = volume
        self.flow = flow
        self.level = level
    def checkTankLevel(self):
        return self.level

class TankA(Tank):
    def __init__(self, volume, flow, level):
        super().__init__(volume, flow, level)

class TankB(Tank):
    def __init__(self, volume, flow, level):
        super().__init__(volume, flow, level)
   
def safety(levelA,levelB):
    if (levelA == 500) and (levelB==250):
        print('stop process')

###############################################################################################
##Water Tank system
##Tank level initialized to full capacity
#current_levelA = 1000
#current_levelB = 1000

def waterTankSystem(current_levelA,current_levelB):
    '''
    info:water tank system 
    args:current water level for tank A current_levelA,
         current water level for tank B current_levelB
    return: None
    '''
    print('start of process')
    while (current_levelB <= 1000):
        print('Tank feeding User')
        print(f'Current level of tankB {current_levelB}L')
        tankB = TankB(100, 10, current_levelB)
        print(f'Updated Current level of tankB in class')
        if current_levelB == 250:
            print('level of water tank B reached 250L')
            tankB = TankB(100, 10, current_levelB)
            print('Valve opened and set to True')
            valve = Valve(True)
            while (current_levelA <= 1000):
                print('Supply from tank A')
                print(f'Current level of tank A {current_levelA}L')
                tankA = TankA(100, 10, current_levelA)
                print(f'Updated Current level of tankA in class')
                if current_levelA == 500:
                    print('level of water tank A reached 500L')
                    print(f'Current water level in Tank A: {current_levelA}L')
                    print(f'Current water level in Tank B:{current_levelB}L')
                    pump = Pump(20, 10, 50,'running')
                    pump.startPump()
                    print('Pump started running')
                    for x in range(500, 1050, 50):
                        print('pumping water into tank A')
                        if (current_levelB == 250):
                            print('current level in tank B is less than 1000 hence pump into Tank B')
                            for y in range(250, 1050, 50):
                                print('pumping water into tank B')
                                current_levelB = y
                                tankB = TankB(100, 10, current_levelB)
                                print(f'tank B current level:{current_levelB}L')
                            valve = Valve(False)
                            print('close valve')
                        elif (current_levelB == 1000):
                            print('current level in tank B is 1000 hence pump into A')
                            current_levelA = x
                            tankA = TankA(100, 10, current_levelA)
                            print(f'tank A current level:{current_levelA}L')
                            if current_levelA == 1000:
                                print('tank A full')
                                print('tank B full')
                                pump.stopPump()
                                print('SYSTEM CLOSE')
                                sys.exit()
                if (current_levelB != 1000):           
                ###use condition to reduce level A                                
                    current_levelA -= 50
            break
        elif (current_levelA < 500) and (current_levelB < 250):
            print('end process using SAFETY CONDITION')
            sys.exit()
        current_levelB -= 50

#call function and set initial values 
waterTankSystem(1000,1000)