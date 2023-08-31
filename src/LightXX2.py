import pygame
import time
from Motor import *
from Buzzer import *
from ADC import *
class Light:
    def run(self):
        try:
            buzzer=Buzzer()
            self.adc=Adc()
            self.PWM=Motor()
            self.PWM.setMotorModel(0,0,0,0)
            while True:
                L = self.adc.recvADC(0)
                R = self.adc.recvADC(1)
                if L < 2.99 and R < 2.99 :
                    buzzer.run('1')
                    time.sleep(0.1)
                    buzzer.run('0')
                    self.PWM.setMotorModel(-1000,-1000,-1000,-1000)
                    time.sleep(2)
                    self.PWM.setMotorModel(0,0,0,0)
                    time.sleep(0.1)
                    self.PWM.setMotorModel(-4000,-4000,-600,-600)
                    time.sleep(2)
                    self.PWM.setMotorModel(0,0,0,0)
                    time.sleep(0.1)
                    buzzer.run('1')
                    time.sleep(0.1)
                    buzzer.run('0')
                    time.sleep(0.1)
                    buzzer.run('1')
                    time.sleep(0.1)
                    buzzer.run('0')
                    time.sleep(5)
                    buzzer.run('1')
                    time.sleep(0.1)
                    buzzer.run('0')
                    time.sleep(0.1)
                    buzzer.run('1')
                    time.sleep(0.1)
                    buzzer.run('0')
                    self.PWM.setMotorModel(4000,4000,600,600)
                    time.sleep(2)
                    self.PWM.setMotorModel(0,0,0,0)
                    time.sleep(0.2)
                    self.PWM.setMotorModel(1000,1000,1000,1000)
                    time.sleep(2)
                    self.PWM.setMotorModel(0,0,0,0)
                    time.sleep(0.2)
                    buzzer.run('1')
                    time.sleep(0.2)
                    buzzer.run('0')
                    break
                    
             
        except KeyboardInterrupt:
           led_Car.PWM.setMotorModel(0,0,0,0) 

if __name__=='__main__':
    print ('Program is running ... ')
    led_Car=Light()
    led_Car.run()
