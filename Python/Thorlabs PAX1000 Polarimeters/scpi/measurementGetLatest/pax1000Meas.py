"""
Example Thorlabs PAX1000 Get Latest Measurement Mode
Example Date of Creation                            2024-06-14
Example Date of Last Modification on Github         2024-06-14
Version of Python                                   3.11.2
==================
This examples shows how to to initialize and start the Thorlabs PAX1000 polarimeter using
pyvisa library and SCPI commands. Once the motor is started and settled the program queries
the recent 100 measurements in "Get Latest" measurement mode. This mode works for slow speeds
up to 120 Hz motor speed. For faster measurements use the "Fifo" measurement mode.
"""

import pyvisa
import time

def TL_PAX1000_get_latest_measurement(device, measCnt:int):
    res = []

    #device.write('INP:ROT:VEL 200.0')  #Maximal supported speed for mode 1
    #device.write('SENS:CALC 1') #512 points for FFT 1/2 turn 

    #device.write('INP:ROT:VEL 150.0')  #Maximal supported speed for mode 2
    #device.write('SENS:CALC 2') #1024 points for FFT 1/2 turn 

    #device.write('INP:ROT:VEL 75.0')   #Maximal supported speed for mode 3
    #device.write('SENS:CALC 3')  #2048 points for FFT 1/2 turn 

    #device.write('INP:ROT:VEL 200.0')  #Maximal supported speed for mode 4
    #device.write('SENS:CALC 4')  #512 points for FFT 1 turn

    #device.write('INP:ROT:VEL 200.0')  #Maximal supported speed for mode 5
    #device.write('SENS:CALC 5')  #1024 points for FFT 1 turn

    #device.write('INP:ROT:VEL 150.0')  #Maximal supported speed for mode 6
    #device.write('SENS:CALC 6')  #2048 points for FFT 1 turn

    #device.write('INP:ROT:VEL 200.0')  #Maximal supported speed for mode 7
    #device.write('SENS:CALC 7') #512 points for FFT 2 turns

    #device.write('INP:ROT:VEL 200.0')  #Maximal supported speed for mode 8
    #device.write('SENS:CALC 8') #1024 points for FFT 2 turns

    #device.write('INP:ROT:VEL 200.0')  #Maximal supported speed for mode 9
    #device.write('SENS:CALC 9') #2048 points for FFT 2 turns

    #Note: FOR SPEEDS FASTER THAN 50 Hz YOU NEED TO CONNECT EXTERNAL POWER SUPPLY

    device.write('SENS:CORR:WAV MIN'); #TODO set your light wavelength here
    
    device.write('INP:ROT:VEL 50.0') 
    device.write('SENS:CALC 3')  #2048 points for FFT 1/2 turn 
    device.write('INP:ROT:STAT 1') #Turn on motor
    
    #Test for errors
    err = device.query('SYST:ERR?').split(',')
    if int(err[0]) != 0:
        print(f'PAX reported error: {err[1]}')

    print('Power up PAX -> Wait until motor speed is settled')
    sett = 0
    while not sett:
        time.sleep(0.5)
        sett = int(device.query('INP:ROT:SETT?'))
    
    print("Powered up! -> Let's go\n")

    print('Query latest measurements')
    lastTS = -1
    while len(res) < measCnt:
        result = device.query('SENS:DATA:LAT?')
        data = result.split(',')
        #Test if value realy changed
        if lastTS != data[1]:
            #Convert string to float
            floatData = [float(y) for y in data]
            res.append(floatData)

            lastTS = data[1]
    print('Fetched all results')
    return res

def TL_PAX1000_print_measurement(paxMeasRes):
    print(f'  revolution cnt: {int(paxMeasRes[0])}')
    print(f'       timestamp: {int(paxMeasRes[1])} [ms]')
    print(f'          opMode: {int(paxMeasRes[2])}')
    print(f'     statusFlags: {hex(int(paxMeasRes[3]))}')
    print(f'      gain Index: {int(paxMeasRes[4])}')
    print(f'         ADC min: {int(paxMeasRes[5])} [Digits]')
    print(f'         ADC max: {int(paxMeasRes[6])} [Digits]')

    print(f'  evolution time: {paxMeasRes[7]} [ms]')
    print(f'    misalignment: {paxMeasRes[8]}')
    print(f'           theta: {paxMeasRes[9]} [rad]')
    print(f'             eta: {paxMeasRes[10]} [rad]')
    print(f'             DOP: {paxMeasRes[11]} %')
    print(f'          Ptotal: {paxMeasRes[12]} [W]')

def main():
    # create a resource manager
    rm = pyvisa.ResourceManager()
    
    #looks for devices, if no devices are connected via USB shows Error:'no devices found'
    devList = rm.list_resources('USB?*INSTR{VI_ATTR_MANF_ID==0x1313 && VI_ATTR_MODEL_CODE==0x8031}')
    if len(devList) == 0:
        raise ValueError('No devices found')

    #Open device for communication
    device = rm.open_resource(devList[0])
    print("Opened device: "+str(devList[0]))

    try:
        print(f'PAX1000 device query: {device.query('*IDN?').strip()}')

        res = TL_PAX1000_get_latest_measurement(device, 20)
    finally:
        # Always try to stop motor and close the connection 
        try:
            device.write('SENS:CALC 0;:INP:ROT:STAT 0')
            device.close()
            rm.close()
        except Exception:
            pass

    #Process the PAX1000 measurement data finally
    print(f'\nProcess {len(res)} results')
    if res:
        print('Print first result in detail')
        TL_PAX1000_print_measurement(res[0])
        print('\nPrint short version of entire result list')
        for meas in res:
            print(f'cnt:{int(meas[0])}, t:{int(meas[1])}, theta:{meas[9]}, eta:{meas[10]}, DOP:{meas[11]}')

if __name__ == '__main__':
    main()