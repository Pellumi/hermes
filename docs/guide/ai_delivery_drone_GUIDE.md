## Tools
- 3D printer (PETG/ABS/PLA capable)
- M3 hex key
- M2 hex key / precision screwdriver set
- Soldering iron with fine tip
- Solder
- Wire strippers
- Flush cutters
- Heat gun (for heat shrink)
- Multimeter
- Cable ties
- Deburring tool
- Drill press or hand drill
- Computer with USB ports

## Assumptions
- Basic soldering experience is required.
- Familiarity with 3D printer operation and material properties (PETG, ABS, PLA).
- Basic understanding of electronics and wiring diagrams.
- Access to a computer with necessary software for firmware flashing and configuration (e.g., flight controller configurator, Linux environment for AI module).
- Components are sourced and ready for assembly.

## 1. Fabrication
### 1.1 3D print all custom mounts and enclosures
**3D print all custom mounts and enclosures with specified materials and settings.**
1. Print six Motor Mounts (PETG, 30% infill, 0.2mm layer, high strength) for propulsion motors.
2. Print the Payload Container Housing (PETG, 20% infill, 0.2mm layer) and two Battery Bay Covers (PETG, 15% infill, 0.2mm layer).
3. Print the Main and Auxiliary RTK GPS Mounts (PETG, 20% infill, 0.2mm layer).
4. Print the four Obstacle LiDAR Mounts (PETG, 25% infill, 0.2mm layer), the Forward Camera Mount (PETG, 20% infill, 0.2mm layer), and the High Precision Barometer Mount (PETG, 30% infill, 0.2mm layer, 4 perimeters).
5. Print the Flight Controller/AI Enclosure (ABS, 30% infill, 0.2mm layer) and the AI Compute Module Mount (PLA, 20% infill, 0.2mm layer).
6. Print the six Motor ESC Mounts, Winch Motor Driver Mount, 4G/5G Cellular Modem Mount, Digital Video Transmitter Mount, WiFi/Bluetooth Module Mount, and Voltage/Current Sensor Mount (all PETG, 30% infill, 0.2mm layer, 4 perimeters), along with the Cable Management Clips (PLA, 20% infill, 0.2mm layer).

### 1.2 Deburr and prepare main frame plates and hexarotor arms
*(not yet generated)*

### 1.3 Attach propulsion motors to their mounts and then to hexarotor arms
*(not yet generated)*

### 1.4 Assemble payload winch system components including the winch motor
*(not yet generated)*

### 1.5 Install downward vision camera into its gimbal
*(not yet generated)*

### 1.6 Mount sensors into their 3D printed enclosures/mounts
*(not yet generated)*

## 2. Wiring
### 2.1 Solder main power leads from BMS to Power Distribution Board
*(not yet generated)*

### 2.2 Solder ESCs to Power Distribution Board and propulsion motors
*(not yet generated)*

### 2.3 Wire all power output rails from PDB to various electrical components
*(not yet generated)*

### 2.4 Connect flight controller to ESCs, power module, and BMS (PWM, ADC, CAN)
*(not yet generated)*

### 2.5 Wire AI compute module to various sensors and communication modules (UART, I2C, SPI, USB, CSI, GPIO)
*(not yet generated)*

### 2.6 Connect winch motor and driver to flight controller (PWM, GPIO)
*(not yet generated)*

### 2.7 Wire digital video transmitter to downward camera and flight controller (MIPI CSI, UART)
*(not yet generated)*

## 3. Bring-up
### 3.1 Perform initial power-on, verify stable voltages from PDB to all components
*(not yet generated)*

### 3.2 Flash flight controller firmware and configure basic settings
*(not yet generated)*

### 3.3 Power on AI compute module, install OS and necessary drivers
*(not yet generated)*

### 3.4 Verify communication with all sensors (GPS, Barometer, LiDAR, Cameras) via AI compute module and flight controller
*(not yet generated)*

### 3.5 Calibrate ESCs and test individual motor spin direction
*(not yet generated)*

### 3.6 Test winch motor control and payload weight sensor readings
*(not yet generated)*

### 3.7 Confirm functionality of cellular, WiFi/Bluetooth, and digital video transmission modules
*(not yet generated)*

## 4. Assembly
### 4.1 Assemble main frame structure: bottom plate, arms, landing gear, and top plate
*(not yet generated)*

### 4.2 Mount flight controller and AI compute module into their enclosure on vibration dampers
*(not yet generated)*

### 4.3 Install power distribution board and BMS into the main frame
*(not yet generated)*

### 4.4 Mount all remaining sensor and communication modules to their designated locations on the frame
*(not yet generated)*

### 4.5 Integrate payload bay enclosure, winch system, and payload container
*(not yet generated)*

### 4.6 Perform thorough cable routing, strain relief, and secure with cable management clips
*(not yet generated)*

### 4.7 Attach battery bay covers and conduct a final visual inspection
*(not yet generated)*
