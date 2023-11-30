# Fire-Detection-and-Sprinkler-Activation--Cisco-packet-tracer

## INTRODUCTION
This experiment focuses on designing a Fire Detection and sprinkler activation circuit using Fire Monitor, Ceiling Sprinkler, MCU-Board and Heating Element. In this experiment IoT components are connected custom IOT cable, and the MCU-Board is configured for sprinkler activation

## REQUIREMENT
1. Fire Monitor
2. CustomMCU
3. Ceiling Sprinkler
4. Heating Element

### Fire Monitor
**Features:**
* Registration Server Compatible
* Detects flames by checking for a property and finding if the "IR" property value is in the range the detector considers a fire and outputs a digital signal.
**Usage:**
* Objects that can be on fire should have a device property "IR" with value. The IR range that is detected as fire is specified in the script. Anything near the detector end will be checked for fire and a digital signal of HIGH or LOW will be sent based on the current detection. HIGH for fire, LOW for no fire detected.

**Specifications:**
```
Message Format: [state]
state: 0 = no fire, 1 = fire
Output Slot: D0
LOW = no fire, High = fire
```

### Sprinkler 

**Features:**
* Registration Server Compatible
* Raises the water level

**Local Control:**
* Connect device to an MCU/SBC/Thing. Use the "customWrite" API per Data
**Specifications**
Remote Control:
* Connect device to Registration Server using Config Tab
**Data Specifications:**
```
Message Format: [state]
state: 0 = off, 1 = on
```

### Heating Element
**Features:**
* Increases the temperature of a typical office space at 10C per hour.
* Reduces the humidity by 2% per hour.
**Usage:**
* Connect to MCU or SBC.

**Local Control:**
* Connect device to MCU or SBC. Use the "digitalWrite" API per Data Specifications.

**Data Specifications:**
```
Message Format: [state]
state: HIGH or 1 = on, LOW or 0 = off
```

## PROCEDURE
1. Launch Cisco packet tracer form the start menu/shortcut icon in desktop
2. From file menu select New file
3. Work in logical window in packet tracer
4. Add the required devices from the network components space, and select the
components required for building the logical network, by simple drag and drop.
5. Connect all the network components using IoT custom cable and Copper Straight
through cable.
![image](https://github.com/Sadhvi19/Fire-Detection-and-Sprinkler-Activation--Cisco-packet-tracer/assets/53933893/4d1e0132-7b25-40bf-9809-0cffb521cbab)

6. Click on the MCU-Board for configuration
* Click on “Programming” and then “New”.
* Name the project as - Fire Detector.
* Under Template choose – Empty Python.
* Click create to proceed.
 
![image](https://github.com/Sadhvi19/Fire-Detection-and-Sprinkler-Activation--Cisco-packet-tracer/assets/53933893/245a092e-5c3e-4953-a9af-66f0341a7b86)

7. Programming the Fire Detector
* Click on the main.py
* Write the following code for the fire detector.
* Click on Run to execute the program.

![image](https://github.com/Sadhvi19/Fire-Detection-and-Sprinkler-Activation--Cisco-packet-tracer/assets/53933893/ba085f2d-8710-464d-93fa-6b66a5e6ea98)

8. Configuring the Heating Element
* Click on “Advanced “ then “Programming” and then “New”.
* Name the project as - Fire
* Under Template choose – Empty Java.
* Click create to create project

![image](https://github.com/Sadhvi19/Fire-Detection-and-Sprinkler-Activation--Cisco-packet-tracer/assets/53933893/9c5fc53a-4e13-4765-9ff4-b4a9fc74ba32)

9. Programming the Heating Element - Fire
* Click on the main.py
* Write the following code attached for the fire detector.
* Click on Run to execute the program

## Outputs
* Circuit before fire detection


![image](https://github.com/Sadhvi19/Fire-Detection-and-Sprinkler-Activation--Cisco-packet-tracer/assets/53933893/52dd6edd-1743-4764-9ec6-f369e6a88dc1)
  

* Circuit After fire detection

  
![image](https://github.com/Sadhvi19/Fire-Detection-and-Sprinkler-Activation--Cisco-packet-tracer/assets/53933893/53891579-4e40-4e61-ac30-367007c4742e)

