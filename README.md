# Two_Photon_Polymerization
This project contains a LabView code in order to control the PI piezo stage using an E-727 controller. The goal of this 2pp project is to achieve automated microfabrication of micro and nano structures. 


# Structure

We have a top level Vi called  controlPanel.vi , inside we have the 3 principal Vi’s 


### 1. SetUp

The setUp.vi is in charge of configuring and establishing communication with the controller E-727. 

Inputs:
- (bool) Simulation/live 
- (bool) Stop



Outputs:
- int) System ID 
- (bool) Ready 
- (array of strings) Axis ID 
- Error

### 2. Main

The Main.vi contains the algorithms need it to achieve the automated process of micro fabrication  (inputs and outputs could change along development)


inputs:

- (array of strings) Axis ID 
- (double) Zaxis Step Size 
- (bool) Simulation/ live

outputs:
- (array of doubles) NormalVector
- (array of doubles) Position
- (3X3 matrix) Three Points 
- (double) D
- (string) Equation




### 3. Clean

The Clean.vi is in charge of closing all communication sessions, saving somo data in .txt files and clearing some variables.


inputs:
- (bool) Simulation/live
- (int) System ID

outputs:
- Error Out


# Hardware
Multi-Axis Piezo Scanner datasheet : https://www.pi-usa.us/en/products/piezo-flexure-nanopositioners/xyz-piezo-flexure-nanopositioning-stages/p-517-p-527-multi-axis-piezo-scanner-201500/

Digital Multi-Channel Piezo Controller E-727 datasheet: https://www.physikinstrumente.com/en/products/controllers-and-drivers/nanopositioning-piezo-controllers/e-727x-e-727xp-digital-multi-channel-piezo-controller-412418442/
