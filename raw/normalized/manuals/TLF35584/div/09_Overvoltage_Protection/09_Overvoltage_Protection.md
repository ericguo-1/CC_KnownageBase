![](_page_0_Figure_1.jpeg)

**Figure 10 Principle post regulators**

### **7.2 µ-Processor Supply**

#### **7.2.1 Functional description**

The linear low drop regulator LDO\_µC offers a precise 3.3 V or 5.0 V output voltage for micro processor supply.

The regulator is supplied from the intermediate circuit voltage *V*PREREG which provides a stabilized voltage. The output voltage *V*QUC (at pin QUC) is controlled by the error amplifier. The actual value is compared to a reference voltage derived from band gap 1 for regulators. The stability of the control loop depends on the load current, the characteristics of the output capacitor and the chip temperature. To ensure a stable operation the output capacitor should be chosen according the specified requirements (capacitance value and electrical series resistance ESR) in **Table 10** "Electrical characteristics". The input capacitor shown in figure below is the output filter capacitor of the step down pre regulator.

Protection circuitry is installed to prevent the regulator and the application from damage:

- To protect the pass element of the LDO\_µC from overstress the current limitation will limit the output current to the maximum specified limit. Current sensing is done via a current mirror, no sense resistor is used. In case the maximum current condition is reached, the current will be limited, thus the output voltage will decrease. The regulator is protected against short circuit to ground.
- The output voltage is monitored by the voltage monitoring. In case of over voltage at pin QUC, the LDO\_µC will be switched off and the device will move into FAILSAFE state. The event will be stored in the SPI status register (**MONSF1**). In case of under voltage at pin QUC, the device will move into INIT state, pin ROT will be pulled low and the event will be stored in an SPI status register (**MONSF2**). The regulator will not be switched off in case of output under voltage, which is shorter than the short to ground detection time *t*StG. If the under voltage should be present for more than *t*StG, the device will move into FAILSAFE state. This event will be stored in an SPI status register as well (**MONSF0**).
- There is a dedicated temperature sensor for this regulator. In case the power stage temperature exceeds the pre warning threshold, an interrupt will indicate this event and it will be stored in an SPI status register (**OTWRNSF**). If the power stage temperature exceeds the temperature shutdown threshold, the device will move into FAILSAFE state, the regulator will be switched off and the event will be stored in an SPI status register (**OTFAIL**). The off time due to temperature shut down will be at least one second.

If the device enters FAILSAFE state the ROT is pulled low and all supplies are switched off.

If the device enters STANDBY state the LDO\_µC is switched off

For further details please refer to **Chapter 11 State Machine**.

![](_page_2_Figure_1.jpeg)

**Figure 11 Low drop linear regulator for micro processor supply LDO\_µC**

# **7.2.2 Electrical characteristics**

**Table 10 Electrical characteristics: µProcessor supply**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                              | Symbol          | Values |      |      | Unit | Note /                                                    | Number     |
|----------------------------------------|-----------------|--------|------|------|------|-----------------------------------------------------------|------------|
|                                        |                 | Min.   | Typ. | Max. |      | Test<br>Condition                                         |            |
| µ Processor supply                     |                 |        |      |      |      |                                                           |            |
| Output voltage<br>TLF35584xxVS1        | VQUC            | 4.9    | 5.0  | 5.1  | V    | 0 mA ≤ IQUC≤ 600<br>mA                                    | P_7.2.2.1  |
| Output voltage<br>TLF35584xxVS2        | VQUC            | 3.23   | 3.3  | 3.37 | V    | 0 mA ≤ IQUC≤ 600<br>mA                                    | P_7.2.2.2  |
| Output current limitation              | IQUC, max       | 650    | –    | 1100 | mA   | –                                                         | P_7.2.2.3  |
| Drop voltage<br>TLF35584xxVS1          | Vdr, QUC        | –      | –    | 400  | mV   | 1)                                                        | P_7.2.2.4  |
| Drop voltage<br>TLF35584xxVS2          | Vdr, QUC        | –      | –    | 500  | mV   | 1)                                                        | P_7.2.2.5  |
| Load regulation<br>TLF35584xxVS1       | ΔVQUC           | –      | 45   | 81   | mV   | IQUC<br>=<br>100µA<br>to<br>600<br>mA                     | P_7.2.2.6  |
| Load regulation<br>TLF35584xxVS2       | ΔVQUC           | –      | 39   | 60   | mV   | IQUC<br>=<br>100µA<br>to<br>600<br>mA                     | P_7.2.2.7  |
| Power supply ripple rejection          | PSRRQUC         | 26     | –    | –    | dB   | 2) VPREREG<br>=<br>5.8<br>V<br>;<br>ESRCQUC<br>≤<br>100mΩ | P_7.2.2.8  |
| Output capacitor                       | CQUC            | 2.2    | –    | 47   | µF   | 2)                                                        | P_7.2.2.9  |
| Output capacitor, ESR                  | ESR CQUC        | 0      | –    | 200  | mΩ   | 2)                                                        | P_7.2.2.10 |
| Over temperature warning<br>threshold  | Tj,OT, WRN      | 130    | 145  | 160  | °C   | Tj<br>increasing<br>2)                                    | P_7.2.2.11 |
| Over temperature shutdown<br>threshold | Tj,OT, shutdown | 175    | 190  | 205  | °C   | Tj<br>increasing<br>2)                                    | P_7.2.2.12 |
| Over temperature sensor<br>hysteresis  | Tj,OT, hyst     | –      | 10   | –    | °C   | 2)                                                        | P_7.2.2.13 |

<sup>1)</sup> Dropout voltage is defined as the difference between input and output voltage when the output voltage decreases 100 mV from output voltage measured at *V*<sup>I</sup> = *V*Q,nom + *V*dr,max + 100 mV.

<sup>2)</sup> Specified by design, not subject to production test

### **7.2.3 Typical Performance Characteristics**

#### **QUC Output Voltage** *V***QUC versus Junction Temperature** *T***<sup>j</sup> (TLF35584xxVS1)**

![](_page_4_Figure_3.jpeg)

**QUC Output Voltage** *V***QUC versus Load Current** *I***QUC (TLF35584xxVS1)**

![](_page_4_Figure_5.jpeg)

#### **QUC Output Voltage** *V***QUC versus Junction Temperature** *T***<sup>j</sup> (TLF35584xxVS2)**

![](_page_4_Figure_7.jpeg)

**QUC Output Voltage** *V***QUC versus Load Current** *I***QUC (TLF35584xxVS2)**

![](_page_4_Figure_9.jpeg)

# **QUC Dropout Voltage** *V***dr,QUC versus Load Current** *I***QUC (TLF35584xxVS1)**

![](_page_5_Figure_2.jpeg)

**QUC Dynamic Load Response (1mA to 400mA) TLF35584xxVS1 (***V***QUC,nom = 5.0 V)**

![](_page_5_Figure_4.jpeg)

# **QUC Dropout Voltage** *V***dr,QUC versus Load Current** *I***QUC (TLF35584xxVS2)**

![](_page_5_Figure_6.jpeg)

**QUC Dynamic Load Response (1mA to 400mA) TLF35584xxVS2 (***V***QUC,nom = 3.3 V)**

![](_page_5_Figure_8.jpeg)

### **QUC Dynamic Load Response (1mA to 600mA) TLF35584xxVS1 (***V***QUC,nom = 5.0 V)**

![](_page_6_Figure_2.jpeg)

![](_page_6_Figure_3.jpeg)

# **QUC Dynamic Load Response (1mA to 600mA) TLF35584xxVS2 (***V***QUC,nom = 3.3 V)**

![](_page_6_Figure_5.jpeg)

![](_page_6_Figure_6.jpeg)

# **7.3 Communication Supply**

#### **7.3.1 Functional description**

The linear low drop regulator LDO\_Com offers a precise 5.0 V output voltage for communication supply.

The regulator is supplied from the intermediate circuit voltage *V*PREREG, which provides a stabilized voltage. The output voltage *V*QCO (at pin QCO) is controlled by the error amplifier. The actual value is compared to a reference voltage derived from band gap 1 for regulators. The stability of the control loop depends on the load current, the characteristics of the output capacitor and the chip temperature. To ensure a stable operation the output capacitor should be chosen according the specified requirements (capacitance value and electrical series resistance ESR) in **Table 11** "Electrical characteristics". The input capacitor shown in figure below is the output filter capacitor of the step down pre regulator.

Protection circuitry is installed to prevent the regulator and the application from damage:

- To protect the pass element of the LDO\_Com from overstress the current limitation will limit the output current to the maximum specified limit. Current sensing is done via a current mirror, no sense resistor is used. In case the maximum current condition is reached, the current will be limited, thus the output voltage will decrease. The regulator is protected against short circuit to ground.
- The output voltage is monitored by the voltage monitoring. In case of over voltage at pin QCO, the LDO\_Com will be switched off, the event will be indicated by an interrupt and stored in an SPI status register (**MONSF1**). In case of under voltage at pin QCO, the event will be indicated by an interrupt and stored in an SPI status register (**MONSF2**). The regulator will not be switched off in case of output under voltage, which is shorter than the short to ground detection time *t*StG. If the under voltage should be present for more than *t*StG, the regulator will be switched off. This event will be stored in the SPI status register (**MONSF0**) and an interrupt will be generated.
- There is a dedicated temperature sensor for this regulator. In case the power stage temperature exceeds the pre warning threshold, an interrupt will indicate this event and it will be stored in an SPI status register (**OTWRNSF**). If the power stage temperature exceeds the temperature shutdown threshold, this event will be stored in an SPI status register (**OTFAIL**), the regulator will be switched off and an interrupt will be generated. After a temperature shut down the LDO\_Com can be re enabled via SPI command.

The regulator LDO\_Com is switched off in STANDBY and FAILSAFE state. In INIT, SLEEP, NORMAL and WAKE state LDO\_Com is ON or OFF depending on the SPI configuration.

For further details please refer to **Chapter 11 State Machine**.

![](_page_8_Figure_1.jpeg)

**Figure 12 Low drop linear regulator for communications supply LDO\_Com**

# **7.3.2 Electrical characteristics**

**Table 11 Electrical characteristics: Communication supply**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                              | Symbol          | Values |      |      | Unit | Note /                                                    | Number     |
|----------------------------------------|-----------------|--------|------|------|------|-----------------------------------------------------------|------------|
|                                        |                 | Min.   | Typ. | Max. |      | Test<br>Condition                                         |            |
| Communication supply                   |                 |        |      |      |      |                                                           |            |
| Output voltage                         | VQCO            | 4.90   | 5.00 | 5.10 | V    | 0 mA ≤ IQCO≤ 200<br>mA                                    | P_7.3.2.1  |
| Output current limitation              | IQCO, max       | 250    | –    | 400  | mA   | –                                                         | P_7.3.2.2  |
| Drop voltage                           | Vdr, QCO        | –      | –    | 400  | mV   | 1)                                                        | P_7.3.2.3  |
| Load regulation                        | ΔVQCO           | –      | 40   | 70   | mV   | IQCO<br>=<br>100µ<br>to<br>200<br>mA                      | P_7.3.2.4  |
| Power supply ripple rejection PSRRQCO  |                 | 26     | –    | –    | dB   | 2) VPREREG<br>=<br>5.8<br>V<br>;<br>ESRCQCO<br>≤<br>100mΩ | P_7.3.2.5  |
| Output capacitor                       | CQCO            | 1      | –    | 47   | µF   | 2)                                                        | P_7.3.2.6  |
| Output capacitor, ESR                  | ESR CQCO        | 0      | –    | 200  | mΩ   | 2)                                                        | P_7.3.2.7  |
| Over temperature warning<br>threshold  | Tj,OT, WRN      | 130    | 145  | 160  | °C   | Tj<br>increasing<br>2)                                    | P_7.3.2.8  |
| Over temperature shutdown<br>threshold | Tj,OT, shutdown | 175    | 190  | 205  | °C   | Tj<br>increasing<br>2)                                    | P_7.3.2.9  |
| Over temperature sensor<br>hysteresis  | Tj,OT, hyst     | –      | 10   | –    | °C   | 2)                                                        | P_7.3.2.10 |

<sup>1)</sup> Dropout voltage is defined as the difference between input and output voltage when the output voltage decreases 100 mV from output voltage measured at *V*<sup>I</sup> = *V*Q,nom + *V*dr,max + 100 mV.

<sup>2)</sup> Specified by design, not subject to production test

# **7.3.3 Typical Performance Characteristics**

#### **QCO Output Voltage** *V***QCO versus Junction Temperature** *T***<sup>j</sup>**

![](_page_10_Figure_3.jpeg)

**QCO Dropout Voltage** *V***dr,QCO versus Load Current** *I***QCO**

![](_page_10_Figure_5.jpeg)

**QCO Output Voltage** *V***QCO versus Load Current** *I***QCO**

![](_page_10_Figure_7.jpeg)

**QCO Dynamic Load Response (1mA to 100mA) (***V***QCO,nom = 5.0 V)**

![](_page_10_Figure_9.jpeg)