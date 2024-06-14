# Python example on SCPI command level

This folder contains python examples on [SCPI](https://de.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments) command level. The examples are not using TLPAX driver but send
text based low level commands to communicate with the Thorlabs Polarimeter. The exmaple python code uses the third-party pyvisa python library based on National Instruments :tm: driver.

## Included Examples

### PAX FIFO measurement method 
The exmaple demonstrates how to initialize, start and query binary measurement results in FIFO mode for all
motor speeds. For closer details refer to [Readme](measurementGetLatest).

### PAX get latest measurement method 
The exmaple shows how to initialize, start and query text measurment results in get latest measurement method
for normal or slow motor speeds. For closer details refer to [Readme](measurementGetLatest).

## SCPI Command documentation
See the PAX detail [SCPI command documentation](commandDocu) in .html file format. 

### National Instruments :tm: Visa

If you want to control the Polarimeter on Windows or Linux, with pyvisa library or with SCPI commands within your CVI or LabView application, 
you have to install National Instruments :tm: Visa Runtime. The library gets also installed along with the Thorlabs PAX software. It might be
installed by NI LabView or NI CVI as well.

To use the NI Visa library in python you have to install pyvisa. 
```
python -m pip install pyvisa
```
