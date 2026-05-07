### **7.4 Voltage Reference**

#### **7.4.1 Functional description**

The linear low drop regulator Volt\_Ref offers a highly precise 5.0 V output voltage as a voltage reference.

The regulator is supplied from the intermediate circuit voltage *V*PREREG, which provides a stabilized voltage. The output voltage *V*QVR at pin QVR is controlled by the error amplifier. The actual value is compared to a reference voltage derived from band gap 1 for regulators. The stability of the control loop depends on the load current, the characteristics of the output capacitor and the chip temperature. To ensure a stable operation the output capacitor should be chosen according the specified requirements (capacitance value and electrical series resistance ESR) in **Table 12** "Electrical characteristics". The input capacitor shown in figure below is the output filter capacitor of the step down pre regulator.

Protection circuitry is installed to prevent the regulator and the application from damage:

- To protect the pass element of the Volt\_Ref from overstress the current limitation will limit the output current to the maximum specified limit. Current sensing is done via a current mirror, no sense resistor is used. In case the maximum current condition is reached the current will be limited, thus the output voltage will decrease. The regulator is protected against short circuit to ground.
- The output voltage is monitored by the voltage monitoring. In case of over voltage at pin QVR, the LDO Volt\_Ref will be switched off and the device will move into FAILSAFE state. The event will be stored in an SPI status register (**MONSF1**). In case of under voltage at pin QVR, the event will be indicated by an interrupt and stored in an SPI status register (**MONSF2**). The regulator will not be switched off in case of output under voltage, which is shorter than the short to ground detection time *t*StG. If the under voltage should be present for more than *t*StG, the regulator will be switched off. This event will be stored in an SPI status register (**MONSF0**) and an interrupt will be generated.
- There is no dedicated temperature sensor for this regulator. The temperature is sensed on the chip by other temperature sensors located at LDO\_µC and step down pre regulator. In case of the chip temperature will exceed the pre warning threshold, an interrupt will indicate this event and it will be stored in a SPI status register (**OTWRNSF**). If the chip temperature will exceed the temperature shutdown threshold, the regulator will be switched off. The temperature switch off time will be at least one second. An overload at LDO Volt\_Ref (over current detected for more than 1ms) will be indicated by an interrupt and it will be stored in a SPI status register (**OTWRNSF**).

If the device enters FAILSAFE state the ROT is pulled low and all supplies are switched off.

The regulator Volt\_Ref is switched off in STANDBY and FAILSAFE state. In INIT, SLEEP, NORMAL and WAKE state Volt\_Ref is ON or OFF depending on the SPI configuration.

For further details please refer to **Chapter 11 State Machine**.

![](_page_1_Figure_1.jpeg)

**Figure 13 Precise low drop linear regulator as a voltage reference Volt\_Ref**

### **7.4.2 Electrical characteristics**

**Table 12 Electrical characteristics: Voltage reference**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                     | Symbol    | Values |      |      | Unit | Note /                                                    | Number    |
|-------------------------------|-----------|--------|------|------|------|-----------------------------------------------------------|-----------|
|                               |           | Min.   | Typ. | Max. |      | Test<br>Condition                                         |           |
| Voltage reference             |           |        |      |      |      |                                                           |           |
| Output voltage                | VQVR      | 4.95   | 5.00 | 5.05 | V    | 0 mA ≤ IQVR≤ 150<br>mA                                    | P_7.4.2.1 |
| Output current limitation     | IQVR, max | 170    | –    | 345  | mA   | –                                                         | P_7.4.2.2 |
| Drop voltage                  | Vdr, QVR  | –      | –    | 400  | mV   | 1)                                                        | P_7.4.2.3 |
| Load regulation               | ΔVQVR     | –      | 4.5  | 9    | mV   | IQVR<br>=<br>100µ<br>to<br>150<br>mA                      | P_7.4.2.4 |
| Power supply ripple rejection | PSRRQVR   | 26     | –    | –    | dB   | 2) VPREREG<br>=<br>5.8<br>V<br>;<br>ESRCQVR<br>≤<br>100mΩ | P_7.4.2.5 |
| Output capacitor              | CQVR      | 1      | –    | 10   | µF   | 2)                                                        | P_7.4.2.6 |
| Output capacitor, ESR         | ESR CQVR  | 0      | –    | 200  | mΩ   | 2)                                                        | P_7.4.2.7 |

<sup>1)</sup> Dropout voltage is defined as the difference between input and output voltage when the output voltage decreases 100 mV from output voltage measured at *V*<sup>I</sup> = *V*Q,nom + *V*dr,max + 100 mV.

<sup>2)</sup> Specified by design, not subject to production test

# **7.4.3 Typical Performance Characteristics**

#### **QVR Output Voltage** *V***QVR versus Junction Temperature** *T***<sup>j</sup>**

![](_page_2_Figure_3.jpeg)

**QVR Dropout Voltage** *V***dr,QVR versus Load Current** *I***QVR**

![](_page_2_Figure_5.jpeg)

### **QVR Output Voltage** *V***QVR versus Load Current** *I***QVR**

![](_page_2_Figure_7.jpeg)

**QVR Dynamic Load Response (1mA to 100mA) (***V***QVR,nom = 5.0 V)**

![](_page_2_Figure_9.jpeg)

# **7.5 Tracker 1 & 2**

# **7.5.1 Functional description**

The linear trackers 1 and 2 offer a sensor supply with a very high accuracy referred to voltage reference output (pin QVR).

Both trackers are supplied by the intermediate circuit voltage *V*PREREG, which provides a stabilized voltage. The output voltage *V*QTx at pin QTx is controlled by the error amplifier. The actual value is compared to a reference voltage provided by the reference voltage *V*QVR at pin QVR. The tracker output voltages follow the Volt\_Ref output with a very small drop. The stability of the control loop depends on the load current, the characteristics of the output capacitor and the chip temperature. To ensure a stable operation the output capacitor for each tracker should be chosen according the specified requirements (capacitance value and electrical series resistance ESR) in **Table 13** "Electrical characteristics". The input capacitor shown in figure below is the output filter capacitor of the step down pre regulator.

Protection circuitry is installed to prevent damage to both trackers and the application:

- To protect the pass element of a tracker from overstress the current limitation will limit the output current to the maximum specified limit. Current sensing is done via a current mirror, no sense resistor is used. In case the maximum current condition is reached, the current will be limited and in consequence the output voltage will decrease. A tracker is protected against short circuit to ground and short circuit to battery voltage.
- The output voltage is monitored by the voltage monitoring. In case of over voltage at pin QTx, the corresponding tracker will be switched off, the event will be stored in an SPI status register (**MONSF1**) and an interrupt will be generated. In case of under voltage at pin QTx, the event will be stored in an SPI status register (**MONSF2**) and an interrupt will be generated. The tracker will not be switched off in case of output under voltage, which is shorter than the short to ground detection time *t*StG. If the under voltage should be present for more than *t*StG, the tracker will be switched off. This event will be stored in an SPI status register (**MONSF0**) and an interrupt will be generated.
- The tracker is capable to withstand a short circuit either to ground or to battery voltage without receiving a damage. In case of a short circuit to battery voltage and if the battery voltage is above the tracker over voltage threshold, the tracker will be switched off, the event will be stored in the SPI status register (**MONSF1**).
- There is no dedicated temperature sensor for this regulator. The temperature is sensed on the chip by other temperature sensors located at LDO\_µC and step down pre regulator. In case of the chip temperature will exceed the pre warning threshold, the event will be stored in an SPI status register (**OTWRNSF**) and an interrupt will be generated. If the chip temperature exceeds the temperature shutdown threshold, the tracker will be switched off. The temperature switch off time is at least one second.

Both trackers are switched off in STANDBY and FAILSAFE. In INIT, NORMAL, SLEEP and WAKE state each tracker is ON or OFF depending on the SPI configuration.

![](_page_4_Figure_1.jpeg)

Figure 14 Tracker 1 & 2 for sensor supply

#### 7.5.2 Electrical characteristics

#### Table 13 Electrical characteristics: Tracker 1 & 2

 $V_{\rm VS}$  =6.0 V to 40 V,  $T_{\rm j}$  = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                                | Symbol               |      | Values |      |          | Note /                                                                     | Number    |
|----------------------------------------------------------|----------------------|------|--------|------|----------|----------------------------------------------------------------------------|-----------|
|                                                          |                      | Min. | Тур.   | Max. |          | Test Condition                                                             |           |
| Sensor supply, Tracker 1 &                               | 2                    |      |        |      | <b>"</b> | -1                                                                         | 1         |
| Output voltage tracking accuracy to voltage reference 1) | $\Delta V_{\rm QTx}$ | - 10 | _      | 10   | mV       | 0 mA ≤ I <sub>QT1</sub> ≤ 150<br>mA                                        | P_7.5.2.1 |
| Output current limitation                                | $I_{QTx,max}$        | 170  | _      | 320  | mA       | _                                                                          | P_7.5.2.2 |
| Drop voltage                                             | $V_{dr,QTx}$         | _    | _      | 400  | mV       | 2)                                                                         | P_7.5.2.3 |
| Power supply ripple rejection                            | PSRR <sub>QTx</sub>  | 26   | _      | _    | dB       | $^{3)}$ $V_{\rm PREREG}$ = 5.8 V ; ESR $C_{\rm QTx}$ $\leq$ 100 m $\Omega$ |           |
| Output capacitor                                         | $C_{QTx}$            | 1    | _      | 10   | μF       | 3)                                                                         | P_7.5.2.5 |
| Output capacitor, ESR                                    | $ESR \ C_{QTx}$      | 0    | _      | 200  | mΩ       | 3)                                                                         | P_7.5.2.6 |

- 1) The output voltage of the tracker (pin QTx) is derived from the output voltage of the voltage reference (pin QVR). If the voltage reference is switched off (voltage at pin QVR = 0V), than the output voltage at pin QTx will also be 0V, if the tracker should be switched on, as the tracker output voltage is derived from pin QVR. But if the tracker is switched on and its output voltage is 0V (because voltage at pin QVR is 0V), an under voltage at pin QTx will be detected and an interrupt will be issued.
- 2) Dropout voltage is defined as the difference between input and output voltage when the output voltage decreases 100 mV from output voltage measured at  $V_1 = V_{Q,nom} + V_{dr,max} + 100$  mV.
- 3) Specified by design, not subject to production test