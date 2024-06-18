# PAX1000 Get Latest measurement mode 
This command line sample demonstrates how to initialize, start and measure data in text based Get Latest measurement mode for Thorlabs Polarimeters. 

# Details 
The text based mode allows querying polarization measurement data at normal or slow motor speeds. The speed limit depends on the measurement mode. The Get Latest mode returns the recently added measurement result out of the device internal queue. The mode does not remove the element from the device internal queue. So if you query faster than the PAX measurement rate you will receive the same sample multiple times. You can use the evolution count or timestampe variable to detect new sample data. If you face problems with the speed you should switch to the binary based FIFO measurement mode. 

## Limitations
The PAX1000 firmware does not support all measurement modes at 200 Hz motor full speed. Especially the half turn FFT modes are limited. If motor speed is to fast you always have a loss of data and the "Out of Sync" status bit is set. For speed limits per mode refer to the sample code. 

### National Instruments :tm: Visa
If you want to control the Polarimeter on Windows or Linux, with pyvisa library or with SCPI commands within your CVI or LabView application, you have to install National Instruments :tm: Visa Runtime. The library gets also installed along with the Thorlabs PAX software. It might be installed by NI LabView or NI CVI as well.

To use the NI Visa library in python you have to install pyvisa. 
```
python -m pip install pyvisa
```

## Supported Thorlabs Polarimeters
- PAX1000
