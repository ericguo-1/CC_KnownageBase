# **4 General Product Characteristics**

#### **4.1 Absolute Maximum Ratings**

**Table 1 Absolute Maximum Ratings1)**

*T*j = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                    | Symbol |      | Values |      | Unit | Note /<br>Test<br>Condition | Number   |
|----------------------------------------------|--------|------|--------|------|------|-----------------------------|----------|
|                                              |        | Min. | Typ.   | Max. |      |                             |          |
| Voltages                                     |        |      |        |      |      |                             |          |
| Boost driver ground                          | VBSG   | -0.3 | –      | 0.3  | V    | –                           | P_4.1.1  |
| Input standby LDO                            | VVST   | -0.3 | –      | 40   | V    | 2) 3)                       | P_4.1.2  |
| Input voltage pin 1 (pre<br>regulator)       | VVS1   | -0.3 | –      | 40   | V    | 2) 3)                       | P_4.1.3  |
| Input voltage pin 2 (pre<br>regulator)       | VVS2   | -0.3 | –      | 40   | V    | 2) 3)<br>PG-LQFP-64 only    | P_4.1.4  |
| External step up power stage,<br>gate        | VDRG   | -0.3 | –      | 40   | V    | 2) 3)                       | P_4.1.5  |
| External power stage, sense<br>resistor high | VRSH   | -0.3 | –      | 40   | V    | 2) 3)                       | P_4.1.6  |
| External power stage, sense<br>resistor low  | VRSL   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.7  |
| Enable                                       | VENA   | -0.3 | –      | 40   | V    | 2) 3)                       | P_4.1.8  |
| Enable                                       | IENA   | -5   | –      | –    | mA   | 4)                          | P_4.1.9  |
| Wake/Inhibit                                 | VWAK   | -0.3 | –      | 40   | V    | 2) 3)                       | P_4.1.10 |
| Wake/Inhibit                                 | IWAK   | -5   | –      | –    | mA   | 4)                          | P_4.1.11 |
| Reset output                                 | VROT   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.12 |
| SPI: Chip select CS                          | VSCS   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.13 |
| SPI: Clock CLK                               | VSCL   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.14 |
| SPI: Data_In DI                              | VSDI   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.15 |
| SPI: Data_Out DO                             | VSDO   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.16 |
| Interrupt                                    | VINT   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.17 |
| Window watchdog trigger                      | VWDI   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.18 |
| Error pin                                    | VERR   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.19 |
| Safe state 1                                 | VSS1   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.20 |
| Safe state 2                                 | VSS2   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.21 |
| Output voltage reference                     | VQVR   | -0.3 | –      | 6.0  | V    | –                           | P_4.1.22 |
| Output tracker 2                             | VQT2   | -0.3 | –      | 40   | V    | –                           | P_4.1.23 |
| Sense Pin for tracker 2                      | VSQT2  | -0.3 | –      | 40   | V    | PG-LQFP-64 only             | P_4.1.24 |
| Output tracker 1                             | VQT1   | -0.3 | –      | 40   | V    | –                           | P_4.1.25 |

**Table 1 Absolute Maximum Ratings1)** (cont'd)

*T*j = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                  | Symbol      |      | Values |      | Unit | Note /<br>Test<br>Condition | Number   |
|--------------------------------------------|-------------|------|--------|------|------|-----------------------------|----------|
|                                            |             | Min. | Typ.   | Max. |      |                             |          |
| Sense Pin for tracker 1                    | VSQT1       | -0.3 | –      | 40   | V    | PG-LQFP-64 only             | P_4.1.26 |
| Output LDO_Com                             | VQCO        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.27 |
| Output LDO_µC                              | VQUC        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.28 |
| Sense Pin for LDO_µC                       | VSQUC       | -0.3 | –      | 6.0  | V    | PG-LQFP-64 only             | P_4.1.29 |
| V_Core_Mon ext core supply                 | VVCI        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.30 |
| Select ext core supply                     | VSEC        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.31 |
| Sync_Out ext core supply                   | VSYN        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.32 |
| Enable ext core supply                     | VEVC        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.33 |
| FB_BUCK4                                   | VFB4        | -0.3 | –      | 7.0  | V    | PG-LQFP-64 only             | P_4.1.35 |
| FB_BUCK3                                   | VFB3        | -0.3 | –      | 7.0  | V    | PG-LQFP-64 only             | P_4.1.36 |
| FB_BUCK2                                   | VFB2        | -0.3 | –      | 7.0  | V    | –                           | P_4.1.37 |
| FB_BUCK1                                   | VFB1        | -0.3 | –      | 7.0  | V    | –                           | P_4.1.38 |
| BU_GND2                                    | VPG2        | -0.3 | –      | 0.3  | V    | –                           | P_4.1.39 |
| BU_GND1                                    | VPG1        | -0.3 | –      | 0.3  | V    | –                           | P_4.1.40 |
| SW2                                        | VSW2        | -0.3 | –      | 40   | V    | PG-LQFP-64 only             | P_4.1.41 |
| SW1                                        | VSW1        | -0.3 | –      | 40   | V    | –                           | P_4.1.42 |
| Select step up pre regulator               | VSTU        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.43 |
| FRE                                        | VFRE        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.44 |
| Q_STBY                                     | VQST        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.45 |
| MPS                                        | VMPS        | -0.3 | –      | 6.0  | V    | –                           | P_4.1.46 |
| Temperatures                               |             |      |        |      |      |                             |          |
| Junction Temperature                       | Tj          | -40  | –      | 150  | °C   | –                           | P_4.1.47 |
| Storage Temperature                        | Tstg        | -55  | –      | 150  | °C   | –                           | P_4.1.48 |
| ESD Susceptibility                         |             |      |        |      |      |                             |          |
| ESD Susceptibility to GND                  | VESD        | -2   | –      | 2    | kV   | HBM5)                       | P_4.1.49 |
| ESD Susceptibility to GND                  | VESD        | -500 | –      | 500  | V    | CDM6)                       | P_4.1.50 |
| ESD Susceptibility (corner<br>pins) to GND | VESD,Corner | -750 | –      | 750  | V    | CDM6)                       | P_4.1.51 |

- 1) Not subject to production test, specified by design.
- 2) Maximum rating is 60 V, if rise time from 0 to 60 V is longer than 10 ms
- 3) Maximum rating is 49 V, for an overall time of 10 s (in the range of 40 V to 49 V) during the lifetime of the product independent from the rise time.
- 4) Consider external series resistor for negative voltages < -0.3 V to ensure maximum rating of current
- 5) ESD susceptibility, HBM according to JEDEC HBM Human Body Model ANSI/ESDA/JEDEC JS001 (1.5k Ω, 100 pF)
- 6) ESD susceptibility, Charged Device Model "CDM" ESDA STM5.3.1 or ANSI/ESD S.5.3.1

#### **Notes**

- *1. Stresses above the ones listed here may cause permanent damage to the device. Exposure to absolute maximum rating conditions for extended periods may affect device reliability.*
- *2. Integrated protection functions are designed to prevent IC destruction under fault conditions described in the data sheet. Fault conditions are considered as "outside" normal operating range. Protection functions are not designed for continuous repetitive operation.*

#### **4.2 Functional Range**

*Note: Within the functional or operating range, the IC operates as described in the circuit description. The electrical characteristics are specified within the conditions given in the Electrical Characteristics table.*

**Table 2 Functional Range** 

| Parameter                                                                         | Symbol |      | Values |      | Unit | Note /<br>Test<br>Condition                                                       | Number  |
|-----------------------------------------------------------------------------------|--------|------|--------|------|------|-----------------------------------------------------------------------------------|---------|
|                                                                                   |        | Min. | Typ.   | Max. |      |                                                                                   |         |
| Supply Voltage Range for<br>Normal Operation at input of<br>the step-up converter | VBat   | 3    | –      | 40   | V    | with step up pre<br>regulator active in<br>front of step down<br>pre regulator1)  | P_4.2.1 |
| Supply Voltage Range for<br>Normal Operation at pin VSx                           | VVS    | 6    | –      | 40   | V    | without step up pre<br>regulator active in<br>front of step down<br>pre regulator | P_4.2.2 |
| Junction Temperature                                                              | Tj     | -40  | –      | 150  | °C   | –                                                                                 | P_4.2.3 |

<sup>1)</sup> To start up the TLF35584 needs a minimum input voltage of 6.0V at the pin VSx.

*Note: Within the functional or operating range, the IC operates as described in the circuit description. The electrical characteristics are specified within the conditions given in the Electrical Characteristics table.*

### **4.3 Thermal Resistance**

*Note: This thermal data was generated in accordance with JEDEC JESD51 standards. For more information, go to <www.jedec.org>.*

**Table 3 Thermal Resistance 1)**

| Parameter                                      | Symbol |      | Values |      | Unit | Note / Test<br>Condition                                                         | Number  |
|------------------------------------------------|--------|------|--------|------|------|----------------------------------------------------------------------------------|---------|
|                                                |        | Min. | Typ.   | Max. |      |                                                                                  |         |
| Junction to Case                               | RthJC  | –    | –      | 12.2 | K/W  | –                                                                                | P_4.3.1 |
| Junction to Soldering Point<br>(pin)           | RthJSP | 20.1 | –      | 22.1 | K/W  | JEDEC 2s2p,<br>measured to pin:<br>VQFN: 1, 6, 7, 28<br>;<br>LQFP: 2, 11, 35, 50 | P_4.3.2 |
| Junction to Soldering Point<br>(pin)           | RthJSP | 34.9 | –      | 37.6 | K/W  | JEDEC 1s0p,<br>measured to pin:<br>VQFN: 1, 6, 7, 28<br>;<br>LQFP: 2, 11, 35, 50 | P_4.3.3 |
| Junction to Soldering Point<br>(soldering pad) | RthJSP | 11.0 | –      | 14.7 | K/W  | JEDEC 2s2p                                                                       | P_4.3.4 |
| Junction to Soldering Point<br>(soldering pad) | RthJSP | 13.1 | –      | 18.0 | K/W  | JEDEC 1s0p                                                                       | P_4.3.5 |
| Junction to Ambient                            | RthJA  | –    | 37     | –    | K/W  | 2)                                                                               | P_4.3.6 |

<sup>1)</sup> Not subject to production test, specified by design.

<sup>2)</sup> Specified *R*thJA value is according to Jedec JESD51-2,-5,-7 at natural convection on FR4 2s2p board; The Product (Chip+Package) was simulated on a 76.2 × 114.3 × 1.5 mm board with 2 inner copper layers (2 × 70 mm Cu, 2 × 35 mm Cu). Where applicable a thermal via array under the exposed pad contacted the first inner copper layer.

#### **4.4 Quiescent Current Consumption**

**Table 4 Quiescent current consumption 1)**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter      | Symbol | Values |      |      | Unit | Note / Test<br>Condition                                                           | Number  |
|----------------|--------|--------|------|------|------|------------------------------------------------------------------------------------|---------|
|                |        | Min.   | Typ. | Max. |      |                                                                                    |         |
| INIT state     | Iq     | –      | –    | 45   | mA   | 1) Tj<br>≤ 85°C<br>Step-Up Converter is<br>off,<br>fPREREG,BUCK<br>=<br>2.2<br>MHz | P_4.4.1 |
| NORMAL state   | Iq     | –      | –    | 45   | mA   | 1) Tj<br>≤ 85°C<br>Step-Up Converter is<br>off,<br>fPREREG,BUCK<br>=<br>2.2<br>MHz | P_4.4.2 |
| STANDBY state  | Iq     | –      | –    | 70   | µA   | 1) LDO_STBY is off<br>VVS<br>V ; Tj<br>=<br>14<br>≤ 40°C                           | P_4.4.3 |
| STANDBY state  | Iq     | –      | –    | 90   | µA   | LDO_STBY is off<br>1) Tj<br>≤ 85°C                                                 | P_4.4.4 |
| STANDBY state  | Iq     | –      | –    | 120  | µA   | LDO_STBY is on<br>1) Tj<br>≤ 85°C                                                  | P_4.4.5 |
| SLEEP state    | Iq     | –      | –    | 200  | µA   | 1) Tj<br>≤ 85°C                                                                    | P_4.4.6 |
| WAKE state     | Iq     | –      | –    | 45   | mA   | 1) Tj<br>≤ 85°C<br>Step-Up Converter is<br>off,<br>fPREREG,BUCK<br>=<br>2.2<br>MHz | P_4.4.7 |
| FAILSAFE state | Iq     | –      | –    | 200  | µA   | 1) Tj<br>≤ 85°C;<br>tFAILSAFE > tFAILSAFE,min                                      | P_4.4.8 |

<sup>1)</sup> All quiescent current parameters are measured at *T*<sup>j</sup> ≤ 85°C and 10 V ≤ *V*VS ≤ 28 V with zero load and all selectable options (Outputs, Watchdog, Timers, Step-Up converter) switched off.

## **4.4.1 Typical Performance Characteristics**

**INIT, NORMAL and WAKE Current Consumption** *I***<sup>q</sup> versus Supply Voltage** *V***VS (FRE-Pin: open)**

![](_page_6_Figure_3.jpeg)

**STANDBY Current Consumption** *I***<sup>q</sup> versus Supply Voltage** *V***VS (QST disabled)**

![](_page_6_Figure_5.jpeg)

**INIT, NORMAL and WAKE Current Consumption** *I***<sup>q</sup> versus Supply Voltage** *V***VS (various configuration)**

![](_page_6_Figure_7.jpeg)

**STANDBY Current Consumption** *I***<sup>q</sup> versus Supply Voltage** *V***VS (QST enabled)**

![](_page_6_Figure_9.jpeg)