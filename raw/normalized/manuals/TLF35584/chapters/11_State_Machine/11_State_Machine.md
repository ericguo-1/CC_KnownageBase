# **7.5.3 Typical Performance Characteristics**

## **QTx Output Voltage** *V***QTx versus Junction Temperature** *T***<sup>j</sup>**

![](_page_0_Figure_3.jpeg)

**QTx Dropout Voltage** *V***dr,QTx versus Load Current** *I***QTx**

![](_page_0_Figure_5.jpeg)

**QTx Output Voltage** *V***QTx versus Load Current** *I***QTx**

![](_page_0_Figure_7.jpeg)

**QTx Dynamic Load Response (1mA to 100mA) (***V***QTx,nom = 5.0 V)**

![](_page_0_Figure_9.jpeg)

## **7.6 External Post Regulator for Core Supply (optional)**

An additional external post regulator may be added to the TLF35584 to provide the core supply voltage *V*Core\_Supply for the µC if needed.

In this case the configuration pin SEC has to be left open to indicate that the external core voltage supply option is active. The configuration of the SEC pin will only be read during the power sequencing at the point the core supply would be started (Movements to INIT, please refer to **Figure 16** and **Figure 17**).

The regulator is fed from the intermediate circuit voltage VPREREG. The post regulator is enabled by a high signal at pin EVC and switched off by a low signal at pin EVC. The EVC signal is controlled by the state machine. For example a detection of over voltage at pin VCI will create a low signal at pin EVC and shut down the post regulator to protect the µC core.

The device offers a synchronization signal of 50% duty cycle at pin SYN equal in phase (only with a very small delay) and frequency or shifted by 180 degree to the internal step down pre regulator (the selection is done via SPI command). It is highly recommended to synchronize the external switch mode post regulator to this signal to avoid interferences. The external post regulator will be enabled as soon as the pre regulator output voltage *V*PREREG is present and the LDO\_µC output voltage *V*QUC is above the lower reset threshold.

The output voltage of the post regulator *V*Core\_Supply will be monitored by the reset function of the device. To obtain a proper monitoring the output voltage of the post regulator has to be connected to the voltage monitoring input at pin VCI via a resistor divider. The resistor divider should be dimensioned to adjust the post regulator output voltage *V*Core\_Supply to the internal reset reference voltage *V*VCI.

The synchronization signal at pin SYN can be switched on via SPI command, default configuration is off.

Protection circuitry should be installed to prevent the external regulator and the application from damage:

- To protect the pass device(s) of the external post regulator from overstress a current limitation function should limit the output current to the maximum specified limit. Current sensing should be done via a current mirror, no sense resistor should be used. In case the maximum current should occur, it will be limited, thus the output voltage will decrease. The regulator should be protected against short circuit to ground.
- The output voltage is monitored by the voltage monitoring of the TLF35584, no further reset function is required on the external post regulator. In case such a reset function should be present, it will not be used or supported by the reset function of the TLF35584. In case of over voltage at pin, VCI the external post regulator will be switched off by pulling pin EVC to low and the TLF35584 will move into FAILSAFE state. The event will be stored in an SPI status register (**MONSF1**). In case of under voltage at pin VCI, the device will move into INIT state, pin ROT will be pulled low and the event will be stored in an SPI status register (**MONSF2**). The external post regulator will not be switched off in case of output under voltage, which is shorter than the short to ground detection time *t*StG. If the under voltage is present for more than *t*StG, the device will move into FAILSAFE state. This event will be stored in an SPI status register as well (**MONSF0**).
- There should be a temperature shutdown function at the external post regulator. If the power stage temperature should exceed the temperature shutdown threshold, the post regulator should be switched off by its own temperature shutdown. The TLF35584 will recognize this as an under voltage and react as described above.

![](_page_2_Picture_1.jpeg)

**Figure 15 External switch mode post regulator for core supply**

### **Table 14 Electrical characteristics: External post regulator**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                            | Symbol     | Values |      |      | Unit | Note /                                | Number    |
|--------------------------------------|------------|--------|------|------|------|---------------------------------------|-----------|
|                                      |            | Min.   | Typ. | Max. |      | Test<br>Condition                     |           |
| Enable signal, pin EVC               |            |        |      |      |      |                                       |           |
| Enable high level<br>TLF35584xxVS1   | VEVC, high | 4.0    | –    | –    | V    | VQUC = 5.0 V,<br>IEVC = -9<br>mA      | P_7.6.0.1 |
| Enable high level<br>TLF35584xxVS1   | VEVC, high | 4.6    | –    | –    | V    | VQUC<br>≥ 4.7 V,<br>IEVC = -0.5<br>mA | P_7.6.0.2 |
| Enable low level<br>TLF35584xxVS1    | VEVC, low  | –      | –    | 0.7  | V    | VQUC = 5.0 V<br>IEVC = 7<br>mA        | P_7.6.0.3 |
| Enable high level<br>TLF35584xxVS2   | VEVC, high | 2.3    | –    | –    | V    | VQUC = 3.3 V<br>IEVC = -7<br>mA       | P_7.6.0.4 |
| Enable high level<br>TLF35584xxVS2   | VEVC, high | 3.0    | –    | –    | V    | VQUC<br>≥ 3.1 V,<br>IEVC = -0.5<br>mA | P_7.6.0.5 |
| Enable low level<br>TLF35584xxVS2    | VEVC, low  | –      | –    | 0.7  | V    | VQUC = 3.3 V<br>IEVC = 5.5<br>mA      | P_7.6.0.6 |
| Enable rise time                     | tEVC, rise | –      | –    | 25   | ns   | CEVC, load = 50<br>pF<br>1)           | P_7.6.0.7 |
| Enable fall time                     | tEVC, fall | –      | –    | 25   | ns   | CEVC, load = 50<br>pF<br>1)           | P_7.6.0.8 |
| Synchronisation signal source        |            |        |      |      |      |                                       |           |
| Sync out high level<br>TLF35584xxVS1 | VSYN, high | 4.0    | –    | –    | V    | VQUC = 5.0 V,<br>ISYN = -9<br>mA      | P_7.6.0.9 |

**Table 14 Electrical characteristics: External post regulator** (cont'd)

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                        | Symbol     | Values |      |      | Unit | Note /                                | Number     |
|--------------------------------------------------|------------|--------|------|------|------|---------------------------------------|------------|
|                                                  |            | Min.   | Typ. | Max. |      | Test<br>Condition                     |            |
| Sync out high level<br>TLF35584xxVS1             | VSYN, high | 4.6    | –    | –    | V    | VQUC<br>≥ 4.7 V,<br>ISYN = -0.5<br>mA | P_7.6.0.10 |
| Sync out low level<br>TLF35584xxVS1              | VSYN, low  | –      | –    | 0.7  | V    | VQUC = 5.0 V<br>ISYN = 7<br>mA        | P_7.6.0.11 |
| Sync out high level<br>TLF35584xxVS2             | VSYN, high | 2.3    | –    | –    | V    | VQUC = 3.3 V<br>ISYN = -7<br>mA       | P_7.6.0.12 |
| Sync out high level<br>TLF35584xxVS2             | VSYN, high | 3.0    | –    | –    | V    | VQUC<br>≥ 3.1 V,<br>ISYN = -0.5<br>mA | P_7.6.0.13 |
| Sync out low level<br>TLF35584xxVS2              | VSYN, low  | –      | –    | 0.7  | V    | VQUC = 3.3 V<br>ISYN = 5.5<br>mA      | P_7.6.0.14 |
| Sync out signal duty cycle                       | DSYN       | –      | 50   | –    | %    | –                                     | P_7.6.0.15 |
| Synch out signal rise time                       | tSYN, rise | –      | –    | 25   | ns   | CSYN ,load = 50<br>pF<br>1)           | P_7.6.0.16 |
| Synch out signal fall time                       | tSYN, fall | –      | –    | 25   | ns   | CSYN, load = 50<br>pF<br>1)           | P_7.6.0.17 |
| Core voltage supply monitoring input             |            |        |      |      |      |                                       |            |
| Core voltage monitoring input<br>pull-up current | IVCI       | –      | 100  | 130  | nA   | VVCI = 0.8<br>V                       | P_7.6.0.18 |

<sup>1)</sup> specified by design, not subject to production test

## **7.7 Power Sequencing**

The TLF35584 includes a power sequencing function to ensure a proper ramping up of all output voltages. After the internal Power-On-Reset (POR) is released the standby regulator and the pre regulator start to operate.

In case of one of the non microcontroller related voltages (Volt\_Ref, LDO\_Com, Tracker1 or Tracker2) cannot be ramped up (e.g. short to GND), the power sequence is stopped, but the reset output is still released after the power on reset delay time *t*rd. The microcontroller should check the status of the outputs by reading the SPI status register (**VMONSTAT**).

In case the microcontroller is sending a SPI request to enable or disable any non microcontroller related LDO (Volt\_Ref, LDO\_Com, Tracker1 or Tracker2) during the power sequencing, the sequence will be stopped and the requested configuration will be executed.

## **7.7.1 Power sequencing from POR to INIT state**

![](_page_4_Figure_6.jpeg)

**Figure 16 Power sequencing POR to INIT state**

Description:

- 1. After POR is released the standby regulator and the pre regulator start to operate.
- 2. When *V*FB is above the lower reset threshold *V*RT,FB,low, the LDO\_µC starts to operate.
- 3. When *V*QUC is above the lower reset threshold *V*RT,QUC,low, the external core supply will be enabled, when selected. If the external core supply is not selected, the voltage reference LDO starts to operate.
- 4. If the external core supply is selected and *V*VCI is above the lower reset threshold *V*RT,VCI,low, the voltage reference LDO starts to operate.
- 5. When *V*QVR is above the lower reset threshold *V*RT,QVR,low, the LDO\_Com starts to operate.
- 6. When *V*QCO is above the lower reset threshold *V*RT,QCO,low, the Tracker 1 starts to operate.
- 7. When *V*QT1 is above the lower reset threshold *V*RT,QTx,low, the Tracker 2 starts to operate.
- 8. This is the time from the enabling of the standby regulator until its output *V*QST is above the lower reset threshold *V*RT,QST,low.
- 9. The reset delay time *t*RD starts after LDO\_STBY, LDO\_µC and the external core supply (if selected) have reached their lower reset threshold *V*RT,x,low. The reset delay time is programmable via SPI. After the rest delay time is expired, the ROT pin is pulled to high. The figure shows the possibilities of the *t*RD starting time.

Once the ROT is high, the microcontroller can change the configuration of the selectable LDOs which might change the power sequencing accordingly.

## **7.7.2 Power sequencing STANDBY to INIT state**

![](_page_6_Figure_2.jpeg)

**Figure 17 Power sequencing STANDBY to INIT state**

Description: Input voltage is present, device is in STANDBY state, LDO\_STBY is active.

- 1. After a valid Wake-Signal or an expired wake-up timer the pre regulator starts to operate.
- 2. When *V*FB is above the lower reset threshold *V*RT,FB,low, the LDO\_µC starts to operate.
- 3. When *V*QUC is above the lower reset threshold *V*RT,QUC,low, the external core supply will be enabled, when selected. If the external core supply is not selected, the voltage reference LDO starts to operate.
- 4. If the external core supply is selected and *V*VCI is above the lower reset threshold *V*RT,VCI,low, the voltage reference LDO starts to operate.
- 5. When *V*QVR is above the lower reset threshold *V*RT,QVR,low, the LDO\_Com starts to operate.
- 6. When *V*QCO is above the lower reset threshold *V*RT,QCO,low, the Tracker 1 starts to operate.

- 7. When *V*QT1 is above the lower reset threshold *V*RT,QTx,low, the Tracker 2 starts to operate.
- 8. The reset delay time *t*RD starts after LDO\_µC and the external core supply (if selected) have reached their lower reset threshold *V*RT,x,low. The reset delay time is programmable via SPI. After the rest delay time is expired the ROT pin is pulled to high. The figure shows the possibilities of the *t*RD starting time.

### **7.7.3 Power sequencing SLEEP to WAKE state**

![](_page_7_Figure_4.jpeg)

**Figure 18 Power sequencing SLEEP to WAKE state**

Description: Input voltage is present, device is in SLEEP state, all selectable LDOs switched off in SLEEP state, all selectable LDOs were switched on in previous NORMAL state:

- 1. After a valid Wake-Signal or an expired wake-up timer the voltage reference starts to operate.
- 2. When *V*QVR is above the lower reset threshold *V*RT,QVR,low, the LDO\_Com starts to operate.
- 3. When *V*QCO is above the lower reset threshold *V*RT,QCO,low, the Tracker 1 starts to operate.
- 4. When *V*QT1 is above the lower reset threshold *V*RT,QTx,low, the Tracker 2 starts to operate.

The reset output ROT is high in SLEEP state and will be kept high for WAKE state.

In case a selectable LDO was switched off in the previous NORMAL state, it will not be enabled during the transition from SLEEP to WAKE, the power sequencing will follow up with the next LDO. In case a LDO was enabled during SLEEP state and was enabled in the previous NORMAL state, it will be kept enabled.

# **8 Monitoring Function**

### **8.1 Introduction**

The TLF35584 includes an independent voltage monitoring function of all output voltages, including the optional external post regulator for µC core supply, if in use.

The monitoring function consists of two comparators for each output voltage. One is for detecting over voltage, the other is for detecting under voltage. Both comparators get their reference value from an independent bandgap only used for the voltage monitoring block. This bandgap is independent from the voltage regulator bandgap. The bandgap provides the reference value for over voltage detection (highvoltage reset threshold *V*RT,xxx,high) and for under voltage detection (low voltage reset threshold *V*RT,xxx,low). Under normal operation conditions the output voltage of the related regulator has to stay within the voltage window defined by the upper limit *V*RT,xxx,high and the lower limit *V*RT,xxx,low.

There is a dedicated temperature sensor for the monitoring block. If the power stage temperature exceeds the temperature shutdown threshold, the device will move into FAILSAFE state, the regulator will be switched off and the event will be stored in an SPI status register (**OTFAIL**). The off time due to temperature shut down will be at least one second.

### **Characteristics:**

The behavior of the over and under voltage comparators is as following:

- The upper limits *V*RT,xxx,high and the lower limits *V*RT,xxx,low are fixed for every regulator and cannot be programmed or varied by SPI command.
- An over voltage will be detected if the regulator output voltage is higher than the related over voltage reset threshold *V*RT,xxx,high for more than the reset reaction time *t*RR. An over voltage higher than the related over voltage reset threshold *V*RT,xxx,high which is present for shorter than the reset reaction time *t*RR will be regarded as a spike and will not be detected.
  - An under voltage will be detected if the regulator output voltage is lower than the related under voltage reset threshold *V*RT,xxx,low for more than the reset reaction time *t*RR. An under voltage lower than the related under voltage reset threshold *V*RT,xxx,low which is present for shorter than the reset reaction time *t*RR will be regarded as a spike and will not be detected.
- The reset reaction time *t*RR is not valid for the internal voltage supplies in case of under and over voltage.
- The detection of an over voltage will shut down the related regulator immediately to protect the loads from harm or destruction. This shut down may lead (depending on the affected regulator) to further action, please refer to chapter **State Machine** for details.
- The detection of an under voltage will not shut down the related regulator.
- The post regulators (including the optional external post regulator for µC core supply) have a short to ground detection. If the detected under voltage is present for more than the short to ground detection time *t*StG, the related regulator will shut down to protect himself and the chip from over heating. This shut down may lead (depending on the affected regulator) to further action, please refer to chapter **State Machine** for details. (It is mandatory that the external post regulator for µC core supply has an enable or inhibit function).
- The over and under voltage detection is active only if the related regulator is in use (including the external post regulator for µC core supply) and switched on.

### **Indication of over and under voltage:**

Depending on the related regulator the indication of over and under voltage will be different, either by reset signal or by interrupt indication:

- Every over and under voltage detection will be stored in the SPI status register (**MONSF0**, **MONSF1**, **MONSF2**).
- For µC related output voltages (*V*QST , *V*QUC , *V*VCI), over and under voltage are indicated by the hardware reset pin ROT. In case of an over or under voltage, pin ROT is pulled to low.
- In case of over voltage or a detection of a short to ground at the external post regulator for µC core supply, the pin EVC will be pulled to low to shut down the regulator.
- For the pre regulator output (*V*FB) and the voltage reference output (*V*QVR) only over voltage is indicated by the hardware reset pin ROT. In case of an over voltage, pin ROT is pulled to low.
- For the pre regulator output and the voltage reference output, only under voltage is indicated by an interrupt.
- For all not µC related output voltages (*V*QCO , *V*QT1 , *V*QT2), over and under voltage are indicated by an interrupt.
- For the internal supply voltages, over and under voltage are indicated by the hardware reset pin ROT. In case of an over or under voltage, pin ROT is pulled to low.

This introduction is an overview, for details please refer to the following sub chapters.

# **8.2 Shutdown Function**

A short to ground detection time *t*StG at the pre regulator output is only active during the power sequence in INIT state. If the output voltage of the pre regulator should not be within the specified limits within a certain time frame, the device will move into FAILSAFE state. There will be no reaction on a detected short to ground once the *V*PREREG,BUCK is in a valid range after crossing the first time its UV threshold (step 1 completed according to the power sequencing described in **Chapter 7.7**). If the output voltage of the pre regulator should be too low in other cases, the behavior of the device will depend on the voltage monitoring of the post regulators.

The detection of an over voltage at output voltages *V*QUC, *V*VCI, *V*QST, *V*QVR or *V*FB will shut down all regulators to protect the loads from harm or destruction and moves the device to FAILSAFE.

The detection of an over voltage at output voltages *V*QCO, *V*QT1 and *V*QT2 will shut down the related regulator to protect the loads from harm or destruction and generate an interrupt event.

If the detected under voltage at output voltages *V*QUC, *V*VCI or *V*QST should be present for more than the short to ground detection time *t*StG, all regulators will shut down to protect themselves and the chip from over heating and move the device to FAILSAFE.

If the detected under voltage at output voltages *V*QVR, *V*QCO, *V*QT1 or *V*QT2 should be present for more than the short to ground detection time tStG, the related regulator will shut down to protect himself and the chip from over heating and generate an interrupt event.

### **8.3 Reset Function**

The reset generator starts to operate as soon as the internal POR is released.

## **Distinguish between "Soft Reset" and "Hard Reset"**

It is called a "Soft Reset" if pin ROT goes below *V*ROT,low, but the pre and post regulator output voltages are not switched off.

It is called a "Hard Reset" if pin ROT goes below  $V_{\rm ROT,low}$  and the post regulator output voltages are switched off. The power sequencing will be restarted after a delay of  $t_{\rm SDT}$ . (Applicable to the second initialization timeout in a row)

#### Safe State Control trigger event

The safe state control function is connected to the monitoring block. In case of a safe state control trigger event is detected, pins Safe State Control Outputs (SS1 and SS2) and ROT will be pulled to ground. The safe state control trigger event will be stored in a SPI register (respective bits in SYSFAIL, INITERR, MONSF1, MONSF2, MONSF3 or OTFAIL). For trigger conditions of safe state signal SS1 please refer to chapter Safe State Control Function.

#### Reset output pin

The reset output pin ROT is an open drain structure. As soon as a reset condition occurs, the ROT pin is pulled below  $V_{\text{ROT,low}}$ . An internal pull up current is pulling the output towards  $V_{\text{QUC}}$ .

![](_page_0_Figure_6.jpeg)

Figure 19 Principle reset function

### **Detailed description of the reset function (Figure 19):**

The following regulators contribute to the reset function:

- Internal supply monitoring (not visible externally)
- The standby regulator (Q\_STBY\_LDO): *V*QST
- The LDO for supplying the µC (Q\_LDO\_µC): *V*QUC
- The external post regulator for µC core supply (Core\_sup adj.): *V*VCI
- The voltage reference (Volt\_Ref.): *V*QVR only over voltage, not under voltage, not short to ground
- The pre regulator (PreReg.): *V*FB only over voltage, not under voltage

The actual values of these outputs are taken directly at the output pins and are monitored by two comparators for each regulator, one for over voltage (named OV), the other for under voltage (named UV). The reference values *V*RT,XXX,high and *V*RT,XXX,low are provided by an independent band gap 2 only related to the monitoring functions.

The "Internal supply voltage regulator monitoring" of over and under voltage events and IBIAS monitoring are contributing to trigger a reset. If one or both of the internal supply voltages should be out of their specified windows, the proper function of the device cannot be guaranteed any more. The IBIAS monitor fault is stored in a status bit (**BIASHI** or **BIASLOW**). The fault of the internal supplies will trigger a "Move to Powerdown" event (please refer to chapter **State Machine** for details).

![](_page_2_Figure_1.jpeg)

**Figure 20 Timing diagram hardware reset signal ROT for output voltages**

## Description:

- *V*XXX = Output voltage monitored by reset generator: *V*QUC , *V*VCI, *V*QST, *V*QVR or *V*FB
- *V*RT,XXX,high= Over voltage reset threshold: *V*RT,QUC,high, *V*RT,VCI,high, *V*RT,QST,high, *V*RT,QVR,high or *V*RT,FB,high
- *V*RT,XXX,low= Under voltage reset threshold: *V*RT,VCI,low, *V*RT,QUC,low or *V*RT,QST,low
- *t*RD = Reset delay time, adjustable by SPI command
- tRR = Reset reaction time, time between detecting over voltage and pulling ROT to low
- < *t*RR = Not detectable, because shorter than reset reaction time
- > *t*StG = Short to ground detection time, time after an under voltage is considered as a short to ground
- *t*FAILSAFE,min = System shutdown time (FAILSAFE), time between pulling ROT to low and restart of the device, for details please refer to chapter **State Machine**
- *V*ROT = Hardware reset signal, ROT
- *V*ROT,high = Hardware reset signal, high level
- *V*ROT,low = Hardware reset signal, low level
- *V*XXX,OV = Over voltage detected for *V*XXX and stored in SPI register (**MONSF1**)
- *V*XXX,UV = Under voltage detected for *V*XXX and stored in SPI register (**MONSF2**)
- *V*XXX,StG = Short to ground detected for *V*XXX and stored in SPI register (**MONSF0**)
- Applies as well to bias current violations, supply overvoltage (**MONSF3**), temperature shutdown (**OTFAIL**) contributing to the reset function. Please refer to **Figure 43** and **Figure 50**

# **8.4 Interrupt Function**

The interrupt generator starts to operate as soon as the internal POR is released.

The voltage monitoring function supervises the values of the non µC related post regulator output voltages *V*QCO, *V*QT1 and *V*QT2, the pre regulator output voltage *V*FB (under voltage only) and the voltage reference output *V*QVR (under voltage and short to ground only). The result is written in a SPI status register (**IF** and **MONSF0**, **MONSF1** or **MONSF2**) and indicated via interrupt (pin INT). The connection of all these monitoring signals is a logic OR.

The interrupt pin INT does not only indicate the result of the voltage monitoring, but also interrupts due to other events in the device.

## **Interrupt output pin**

The interrupt output pin INT is a push pull structure. An interrupt is indicated by pulling the INT pin to ground.

![](_page_3_Figure_7.jpeg)

**Figure 21 Principle indication of voltage monitoring via interrupt**

## **Detailed description of the voltage monitoring via interrupt function (Figure 21):**

The following regulators contribute to the voltage monitoring via interrupt function:

- The pre regulator (PreReg.): *V*FB , just under voltage
- The voltage reference (Volt\_Ref.): *V*QVR , just under voltage and short to GND
- The LDO for supplying the communication (LDO\_Com): *V*QCO
- The sensor supply 1 (Tracker 1): *V*QT1
- The sensor supply 2 (Tracker 2): *V*QT2

The actual values of these outputs are taken directly at the output pins and monitored by two comparators for each regulator, one for over voltage (named OV), the other for under voltage (named UV). The reference values *V*RT,XXX,high and *V*RT,XXX,low are provided by an independent band gap 2 only related to the monitoring functions.

![](_page_4_Figure_9.jpeg)

**Figure 22 Timing diagram interrupt indication for output voltages**

#### Description:

- *V*XXX = Output voltage monitored by interrupt indication: *V*FB , *V*QVR, *V*QCO , *V*QT1 or *V*QT2
- *V*RT,XXX,high= Over voltage interrupt indication: *V*RT,QCO,high, *V*RT,QT1,high or *V*RT,QT2,high
- *V*RT,XXX,low= Under voltage interrupt indication: *V*RT,FB,low, *V*RT,QVR,low, *V*RT,QCO,low, *V*RT,QT1,low or *V*RT,QT2,low
- *t*RR = Reset reaction time, time between detecting overvoltage and an interrupt is generated
- < *t*RR = Not detectable, because shorter than reset reaction time
- > *t*StG = Short to ground detection time, time after an under voltage is considered as a short to ground
- *V*XXX,OV = Over voltage detected for *V*XXX and stored in SPI register (**MONSF1**)
- *V*XXX,UV = Under voltage detected for *V*XXX and stored in SPI register (**MONSF2**)
- *V*XXX,StG = Short to ground detected for *V*XXX and stored in SPI register (**MONSF0**)
- Applies as well to detection of bandgap 1 to 2 variations (**MONSF3**), over load and temperature events (**OTWRNSF**, **OTFAIL**) contributing to the interrupt function. Please refer to **Figure 42**

# **8.5 Electrical Characteristics Voltage Monitoring and Reset Function**

**Table 15 Electrical Characteristics: Hardware reset signals**

| Parameter                                             | Symbol             | Values |      |       | Unit   | Note /                                                       | Number   |
|-------------------------------------------------------|--------------------|--------|------|-------|--------|--------------------------------------------------------------|----------|
|                                                       |                    | Min.   | Typ. | Max.  |        | Test<br>Condition                                            |          |
| Timing                                                |                    |        |      |       |        |                                                              |          |
| Reset cycle time                                      | tCYCLE             | 9.4    | 10   | 10.65 | µs     | –                                                            | P_8.5.1  |
| Reset delay time, default<br>value                    | tRD                | –      | 1000 | –     | tCYCLE | –                                                            | P_8.5.2  |
| Reset delay time, adjustable<br>range by SPI command  | tRD                | 20     | –    | 1500  | tCYCLE | 1)                                                           | P_8.5.3  |
| Reset reaction time                                   | tRR                | 8      | –    | 20    | µs     | –                                                            | P_8.5.4  |
| Reset reaction time, standby<br>regulator             | tRR, STBY          | 8      | –    | 40    | µs     | –                                                            | P_8.5.5  |
| Short to ground detection<br>time                     | tStG               | 2.7    | 3    | 3.3   | ms     |                                                              | P_8.5.6  |
| Step-down regulator short to<br>ground detection time | tStG,HF            | 2.7    | 3    | 3.3   | ms     | step down pre<br>regulator 2.2<br>MHz<br>switching frequency | P_8.5.7  |
| Step-down regulator short to<br>ground detection time | tStG,LF            | 5.4    | 6    | 6.6   | ms     | step down pre<br>regulator 400 kHz<br>switching frequency    | P_8.5.8  |
| System shutdown time                                  | tSDT               | 9      | –    | 20    | ms     | –                                                            | P_8.5.9  |
| Reset thresholds standby regulator, pin QST           |                    |        |      |       |        |                                                              |          |
| Over voltage reset threshold<br>TLF35584xxVS1         | VRT,QST,high       | 5.25   | 5.35 | 5.45  | V      | VQST increasing                                              | P_8.5.10 |
| Over voltage reset hysteresis<br>TLF35584xxVS2        | VRT,QST,OV<br>hyst | 30     | –    | 90    | mV     | –                                                            | P_8.5.11 |
| Under voltage reset threshold<br>TLF35584xxVS1        | VRT,QST,low        | 4.2    | 4.3  | 4.4   | V      | VQST decreasing                                              | P_8.5.12 |
| Under voltage reset<br>hysteresis TLF35584xxVS1       | VRT,QST,UV<br>hyst | 30     | –    | 70    | mV     | –                                                            | P_8.5.13 |
| Over voltage reset threshold<br>TLF35584xxVS2         | VRT,QST,high       | 3.46   | 3.53 | 3.6   | V      | VQST increasing                                              | P_8.5.14 |
| Over voltage reset hysteresis<br>TLF35584xxVS2        | VRT,QST,OV<br>hyst | 20     | –    | 55    | mV     | –                                                            | P_8.5.15 |
| Under voltage reset threshold<br>TLF35584xxVS2        | VRT,QST,low        | 2.9    | 2.97 | 3.05  | V      | VQST decreasing                                              | P_8.5.16 |
| Under voltage reset<br>hysteresis TLF35584xxVS2       | VRT,QST,UV<br>hyst | 20     | –    | 50    | mV     | –                                                            | P_8.5.17 |
| Reset thresholds LDO_µC, pin QUC                      |                    |        |      |       |        |                                                              |          |

**Table 15 Electrical Characteristics: Hardware reset signals** (cont'd)

| Parameter                                       | Symbol             | Values |      |      | Unit | Note /             | Number   |
|-------------------------------------------------|--------------------|--------|------|------|------|--------------------|----------|
|                                                 |                    | Min.   | Typ. | Max. |      | Test<br>Condition  |          |
| Over voltage reset threshold<br>TLF35584xxVS1   | VRT,QUC,high       | 5.25   | 5.35 | 5.45 | V    | VLDO_µC increasing | P_8.5.18 |
| Over voltage reset hysteresis<br>TLF35584xxVS1  | VRT,QUC,OV<br>hyst | 30     | –    | 90   | mV   | 2)                 | P_8.5.19 |
| Under voltage reset threshold<br>TLF35584xxVS1  | VRT,QUC,low        | 4.2    | 4.3  | 4.4  | V    | VLDO_µC decreasing | P_8.5.20 |
| Under voltage reset<br>hysteresis TLF35584xxVS1 | VRT,QUC,UV<br>hyst | 30     | –    | 70   | mV   | 2)                 | P_8.5.21 |
| Over voltage reset threshold<br>TLF35584xxVS2   | VRT,QUC,high       | 3.46   | 3.53 | 3.6  | V    | VQUC increasing    | P_8.5.22 |
| Over voltage reset hysteresis<br>TLF35584xxVS2  | VRT,QUC,OV<br>hyst | 20     | –    | 55   | mV   | 2)                 | P_8.5.23 |
| Under voltage reset threshold<br>TLF35584xxVS2  | VRT,QUC,low        | 2.9    | 2.97 | 3.05 | V    | VQUC decreasing    | P_8.5.24 |
| Under voltage reset<br>hysteresis TLF35584xxVS2 | VRT,QUC,UV<br>hyst | 20     | –    | 50   | mV   | 2)                 | P_8.5.25 |
| Reset thresholds external core supply, pin VCI  |                    |        |      |      |      |                    |          |
| Over voltage reset threshold                    | VRT,VCI,high       | 860    | 872  | 884  | mV   | VVCI increasing    | P_8.5.26 |
| Over voltage reset hysteresis                   | VRT,VCI,OV<br>hyst | 5      | –    | 15   | mV   | 2)                 | P_8.5.27 |
| Under voltage reset threshold                   | VRT,VCI,low        | 716    | 728  | 740  | mV   | VVCI decreasing    | P_8.5.28 |
| Under voltage reset<br>hysteresis               | VRT,VCI,UV<br>hyst | 5      | –    | 15   | mV   | 2)                 | P_8.5.29 |
| Reset thresholds V_PreReg, pins FBx             |                    |        |      |      |      |                    |          |
| Over voltage reset threshold                    | VRT,FB,high        | 6.46   | 6.58 | 6.7  | V    | VFB increasing     | P_8.5.30 |
| Over voltage reset hysteresis                   | VRT,FB,OV hyst     | 40     | –    | 120  | mV   | –                  | P_8.5.31 |
| Under voltage reset threshold                   | VRT,FB,low         | 5.0    | 5.1  | 5.2  | V    | VFB decreasing     | P_8.5.32 |
| Under voltage reset<br>hysteresis               | VRT,FB,UV hyst     | 30     | –    | 90   | mV   | –                  | P_8.5.33 |
| Reset thresholds LDO_Com, pin QCO               |                    |        |      |      |      |                    |          |
| Over voltage reset threshold                    | VRT,QCO,high       | 5.4    | 5.5  | 5.6  | V    | VQCO increasing    | P_8.5.34 |
| Over voltage reset hysteresis                   | VRT,QCO,OV<br>hyst | 30     | –    | 90   | mV   | –                  | P_8.5.35 |
| Under voltage reset threshold                   | VRT,QCO,low        | 4.4    | 4.5  | 4.6  | V    | VQCO decreasing    | P_8.5.36 |
| Under voltage reset<br>hysteresis               | VRT,QCO,UV<br>hyst | 20     | –    | 80   | mV   | –                  | P_8.5.37 |
| Reset thresholds voltage reference, pin QVR     |                    |        |      |      |      |                    |          |
| Over voltage reset threshold                    | VRT,QVR,high       | 5.25   | 5.35 | 5.45 | V    | VQVR increasing    | P_8.5.38 |
|                                                 |                    |        |      |      |      |                    |          |

**Table 15 Electrical Characteristics: Hardware reset signals** (cont'd)

| Parameter                                | Symbol             | Values |      |      | Unit | Note /                            | Number   |
|------------------------------------------|--------------------|--------|------|------|------|-----------------------------------|----------|
|                                          |                    | Min.   | Typ. | Max. |      | Test<br>Condition                 |          |
| Over voltage reset hysteresis            | VRT,QVR,OV<br>hyst | 30     | –    | 80   | mV   | –                                 | P_8.5.39 |
| Under voltage reset threshold            | VRT,QVR,low        | 4.2    | 4.3  | 4.4  | V    | VQVR decreasing                   | P_8.5.40 |
| Under voltage reset<br>hysteresis        | VRT,QVR,UV<br>hyst | 30     | –    | 70   | mV   | –                                 | P_8.5.41 |
| Reset thresholds tracker 1, pin QT1      |                    |        |      |      |      |                                   |          |
| Over voltage reset threshold             | VRT,QT1,high       | 5.4    | 5.5  | 5.6  | V    | VQT1 increasing                   | P_8.5.42 |
| Over voltage reset hysteresis            | VRT,QT1,OV<br>hyst | 30     | –    | 90   | mV   | –                                 | P_8.5.43 |
| Under voltage reset threshold            | VRT,QT1,low        | 4.4    | 4.5  | 4.6  | V    | VQT1 decreasing                   | P_8.5.44 |
| Under voltage reset<br>hysteresis        | VRT,QT1,UV<br>hyst | 20     | –    | 80   | mV   | –                                 | P_8.5.45 |
| Reset thresholds tracker 2, pin QT2      |                    |        |      |      |      |                                   |          |
| Over voltage reset threshold             | VRT,QT2,high       | 5.4    | 5.5  | 5.6  | V    | VQT2 increasing                   | P_8.5.46 |
| Over voltage reset hysteresis            | VRT,QT2,OV<br>hyst | 30     | –    | 90   | mV   | –                                 | P_8.5.47 |
| Under voltage reset threshold            | VRT,QT2,low        | 4.4    | 4.5  | 4.6  | V    | VQT2 decreasing                   | P_8.5.48 |
| Under voltage reset<br>hysteresis        | VRT,QT2,UV<br>hyst | 20     | –    | 80   | mV   | –                                 | P_8.5.49 |
| Input Voltage VSx Monitoring, pin VSx    |                    |        |      |      |      |                                   |          |
| Input over voltage reset<br>threshold    | VVS,OV             | 45     | 47   | 49   | V    |                                   | P_8.5.50 |
| Overtemperature Protection of Monitoring |                    |        |      |      |      |                                   |          |
| Over temperature shutdown<br>threshold   | Tj,OT, shutdown    | 175    | 190  | 205  | °C   | Tj<br>increasing<br>2)            | P_8.5.51 |
| Over temperature shutdown<br>hysteresis  | Tj,OT, hyst        | –      | 10   | –    | °C   | 2)                                | P_8.5.52 |
| Reset output ROT                         |                    |        |      |      |      |                                   |          |
| Reset output, pull-up current            | IROT, pu           | -175   | -110 | -15  | µA   | VROT <= 2.0<br>V                  | P_8.5.53 |
| Reset output, low level<br>TLF35584xxVS1 | VROT, low          | –      | –    | 0.7  | V    | VQUC = 5.0 V,<br>IROT = 7<br>mA   | P_8.5.54 |
| Reset output, low level<br>TLF35584xxVS1 | VROT, low          | –      | –    | 0.4  | V    | VQUC = 5.0 V,<br>IROT = 3.5<br>mA | P_8.5.55 |
| Reset output, low level<br>TLF35584xxVS2 | VROT, low          | –      | –    | 0.7  | V    | VQUC = 3.3 V,<br>IROT = 5.5<br>mA | P_8.5.56 |
| Reset output, low level<br>TLF35584xxVS2 | VROT, low          | –      | –    | 0.4  | V    | VQUC = 3.3 V,<br>IROT = 3<br>mA   | P_8.5.57 |
| Reset output fall time 2)                | tROT, fall         | –      | –    | 25   | ns   | CROT,load = 50<br>pF              | P_8.5.58 |

**Table 15 Electrical Characteristics: Hardware reset signals** (cont'd)

| Parameter                                     | Symbol     | Values |      |      | Unit | Note /                           | Number   |
|-----------------------------------------------|------------|--------|------|------|------|----------------------------------|----------|
|                                               |            | Min.   | Typ. | Max. |      | Test<br>Condition                |          |
| Interrupt output INT                          |            |        |      |      |      |                                  |          |
| Interrupt output, high level<br>TLF35584xxVS1 | VINT, high | 4.0    | –    | –    | V    | VQUC = 5.0 V,<br>IINT = -9<br>mA | P_8.5.59 |
| Interrupt output, low level<br>TLF35584xxVS1  | VINT, low  | –      | –    | 0.7  | V    | VQUC = 5.0 V<br>IINT = 7<br>mA   | P_8.5.60 |
| Interrupt output, high level<br>TLF35584xxVS2 | VINT, high | 2.3    | –    | –    | V    | VQUC = 3.3 V<br>IINT = -7<br>mA  | P_8.5.61 |
| Interrupt output, low level<br>TLF35584xxVS2  | VINT, low  | –      | –    | 0.7  | V    | VQUC = 3.3 V<br>IINT = 5.5<br>mA | P_8.5.62 |
| Interrupt output rise time 2)                 | tINT, rise | –      | –    | 25   | ns   | CINT,load = 50<br>pF             | P_8.5.63 |
| Interrupt output fall time 2)                 | tINT, fall | –      | –    | 25   | ns   | CINT,load = 50<br>pF             | P_8.5.64 |

<sup>1)</sup> Due to internal delays the reset delay time can be enlarged by max 50µs. Please consider the transition time into INIT state *t*r,INIT specified in **Table 11-8** prior to the power sequencing started by entering INIT state.

<sup>2)</sup> Specified by design, not subject to production test

# **9 Standby LDO and Internal Supplies**

# **9.1 Standby LDO:**

# **9.1.1 Functional description**

The standby regulator LDO\_STBY is independent from the pre regulator stage and the other post regulators. It might be switched ON or OFF in all states (for details please refer to chapter **State Machine**). The linear low drop regulator LDO\_STBY offers a precise 3.3 V (or 5.0 V, equal to LDO\_µC) output voltage for standby supply.

The LDO\_STBY will keep its state by leaving the STANDBY state according to its previous configuration. For STANDBY state, the status of LDO\_STBY (ON or OFF) has to be defined in previous states.

The regulator is supplied from pin VST. Depending on the needs of the application pin VST might be connected directly to battery voltage (protected by reverse polarity diode) or to the output of the step up pre regulator (pin VSx). The output voltage *V*QST (at pin QST) is controlled by the error amplifier. The actual value is compared to a reference voltage derived from band gap 1 for regulators. The stability of the control loop is depending on the load current, the characteristics of the output capacitor and the chip temperature. To ensure stable operation the output capacitor should be chosen according the specified requirements (capacitance value and electrical series resistance ESR) in table "Electrical characteristics".

Protection circuitry is installed to prevent the regulator and the application from damage:

- To protect the pass element from overstress the current limitation will limit the output current to the maximum specified limit. Current sensing is done via a current mirror, no sense resistor is used. In case the maximum current should occur, it will be limited., thus the output voltage will decrease. The regulator is protected against short circuit to ground.
- The output voltage is monitored by the voltage monitoring. In case of over voltage at pin QST, the LDO\_STBY will be switched off and the device will move into FAILSAFE state. The event will be stored in an SPI status register (**MONSF1**). In case of under voltage at pin QST, the device will move into INIT state, pin ROT will be pulled low and the event will be stored in an SPI status register (**MONSF2**). The regulator will not be switched off in case of output under voltage, which is shorter than the short to ground detection time *t*StG. If the under voltage should be present for more than *t*StG, the device will move into FAILSAFE state. This event will be stored in an SPI status register as well (**MONSF0**).
- There is no dedicated temperature sensor for this regulator. The temperature is sensed on the chip by other temperature sensors located at LDO\_µC and step down pre regulator. In case of the chip temperature will exceed the pre warning threshold, an interrupt will indicate this event and it will be stored in an SPI status register (**OTFAIL**). If the chip temperature will exceed the temperature shutdown threshold, the post regulator will be switched off. The temperature switch off time will be at least one second. An overload at LDO STBY (over current detected for more than 1ms) will be indicated by interrupt, except if the device is in STANDBYstate and the event will be stored in SPI status register (**OTWRNSF**).

The regulator LDO\_STBY may be configured to be ON or OFF in every state, except FAILSAFE. The selection for STANDBY state shall be done by SPI command before entering this state.

For further details please refer to **Chapter 11 State Machine**.

![](_page_0_Figure_1.jpeg)

**Figure 23 Low drop linear regulator for standby supply**

### **9.1.2 Electrical characteristics**

### **Table 16 Electrical characteristics: Standby LDO**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                        | Symbol      | Values |      |      | Unit | Note /                                | Number  |
|----------------------------------|-------------|--------|------|------|------|---------------------------------------|---------|
|                                  |             | Min.   | Typ. | Max. |      | Test<br>Condition                     |         |
| Standby LDO                      |             |        |      |      |      |                                       |         |
| Output voltage<br>TLF35584xxVS1  | VQST        | 4.8    | 5.0  | 5.2  | V    | 0 mA ≤ IQST≤ 10 mA                    | P_9.1.1 |
| Output voltage<br>TLF35584xxVS2  | VQST        | 3.17   | 3.3  | 3.43 | V    | 0 mA < IQST< 10 mA                    | P_9.1.2 |
| Output current limitation        | IQST, max   | 15     | –    | 40   | mA   | –                                     | P_9.1.3 |
| Drop voltage                     | Vdr, QST    | –      | –    | 400  | mV   | –                                     | P_9.1.4 |
| Load regulation<br>TLF35584xxVS1 | ∆VQST, load | –      | 25   | 40   | mV   | IQST<br>=<br>100<br>µA to<br>10<br>mA | P_9.1.5 |
| Load regulation<br>TLF35584xxVS2 | ∆VQST, load | –      | 20   | 40   | mV   | IQST<br>=<br>100<br>µA to<br>10<br>mA | P_9.1.6 |
| Line regulation<br>TLF35584xxVS1 | ∆VQST, line | –      | 0.1  | 0.5  | mV/V | –                                     | P_9.1.7 |
| Line regulation<br>TLF35584xxVS2 | ∆VQST, line | –      | 0.1  | 0.5  | mV/V | –                                     | P_9.1.8 |

#### **Standby LDO and Internal Supplies**

**Table 16 Electrical characteristics: Standby LDO** (cont'd)

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                     | Symbol   | Values |      |      | Unit | Note /                     | Number   |
|-------------------------------|----------|--------|------|------|------|----------------------------|----------|
|                               |          | Min.   | Typ. | Max. |      | Test<br>Condition          |          |
| Power supply ripple rejection | PSRRQST  | 40     | –    | –    | dB   | fripple = 100<br>kHz<br>1) | P_9.1.9  |
|                               |          |        |      |      |      | ESRCQST<br>≤<br>100mΩ      |          |
| Output capacitor              | CQST     | 0.47   | –    | 10   | µF   | 1)                         | P_9.1.10 |
| Output capacitor, ESR         | ESR CQST | 0      | –    | 200  | mΩ   | 1)                         | P_9.1.11 |

<sup>1)</sup> Specified by design, not subject to production test

#### 9.1.3 Typical Performance Characteristics

#### QST Output Voltage $V_{\rm QST}$ versus Junction Temperature $T_{\rm i}$ (TLF35584xxVS1)

![](_page_2_Figure_3.jpeg)

QST Output Voltage  $V_{\rm QST}$  versus Supply Voltage  $V_{\rm VS}$  (TLF35584xxVS1)

![](_page_2_Figure_5.jpeg)

### QST Output Voltage $V_{\rm QST}$ versus Junction Temperature $T_{\rm i}$ (TLF35584xxVS2)

![](_page_2_Figure_7.jpeg)

QST Output Voltage  $V_{\rm QST}$  versus Supply Voltage  $V_{\rm VS}$  (TLF35584xxVS2)

![](_page_2_Figure_9.jpeg)

# **QST Output Voltage** *V***QST versus Load Current** *I***QST (TLF35584xxVS1)**

![](_page_3_Figure_2.jpeg)

**QST Dropout Voltage** *V***dr,QST versus Load Current** *I***QST (TLF35584xxVS1)**

![](_page_3_Figure_4.jpeg)

# **QST Output Voltage** *V***QST versus Load Current** *I***QST (TLF35584xxVS2)**

![](_page_3_Figure_6.jpeg)

**QST Dropout Voltage** *V***dr,QST versus Load Current** *I***QST (TLF35584xxVS2)**

![](_page_3_Figure_8.jpeg)

# **QST Dynamic Load Response (0mA to 5mA) TLF35584xxVS1 (***V***QST,nom = 5.0 V)**

![](_page_4_Figure_2.jpeg)

![](_page_4_Figure_3.jpeg)

### **QST Dynamic Load Response (0mA to 5mA) TLF35584xxVS2 (***V***QST,nom = 3.3 V)**

![](_page_4_Figure_5.jpeg)

![](_page_4_Figure_6.jpeg)

# **9.2 Internal Supplies**

The TLF35584 includes internal voltage supplies and bias currents to operate all regulators, monitoring and logic functions. These internal supplies are monitored internally to ensure proper functionality of the functional blocks the TLF35584 provides. The device will react on internal failure conditions as described in the **State Machine**, **Monitoring Function**, **Interrupt Generation** and **Safe State Control Function**.

The internal regulators do not require external components (i.e capacitors). The internal voltages are not visible at any pin.

# 10 Wake Up Timer

### 10.1 Description

The wake up timer is a function to wake up the TLF35584.

The wake up timer value may be set by SPI in INIT, NORMAL and WAKE state. The value is stored in the 24 bit wide wake up timer register (WKTIMCFG1, WKTIMCFG1, WKTIMCFG2).

The wake up timer is implemented as a 24 bit counter which is clocked by a 100 kHz or 100 Hz clock (time-base). The time-base may be selected via SPI.

For the chosen time-base of 100 kHz the timer resolution is 10  $\mu$ s and a wake up time between 10  $\mu$ s to 168 s can be configured via SPI.<sup>1)</sup>

For the chosen time-base of 100 Hz the timer resolution is 10 ms and a wake up time between 10 ms to 1.9 days can be configured via SPI.

When entering STANDBY or SLEEP state, the counter is loaded with the value of the wake up timer register and starts decrementing. At underflow, the timer will wake up the device from either SLEEP or STANDBY state. When leaving SLEEP state, an interrupt will be generated.

![](_page_6_Figure_9.jpeg)

Figure 24 Wake up timer principle

<sup>1)</sup> An additional activation delay time for the start of the wake up timer of max. 40 µs has to be considered after entering SLEEP or STANDBY state.

# **10.2 Electrical Characteristics**

**Table 17 Electrical Characteristics: Wake up timer**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

|                       | Symbol       | Values |      |      | Unit | Note /            | Number   |
|-----------------------|--------------|--------|------|------|------|-------------------|----------|
| Parameter             |              |        |      |      |      |                   |          |
|                       |              | Min.   | Typ. | Max. |      | Test<br>Condition |          |
| Wake up timer         |              |        |      |      |      |                   |          |
| Time base, resolution | tWakeUpTimer | 9.5    | 10   | 10.5 | µs   | 1)                | P_10.2.1 |
| Time base, resolution | tWakeUpTimer | 9.5    | 10   | 10.5 | ms   | –                 | P_10.2.2 |
| Counter               | C            | -      | 24   | -    | bit  | 2)                | P_10.2.3 |

<sup>1)</sup> Due to internal delays the wake-up time can be enlarged by max 50µs.

<sup>2)</sup> Specified by design, not subject to production test

#### 11 State Machine

#### 11.1 Introduction

The state machine describes the different states of operation, the device may get into. The following figure shows the state machine flow diagram, for detailed information please refer to following pages.

![](_page_8_Figure_4.jpeg)

Figure 25 Flow Diagram State Machine

#### **Description:**

- ON /OFF:= Switched ON or OFF, not configurable by SPI command
- ON\*:= Switched ON by entering the INIT state, then selectable via SPI
- SELECTED:= May be configured (switched ON or OFF) by SPI command in previous state or is selected by the state transition request (DEVCTRL) in case of LDO configuration for SLEEP state.
- SELECTABLE:= May be switched ON or OFF by SPI command in this state
- SELECTABLE\*\*:= Switched ON by default after POR, then selectable via SPI
- ADJUSTED:= Defined present or not present by configuration pin, not configurable by SPI command
- ACTIVE:= as described in INIT-State
- SSC, SS1&2:= Safe State Control signals 1 and 2
- LOW:= Signal is low
- HIGH:= Signal is high
- OV:= Over voltage
- UV:= Under voltage
- StG:= Short to ground
- TSD:= Thermal shut down
- OC:= Over current
- ABIST:= Analog built in self test
- Comp BG1 <-> BG2 > 4%: The difference between both band gaps 1 and 2 is more than 4%

## **11.2 Description of States**

### **11.2.1 POWERDOWN-state**

The device is in POWERDOWN-state as long the Power-on-Reset (POR) is not released.

|           | POWERDOWN        |              |
|-----------|------------------|--------------|
| LDO_Stby  | Error Monitoring | PreReg       |
| OFF       | OFF              | OFF          |
| LDO_μC    | LDO_Com          | Core_Sup adj |
| OFF       | OFF              | OFF          |
| Volt_Ref  | Tr 1 & 2         | Wakeup-T     |
| OFF       | OFF              | OFF          |
| WatchDogs | RESET            | SSC, SS1&2   |
| OFF       | LOW              | LOW          |

**Figure 26 POWERDOWN-state**

**Table 11-1 POWERDOWN-state Settings**

| Part/Function    | Value | Description                                                               |
|------------------|-------|---------------------------------------------------------------------------|
| LDO_Stby         | OFF   | •<br>The LDO_Stby is off                                                  |
| PreReg           | OFF   | •<br>The pre regulators are off                                           |
| LDO_µC           | OFF   | •<br>The LDO_µC is off                                                    |
| LDO_Com          | OFF   | •<br>The LDO_Com is off                                                   |
| Core_Sup adj.    | OFF   | •<br>The function Core_Sup adj. is off                                    |
| Volt_Ref         | OFF   | •<br>The voltage reference is off                                         |
| Tr.1 & 2         | OFF   | •<br>Both trackers 1 & 2 are off                                          |
| Wake-up-T.       | OFF   | •<br>The wake-up timer is off                                             |
| Watchdogs        | OFF   | •<br>The watchdogs are off                                                |
| Error monitoring | OFF   | •<br>The Error monitoring is off                                          |
| RESET            | LOW   | •<br>The reset output is low                                              |
| SSC, SS1&2       | LOW   | •<br>Both safe state signals are LOW and the application is in safe state |

# **11.2.2 INIT-state**

During INIT-state the device expects valid communication with the µC within the INIT timer. Otherwise an initialization timeout will occur. The INIT timer starts with the rising edge of ROT.

The INIT timer is stopped as soon as three boundary conditions are fulfilled:

- Valid SPI communication received from µC
- Watchdog(s) serviced once according to default configuration or according to reconfiguration
- ERR monitoring serviced properly (minimum 3 periods provided) or configured to be OFF

| INIT         |                  |              |
|--------------|------------------|--------------|
| LDO_Stby     | Error Monitoring | PreReg       |
| SELECTABLE** | ON*              | ON           |
| LDO_μC       | LDO_Com          | Core_Sup adj |
| ON           | ON*              | ADJUSTED     |
| Volt_Ref     | Tr 1 & 2         | Wakeup-T     |
| ON*          | ON*              | OFF          |
| WatchDogs    | RESET            | SSC, SS1&2   |
| ON*          | ACTIVE           | LOW          |

**Figure 27 INIT-state**

**Table 11-2 INIT-state Settings**

| Part/Function    | Value    | Description                                                                                                                |
|------------------|----------|----------------------------------------------------------------------------------------------------------------------------|
| LDO_Stby         | SELECTAB | •<br>The LDO_Stby is switched on when entering from POWERDOWN-state                                                        |
|                  | LE**     | •<br>It may be switched on or off by SPI command. This configuration is kept<br>through all states, except POWERDOWN-state |
| PreReg           | ON       | •<br>The step down pre regulator is on                                                                                     |
|                  |          | •<br>Step up pre regulator is active depending on the input voltage and this<br>option is selected by pin STU.             |
| LDO_µC           | ON       | •<br>The LDO_µC is on                                                                                                      |
| LDO_Com          | ON*      | •<br>The LDO_Com is switched on per default                                                                                |
|                  |          | •<br>The LDO_Com may be switched off and on by SPI                                                                         |
| Core_Sup adj.    | ADJUSTED | •<br>The Core_Sup adj. is switched ON or OFF depending on pin SEC<br>(SEC pin considered only during power-sequencing)     |
| Volt_Ref         | ON*      | •<br>The Volt_Ref is switched on per default                                                                               |
|                  |          | •<br>The Volt_Ref may be switched off and on by SPI                                                                        |
| Tr.1 & 2         | ON*      | •<br>Both trackers 1 & 2 are switched on per default                                                                       |
|                  |          | •<br>Both trackers 1 & 2 may be switched off and on by SPI independently                                                   |
| Wake-up-T.       | OFF      | •<br>The wake-up timer is off                                                                                              |
| Watchdogs        | ON*      | •<br>The window watchdog is switched on per default in SPI triggered mode                                                  |
|                  |          | •<br>The functional watchdog is switched off per default                                                                   |
|                  |          | •<br>The watchdogs may be configured and switched ON or OFF by SPI                                                         |
| Error monitoring | ON       | •<br>The Error monitoring is switched on per default                                                                       |
|                  |          | •<br>The Error monitoring may be configured and switched ON or OFF by SPI                                                  |

**Table 11-2 INIT-state Settings** (cont'd)

| Part/Function | Value  | Description                                                                                                                                                                                        |  |
|---------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| RESET         | ACTIVE | •<br>The reset output goes HIGH as soon as all µC related output voltages<br>VQST, VQUC and VVCI are above their under voltage reset<br>threshold,VRT,XXX,low delayed by the reset delay time tRD. |  |
| SSC, SS1&2    | LOW    | •<br>Both safe state signals are LOW and the application is in safe state                                                                                                                          |  |

## **11.2.3 NORMAL -state**

In NORMAL-state the device is supplying the µC and the applications. Safety and monitoring functions (like resetblock and safe state control) are active. The µC may configure several post regulators of the device and the wakeup-timer via SPI command for this state.

| NORMAL     |                  |              |
|------------|------------------|--------------|
| LDO_Stby   | Error Monitoring | PreReg       |
| SELECTABLE | SELECTABLE       | ON           |
| LDO_μC     | LDO_Com          | Core_Sup adj |
| ON         | SELECTABLE       | ADJUSTED     |
| Volt_Ref   | Tr 1 & 2         | Wakeup-T     |
| SELECTABLE | SELECTABLE       | OFF          |
| WatchDogs  | RESET            | SSC, SS1&2   |
| SELECTABLE | HIGH             | HIGH         |

**Figure 28 NORMAL-state**

**Table 11-3 NORMAL-state Settings**

| Part/Function    | Value          | Description                                                                                                       |  |  |
|------------------|----------------|-------------------------------------------------------------------------------------------------------------------|--|--|
| LDO_Stby         | SELECTAB<br>LE | •<br>The LDO_Stby may be switched on or off by SPI command.                                                       |  |  |
| PreReg           | ON             | •<br>The step down pre regulator is on                                                                            |  |  |
|                  |                | •<br>Step up pre regulator is active depending on the input voltage and this<br>option is selected by pin STU.    |  |  |
| LDO_µC           | ON             | •<br>The LDO_µC is on                                                                                             |  |  |
| LDO_Com          | SELECTAB<br>LE | •<br>The LDO_Com may be switched on of off by SPI command                                                         |  |  |
| Core_Sup adj.    | ADJUSTED       | The Core_Sup adj. is switched ON or OFF depending on pin SEC<br>(SEC pin considered only during power-sequencing) |  |  |
| Volt_Ref         | SELECTAB<br>LE | •<br>The Volt_Ref may be switched on of off by SPI command                                                        |  |  |
| Tr.1 & 2         | SELECTAB<br>LE | •<br>Both trackers 1 & 2 may be switched off and on by SPI independently                                          |  |  |
| Wake-up-T.       | OFF            | The wake-up timer is switched off                                                                                 |  |  |
| Watchdogs        | SELECTAB<br>LE | •<br>The watchdogs may be configured and switched ON or OFF by SPI                                                |  |  |
| Error monitoring | SELECTAB<br>LE | The Error monitoring may be configured and switched ON or OFF by SPI                                              |  |  |
| RESET            | HIGH           | •<br>The reset output is HIGH                                                                                     |  |  |
| SSC, SS1&2       | HIGH           | •<br>Both safe state signals are HIGH                                                                             |  |  |

### **11.2.4 STANDBY-state**

The STANDBY-state is a low power state which the µC may enter to reduce the current consumption to a minimum when the application is not used for a long time. The application is in a safe state.

| STANDBY       |                  |                     |  |
|---------------|------------------|---------------------|--|
| LDO_Stby      | Error Monitoring | PreReg              |  |
| SELECTED      | OFF              | OFF                 |  |
| LDO_μC<br>OFF | LDO_Com<br>OFF   | Core_Sup adj<br>OFF |  |
| Volt_Ref      | Tr 1 & 2         | Wakeup-T            |  |
| OFF<br>OFF    |                  | SELECTED            |  |
| WatchDogs     | RESET            | SSC, SS1&2          |  |
| INACTIVE      | LOW              | LOW                 |  |

**Figure 29 STANDBY-state**

#### **Table 11-4 STANDBY-state Settings**

| Part/Function    | Value    | Description                                                   |  |
|------------------|----------|---------------------------------------------------------------|--|
| LDO_Stby         | SELECTED | •<br>The LDO_Stby is ON or OFF depending on its configuration |  |
| PreReg           | OFF      | The pre regulator are off                                     |  |
| LDO_µC           | OFF      | •<br>The LDO_µC is off                                        |  |
| LDO_Com          | OFF      | •<br>The LDO_Com is off                                       |  |
| Core_Sup adj.    | OFF      | •<br>The function Core_Sup adj. is off                        |  |
| Volt_Ref         | OFF      | The voltage reference is off                                  |  |
| Tr.1 & 2         | OFF      | Both trackers 1 & 2 are off                                   |  |
| Wake-up-T.       | SELECTED | The wake-up timer is ON or OFF depending on its configuration |  |
| Watchdogs        | OFF      | The watchdogs are off                                         |  |
| Error monitoring | OFF      | The Error monitoring is off                                   |  |
| RESET            | LOW      | The reset output is low                                       |  |
| SSC, SS1&2       | LOW      | •<br>Safe state signals 1 and 2 are low                       |  |
|                  |          | •<br>The application is in a safe state                       |  |

## **11.2.5 SLEEP-state**

The SLEEP-state is a low power state which the µC may enter to reduce the current consumption when the application is not used (e.g. micro controller is in STOP mode). The µC may configure the status of regulators and the safety functions via SPI command in the previous state. The application is in a safe state

|           | SLEEP            |              |
|-----------|------------------|--------------|
| LDO_Stby  | Error Monitoring | PreReg       |
| SELECTED  | SELECTED         | ON           |
| LDO_μC    | LDO_Com          | Core_Sup adj |
| ON        | SELECTED         | ADJUSTED     |
| Volt_Ref  | Tr 1 & 2         | Wakeup-T     |
| SELECTED  | SELECTED         | SELECTED     |
| WatchDogs | RESET            | SSC, SS1&2   |
| SELECTED  | HIGH             | LOW          |

**Figure 30 SLEEP-state**

**Table 11-5 SLEEP-state Settings**

| Part/Function    | Value    | Description                                                                                                                                                                                                           |
|------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LDO_Stby         | SELECTED | •<br>The LDO_Stby is switched ON or OFF according to previous configuration.                                                                                                                                          |
| PreReg           | ON       | •<br>The step down pre regulator is on                                                                                                                                                                                |
|                  |          | •<br>Step up pre regulator is active depending on the input voltage and this<br>option is selected by pin STU                                                                                                         |
| LDO_µC           | ON       | •<br>The LDO_µC is switched on                                                                                                                                                                                        |
|                  |          | •<br>In SLEEP-state the device is monitoring the output current of LDO_µC: If<br>the LDO_µC current exceeds a certain threshold ILDO_µC,att, an interrupt will<br>be generated and the device will move to WAKE state |
| LDO_Com          | SELECTED | •<br>The LDO_Com is switched ON or OFF depending on the configuration by<br>the state transition request to move into SLEEP and cannot be changed in<br>SLEEP state.                                                  |
| Core_Sup adj.    | ADJUSTED | •<br>The Core_Sup adj. is switched ON or OFF depending on pin SEC<br>(SEC pin considered only during power-sequencing)                                                                                                |
| Volt_Ref         | SELECTED | •<br>The Volt_Ref is switched ON or OFF depending on the configuration by the<br>state transition request to move into SLEEP and cannot be changed in<br>SLEEP state.                                                 |
| Tr.1 & 2         | SELECTED | •<br>The trackers are switched ON or OFF depending on the configuration by<br>the state transition request to move into SLEEP and cannot be changed in<br>SLEEP-state                                                 |
| Wake-up-T.       | SELECTED | •<br>The wake-up timer is ON or OFF depending on its configuration                                                                                                                                                    |
| Watchdogs        | SELECTED | •<br>The watchdogs are ON or OFF depending on their configuration for SLEEP                                                                                                                                           |
| Error monitoring | SELECTED | •<br>The Error monitoring is ON or OFF depending on its configuration for<br>SLEEP                                                                                                                                    |
| RESET            | HIGH     | •<br>The reset output is HIGH                                                                                                                                                                                         |
| SSC, SS1&2       | LOW      | •<br>Both safe state signals are LOW and the application is in safe state                                                                                                                                             |
|                  |          |                                                                                                                                                                                                                       |

## **11.2.6 WAKE-state**

The WAKE-state is an intermediate state between NORMAL and the low power states SLEEP and STANDBY. This state provides the same functionality as the NORMAL state, but shall ensure the application being in safe state by keeping low the safe state outputs. It should be used to prepare the system for a correct and safe reentry to the NORMAL state by servicing the watchdogs and the error monitoring (minimum 3 periods) according to the selected configuration. Furthermore it provides the possibility to move the device into the low power states SLEEP and STANDBY.

The TLF35584 moves from SLEEP or from the transition to SLEEP into WAKE state, if the output current from LDO\_µC exceeds a certain threshold *I*LDO\_µC,att, an valid ENA or WAK signal is recognized or the SPI command GoToWake is sent. Another transition into WAKE state is initiated by the usage of the ABIST in NORMAL state.

By entering the state an interrupt is generated and the supervision functions (watchdogs and ERR monitoring) will become active according to their previous configuration in NORMAL state. Upon entering the WAKE-state the configuration of the LDOs resumes to the one of the previous NORMAL state. The application is in a safe state

| WAKE       |                  |              |  |  |
|------------|------------------|--------------|--|--|
| LDO_Stby   | Error Monitoring | PreReg       |  |  |
| SELECTABLE | SELECTABLE       | ON           |  |  |
| LDO_μC     | LDO_Com          | Core_Sup adj |  |  |
| ON         | SELECTABLE       | ADJUSTED     |  |  |
| Volt_Ref   | Tr 1 & 2         | Wakeup-T     |  |  |
| SELECTABLE | SELECTABLE       | OFF          |  |  |
| WatchDogs  | RESET            | SSC, SS1&2   |  |  |
| SELECTABLE | ACTIVE           | LOW          |  |  |

**Figure 31 WAKE-state**

**Table 11-6 WAKE-state Settings**

| Part/Function | Value          | Description                                                                                                                                              |
|---------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| LDO_Stby      | SELECTAB<br>LE | •<br>The LDO_Stby may be switched ON or OFF by SPI command.                                                                                              |
| PreReg        | ON             | •<br>The step down pre regulator is on                                                                                                                   |
|               |                | •<br>Step up pre regulator is active depending on the input voltage and this<br>option is selected by pin STU.                                           |
| LDO_µC        | ON             | •<br>The LDO_µC is on                                                                                                                                    |
| LDO_Com       | SELECTAB<br>LE | •<br>The LDO_Com will be switched ON or OFF depending on its configuration<br>in the NORMAL-state prior to SLEEP-state when entering WAKE-state          |
|               |                | •<br>It may be switched on of off by SPI command                                                                                                         |
| Core_Sup adj. | ADJUSTED       | •<br>The Core_Sup adj. is switched ON or OFF depending on pin SEC<br>(SEC pin considered only during power-sequencing)                                   |
| Volt_Ref      | SELECTAB<br>LE | •<br>The voltage reference will be switched ON or OFF depending on its<br>configuration in NORMAL-state prior to SLEEP-state when entering<br>WAKE-state |
|               |                | •<br>It may be switched on of off by SPI command                                                                                                         |

**Table 11-6 WAKE-state Settings** (cont'd)

| Part/Function    | Value          | Description                                                                                                                                              |
|------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tr.1 & 2         | SELECTAB<br>LE | •<br>Both trackers 1 & 2 will be switched ON or OFF depending on their<br>configuration in NORMAL-state prior to SLEEP-state when entering<br>WAKE-state |
|                  |                | •<br>It may be switched on of off by SPI command                                                                                                         |
| Wake-up-T.       | OFF            | •<br>The wake-up timer is switched off                                                                                                                   |
| Watchdogs        | SELECTAB<br>LE | •<br>The watchdogs will be switched ON or OFF depending on their<br>configuration in NORMAL-State prior to SLEEP-state when entering<br>WAKE-State       |
|                  |                | •<br>The watchdogs may be configured and switched ON or OFF by SPI                                                                                       |
| Error monitoring | SELECTAB<br>LE | •<br>The Error monitoring will be switched ON or OFF depending on the<br>configuration in NORMAL-state prior to SLEEP-state when entering<br>WAKE-state  |
|                  |                | •<br>The Error monitoring may be configured and switched ON or OFF by SPI                                                                                |
| RESET            | HIGH           | •<br>The reset output is HIGH                                                                                                                            |
| SSC, SS1&2       | LOW            | •<br>Both safe state signals are LOW and the application is in safe state                                                                                |

### **11.2.7 FAILSAFE-state**

FAILSAFE-state occurs after the detection of a severe failure. In FAILSAFE-state all regulators are switched off. The application is in a safe state.

![](_page_8_Picture_3.jpeg)

**Figure 32 Fail safe-state**

#### **Table 11-7 FAILSAFE-state Settings**

| Part/Function    | Value | Description                                                               |
|------------------|-------|---------------------------------------------------------------------------|
| LDO_Stby         | OFF   | •<br>The LDO_Stby is off                                                  |
| PreReg           | OFF   | •<br>The pre regulators are off                                           |
| LDO_µC           | OFF   | •<br>The LDO_µC is off                                                    |
| LDO_Com          | OFF   | •<br>The LDO_Com is off                                                   |
| Core_Sup adj.    | OFF   | •<br>The function Core_Sup adj. is off                                    |
| Volt_Ref         | OFF   | •<br>The voltage reference is off                                         |
| Tr.1 & 2         | OFF   | •<br>Both trackers 1 & 2 are off                                          |
| Wake-up-T.       | OFF   | •<br>The wake-up timer is off                                             |
| Watchdogs        | OFF   | •<br>The watchdogs are off                                                |
| Error monitoring | OFF   | •<br>The Error monitoring is off                                          |
| RESET            | LOW   | •<br>The reset output is low                                              |
| SSC, SS1&2       | LOW   | •<br>Both safe state signals are LOW and the application is in safe state |

## **11.3 Transition Between States**

State transitions requested via SPI command are initiated with a valid positive going edge of the chip select (SCS).

## **11.3.1 POWERDOWN -> INIT-state**

The device moves from POWERDOWN to INIT-state when the Power-on-Reset (POR) is released. The POR is only released when all of the following conditions are met:

- *V*VS above *V*PD,hi when increasing
- no under or over voltage on internal supplies

# **11.3.2 INIT -> NORMAL-state**

## **Prerequisites:**

- Watchdog(s) need to be serviced once according to default configuration or according to reconfiguration within the INIT timer
- ERR monitor needs to be serviced with a valid signal (minimum 3 periods) or disabled within the INIT timer.
- If functional watchdog is activated, a valid FWD triggering needs to be provided.
- A delay of 60µs after the provided services has to be considered to ensure proper release of internal validation signals.

## **Triggering Events:**

• State transition is only initiated by the SPI command "Go to NORMAL".

## **Exceptions:**

• none

#### **Timing Description:**

![](_page_1_Figure_2.jpeg)

**Figure 33 Transition from INIT to NORMAL state**

- A valid SPI command "Go to NORMAL" (valid with chip select high at pin SCS) will move the device from INIT state to NORMAL state.
- Reset pin ROT stays HIGH as the post regulators are already active in INIT state.
- With the positive edge of chip select high (at pin SCS) the safe state signals SS1 and SS2 are pulled to HIGH at same time. (Internal reaction time for the safe state outputs according to **Table 18** has to be considered)

# **11.3.3 Movements between NORMAL and SLEEP state**

# **11.3.3.1 NORMAL -> SLEEP-state**

## **Prerequisites:**

- Selection of LDO\_µC current monitor or absolute transition timer.
- Transition delay timer *t*tr,del needs to be configured or default is used.
- Optionally LDO\_µC current threshold needs to be defined or default is used.

### **Triggering Events:**

• State transition is only initiated by the SPI command "Go to SLEEP".

#### **Exceptions:**

- If a valid ENA (edge) or WAK (level) signal is detected in the transition state to SLEEP state, the device will move to the WAKE state and send an interrupt (at pin INT)
- If the LDO\_µC current monitor is activated and the current consumption of the microcontroller is not below the selected LDO\_µC current threshold before the transition delay timer *t*tr,del has expired, the device will move to the WAKE state and send an interrupt (at pin INT)

#### **Timing Diagram**

![](_page_3_Figure_2.jpeg)

Figure 34 Transition from NORMAL to SLEEP state

- Before the SPI command "Go to SLEEP" is applied, the watchdog(s) if in use should be serviced, so that the positive edge of SCS signal is well in between the "closed window" of the window watchdog. This is recommended to avoid interference between a missing watchdog trigger and the transition command "Go to SLEEP"
- The positive edge of chip select (pin SCS) after the SPI command "Go to SLEEP" initiates the transition. With chip select high the safe state signal SS1 is pulled to zero and the device leaves NORMAL state and enters the transition state (to SLEEP state). (Internal reaction time for the safe state outputs according to Table 18 has to be considered)
- With chip select (pin SCS) high the error monitoring (pin ERR) is stopped the toggling may end with the
  positive edge at pin SCS. If the error monitoring should be selected to be active in SLEEP state continuos
  toggling is mandatory.
- The monitoring of window watchdog and functional watchdog is stopped with the positive edge at pin SCS. If
  one or both watchdogs should be selected to be active in SLEEP state continuos watchdog service is
  mandatory.
- Reset pin ROT stays HIGH as the post regulators are not switched off.
- In case the absolute transition timer is selected, the device moves from transition state to SLEEP state after
  the transition delay time t<sub>tr,del</sub>. The transition time t<sub>tr,del</sub> can be determined by SPI command between 100 μs to
  1.6 ms, the default setting is 900 μs. After this transition time it should be ensured that the μC current
  consumption has fallen below the LDO\_μC monitoring threshold I<sub>LDO μC,att</sub> to keep the device in SLEEP state.

- If the LDO\_µC current monitor is enabled the µC current out of pin QUC must fall below the LDO\_µC monitoring threshold ILDO\_µC,att within the configured maximum transition time *t*tr,del in **DEVCFG0**.**TRDEL**. The time for the transition is depending, how long it takes that the µC current falls below the LDO\_µC monitoring threshold ILDO\_µC,att , if it is below the transition is done.
- After delay time *Δt*SS2 the safe state signal SS2 goes to zero. The adjusted delay time *Δt*SS2 is independent from the transition delay time *t*tr,del.

### 11.3.3.2 SLEEP -> WAKE-state

### Prerequisites:

none

### **Triggering Events:**

- SPI command "Go to WAKE".
- Valid Wake-Signal (ENA or WAK).
- Current of LDO\_µC exceeding the configured threshold.
- · Wake-up timer expired, if enabled

#### **Exceptions:**

none

### **Timing Diagram**

![](_page_5_Figure_12.jpeg)

Figure 35 Transition from SLEEP to WAKE state

- The state transition is completed without a transition time and is indicated by an interrupt at pin INT. The triggering event for the transition from SLEEP can be read from the status register **WKSF**.
- All three monitoring functions (window watchdog, functional watchdog and error monitoring) will recover to the condition active or inactive (switched off) as they were in the NORMAL state previous to the SLEEP state.
- The configuration of the LDOs will recover to the condition active or inactive (switched off) as they were in the NORMAL state previous to the SLEEP state.
- In case the window watchdog was active in the previous NORMAL state, with the negative edge of interrupt signal (at pin INT) the window watchdog will open the first Open Window, the time of this first Open Window depends on the configured cycle time and is 600 ms (**WDCYC** = 1) or 60 ms (**WDCYC** = 0) (if the window watchdog has not been active in SLEEP state) and requires service. If the window watchdog has been active in SLEEP state continuos service is mandatory.
- In case the functional watchdog was active in the previous NORMAL state, with the negative edge of interrupt signal (at pin INT) the functional watchdog will start the heartbeat timer and require service. If the functional watchdog has been active in SLEEP state continuos service is mandatory.
- In case the ERR pin monitoring was active in the previous NORMAL state, with the negative edge of interrupt signal (at pin INT) the error monitoring will become active again. Latest 10 ms after the activation a toggling signal (with at least three periods past) at pin ERR is required. If the error monitoring has been active in SLEEP state continuos toggling is mandatory.
- Reset pin ROT stays HIGH as the post regulators are active in SLEEP state and in WAKE state.
- The safe signals SS1 and SS2 will stay LOW in SLEEP and in WAKE state.
- If all active monitoring functions (window watchdog, functional watchdog and error monitoring) are serviced properly in WAKE state, you may stay in WAKE state as long as you want.
- If all three monitoring functions (window watchdog, functional watchdog and error monitoring) are inactive (switched off) in WAKE state, you may stay in WAKE state as long as you want.

# **11.3.3.3 WAKE -> SLEEP state**

## **Prerequisites:**

- Selection of LDO\_µC current monitor or absolute transition timer.
- Transition delay timer *t*tr,del needs to be configured or default is used.
- Optionally LDO\_µC current threshold needs to be defined or default is used.

## **Triggering Events:**

• State transition is only initiated by the SPI command "Go to SLEEP".

## **Exceptions:**

- If a valid ENA (edge) or WAK (level) signal is detected in the transition state to SLEEP state, the device will move back to the WAKE state and send an interrupt (at pin INT)
- If the LDO\_µC current monitor is activated and the current consumption of the microcontroller is not below the selected LDO\_µC current threshold before the transition delay timer *t*tr,del has expired, the device will move back to the WAKE state and send an interrupt (at pin INT)

#### **Timing Diagram**

![](_page_8_Figure_2.jpeg)

Figure 36 Transition from WAKE to SLEEP state

- Before the SPI command "Go to SLEEP" is applied, the watchdog(s) if in use should be serviced, so that the positive edge of SCS signal is well in between the "closed window" of the window watchdog. This is recommended to avoid interference between a missing watchdog trigger and the transition command "Go to SLEEP"
- The positive edge of chip select (pin SCS) after the SPI command "Go to SLEEP" initiates the transition. With chip select high the device leaves WAKE state and enters the transition state (to SLEEP state).
- With chip select (pin SCS) high the error monitoring (pin ERR) is stopped the toggling may end with the
  positive edge at pin SCS. If the error monitoring should be selected to be active in SLEEP state continuos
  toggling is mandatory.
- The monitoring of window watchdog and functional watchdog is stopped with the positive edge at pin SCS. If
  one or both watchdogs should be selected to be active in SLEEP state continuos watchdog service is
  mandatory.
- · Reset pin ROT stays HIGH as the post regulators are not switched off.
- If the LDO\_μC current monitor is enabled the μC current out of pin QUC must fall below the LDO\_μC monitoring threshold I<sub>LDO\_μC,att</sub> within the configured maximum transition delay time t<sub>tr,del</sub>. The time for the transition is depending, how long it takes that the μC current falls below the LDO\_μC monitoring threshold I<sub>LDO μC,att</sub>, if it is below the transition is done.
- · Safe state signals SS1 and SS2 stay LOW all the time.

# **11.3.4 Movements between NORMAL and STANDBY state**

# **11.3.4.1 NORMAL -> STANDBY-state**

## **Prerequisites:**

- Selection of LDO\_µC current monitor or absolute transition timer.
- Transition timer needs to be configured or default is used.
- Optionally LDO\_µC current threshold needs to be defined or default is used.

### **Triggering Events:**

• State transition is only initiated by the SPI command "Go to STANDBY".

## **Exceptions:**

- If a valid ENA (edge) or WAK (level) signal is detected in the transition state to STANDBY state, the device will move to the INIT state and a reset (ROT) is generated.
- If the LDO\_µC current monitor is activated and the current consumption of the microcontroller is not below the selected LDO\_µC current threshold before the transition delay timer *t*tr,del has expired, the device will move to the INIT state and a reset (ROT) is generated.

#### **Timing Diagram:**

![](_page_0_Figure_2.jpeg)

Figure 37 Transition from NORMAL to STANDBY state

- Before the SPI command "Go to STANDBY" is applied, the watchdog(s) if in use should be serviced, so that the positive edge of SCS signal is well in between the "closed window" of the window watchdog. This is recommended to avoid interference between a missing watchdog trigger and the transition command "Go to STANDBY"
- The positive edge of chip select (pin SCS) after the SPI command "Go to STANDBY" initiates the transition. With chip select high the safe state signals SS1 and SS2 are pulled to zero without delay between SS1 and SS2. The device leaves NORMAL state and enters the transition state (to STANDBY state).
  (Internal reaction time for the safe state outputs according to Table 18 has to be considered)
- With chip select (pin SCS) high the error monitoring (pin ERR) is stopped the toggling may end with the positive edge at pin SCS.
- The monitoring of window watchdog and functional watchdog is stopped with the positive edge at pin SCS.
- With a successful transition from NORMAL to STANDBY state the reset (ROT) is pulled to LOW after the transition time after chip select (pin SCS) going high.
- All pre regulators and all post regulators (with the exception of the standby LDO it may be ON or OFF in STANDBY state) are switched off at the point when the transition is completed after the reset (ROT) is pulled low.

- In case the absolute transition timer is selected, the device moves from transition state to STANDBY state after the transition delay time *t*tr,del. The transition time *t*tr,del can be determined by SPI command between 100 µs to 1.6 ms, the default setting is 900 µs.
- In case the LDO\_µC current monitor is selected for the transition, the device moves from transition state to STANDBY state at the point the current consumption measured at the LDO\_µC drops below the selected threshold before the transition delay timer *t*tr,del has expired.

## **11.3.4.2 STANDBY -> INIT state**

## **Prerequisites:**

• none

## **Triggering Events:**

- Valid ENA (edge) or WAK (level) signal.
- Wake-up timer expired, if enabled

## **Exceptions:**

• none

#### **Timing Diagram**

![](_page_2_Figure_10.jpeg)

**Figure 38 Transition from STANDBY to INIT state**

- All pre regulators and all post regulators are switched on according to the power sequencing, except the LDO\_Stby is kept ON or OFF according to its configuration (simplified in figure above).
- The power on reset delay time is started as soon as the latest of the µC related regulators *V*QUC or *V*VCI (if enabled) crosses the related under voltage reset threshold *V*RT,xxx,low on the way up.
- After the power on reset delay time has expired the reset (ROT) is set to HIGH.
- The safe signals SS1 and SS2 will stay LOW in STANDBY state and in INIT state.

# **11.3.4.3 INIT -> NORMAL state**

For this state transition please refer to the **Chapter 11.3.2**.

# **11.3.5 NORMAL -> WAKE state**

For this state transition please refer to the description of ABIST in **Chapter 11.6.1**.

## **11.3.6 WAKE -> NORMAL-state**

## **Prerequisites:**

• The activated supervision functions (e.g. window watchdog, functional watchdog, ERR pin monitoring) need to be serviced at least once (minimum 3 periods for ERR monitoring) in the active WAKE state, if they are restarted/reinitialized in WAKE state (e.g. watchdog being inactive in previous SLEEP state)

## **Triggering Events:**

• State transition is only initiated by the SPI command "Go to NORMAL".

### **Exceptions:**

• none

#### **Timing Diagram**

![](_page_5_Figure_2.jpeg)

**Figure 39 Transition from WAKE to NORMAL state**

- The enable signal will be disregarded. A valid enable (edge) signal will not move the device from WAKE to NORMAL state.
- The state of wake signal will be disregarded. A valid wake (level) signal will not move the device from WAKE to NORMAL state.
- The window watchdog (if active in WAKE state) will require continuos service not synchronized to the transition from WAKE state to NORMAL state.
- The functional watchdog (if active in WAKE state) will require continuos service not synchronized to the transition from WAKE state to NORMAL state.
- The error monitoring (at pin ERR) (if active in WAKE state) will require a continuos toggling signal not synchronized to the transition from WAKE state to NORMAL state - but minimum 3 periods detected to enter accept the movement into NORMAL state.
- Reset pin ROT stays HIGH as the post regulators are active in WAKE state and in NORMAL state.
- With the positive edge of chip select high (at pin SCS) the safe state signals SS1 and SS2 are pulled to HIGH at same time. (Internal reaction time for the safe state outputs according to **Table 18** has to be considered)

# **11.3.7 WAKE -> STANDBY state**

## **Prerequisites:**

- Selection of LDO\_µC current monitor or absolute transition timer.
- Transition timer needs to be configured or default is used.
- Optionally LDO\_µC current threshold needs to be defined or default is used.

#### **Triggering Events:**

• State transition is only initiated by the SPI command "Go to STANDBY".

## **Exceptions:**

- If a valid ENA (edge) or WAK (level) signal is detected in the transition state to STANDBY state, the device will move to the INIT state and a reset (ROT) is generated.
- If the LDO\_µC current monitor is activated and the current consumption of the microcontroller is not below the selected current threshold before the transition timer has expired, the device will move to the INIT state and a reset (ROT) is generated.

#### **Timing Diagram:**

![](_page_7_Figure_2.jpeg)

Figure 40 Transition from WAKE to STANDBY state

- Before the SPI command "Go to STANDBY" is applied, the watchdog(s) if in use should be serviced, so that the positive edge of SCS signal is well in between the "closed window" of the window watchdog. This is recommended to avoid interference between a missing watchdog trigger and the transition command "Go to STANDBY"
- The positive edge of chip select (pin SCS) after the SPI command "Go to STANDBY" initiates the transition. In the WAKE state the safe state signals SS1 and SS2 are LOW and will be kept LOW for the transition to STANDBY. The device leaves WAKE state and enters the transition state (to STANDBY state).
- With chip select (pin SCS) high the error monitoring (pin ERR) is stopped the toggling may end with the positive edge at pin SCS.
- The monitoring of window watchdog and functional watchdog is stopped with the positive edge at pin SCS.
- With a successful transition from WAKE to STANDBY state the reset (ROT) is pulled to LOW after the transition time after chip select (pin SCS) going high.
- All pre regulators and all post regulators (with the exception of the standby LDO it may be ON or OFF in STANDBY state) are switched off at the point when the transition is completed after the reset (ROT) is pulled low.

- In case the absolute transition timer is selected, the device moves from transition state to STANDBY state after the transition time *t*tr,del. The transition time ttr,del can be determined by SPI command between 100 µs to 1.6 ms, the default setting is 900 µs.
- In case the LDO\_µC current monitor is selected for the transition, the device moves from transition state to STANDBY state at the point the current consumption measured at the LDO\_µC drops below the selected threshold before the transition delay timer *t*tr,del has expired.

## **11.3.8 FAILSAFE -> INIT state**

## **Prerequisites:**

• FAILSAFE timer has expired.

### **Triggering Events:**

- Self triggered transition after the prerequisite is fulfilled.
- Valid ENA (edge) or WAK (level) signal (only needed if exception true)

## **Exceptions:**

• In case the FAILSAFE is entered three times in a row with the same failure the self-triggered transition is blocked.

## **Timing Diagram**

![](_page_9_Figure_10.jpeg)

**Figure 41 Transition from FAILSAFE to INIT state**

- The device transition from FAILSAFE state to INIT state happens earliest after the minimum FAILSAFE time *t*FAILSAFE,min, which is 20 ms for all failures except a thermal shutdown. In case of a thermal shutdown the minimum FAILSAFE time *t*FAILSAFE,min is 1s. A command to transition before the minimum FAILSAFE time *t*FAILSAFE,min has expired, will not be executed.
- After entering INIT state the voltage regulators will ramp up according to the power sequencing.

- The power on reset delay time is started as soon as the latest of the µC related regulators *V*QUC, *V*VCI or *V*QST (according to the previous configuration) crosses the related under voltage reset threshold *V*RT,xxx,low on the way up.
- After the power on reset delay time has expired the reset (ROT) is set to HIGH.
- The device needs to be configured and initiated. All settings done in the configuration registers before the device went into FAILSAFE state are lost, except the configuration of the LDO\_Stby (**RSYSPCFG0**) and the reset delay time (**DEVCFG1**).
- The safe state signal SS1 and SS2 are LOW in FAILSAFE state and will be LOW in INIT state

# **11.4 Reaction on detected faults**

Errors are classified according to their severity into 4 different error classes:

- Stay in Current State Failures affecting peripherals without direct risk for the microcontroller, that are indicated by an interrupt to allow analysis by the microcontroller without changing the state.
- Move to INIT Medium severity errors that brings the device back to INIT state and generate a reset for the microcontroller.
- Move to FAILSAFE Critical error with high risk of damaging the microcontroller.
- Move to POWERDOWN Most critical error with high risk of damaging ourself plus the microcontroller

The error classes are overruled according to their severity, e.g. movement to POWERDOWN takes precedence over movement to FAILSAFE which takes precedence over movement to INIT.

The move to INIT, FAILSAFE and POWERDOWN errors are named "error triggered state transitions" in this document.

# **11.4.1 Stay in current State**

![](_page_1_Picture_10.jpeg)

**Figure 42 Stay in current State**

The following failures will not trigger a movement of the device to another state by themselves, but will indicate the failure by an interrupt event:

- Detection of under voltage or a short to ground or overload detection at voltage reference
- Detection of over voltage, under voltage or a short to ground at trackers 1 or 2
- Detection of over voltage, under voltage, a short to ground or thermal shutdown at LDO\_Com
- Detection of under voltage at pre regulator.
- Detection of overload at standby regulator
- Increase of window/functional watchdog status counter, but actual value still stays below the threshold
- Error monitoring recovery delay time is active and ERR signal stops toggling.
- Thermal shutdown pre warning (Step down pre regulator or/and LDO\_µC or/and LDO\_Com)
- Bandgap monitoring: If the deviation between both bandgaps is larger than 4%

The interrupt may not be visible on the INT pin in STANDBY and FAILSAFE state due to microcontroller supplies being switched off. The event is stored in the status flags (**IF**, **SYSSF**, **MONSF0**, **MONSF1**, **MONSF2**, **OTWRNSF**, **OTFAIL**).

## **11.4.2 Transition into INIT State**

![](_page_2_Picture_2.jpeg)

**Figure 43 Move to INIT State**

The following failures will bring the device from any state to INIT-state:

- Detection of under voltage at LDO\_µC, Core\_Sup adj. or LDO\_Stby
- Detection of window/functional watchdog status counter overflow
- Stop of error signal detected (immediate reaction mode) or stop or error signal detected for more than recovery delay time (recovery mode)
- One or two consecutive expires of the INIT timer (configuration in INIT state failed)

## **11.4.2.1 INIT -> INIT state due to detected fault**

## **11.4.2.1.1 INIT -> INIT-state due to INIT timer expired for the first time**

![](_page_3_Figure_3.jpeg)

**Figure 44 Transition from INIT to INIT state - first movement**

### Description:

• The device transition from INIT to INIT state (or stays in INIT state) for the first time is issuing a "soft reset". Pin ROT is pulled to LOW for the reset delay time *t*RD in case all µC related voltages are in valid range. The power sequence is started after entering the INIT state: the disabled outputs are re-activated, the other ones are kept enabled, except the LDO\_Stby will keep its configuration being ON or OFF.

# **11.4.2.1.2 INIT -> INIT-state due to INIT timer expired for the second time**

![](_page_4_Figure_2.jpeg)

**Figure 45 Transition from INIT to INIT state - second movement**

#### Description:

- The device transition from INIT to INIT state (or stays in INIT state) for the second time is issuing a "hard reset" - pin ROT is pulled to LOW and all outputs are disabled for the time *t* and restarted according to the power sequencing (Please refer to **Chapter 8.3**), except the LDO\_Stby will restore its configuration being ON or OFF.
- The ROT pin will be released according to the power sequencing using the reset delay time *t*rd.

*Note: Please refer also to the transition INIT to FAILSAFE*

## **11.4.2.2 NORMAL -> INIT state due to detected fault**

### **Timing Diagram**

![](_page_5_Figure_3.jpeg)

**Figure 46 Transition from NORMAL to INIT state**

### Description:

- The device transitions from NORMAL into INIT state issuing a "soft reset" pin ROT is pulled to LOW and all the outputs are enabled, except the LDO\_Stby will keep its configuration being ON or OFF. Outputs that where disabled in NORMAL state will get switched on again.
- This might be issued by an undervoltage of the µC related voltages *V*QUC, *V*QST or *V*VCI as shown in the figure. The under voltage is shorter than the short to ground detection time *t*StG. The reset delay time *t*RD is started as soon as all µC related voltages *V*QUC, *V*QST or *V*VCI are back in the valid range. The ROT pin is released accordingly. An under voltage longer than the short to ground detection time *t*StG would first lead to a transition from NORMAL to INIT state and then, after the short to ground detection time *t*StG has expired, to a transition from INIT to FAILSAFE state.
- The "soft reset" can also be initiated by a window watchdog error counter overflow (> ΣWWD), a functional watchdog error counter overflow (> ΣFWO), an error indication (immediate or recovery delay time mode), if these monitoring functions are in use. In this case the reset delay time *t*RD will be started falling edge of the ROT pin. Please consider the state transition time to INIT state in **Table 11-8**.
- SS1 will be pulled to LOW immediately with pin ROT, SS2 will be pulled to LOW after the selected *Δt*SS2.
- Please mind that in case of an UV event on QUC, a delayed SS2 signal will follow *V*QUC as it is supplied from QUC.

*Note: In case the device is sent back to NORMAL state before the configured ΔtSS2 has expired the SS2 will be kept HIGH without being set to LOW.*

# **11.4.2.3 STANDBY -> INIT state due to detected fault**

### **Timing Diagram**

![](_page_6_Figure_3.jpeg)

**Figure 47 Transition from STANDBY to INIT state**

#### Description:

- The device transitions from STANDBY into INIT because of an under voltage of the µC related voltage *V*QST as shown in the figure. The under voltage is shorter than the short to ground detection time *t*StG. An under voltage longer than the short to ground detection time *t*StG would first lead to a transition from STANDBY to INIT state and then, after the short to ground detection time *t*StG has expired, to a transition from INIT to FAILSAFE state.
- The power sequence is started after entering the INIT state: the disabled outputs are re-activated, except the LDO\_Stby will keep its configuration being ON or OFF.
- The power on reset delay time is started according to the power sequencing and releases the ROT accordingly.
- The safe state signals SS1 and SS2 are LOW in STANDBY state and will be LOW in INIT state Exception:
- Exception: In case of an over or undervoltage of the internal supply voltages a "hard reset" is always initiated. Please refer to **Chapter 8.3**.

## **11.4.2.4 SLEEP -> INIT state due to detected fault**

### **Timing Diagram**

![](_page_7_Figure_3.jpeg)

**Figure 48 Transition from SLEEP to INIT state**

### Description:

- The device transitions from SLEEP into INIT state issuing a "soft reset" pin ROT is pulled to LOW for a certain time *t*RD and all the outputs are kept enabled. Outputs that where disabled in SLEEP state will get switched on again, except the LDO\_Stby will keep its configuration being ON or OFF.
- This might be issued by an undervoltage of the µC related voltages *V*QUC, *V*QST or *V*VCI as shown in the figure. The under voltage is shorter than the short to ground detection time *t*StG. The reset delay time *t*RD is started as soon as all µC related voltages *V*QUC, *V*QST or *V*VCI are back in the valid range. The ROT pin is released accordingly. An under voltage longer than the short to ground detection time *t*StG would first lead to a transition from SLEEP to INIT state and then, after the short to ground detection time *t*StG has expired, to a transition from INIT to FAILSAFE state
- The "soft reset" can also be initiated by a window watchdog error counter overflow (> ΣWWO), a functional watchdog error counter overflow (> ΣFWO), an error indication (immediate or recovery delay time mode), if these monitoring functions are in use. In this case the reset delay time *t*RD will be started falling edge of the ROT pin. Please consider the state transition time to INIT state in **Table 11-8**.
- The safe state signals SS1 and SS2 are LOW in SLEEP state and will be LOW in INIT state Exception:
- Exception: In case of an over or undervoltage of the internal supply voltages a "hard reset" is always initiated. Please refer to **Chapter 8.3**.

## **11.4.2.5 WAKE -> INIT state due to detected fault**

#### **Timing Diagram**

![](_page_8_Figure_3.jpeg)

**Figure 49 Transition from WAKE to INIT state**

#### Description:

- The device transitions from WAKE into INIT state issuing a "soft reset" pin ROT is pulled to LOW for a certain time *t*RD and all the outputs are kept enabled. Outputs that where disabled in WAKE state will get switched on again, except the LDO\_Stby will keep its configuration being ON or OFF.
- This might be issued by an undervoltage of the µC related voltages *V*QUC, *V*QST or *V*VCI as shown in the figure. The under voltage is shorter than the short to ground detection time *t*StG. The reset delay time *t*RD is started as soon as all µC related voltages *V*QUC, *V*QST or *V*VCI are back in the valid range. The ROT pin is released accordingly. An under voltage longer than the short to ground detection time *t*StG would first lead to a transition from WAKE to INIT state and then, after the short to ground detection time *t*StG has expired, to a transition from INIT to FAILSAFE state.
- The "soft reset" can also be initiated by a window watchdog error counter overflow (> ΣWWO), a functional watchdog error counter overflow (> ΣFWO), an error indication (immediate or recovery delay time mode), if these monitoring functions are in use. In this case the reset delay time *t*RD will be started falling edge of the ROT pin. Please consider the state transition time to INIT state in **Table 11-8**.
- The safe state signals SS1 and SS2 are LOW in WAKE state and will be LOW in INIT state.

#### Exception:

• Exception: In case of an over or undervoltage of the internal supply voltages a "hard reset" is always initiated. Please refer to **Chapter 8.3**.

#### 11.4.3 Transition into FAILSAFE State

![](_page_9_Picture_2.jpeg)

Figure 50 Move to FAILSAFE State

The following failures will bring the device from any state to FAILSAFE-state:

- Detection of over voltage, a short to ground or thermal shutdown at LDO  $\,\mu C$
- Detection of over voltage or a short to ground at Core Sup adj. or LDO Stby
- · Detection of over voltage at voltage reference
- Detection of over voltage, short to ground<sup>1)</sup> (only during startup phase in INIT state) or thermal shutdown at pre regulator
- Three consecutive initialization failures(e.g. configuration in INIT state failed)
- · A BIAS current monitor failure
- A over temperature shutdown due to exceeded temperature in the monitoring block.
- A fuse selection monitor failure
- An over voltage at the supply pins (VS) will trigger the overvoltage protection and move the device into FAILSAFE-state (except for STANDBY state)

<sup>1)</sup> A detected short to GND of the pre regulator after the power sequencing in INIT state (once above the UV threshold) will not be considered as a Move to FAILSAFE event, but the event will be stored in MONSF0.PREGSG without an interrupt.

#### 11.4.3.1 INIT -> FAILSAFE state due to detected fault

#### **Timing Diagram**

![](_page_0_Figure_3.jpeg)

Figure 51 Transition from INIT to FAILSAFE state

- The transition from INIT state into FAILSAFE state will be initiated by any failure (external or internal) case mentioned in **Chapter 11.4.3**.
- Pin ROT will be pulled to LOW as soon as one of the MoveToFailsafe failures is detected, if is not already LOW
  due to an undervoltage on a μC related regulator.
- All regulators will be switched off, when the device turns from INIT into FAILSAFE state, regardless if they are in over voltage condition or not.
- The safe state signals SS1 and SS2 are LOW in INIT state and will be LOW in FAILSAFE state.

# **11.4.3.2 XXXX -> INIT -> FAILSAFE state due to detected fault**

# **Timing Diagram**

![](_page_1_Figure_3.jpeg)

**Figure 52 Transition from XXXX to INIT to FAILSAFE state after detection of short to ground**

- The detection of an under voltage of the µC related voltages *V*QUC, *V*QST or *V*VCI as shown in the figure will initiate the transition into INIT state. (please refer to previous chapter Transition into INIT state)
- Pin ROT will be pulled to LOW as soon as the under voltage is detected (at one or more of the regulators mentioned above - whichever is the first)
- The safe state signal SS1 will be pulled to LOW together with pin ROT going to low
- If the short to ground maintains for longer than the short to ground detection time *t*StG a short to ground event is detected.
- All regulators will be switched off as soon as the short to GND is detected, regardless if they are in under voltage condition or not.
- The device moves from INIT state to FAILSAFE state
- The safe state signal SS2 will be pulled to LOW together with the transition from INIT to FAILSAFE state, even if the delay time *Δt*SS2 has not expired yet, because LDO\_µC is switched off (LDO\_µC is switched on in INIT state, but switched off in FAILSAFE state).

#### 11.4.3.3 NORMAL -> FAILSAFE state due to detected fault

# **Timing Diagram**

![](_page_2_Figure_3.jpeg)

Figure 53 Transition from NORMAL to FAILSAFE state

- The detection of an over voltage of the preregulator voltage  $V_{\text{PREREG}}$  or the  $\mu\text{C}$  related voltages  $V_{\text{QUC}}$ ,  $V_{\text{QST}}$ ,  $V_{\text{VCI}}$  or  $V_{\text{QVR}}$  as shown in the figure will initiate the transition from NORMAL state to FAILSAFE state.
- Pin ROT will be pulled to LOW as soon as the over voltage event is detected (at one or more of the regulators mentioned above whichever is the first).
- All regulators will be switched off, when the device turns from NORMAL into FAILSAFE state, regardless if they are in over voltage condition or not.
- The safe state signals will be pulled to LOW immediately with pin ROT going to low, because the LDO\_μC is switched off.
- The transition from NORMAL state into FAILSAFE state will be initiated by any failure (external or internal) case mentioned in **Chapter 11.4.3**.
- The detection of a short to ground of the  $\mu$ C related voltages  $V_{\rm QUC}$ ,  $V_{\rm QST}$  or  $V_{\rm VCI}$  as shown in the **Figure 52** will first be detected as an under voltage event and move the device from NORMAL state to INIT state. After the short to ground detection time  $t_{\rm SIG}$  the device will then move from INIT state to FAILSAFE state (please refer to transition from INIT state to FAILSAFE state).

# **11.4.3.4 STANDBY -> FAILSAFE state due to detected fault**

# **Timing Diagram**

![](_page_3_Figure_3.jpeg)

**Figure 54 Transition from STANDBY to FAILSAFE state**

- The detection of an over voltage of the µC related voltage *V*QST as shown in the figure will initiate the transition from STANDBY state to FAILSAFE state.
- Pin ROT is LOW in STANDBY state and will stay LOW in FAILSAFE state.
- The safe state signals SS1 and SS2 are LOW in STANDBY state and will be LOW in FAILSAFE state.
- Beside the example above the transition from STANDBY state into FAILSAFE is initiated by an internal BIAS current monitor failure.
- The detection of a short to ground of the µC related voltages *V*QUC, *V*QST or *V*VCI as shown in the **Figure 52** will first be detected as an under voltage event and move the device from STANDBY state to INIT state. After the short to ground detection time *t*StG the device will then move from INIT state to FAILSAFE state (please refer to transition from INIT state to FAILSAFE state).

#### 11.4.3.5 SLEEP -> FAILSAFE state due to Fault

# **Timing Diagram**

![](_page_4_Figure_3.jpeg)

Figure 55 Transition from SLEEP to FAILSAFE state

- The detection of an over voltage of the preregulator voltage  $V_{\text{PREREG}}$  or the  $\mu\text{C}$  related voltages  $V_{\text{QUC}}$ ,  $V_{\text{QST}}$ ,  $V_{\text{VCI}}$  or  $V_{\text{QVR}}$  as shown in the figure will initiate the transition from SLEEP state to FAILSAFE state.
- Pin ROT will be pulled to LOW as soon as the over voltage event is detected (at one or more of the regulators mentioned above whichever is the first).
- All regulators will be switched off, when the device turns from SLEEP into FAILSAFE state., regardless if they are in over voltage condition or not.
- The safe state signals will stay at LOW as in the SLEEP state.
- The transition from SLEEP state into FAILSAFE state will be initiated by any failure (external or internal) case mentioned in **Chapter 11.4.3**.
- The detection of a short to ground of the  $\mu$ C related voltages  $V_{\text{QUC}}, V_{\text{QST}}$  or  $V_{\text{VCI}}$  as shown in the **Figure 52** will first be detected as an under voltage event and move the device from SLEEP state to INIT state. After the short to ground detection time  $t_{\text{SIG}}$  the device will then move from INIT state to FAILSAFE state (please refer to transition from INIT state to FAILSAFE state).

#### 11.4.3.6 WAKE -> FAIL SAFE state due to detected fault

# **Timing Diagram**

![](_page_5_Figure_3.jpeg)

Figure 56 Transition from WAKE to FAILSAFE state

- The detection of an over voltage of the preregulator voltage  $V_{\text{PREREG}}$  or the  $\mu\text{C}$  related voltages  $V_{\text{QUC}}$ ,  $V_{\text{QST}}$ ,  $V_{\text{VCI}}$  or  $V_{\text{QVR}}$  as shown in the figure will initiate the transition from WAKE state to FAILSAFE state.
- Pin ROT will be pulled to LOW as soon as the over voltage event is detected (at one or more of the regulators mentioned above whichever is the first).
- All regulators will be switched off, when the device turns from WAKE into FAILSAFE state., regardless if they are in over voltage condition or not.
- The safe state signals will stay at LOW as in the WAKE state.
- The transition from WAKE state into FAILSAFE state will be initiated by any failure (external or internal) case mentioned in **Chapter 11.4.3**.
- The detection of a short to ground of the  $\mu$ C related voltages  $V_{\text{QUC}}$ ,  $V_{\text{QST}}$  or  $V_{\text{VCI}}$  as shown in the **Figure 52** will first be detected as an under voltage event and move the device from WAKE state to INIT state. After the short to ground detection time  $t_{\text{SIG}}$  the device will then move from INIT state to FAILSAFE state (please refer to transition from INIT state to FAILSAFE state).

#### 11.4.3.7 Transition into FAILSAFE state due to thermal shutdown

#### **Timing Diagram**

![](_page_6_Figure_3.jpeg)

Figure 57 Transition into to FAILSAFE state due to thermal shutdown

- The transition from any state into FAILSAFE state will be initiated by a thermal shutdown (TSD).
- Pin ROT will be pulled to LOW as soon as the thermal shutdown will be detected.
- All regulators will be switched off, when the device turns from xxx into FAILSAFE state. regardless if they are in over temperature condition or not
- Out of NORMAL state the safe state signals SS1 and SS2 will be pulled to LOW immediately with pin ROT going to low, because the LDO\_µC is switched off. Out of any other state the safe state signals SS1 and SS2 are LOW and will stay low.
- The device will stay in FAILSAFE state after a thermal shutdown (TSD) at least for 1 s.

# **11.4.4 Transition into POWERDOWN-state**

![](_page_7_Picture_2.jpeg)

**Figure 58 Move to POWERDOWN-state**

The following failures/event will bring the device always with highest priority to POWERDOWN-state:

- *V*VS below *V*PD,lo,min when decreasing
- Detection of over- or under voltage on internal supplies

# **11.5 Electrical Characteristics**

**Table 11-8 Electrical characteristics: State machine**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                         | Symbol            | Values |      |      | Unit | Note /                                                                                                       | Number    |
|---------------------------------------------------|-------------------|--------|------|------|------|--------------------------------------------------------------------------------------------------------------|-----------|
|                                                   |                   | Min.   | Typ. | Max. |      | Test<br>Condition                                                                                            |           |
| INIT timer / Initialization<br>time-out           | tINIT             | 550    | 600  | 650  | ms   | –                                                                                                            | P_11.5.1  |
| FAILSAFE time                                     | tFAILSAFE,<br>min | 18     | 20   | 22   | ms   | –                                                                                                            | P_11.5.2  |
| FAILSAFE time TSD                                 | tFAILSAFE,<br>min | 0.9    | 1    | 1.1  | s    | for thermal<br>shutdown TSD                                                                                  | P_11.5.3  |
| Transition delay timer<br>accuracy                | ttr,del           | -20    | –    | +20  | %    | 1)<br>Configurable value<br>DEVCFG0.TRDEL                                                                    | P_11.5.4  |
| LDO_µC current monitoring<br>for low power states | ILDO_µC,<br>att   | -30    | –    | +30  | %    | Configurable value<br>DEVCFG2.CTHR<br>;<br>VPREREG<br>VQUC<br>><br>+<br>Vdr,QUC                              | P_11.5.5  |
| State transition time                             | ttr               | –      | –    | 100  | µs   | except transitions<br>to SLEEP,<br>to STANDBY2) or<br>from STANDBY                                           | P_11.5.6  |
| State transition time to INIT                     | ttr,INIT          | –      | –    | 150  | µs   | valid for "Move to<br>INIT" events<br>excluding<br>transitions from<br>STANDBY,<br>FAILSAFE and<br>POWERDOWN | P_11.5.7  |
| State transition time to INIT                     | ttr,INIT          | –      | –    | 250  | µs   | valid for transitions<br>from STANDBY,<br>FAILSAFE and<br>interrupted<br>transition to<br>STANDBY            | P_11.5.8  |
| Internal start-up time from<br>POWERDOWN          | ttr,pwrd          | –      | 0.4  | 2    | ms   | from first VS<br>connection to INIT/<br>power sequence                                                       | P_11.5.9  |
| PowerDown threshold high<br>(Power-On-Reset POR)  | VPD,hi            | –      | –    | 6    | V    | VVS increasing                                                                                               | P_11.5.10 |
| PowerDown threshold low<br>(Power-On-Reset POR)   | VPD,lo            | 2      | –    | 3.5  | V    | VVS decreasing                                                                                               | P_11.5.11 |

<sup>1)</sup> Due to internal delays the transition delay time can be enlarged by max 30 µs.

| DEVCFG0.TRDEL and its accuracy specified in Table 11-8. |  |  |  |  |  |  |  |  |  |  |
|---------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |
|                                                         |  |  |  |  |  |  |  |  |  |  |

2) For transition times into SLEEP or STANDBY please refer to the transition delay timer configurable by register

## **11.6 Built In Self Test (BIST) Features**

TLF35584 provides the option to test certain observation functions with the assistance of the external µC via built in self-test features. These features are described in the following chapters.

#### **11.6.1 Analog Built In Self Test (ABIST)**

TLF35584 provides the option to test the comparator and evaluation logic related to the monitoring functions contributing to the activation of the secondary safety shutdown path and the generation of an interrupt. Further on additional comparators and evaluation logic related to the safe state control itself can be tested (SSC overvoltage watchdog and toggling monitor). This is accomplished via an internal ABIST controller which performs tests on each comparator generating artificial undervoltage and overvoltage (or current) conditions, is checking the result and generates the information which needs to be evaluated by the µC to judge, if the ABIST operation has been performed successfully or not.

The following status information on ABIST operation is generated by the system:

• In case an ABIST operation has been requested by the µC, a status is provided after the ABIST has been performed (**ABIST\_CTRL0**.**STATUS**). This status needs to be evaluated by the µC. The provided status is just a GO-NOGO information, which means information about a particularly tested path is provided. The basic comparator function is tested, but not the respective threshold values.

The test of the monitoring and safety relevant output functions is run on three different areas in the system:

- The functionality of a comparator and its corresponding deglitching logic can be tested by a "comparator only" test. This test is performed by generating the failure condition for a time shorter than the deglitching time, accordingly the secondary safety shutdown path nor the interrupt is triggered due to the detected failure. During this test only the selected comparator(s) are tested. In case more than one comparator is selected, the test is performed with a fixed sequence of comparators to be tested. The completion of the test is indicated by an interrupt.
- The functionality of a comparator including its corresponding deglitching logic and the contribution to the respective safety measure can be tested. The safety measure is either the activation of the secondary safety shutdown path or the generation of an interrupt. This test is performed in a time longer than the deglitching time.
- While the device provides information about the status for the first and the second ABIST, further microcontroller cooperation is required for the third area. The µC is responsible to check if the secondary safety shutdown path has been activated successfully (SS1/SS2 are set low) or an interrupt event has been detected by the µC.

## **11.6.1.1 How to run the ABIST**

During ABIST, servicing of the watchdog(s) and error monitoring is required to be performed according to the configuration by the microcontroller. Error in not doing so will lead to failure events in these functions and will lead to the assertion of interrupt, reset or safe state output events accordingly, which is disturbing the proper analysis of the ABIST results. Optionally watchdog functionality and/or error monitoring can be disabled during ABIST operation via a protected register access. In this case, no servicing is required.

During a performed ABIST including the deglitching logic the FLAG registers (**SYSFAIL**, **INITERR**, **IF**) as well as the status information (**MONSF1**, **MONSF2**, **MONSF3**) are triggered and updated by out of range conditions caused by the ABIST functionality, which has to be considered beside the results provided in the ABIST related registers (**ABIST\_CTRL0** to **ABIST\_SELECT2**).

During the time, when the ABIST is performed by internal hardware, the assertion of ROT due to the occurrence of any event which is supposed to trigger the respective action and is part of the logic which is affected by the ABIST control is blocked. In addition, the state machine will not change its state according to the reaction on detected faults described in **Chapter 11.4**. In case an ABIST contributing to the secondary safety shutdown path is started and the device is in NORMAL state, the state machine will move from NORMAL to WAKE state. Furthermore, all voltages will be kept enabled regardless of any out of range detection caused by ABIST itself.

The test of a single functionality is basically always performed in the same way:

- All comparators are assumed to be enabled in case they are selected to be tested, while this is true for any µC related voltage it might not be the case for non µC related voltages. Accordingly, configurable LDO's have to be enabled before they can be tested. On the other hand the ABIST test on a comparator which is not used by the system is not required to be performed.
- The comparators to be tested shall be selected by setting the individual bit(s) in the respective register(s) (**ABIST\_SELECT0**, **ABIST\_SELECT1** and **ABIST\_SELECT2**). For this selection it is necessary to differentiate by the contribution to the different safety measure. The differentiation can be derived from **Table 11-9**.
- The microcontroller shall configure the register **ABIST\_CTRL0** according to the functionality to be tested. The configuration consist of the tested safety measure (**ABIST\_CTRL0**.**INT**), the tested area/coverage by the ABIST (**ABIST\_CTRL0**.**PATH**) and the configuration whether a sequence or a single comparator shall be tested (**ABIST\_CTRL0**.**SINGLE**).
- The microcontroller shall set the global ABIST start bit (**ABIST\_CTRL0**.**START**) to start the ABIST.
- The global ABIST start bit shall be read by the µC. If this bit is still set, ongoing ABIST functionality is performed. Upon completion of the selected ABIST operation(s) the start bit is cleared and an interrupt event is generated.
- Each bit which has been set to select the test of a dedicated comparator (**ABIST\_SELECT0**, **ABIST\_SELECT1** and **ABIST\_SELECT2**) is cleared once a successful ABIST operation has been performed on the particular comparator. Each bit which has been set to select the test of a dedicated comparator is kept unchanged if the ABIST operation on this particular comparator has not been performed successfully.

In this way the µC can determine which comparator failed in case the ABIST status information shows a failing ABIST operation.

**Table 11-9 Contribution of comparators to safety measures**

| Comparator           | Secondary Safety<br>Shutdown Path | Interrupt | ABIST_Select register bit |
|----------------------|-----------------------------------|-----------|---------------------------|
| LDO_µC Overvoltage   | X                                 |           | ABIST_SELECT0.UCOV        |
| Core_Sup Overvoltage | X                                 |           | ABIST_SELECT0.VCOREOV     |
| LDO_Stby Overvoltage | X                                 |           | ABIST_SELECT0.STBYOV      |

**Table 11-9 Contribution of comparators to safety measures** (cont'd)

| Comparator                  | Secondary Safety<br>Shutdown Path | Interrupt | ABIST_Select register bit |
|-----------------------------|-----------------------------------|-----------|---------------------------|
| Volt_Ref Overvoltage        | X                                 |           | ABIST_SELECT0.VREFUV      |
| PreReg Overvoltage          | X                                 |           | ABIST_SELECT0.PREGOV      |
| LDO_µC Undervoltage         | X                                 |           | ABIST_SELECT1.UCUV        |
| Core_Sup Undervoltage       | X                                 |           | ABIST_SELECT1.VCOREUV     |
| LDO_Stby Undervoltage       | X                                 |           | ABIST_SELECT1.STBYUV      |
| BIAS current low            | X                                 |           | ABIST_SELECT2.BIASLOW     |
| BIAS current high           | X                                 |           | ABIST_SELECT2.BIASHI      |
| Supply VS Overvoltage       | X                                 |           | ABIST_SELECT2.VBATOV      |
| Internal Supply Overvoltage | X 1)                              |           | ABIST_SELECT2.INTOV       |
| Tracker 1 Overvoltage       |                                   | X         | ABIST_SELECT0.TRK1OV      |
| Tracker 2 Overvoltage       |                                   | X         | ABIST_SELECT0.TRK2OV      |
| LDO_Com Overvoltage         |                                   | X         | ABIST_SELECT0.COMOV       |
| Volt_Ref Undervoltage       |                                   | X         | ABIST_SELECT1.VREFUV      |
| Tracker 1 Undervoltage      |                                   | X         | ABIST_SELECT1.TRK1UV      |
| Tracker 2 Undervoltage      |                                   | X         | ABIST_SELECT1.TRK2UV      |
| LDO_Com Undervoltage        |                                   | X         | ABIST_SELECT1.COMUV       |
| Pre_Reg Undervoltage        |                                   | X         | ABIST_SELECT1.PREGUV      |
| VBG1 - 4% ≤<br>VBG2         |                                   | X         | ABIST_SELECT2.BG12UV      |
| VBG1 + 4% ≥<br>VBG2         |                                   | X         | ABIST_SELECT2.BG12OV      |

<sup>1)</sup> This comparator must be tested only by "comparator only" test

## **11.6.1.2 Testing the comparator logic only**

During the ABIST operation the comparators are triggered by the ABIST controller for a time shorter than the internal deglitching time *t*rr (reset reaction time). A properly working comparator signals an out of range condition to its output for the time the failure condition is applied.

The provided information of each comparator is checked against the expected value. If the comparator output value matches the expected value this is considered as a passing test by the ABIST controller. If any of the provided output values do not match the expected value, this is considered as a failing test. The general result of the ABIST is provided by the **STATUS** in the register **ABIST\_CTRL0**. The detailed result for each selected comparator can be checked by the registers **ABIST\_SELECT0**, **ABIST\_SELECT1** and **ABIST\_SELECT2**. In case the previously selected bits are reset after the test is finished, it can be considered as pass. A bit which is still set, would indicated the failing comparator(s), that makes the overall **STATUS** to be failed.

Accordingly the maximum selection1) (including possible ones) for the comparator test would be the following: Secondary safety shutdown path (SS1/2) related:

```
• ABIST_SELECT0 : 00101111B (2FH)
• ABIST_SELECT1 : 00001110B (0EH)
• ABIST_SELECT2 : 11001001B (C9H)
```

• Start of the test by **ABIST\_CTRL0** : 00000001B (01H)

Interrupt (INT) related:

```
• ABIST_SELECT0 : 11010000B (D0H)
• ABIST_SELECT1 : 11110001B (F1H)
• ABIST_SELECT2 : 00110000B (30H)
• Start of the test by ABIST_CTRL0 : 00001001B (09H)
```

This type of ABIST can be performed in the following states of the **State Machine**: INIT, NORMAL, WAKE. In case of an successful ABIST there shall be no reaction of secondary safety shutdown path SS1/2 and only an interrupt generated due to the finished ABIST (**IF**.**ABIST** set and **IF**.**MON** not set, considering cleared interrupt flags prior to the ABIST and no real failure events during the ABIST).

<sup>1)</sup> Please mind that for a test of a comparators the corresponding output has to be enabled.

## **11.6.1.3 Testing the comparator logic and the corresponding deglitching logic**

During the ABIST operation the comparators are triggered by the the ABIST controller for a time longer than the internal deglitching time *t*rr (reset reaction time). A properly working comparator signals an out of range condition to its output for the time the failure condition is applied. The deglitching logic will forward the failure trigger after *t*rr and makes the device react on the recognized failure event. This reaction consists the storage of the respective monitoring failure flags and as well the triggering of the respective output function, which is either the interrupt INT or the secondary safety shutdown path SS1/2. The reaction of the safe state outputs SS1/2 can only be observed in case the test is started in NORMAL state.

Furthermore the provided information of each deglitching logic output is checked against the expected value. If the deglitching logic output value matches the expected value this is considered as a passing test by the ABIST controller. If any of the provided output values do not match the expected value, this is considered as a failing test. The general result of the ABIST is provided by the **STATUS** in the register **ABIST\_CTRL0**. The detailed result for each selected comparator can be checked by the registers **ABIST\_SELECT0**, **ABIST\_SELECT1** and **ABIST\_SELECT2**. In case the previously selected bits are reset after the test is finished, it can be considered as pass recognized by the ABIST controller. A bit which is still set, would indicated the failing comparator(s), that makes the overall **STATUS** to be failed.

Beside the results read from the ABIST controller related registers, the result provided in the failure/interrupt flags (**SYSFAIL**, **INITERR** and **IF**) and monitoring status flags (**MONSF1**, **MONSF2** or **MONSF3**) have to be read and checked by the microcontroller against the expected result considering the configuration set before the start of the ABIST.

**INTOV** located in register **ABIST\_SELECT2** cannot be tested in this way, testing of the comparator logic only is required according to **Chapter 11.6.1.2**.

The maximum selection1) for the comparator and deglitching logic test would be the following:

Secondary safety shutdown path (SS1/2) related:

- **ABIST\_SELECT0** : 00101111B (2FH)
- **ABIST\_SELECT1** : 00001110B (0EH)
- **ABIST\_SELECT2** : 11000001B (C1H)
- Start of the test by **ABIST\_CTRL0** : 00000011B (03H)

#### Interrupt (INT) related:

- **ABIST\_SELECT0** : 11010000B (D0H)
- **ABIST\_SELECT1** : 11110001B (F1H)
- **ABIST\_SELECT2** : 00110000B (30H)
- Start of the test by **ABIST\_CTRL0** : 00001011B (0BH)

<sup>1)</sup> Please mind that for a test of a comparators the corresponding output has to be enabled.

The analysis based on the maximum possible selection would consist the following: Secondary safety shutdown path (SS1/2) related:

```
• IF : 01000000B (40H)
• INITERR : 00000100B (04H)
• SYSFAIL : 00000100B (04H)
• MONSF1 : 00101111B (2FH)
• MONSF2 : 00001110B (0EH)
• MONSF3 : 11000001B (C1H)
• Start of the test by ABIST_CTRL0 : 00000011B (03H)
```

#### Interrupt (INT) related:

```
• IF : 01001000B (48H)
• INITERR : 00000000B (00H)
• SYSFAIL : 00000000B (00H)
• MONSF1 : 11010000B (D0H)
• MONSF2 : 11110001B (F1H)
• MONSF3 : 00110000B (30H)
```

• Start of the test by **ABIST\_CTRL0** : 00001011B (0BH)

This type of ABIST can be performed in the following states of the **State Machine**: INIT, WAKE, NORMAL. If this test is run in NORMAL state on comparators contributing to the secondary safety shutdown path the device will switch low the safe state outputs SS1/2 and the **State Machine** will move to WAKE state, without triggering a reset ROT.

It has to be considered that testing the complete monitoring chain till the respective output (SS1/2 or INT) in this way will cover only the first comparator in the sequence, as this one will trigger the output reaction. For further details, please refer to **Chapter 11.6.1.4**.

If this test is run in INIT or WAKE state, contribution to activation of the secondary safety shutdown path cannot be tested. The system is in a safe state already and the secondary safety shutdown path is already activated. In any way the proper behavior of the secondary shutdown p3ath as well as the interrupt signal needs to be checked by the microcontroller.

## **11.6.1.4 Testing the complete monitoring chain (comparators, deglitching and output)**

The testing of the complete monitoring chain from the comparator till the respective output function has to be divided into the two functions available in TLF35584. First the secondary safety shutdown path called SS1/2 for severe microcontroller related failure events and secondly the interrupt function INT for peripheral related failure events in terms of voltage and current monitoring.

#### **11.6.1.4.1 Testing the activation of the secondary safety shutdown path**

To test the activation of the secondary safety shutdown path, the device has to be brought into NORMAL state. The µC shall check if the secondary safety shutdown path has been de-activated successfully (SS1/2 high).

Once in NORMAL state a single comparator contributing to the secondary safety shutdown path shall be selected. A single bit ('x') has to be set for a corresponding comparator in registers **ABIST\_SELECT0** (00x0xxxxB), **ABIST\_SELECT1** (0000xxx0B) or **ABIST\_SELECT2** (xx00000xB). A randomized selection by the microcontroller ensures maximum coverage of the contributions to the secondary safety shutdown path. Then a single comparator ABIST operation on the full path of the secondary safety shutdown path needs to be started (register **ABIST\_CTRL0**: 00000111B (07H) ). Upon completion of the requested ABIST operation the device will autonomously move into WAKE state and an interrupt event is generated. The interrupt event will indicate the completion of the ABIST (**IF**.**ABIST**). Furthermore the respective monitoring failure flag for the selected comparator will be set (either **INITERR**.**VMONF** for "**Move to INIT State**" failures or **SYSFAIL**.**VMONF** for "**Move to FAILSAFE State**" failures) which has to be checked and cleared by the microcontroller.

The secondary safety shutdown path shall be activated (SS1/2 low), it is the responsibility of the µC to check the activation of the secondary safety shutdown path. If SS2 delay is enabled, this delay will be applied when the ABIST operation is performed, i.e. the activation of the shutdown path connected to SS2 will be delayed according to the programmed value for failure cases not leading to FAILSAFE.

The µC needs to read and check the status of the requested ABIST operation (**ABIST\_CTRL0**.**STATUS**), the respective monitoring status flag (**MONSF1**, **MONSF2** or **MONSF3**) to be set according to the previous selection and **ABIST\_SELECT0**, **ABIST\_SELECT1** and **ABIST\_SELECT2** bits to be cleared.

Furthermore, the microcontroller has to proceed with the following steps to check the safe state control and the safe state outputs:

- Check that the secondary safety shutdown path has been activated successfully (SS1/2 low)
- Enable overvoltage trigger of the safe state control (set **ABIST\_CTRL1**.**OV\_TRIG**)
- Wait for 50µs and check that the secondary safety shutdown path is still activated successfully (SS1/2 low)
- Select generation of valid toggling signal for the safe state control (set **ABIST\_CTRL1**.**ABIST\_CLK\_EN**)
- Wait for 50µs and check that the secondary safety shutdown path is still activated successfully (SS1/2 low)
- De-select generation of toggling signal for the safe state control (reset **ABIST\_CTRL1**.**ABIST\_CLK\_EN**)
- Wait for 50µs and check that the secondary safety shutdown path is still activated successfully (SS1/2 low)
- Disable overvoltage trigger of the safe state control (set **ABIST\_CTRL1**.**OV\_TRIG**)
- Wait for 50µs and check that the secondary safety shutdown path is still activated successfully (SS1/2 low)

Afterwards a test of all comparators which contribute to the activation of the secondary safety shutdown path shall be configured and started according to **Chapter 11.6.1.3**.

## **11.6.1.4.2 Testing the generation of an interrupt event**

The test of the generation of an interrupt event can be done in the states INIT, NORMAL and WAKE state. Even though it is recommended to have the application in safe state (INIT or WAKE state).

For this test first a single comparator contributing to the interrupt function shall be selected. A single bit ('x') has to be set for a corresponding comparator in registers **ABIST\_SELECT0** (xx0x0000B), **ABIST\_SELECT1** (xxxx000xB) or **ABIST\_SELECT2** (00xx0000B). A randomized selection by the microcontroller ensures maximum coverage of the contributions to the interrupt function. Then a single comparator ABIST operation on the full path of the interrupt needs to be started (register **ABIST\_CTRL0**: 00001111B (0FH) ). The artificial failure, triggered by the ABIST controller, on the selected comparator will generate an interrupt (INT) event. It is the responsibility of the µC to check the generation of this interrupt event on the triggered failure. As this is a test of the generation of an interrupt based on a failure event, there is no dedicated ABIST completion event, nor the **ABIST** bit in the interrupt flags will be set. Accordingly it is recommended to store the information about the started ABIST in the firmware. After the interrupt has been generated the interrupt flag register shall be checked for the monitoring bit (**IF**.**MON**) set and the ABIST completion bit (**IF**.**ABIST**) not set.

The µC needs to read and check the status of the requested ABIST operation (**ABIST\_CTRL0**.**STATUS**), the respective monitoring status flag (**MONSF1**, **MONSF2** or **MONSF3**) to be set according to the previous selection and **ABIST\_SELECT0**, **ABIST\_SELECT1** and **ABIST\_SELECT2** bits to be cleared.

Afterwards a test of all comparators which contribute to the interrupt generation shall be configured and started according to **Chapter 11.6.1.3**.

#### **11.6.1.5 Abort conditions for ABIST operation**

In case of an severe monitoring failure event (contribution to the secondary safety shutdown path) detected on a not selected comparator1) or a severe failure event not related to the voltage or bias current monitoring function during the proceeding of an ABIST operation on the comparators only (**ABIST\_CTRL0**.**PATH** not set), the device will react as it is supposed to do in normal operation. Accordingly the monitoring, reset and safe state control are reacting. Bringing the device into safe state and trigger the **State Machine** to move into FAILSAFE or INIT state. The ABIST is aborted in this case.

In case of an ABIST operation on the full path (**ABIST\_CTRL0**.**PATH** set) the comparators for voltage and bias current monitoring are blind for the time of the ABIST operation. Therefore it is recommended to do the test in safe state unless it is needed to start the test in NORMAL state (e.g. test of activation of secondary safety shutdown path described in **Chapter 11.6.1.4.1**). Severe failure events not related to the voltage and bias current monitoring will trigger the same device reaction as in usual condtion. Bringing the device into safe state and trigger the **State Machine** to move into FAILSAFE or INIT state. The ABIST is aborted in this case.

This ABIST abort will be shown by the TLF35584 in the register **SYSFAIL**.**ABISTERR**. The artificial failure events, that have been generated until the abort of the ABIST due to the detected real failure, will be stored as well in the monitoring registers.

<sup>1)</sup> Please mind that selected comparators might be blind for the time of the ABIST operation. Therefore it is recommended to do the test in safe state unless it is needed to start the test in NORMAL state (e.g. test of activation of secondary safety shutdown path described in **Chapter 11.6.1.4.1**).

# **11.6.2 Logic Built In Self Test**

No dedicated Built In Self Test for the digital logic exists in the device. It is therefore assumed that any test which is related to the digital logic is performed by the µC.

The following blocks inside the digital logic can be tested by the µC:

- FWD/WWD
- Error monitoring

In order to verify correct functionality of these blocks and to check their contribution to ROT/INT and finally SS1/2 the µC shall generate an error condition on the particular block and check for the occurrence of the expected system behavior.

- For the watchdog functionality this basically means either stop triggering the WD(s) and/or generate false trigger events. This will either generate and interrupt or even assert the reset. Finally the secondary safety shutdown path will be activated, the µC will be reset and the device will move into INIT state. In order to verify the activation of the secondary shutdown path, this kind of test shall only be executed after the device has been moved into NORMAL state.
- For the error monitoring block, this means that the toggling at the ERR pin needs to be stopped in order to observe the required system behavior. It is up to the µC to make use of the error recovery mechanism or not.

# **11.7 Microcontroller Programming Support**

The TLF35584 offers a microcontroller programming support feature, that can be used to avoid periodic reset triggering due to missing triggering of the window watchdog and error monitoring within the INIT timer. The activation of the microcontroller programming support feature shall be done by pulling the MPS pin to 5 V. The voltage shall be provided earliest with the enabling of the voltage reference. Therefore it would be one option to connect the MPS pin to the output QVR during microcontroller programming.

The active microcontroller programming support feature includes the following changes to the normal operation of the device:

- The INIT timer will be stopped.
- The contribution of the window watchdog failure counter overflow to the reset ROT will be blocked.
- The contribution of the functional watchdog failure counter overflow to the reset ROT will be blocked.
- The contribution of the error monitoring to the reset ROT will be blocked.

As only the contribution of the watchdogs and the error monitoring to the reset function is blocked/disconnected, the state machine and safe state control function are not affected. Accordingly an overflow of the window or functional watchdog failure counter will trigger a "Move to INIT" event, but without issuing a reset of the microcontroller.

The microcontroller programming support feature offers as well the possibility to move the TLF35584 to any other state according to the state machine. E.g. in case MPS pin is high in NORMAL and there is a watchdog error counter overflow the device would move into INIT without issuing a reset.