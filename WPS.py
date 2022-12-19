
'''
1. System start : Tank B feed the user with water
2. When Tank B reaches 250L, the valve opens [water level == 250L]
3. When Tank A reaches 500L [water level == 500L] , then the Pump turnON
4. The pump will continue supplying until Tank B reaches 1000L, then the valve closes.
5. The Tank A gets water from the pump until it reaches 1000L 
6. When tank A reaches 1000L, the pump turnOFF and the system will close
7. When TankB waterLevel is less than 250L AND TankA waterLevel is less than 500L, then pump shut down [safety condition]



    pump = Pump(20, 10, 5,'running')
    pump.startPump()
    while (current_levelB <= 1000):
  
        current_levelA += 1 
        current_levelB += 1
        if current_levelB == 1000:
            tankB = TankB(100, 10, current_levelB)
            valve = Valve(False)
            while (current_levelA <= 1000):
                current_levelA += 1 
                if current_levelA == 1000:
                    tankA = TankA(100, 10, current_levelA)
                    pump.stopPump()
                    pump = Pump(20, 10, 5,'stopped')
                    pump.pumpStatus()
                    ##stop the process
                    break
   


'''

    