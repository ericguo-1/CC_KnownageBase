# **12 Safe State Control Function**

## **12.1 Introduction**

The safe state control monitors safety related signals and controls the safe state signals SS1 and SS2.

The following description summarizes the contributors to the safe state control function and the possibilities to adjust them.

### **Principle of operation:**

The safe state control function monitors the following inputs:

- Result of the Error Monitoring. "Error"-signal at pin ERR is expected to be a toggling signal. A permanent low or high signal will be detected as an error.
- Over and under voltage of the micro processor related regulators (for details please refer to chapter **Monitoring Function**)
- Result of Window Watchdog Failure Counter Threshold Comparator. Whether threshold ΣWWO for "Invalid window watchdog triggering" has been exceeded.
- Result of Functional Watchdog Failure Counter Threshold Comparator: Whether threshold ΣFWO for "Invalid functional watchdog triggering" has been exceeded.
- Thermal shutdown signal (TSD) for relevant events moving the device into FAILSAFE state.
- Internal clock
- SPI state transition request. A valid GoToNORMAL command triggers the signals SS1/2 to switch high in case the other boundary conditions are fulfilled. Moving the device out of NORMAL state by SPI command will switch the signals SS1 and 2 (optionally delayed by *t*SS2) to low.

The following parameters of the safe state control function are programmable via SPI, this settings can be done during INIT, NORMAL, SLEEP and WAKE state, WWD and FWD configuration and error pin configuration including disabling of individual functionality via protected register (for description of states please refer to chapter **State Machine**):

- Number of invalid watchdog triggers, that lead to activating SS1 and SS2: There are two watchdog trigger failure counters implemented, one for the window watchdog the other for the functional watchdog. Every counter increments by two at every invalid watchdog triggering and decrements by one at every valid watchdog triggering. (valid and invalid triggering is described in chapter functional and window watchdog). An incrementing change is indicated by an interrupt. A decrementing change is not indicated by an interrupt. The thresholds can be programmed by SPI command for each counter individually. This function might be used to test the watchdog function.
- Immediate reaction or recovery delay reaction, only related to input signal ERR: This parameter determines whether the safe state control will immediately react to an error indicated by SMU or react after a certain delay, if the error indication is still present. In recovery delay reaction the safe state control will generate an interrupt and start the programmed recovery delay time. If within this time the error should disappear (means the error signal should toggle again, before the recovery delay time has ended), the safe state control will keep the safe state output SS1/2 high. If within this time the error signal should not disappear and maintain the error indication (means the error signal should not toggle again, before the recovery delay time has ended), the safe state control will activate the safe state signals SS1 and SS2 after the recovery delay time has ended. Immediate reaction means reaction after signal detection delay time.
- Recovery delay time *Δt*REC, only related to input signal ERR: An error (violation of valid ERR signal) has to be longer than this delay time to lead to activating the safe state signals SS1 and SS2. This delay time is only active if recovery delay time mode was selected.

• Delay time *Δt*SS2 between safe state signal 1 and safe state signal 2

The safe state function offers two output signals, both of them as output stages to drive external switches (additional driver stage is necessary):

- Safe state signal 1 (present at pin SS1)
- Safe state signal 2 (present at pin SS2), it may be delayed to safe state signal 1 by an adjustable delay time *Δt*SS2 (via SPI)

### **Error signal from microcontroller safety management unit (SMU) at pin ERR:**

The error monitoring function requires a toggling signal at pin ERR with a determined timing in case of fault-free operation of the microcontroller by its SMU. This toggling signal is considered as a "being alive" indication. An error should be indicated by a constant low signal. A constant high signal will also be regarded as a failure indication, probably caused by a short circuit. The result is given to the safe state control.

![](_page_1_Figure_7.jpeg)

**Figure 59 Principle safe state control function**

- State Transition Request= Micro processor can request a de-activation of the Secondary Safety Shutdown path (SS1/2 high) via SPI. Being in NORMAL state the micro processor can activate the Secondary Safety Shutdown path (SS1/2 low) by moving the device out of NORMAL state by SPI.
- ERR = Error pin connected to safety management unit (SMU) of micro processor
- TSD = Thermal shutdown
- ROT = Reset output
- ΣWWO = Number of "Invalid WWD triggering", after safe state control shall activate the safe state signal SS1 and SS2, located in window watchdog block

#### **Safe State Control Function**

- ΣFWO = Number of "Invalid FWD triggering", after safe state control shall activate the safe state signal SS1 and SS2, locked in functional watchdog block
- IMMEDIATE/RECOVERY = Distinguish between immediate reaction to SMU signal or recovery delay time, located in error monitoring block
- *Δt*REC = Recovery delay time for SMU signal at pin ERR, located in error monitoring block
- *Δt*SS2 = Delay time between safe state signal 1 and safe state signal 2
- SS1 = Safe state signal 1
- SS2 = Safe state signal 2

## **12.2 Electrical Characteristics**

**Table 18 Electrical Characteristics: Safe State Control**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                                      | Symbol          |      | Values |      | Unit | Note /                                            | Number    |
|----------------------------------------------------------------|-----------------|------|--------|------|------|---------------------------------------------------|-----------|
|                                                                |                 | Min. | Typ.   | Max. |      | Test<br>Condition                                 |           |
| ERR pin                                                        |                 |      |        |      |      |                                                   |           |
| ERR valid high level                                           | VERR,hi         | 3.6  | –      | –    | V    | VERR increasing,<br>VQUC = 5.0 V                  | P_12.2.1  |
| ERR valid low level                                            | VERR,lo         | –    | –      | 0.8  | V    | VERR decreasing,<br>VQUC = 5.0 V                  | P_12.2.2  |
| ERR hysteresis                                                 | VERR,hyst       | –    | 350    | –    | mV   | VQUC = 5.0 V                                      | P_12.2.3  |
| ERR valid high level                                           | VERR,hi         | 2.0  | –      | –    | V    | VERR increasing,<br>VQUC = 3.3 V                  | P_12.2.4  |
| ERR valid low level                                            | VERR,lo         | –    | –      | 0.8  | V    | VERR decreasing,<br>VQUC = 3.3 V                  | P_12.2.5  |
| ERR hysteresis                                                 | VERR,hyst       | –    | 160    | –    | mV   | VQUC = 3.3 V                                      | P_12.2.6  |
| ERR pull-down current                                          | IERR            | –    | 150    | 330  | µA   | VERR = VQUC                                       | P_12.2.7  |
| ERR input capacitance                                          | CERR            | –    | 4      | 15   | pF   | 1)                                                | P_12.2.8  |
| Valid ERR input signal<br>frequency                            | fERR,valid      | 10   | –      | 45   | kHz  | considering a duty<br>cycle of 50%                | P_12.2.9  |
| Invalid ERR input signal<br>frequency (low frequency)          | fERR,invalid,LF | 0    | –      | 5    | kHz  | considering a duty<br>cycle of 50%                | P_12.2.10 |
| Invalid ERR input signal<br>frequency (high frequency)         | fERR,invalid,HF | 96.2 | –      | 500  | kHz  | considering a duty<br>cycle of 50%                | P_12.2.11 |
| Invalid ERR input signal<br>detection time (low<br>frequency)  | ΔtDET,LF        | 50.1 | –      | 99.9 | µs   | derived from<br>fERR,valid and<br>fERR,invalid,LF | P_12.2.12 |
| Invalid ERR input signal<br>detection time (high<br>frequency) | ΔtDET,HF        | 5.2  | –      | 11.1 | µs   | derived from<br>fERR,valid and<br>fERR,invalid,HF | P_12.2.13 |
| ERR reactivation time-out                                      | tERR,TO         | 9    | 10     | 11   | ms   | after SLEEP                                       | P_12.2.14 |
| ERR reactivation time-out<br>(first edge expected)             | tERR,ren        | 50.1 | –      | 110  | µs   | after reenabling via<br>SPI 2)                    | P_12.2.15 |
| Safe state signal 1 pin SS1                                    |                 |      |        |      |      |                                                   |           |
| SS1 output, high level<br>TLF35584xxVS1                        | VSS1,hi         | 3.6  | 4.8    | VQUC | V    | ISS1<br>≥<br>-1<br>mA;<br>VQUC<br>=<br>5.0<br>V   | P_12.2.16 |
| SS1 output, high level<br>TLF35584xxVS1                        | VSS1,hi         | 3.0  | 4.3    | VQUC | V    | ISS1<br>≥<br>-5<br>mA;<br>VQUC<br>=<br>5.0<br>V   | P_12.2.17 |
| SS1 output, high level<br>TLF35584xxVS2                        | VSS1,hi         | 2.9  | 3.2    | VQUC | V    | ISS1<br>≥<br>-1<br>mA;<br>VQUC<br>=<br>3.3<br>V   | P_12.2.18 |

**Table 18 Electrical Characteristics: Safe State Control** (cont'd)

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                    | Symbol   |      | Values |      | Unit | Note /                                                                                                             | Number    |
|----------------------------------------------|----------|------|--------|------|------|--------------------------------------------------------------------------------------------------------------------|-----------|
|                                              |          | Min. | Typ.   | Max. |      | Test<br>Condition                                                                                                  |           |
| SS1 output, high level<br>TLF35584xxVS2      | VSS1,hi  | 2.0  | 2.8    | VQUC | V    | ISS1<br>≥<br>-5<br>mA;<br>VQUC<br>=<br>3.3<br>V                                                                    | P_12.2.19 |
| SS1 pull-down resistor                       | RSS1,pd  | 70   | 100    | 130  | kΩ   |                                                                                                                    | P_12.2.20 |
| SS1 output, low level                        | VSS1,lo  | –    | 0      | 0.8  | V    | 3) 4)<br>RSS1,pd<br>≤<br>100<br>kΩ<br>;<br>CSS1<br>≥<br>50<br>pF<br>;<br>LDO_µC active<br>;<br>VQUC<br>≥<br>2<br>V | P_12.2.21 |
| SS1 internal reaction time                   | tSS1,act | –    | 12     | 30   | µs   |                                                                                                                    | P_12.2.22 |
| Safe state signal 2 pin SS2                  |          |      |        |      |      |                                                                                                                    |           |
| SS2 output, high level<br>TLF35584xxVS1      | VSS2,hi  | 3.6  | 4.8    | VQUC | V    | ISS2<br>≥<br>-1<br>mA;<br>VQUC<br>=<br>5.0<br>V                                                                    | P_12.2.23 |
| SS2 output, high level<br>TLF35584xxVS1      | VSS2,hi  | 3.0  | 4.3    | VQUC | V    | ISS2<br>≥<br>-5<br>mA;<br>VQUC<br>=<br>5.0<br>V                                                                    | P_12.2.24 |
| SS2 output, high level<br>TLF35584xxVS2      | VSS2,hi  | 2.9  | 3.2    | VQUC | V    | ISS2<br>≥<br>-1<br>mA;<br>VQUC<br>=<br>3.3<br>V                                                                    | P_12.2.25 |
| SS2 output, high level<br>TLF35584xxVS2      | VSS2,hi  | 2.0  | 2.8    | VQUC | V    | ISS2<br>≥<br>-5<br>mA;<br>VQUC<br>=<br>3.3<br>V                                                                    | P_12.2.26 |
| SS2 pull-down resistor                       | RSS2,pd  | 70   | 100    | 130  | kΩ   |                                                                                                                    | P_12.2.27 |
| SS2 output, low level                        | VSS2,lo  | –    | 0      | 0.8  | V    | 3) 4)<br>RSS2,pd<br>≤<br>100<br>kΩ<br>;<br>CSS2<br>≥<br>50<br>pF<br>;<br>LDO_µC active<br>;<br>VQUC<br>≥<br>2<br>V | P_12.2.28 |
| SS2 internal reaction time                   | tSS2,act | –    | 12     | 30   | µs   |                                                                                                                    | P_12.2.29 |
| Adjustable parameters                        |          |      |        |      |      |                                                                                                                    |           |
| SSC time base accuracy                       | tSSC     | -10  | –      | 10   | %    | timebase for ∆tREC<br>and ∆tSS2                                                                                    | P_12.2.30 |
| adjustable recovery delay<br>time            | ∆tREC    | 0    | –      | 10   | ms   | selectable 0, 1.0,<br>2.5, 5.0 and 10 ms;<br>tSSC to be<br>considered                                              | P_12.2.31 |
| adjustable delay time<br>between SS1 and SS2 | ∆tSS2    | 0    | –      | 250  | ms   | selectable 0, 10,50,<br>100 and 250 ms;<br>tSSC to be<br>considered                                                | P_12.2.32 |

- 1) Specified by design, not subject to production test
- 2) It is recommended to provide the ERR signal to the ERR pin before activating the function again via SPI.
- 3) Internal and external pull-down resistors have to be considered for failure cases with QUC being off.
- 4) Considering loss of analog safety ground (AGS1 and AGS2).

## **12.3 Reaction On Microprocessor Safety Management Unit (SMU - Pin ERR):**

### **12.3.1 Immediate reaction on ERR monitoring failure**

The micro processor safety management unit (SMU) indicates a serious error by stopping the toggling signal at pin ERR, immediate reaction to error signal is set:

![](_page_5_Figure_4.jpeg)

**Figure 60 Flow diagram reaction on SMU signal (ERR signal remains low)**

### Description:

- The ERR signal stops toggling and remains low.
- This is detected as an error after the expiration of the detection time *Δt*DET,LF.
- *Δt*DET,LF is measured from the last recognized falling edge.
- The safe state signal 1 (at pin SS1) is pulled to low
- The safe state signal 2 (at pin SS2) is pulled to low after an optional delay time *Δt*SS2

![](_page_5_Figure_12.jpeg)

**Figure 61 Flow diagram reaction on SMU signal (ERR signal remains high)**

- The ERR signal stops toggling and remains high.
- This is detected as an error after the expiration of the detection time *Δt*DET,LF.
- *Δt*DET,LF is measured from the last recognized rising edge.
- The safe state signal 1 (at pin SS1) is pulled to low
- The safe state signal 2 (at pin SS2) is pulled to low after an optional delay time *Δt*SS2

![](_page_6_Figure_1.jpeg)

**Figure 62 Flow diagram reaction on SMU signal (ERR signal frequency too high)**

### Description:

- The ERR signal starts toggling with a frequency of *f*ERR,invalid,HF.
- This is detected as an error as soon as the edge-to-edge time is shorter than the detection time *Δt*DET,HF.
- The safe state signal 1 (at pin SS1) is pulled to low.
- The safe state signal 2 (at pin SS2) is pulled to low after an optional delay time *Δt*SS2.

![](_page_6_Figure_8.jpeg)

**Figure 63 Flow diagram reaction on SMU signal (duty-cycle different than 50%,** *t***low or** *t***high too long)**

- The ERR signal toggles with changing high and low times (duty cycle can vary as well), but *t*low and *t*high are in the valid range between *t*DET,HF and *t*DET,LF first.
- Then a low pulse of ERR shown in the figure is longer than the detection time *t*DET,LF.
- This is detected as an error as soon as the edge-to-edge time is longer than the detection time *Δt*DET,LF.
- The safe state signal 1 (at pin SS1) is pulled to low.
- The safe state signal 2 (at pin SS2) is pulled to low accordingly after an optional delay time *Δt*SS2.(not in figure)
- The condition can be applied to the high pulse being longer than the detection time *t*DET,LF in the same way.

![](_page_7_Figure_1.jpeg)

**Figure 64 Flow diagram reaction on SMU signal (duty-cycle different than 50%,** *t***low or** *t***high too short)**

#### Description:

- The ERR signal toggles with changing high and low times (duty cycle can vary as well), but *t*low and *t*high are in the valid range between *t*DET,HF and *t*DET,LF first.
- Then a low pulse of ERR shown in the figure is shorter than the detection time *t*DET,HF.
- This is detected as an error as soon as the edge-to-edge time is shorter than the detection time *Δt*DET,HF.
- The safe state signal 1 (at pin SS1) is pulled to low.
- The safe state signal 2 (at pin SS2) is pulled to low accordingly after an optional delay time *Δt*SS2.(not in figure)
- The condition can be applied to the high pulse being shorter than the detection time *t*DET,HF in the same way.

## **12.3.2 Recovery delay reaction on ERR monitoring failure**

The micro processor safety management unit (SMU) indicates a serious error by stopping the toggling signal at pin ERR, recovery delay time reaction to error signal is set - the SMU is given time to recover:

![](_page_7_Figure_12.jpeg)

**Figure 65 Flow diagram reaction on SMU signal, error longer than recovery delay time**

- The ERR signal stops toggling and remains low (or high).
- This is detected as an error after the expiration of the detection time *Δt*DET,LF.
- *Δt*DET,LF is measured from the last recognized edge.
- An interrupt is generated after the detection to indicate the start of the recovery delay time *Δt*REC
- The safe state signal 1 (at pin SS1) is pulled to low after *Δt*REC has expired
- The safe state signal 2 (at pin SS2) is pulled to low after an optional delay time *Δt*SS2

![](_page_8_Figure_1.jpeg)

**Figure 66 Flow diagram reaction on SMU signal, error longer than recovery delay time (ERR signal frequency too high)**

### Description:

- The ERR signal starts toggling with a frequency of *f*ERR,invalid,HF.
- This is detected as an error as soon as the edge-to-edge time is shorter than the detection time *Δt*DET,HF.
- An interrupt is generated after the detection to indicate the start of the recovery delay time *Δt*REC
- The safe state signal 1 (at pin SS1) is pulled to low after *Δt*REC has expired
- The safe state signal 2 (at pin SS2) is pulled to low after an optional delay time *Δt*SS2

![](_page_8_Figure_9.jpeg)

**Figure 67 Flow diagram reaction on SMU signal, error shorter than recovery delay time**

- The ERR signal stops toggling and remains low (or high).
- This is detected as an error after the expiration of the detection time *Δt*DET,LF.
- *Δt*DET,LF is measured from the last recognized edge.
- An interrupt is generated after the detection to indicate the start of the recovery delay time *Δt*REC
- Before *Δt*REC has expired the ERR signal resumes toggling.

• The safe state signals 1 (at pin SS1) and 2 (at pin SS2) are kept high all the time.

![](_page_9_Figure_2.jpeg)

**Figure 68 Flow diagram reaction on SMU signal, error shorter than recovery delay time (ERR signal frequency too high)**

- The ERR signal starts toggling with a frequency of *f*ERR,invalid,HF.
- This is detected as an error as soon as the edge-to-edge time is shorter than the detection time *Δt*DET,HF.
- An interrupt is generated after the detection to indicate the start of the recovery delay time *Δt*REC
- Before *Δt*REC has expired the ERR signal resumes toggling with a valid frequency.
- The safe state signals 1 (at pin SS1) and 2 (at pin SS2) are kept high all the time.

## **12.4 Reaction On Error Triggered State Transitions**

The reset output (ROT) indicates the behavior of the microcontroller related regulators (for details please refer to chapter voltage monitoring and reset function).

![](_page_10_Figure_3.jpeg)

**Figure 69 Flow diagram reaction on an error triggered state transition- soft reset**

### Description:

- The falling edge of ROT signal indicates an error
- Safe state signal 1 (at pin SS1) goes to low immediately with the occurrence of the error
- Safe state signal 2 (at pin SS2) goes to low after a delay time *Δt*SS2 which was set by SPI command
- Please mind that in case of an UV event on QUC, a delayed SS2 signal will follow *V*QUC as it is supplied from QUC.

![](_page_10_Figure_10.jpeg)

**Figure 70 Flow diagram reaction on an error triggered state transitions - hard reset**

- The falling edge of ROT signal indicates an error
- Safe state signal 1 (at pin SS1) goes to low immediately with the occurrence of the error
- Safe state signal 2 (at pin SS2) goes to low together with SS1 as the supplying post regulator LDO\_µC is switched off when pin ROT goes to low

## **12.5 Reaction On Window Watchdog Output (WWO)**

The TLF35584 has an implemented window watchdog failure counter (**WWDSTAT**.**WWDECNT**). The counter increments by two at every invalid window watchdog triggering and decrements by one at every valid window watchdog triggering. (For specification of valid and invalid triggering please refer to chapter functional and window watchdog).

The status of the window watchdog failure counter is written in the so called window watchdog status counter. Any incrementation of the window watchdog status counter is indicated by an interrupt. Any decrementation of the window watchdog status counter is not indicated by an interrupt. The content of the window watchdog status counter cannot be less than zero.

The threshold for activating the safe state signals SS1 and SS2 ΣWWO can be changed in INIT, NORMAL and WAKE state. (**WDCFG0**.**WWDETHR**)

The content of the status counter will be compared to the programmed threshold ΣWWO (**RWDCFG0**.**WWDETHR**). If the content of the status counter is equal or higher than ΣWWO, the safe state signals SS1 and SS2 will be activated (low).

![](_page_11_Figure_6.jpeg)

**Figure 71 Flow diagram reaction on WWO**

- The threshold ΣWWO is set to 6 (example)
- An invalid watchdog triggering increments the window watchdog status counter by two, this is indicated by an interrupt
- A valid watchdog triggering decrements the window watchdog status counter by one, this is not indicated by an interrupt
- The status counter value 7 is recognized as an error

- Safe state signal 1 (at pin SS1) goes to low immediately with the counter status change
- Safe state signal 2 (at pin SS2) goes to low after a delay time *Δt*SS2 which was set by SPI command

### **12.6 Reaction On Functional Watchdog Output (FWO)**

The TLF35584 has an implemented functional watchdog failure counter (**FWDSTAT1**.**FWDECNT**). The counter increments by two at every invalid functional watchdog triggering and decrements by one at every valid functional watchdog triggering. (For specification of valid and invalid triggering please refer to chapter functional and window watchdog).

The status of the functional watchdog failure counter is written in the so called functional watchdog status counter. Any incrementation of the functional watchdog status counter is indicated by an interrupt. Any decrementation of the functional watchdog status counter is not indicated by an interrupt. The content of the functional watchdog status counter cannot be less than zero.

The threshold for activating the safe state signals SS1 and SS2 ΣFWO can be changed in INIT, NORMAL and WAKE state. (**WDCFG1**.**FWDETHR**)

The content of the status counter will be compared to the programmed threshold ΣFWO (**RWDCFG1**.**FWDETHR**). If the content of the status counter is equal or higher than ΣFWO, the safe state signals SS1 and SS2will be activated (low).

![](_page_12_Figure_8.jpeg)

**Figure 72 Flow diagram reaction on FWO**

- The threshold ΣFWO is set to 6 (example)
- An invalid watchdog triggering increments the functional watchdog status counter by two, this is indicated by an interrupt

- A valid watchdog triggering decrements the functional watchdog status counter by one, this is not indicated by an interrupt
- The status counter value 7 is recognized as an error
- Safe state signal 1 (at pin SS1) goes to low immediately with the counter status change
- Safe state signal 2 (at pin SS2) goes to low after a delay time *Δt*SS2 which was set by SPI command

## **12.7 Reaction On Thermal Shutdown (TSD)**

The thermal shutdown (TSD) indicates temperature overstress: on the chip: As a consequence all pre and post regulators will be shut down immediately.

![](_page_13_Figure_7.jpeg)

**Figure 73 Flow diagram reaction on TSD**

- The rising edge of TSD signal (internal) is recognized as an error
- Safe state signal 1 (at pin SS1) goes to low immediately with the rising edge of TSD
- Safe state signal 2 (at pin SS2) goes to low together with SS1 as the supplying post regulator LDO\_µC is switched off when pin ROT goes to low