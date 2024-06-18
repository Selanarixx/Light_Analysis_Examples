# PAX1000 measurement FIFO mode 
This command line sample demonstrates how to initialize, start and measure data in binary FIFO mode for Thorlabs PAX1000. 

# Details 
The binary mode allows querying polarization measurement data at 400 Hz max. The mode works for slower speeds as well. The FIFO mode polls the data out of the PAX internal FIFO data structure. This queue buffers the recent measurements. Reading the measurement results slower than PAX measurement rate will result in a loss of data. You can use the evolution count or timestampe variable to detect this loss. If you face problems with the binary data format you can also use the text based Latest Measurement mode for normal and slower measurement rates. 

## Limitations
The PAX1000 firmware does not support all measurement modes at 200 Hz motor full speed. Especially the half turn FFT modes are limited. If motor speed is to fast you always have a loss of data and the "Out of Sync" status bit is set. For speed limits per mode refer to the sample code. 

### National Instruments :tm: Visa
If you want to control the Polarimeter on Windows or Linux, with pyvisa library or with SCPI commands within your CVI or LabView application, 
you have to install National Instruments :tm: Visa Runtime. The library gets also installed along with the Thorlabs PAX software. It might be
installed by NI LabView or NI CVI as well.

To use the NI Visa library in python you have to install pyvisa. 
```
python -m pip install pyvisa
```

## Supported Thorlabs Polarimeters
- PAX1000
