### **6.3.2 Electrical characteristics**

**Table 8 Electrical Characteristics: Step down pre regulator**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                           | Symbol           | Values |       |       | Unit | Note /                                                                                                              | Number     |
|-----------------------------------------------------|------------------|--------|-------|-------|------|---------------------------------------------------------------------------------------------------------------------|------------|
|                                                     |                  | Min.   | Typ.  | Max.  |      | Test<br>Condition                                                                                                   |            |
| Step Down Pre Regulator                             |                  |        |       |       |      |                                                                                                                     |            |
| Output voltage                                      | VPREREG,BUC<br>K | 5.65   | 5.8   | 5.95  | V    | PWM-mode;<br>VVS<br>≥<br>6.5<br>V                                                                                   | P_6.3.2.1  |
| Output voltage                                      | VPREREG,BUC<br>K | 5.6    | 5.8   | 6.00  | V    | PFM-mode;<br>VVS<br>≥<br>6.5<br>V                                                                                   | P_6.3.2.2  |
| Power stage high side switch<br>on resistance       | RON, HS          | 150    | 360   | 630   | mΩ   | VVS<br>≥<br>6<br>V                                                                                                  | P_6.3.2.3  |
| Power stage low side switch<br>on resistance        | RON, LS          | 50     | 200   | 300   | mΩ   | VVS<br>≥<br>6<br>V                                                                                                  | P_6.3.2.4  |
| Buck peak over current limit                        | IPREREG, max     | 1.578  | 1.857 | 2.135 | A    | –                                                                                                                   | P_6.3.2.5  |
| SW rise time                                        | tR, Buck         | 2      | 6     | 14    | ns   | 1)<br>VVS<br>6.5V<br>≤<br>≤<br>18<br>V;<br>IPREREG<br>≥<br>0.5<br>A                                                 | P_6.3.2.6  |
| SW fall time                                        | tF, Buck         | 2      | 9     | 18    | ns   | 1)<br>VVS<br>6.5V<br>≤<br>≤<br>18<br>V;<br>IPREREG<br>≥<br>0.5<br>A                                                 | P_6.3.2.7  |
| Maximum duty cycle                                  | DBUCK, max       | -      | -     | 100   | %    | –                                                                                                                   | P_6.3.2.8  |
| Minimum switch on time                              | tON, min         | 20     | 50    | 80    | ns   | IPREREG<br>≥<br>0.5<br>A                                                                                            | P_6.3.2.9  |
| Soft start ramp                                     | tSS, BUCK        | 70     | 190   | 380   | µs   | 1) VPRE_REG,BUCK<br>rising from 5% to<br>95% of<br>VPREREG,nominal ;<br>2.2<br>MHz switching<br>frequency, no load  | P_6.3.2.10 |
| Soft start ramp                                     | tSS, BUCK        | 0.7    | 2.0   | 3.5   | ms   | 1) VPRE_REG,BUCK<br>rising from 5% to<br>95% of<br>VPRE_REG,nominal ;<br>400<br>kHz switching<br>frequency, no load | P_6.3.2.11 |
| Current threshold for<br>transition from PWM to PFM | IPWM/PFM         | 26     | 57    | 90    | mA   | –                                                                                                                   | P_6.3.2.12 |
| Current threshold for<br>transition from PFM to PWM | IPFM/PWM         | 100    | 145   | 190   | mA   | –                                                                                                                   | P_6.3.2.13 |
| Over temperature warning<br>threshold               | Tj,OT, WRN       | 130    | 145   | 160   | °C   | Tj<br>increasing<br>1)                                                                                              | P_6.3.2.14 |

**Table 8 Electrical Characteristics: Step down pre regulator** (cont'd)

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                              | Symbol          | Values |      |      | Unit | Note /                 | Number     |
|----------------------------------------|-----------------|--------|------|------|------|------------------------|------------|
|                                        |                 | Min.   | Typ. | Max. |      | Test<br>Condition      |            |
| Over temperature shutdown<br>threshold | Tj,OT, shutdown | 175    | 190  | 205  | °C   | Tj<br>increasing<br>1) | P_6.3.2.15 |
| Over temperature sensor<br>hysteresis  | Tj,OT, hyst     | –      | 10   | –    | °C   | 1)                     | P_6.3.2.16 |

<sup>1)</sup> Specified by design, not subject to production test

### **6.3.3 Typical Performance Characteristics**

#### **Pre Regulator Output Voltage** *V***PreReg versus Junction Temperature** *T***<sup>j</sup> (FRE-Pin: open)**

![](_page_2_Figure_3.jpeg)

**Pre Regulator Output Voltage** *V***PreReg versus Load Current** *I***PreReg (FRE-Pin: open)**

![](_page_2_Figure_5.jpeg)

#### **Pre Regulator Output Voltage** *V***PreReg versus Junction Temperature** *T***<sup>j</sup> (FRE-Pin: GND)**

![](_page_2_Figure_7.jpeg)

**Pre Regulator Output Voltage** *V***PreReg versus Load Current** *I***PreReg (FRE-Pin: GND)**

![](_page_2_Figure_9.jpeg)

# Pre Regulator Output Voltage $V_{\rm PreReg}$ versus Supply Voltage $V_{\rm VS}$ (FRE-Pin: open)

![](_page_3_Figure_2.jpeg)

High-Side Switch ON resistance  $R_{\mathrm{ON,\,HS}}$  versus Supply Voltage  $V_{\mathrm{VS}}$ 

![](_page_3_Figure_4.jpeg)

# Pre Regulator Output Voltage $V_{\rm PreReg}$ versus Supply Voltage $V_{\rm VS}$ (FRE-Pin: GND)

![](_page_3_Figure_6.jpeg)

Low-Side Switch ON resistance  $R_{\mathrm{ON,\,LS}}$  versus Supply Voltage  $V_{\mathrm{VS}}$ 

![](_page_3_Figure_8.jpeg)