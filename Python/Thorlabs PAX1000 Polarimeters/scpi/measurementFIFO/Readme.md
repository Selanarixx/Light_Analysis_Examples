# PAX1000 measurement FIFO mode 
This command line sample demonstrates how to initialize, start and measure data in binary FIFO mode for Thorlabs PAX1000. 

# Details 
The binary mode allows querying polarization measurement data at 400 Hz max. The mode works for slower speeds as well. The FIFO mode polls the data out of the PAX internal FIFO data structure. This queue buffers the recent measurements. Reading the measurement results slower than PAX measurement rate will result in a loss of data. You can use the evolution count or timestampe variable to detect this loss. If you face problems with the binary data format you can also use the text based Latest Measurement mode for normal and slower measurement rates. 

## Limitations
The PAX1000 firmware does not support all measurement modes at 200 Hz motor full speed. Especially the half turn FFT modes are limited.

# Example Output

## pyvisa python Library
The same requires a local National Instrument installation and the python pyvsia library. Use 

## Supported Thorlabs Polarimeters
- PAX1000
