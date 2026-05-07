# **15 Window Watchdog And Functional Watchdog**

## **15.1 Introduction**

Two independent types of watchdogs are implemented in the TLF35584:

- A standalone window watchdog (WWD) with programmable input trigger signal (either pin WDI or trigger via SPI command to **WWDSCMD** register)
- A standalone functional or question/answer watchdog (FWD).

The watchdogs have independent timers and error counters, which allows to run both watchdogs in parallel.

![](_page_0_Figure_7.jpeg)

**Figure 78 Window watchdog and functional watchdog**

#### Description:

- The functional watchdog is not synchronized to the window watchdog, both are fully independent.
- The functional watchdog and the window watchdog can be activated and deactivated independently.
- The result of the watchdogs (valid or invalid triggering) are monitored independently by the related watchdog failure counters.
- The status of the window watchdog is WWO, it may have the values "Valid WWD triggering" or "Invalid WWD triggering"
- The status of the functional watchdog is FWO, it may have the values "Valid FWD triggering" or "Invalid FWD triggering
- The influence of the settings of both watchdogs on safe state control is described in chapter safe state control for better understanding

# **15.2 Window Watchdog**

### **Principle of Operation**

The window watchdog is integrated in the TLF35584 to monitor the microcontroller. The microcontroller that is being monitored has to provide periodical triggering within the "Open Windows". A triggering can consist of a falling edge on the WDI pin or writing to the register **WWDSCMD** by an SPI command depending on the configuration. This triggering terminates the "Open Window". The watchdog output indicates a "Valid" or "Invalid" WWD triggering to the WWD failure counter. In case of a "Valid" triggering a "Closed Window" is started.In case there is no triggering during the "Open Window" or a triggering during a "Closed Window", the watchdog output indicates an "Invalid WWD triggering" to the WWD failure counter and a new "Open Window" is started.

In case the microcontroller is not able to trigger the window watchdog with a correct timing, it is assumed that the microcontroller doesn't work as expected. The microcontroller will get informed by the TLF35584 and a reset in case of multiple failure events.

#### **Configuration**

The following parameters of the window watchdog can be configured in INIT, NORMAL and WAKE state:

- The triggering can be set either to pin triggering (pin WDI) or triggering via SPI command (register **WWDSCMD**). The default configuration is the triggering via SPI.
- The length of open and closed window can be modified according to the application needs by SPI. (combination of cycle time **WDCYC** and number of cycles for open **OW** and closed **CW** window)
- The threshold for the window watchdog failure counter overflow can defined by SPI

#### **Initialization**

The window watchdog will become active in INIT state as soon as reset output pin ROT turns from low to high. After activation the watchdog opens a so called "Long Open Window" (LOW) of duration of *t*LOW. During the "Long Open Window" the window watchdog expects a valid triggering, which has to be provided via SPI in case the default configuration is kept, since any signal to watchdog trigger pin WDI is ignored. This is to avoid wrong triggering at pin WDI due to glitches at the micro controller outputs during startup and initialization.

The microcontroller can change the configuration of the window watchdog during the "Long Open Window" to change the trigger selection as well as the times for the "Open" and "Closed Window". With a reconfiguration the window watchdog will be restarted with the new configuration. A "Open Window" will be started accordingly, expecting a valid triggering by the selected triggering input.

If no valid triggering or configuration of the watchdog takes place during the "Long Open Window", the window watchdog recognizes an "invalid WWD triggering". If the INIT timer expires with an invalid WWD triggering present, a so-called "Soft Reset" will be issued. After the so-called "Soft-Reset" the window watchdog opens a new "Long Open Window". This is not indicated by interrupt. The repetition of "Long Open Windows" is limited. Should within the second "Long Open Window" the window watchdog not be triggered correctly, a normal or "hard" reset will occur, which means that pin ROT goes to zero and the post regulator output voltages will be switched off. After the third "Long Open Window" without valid triggering in a row the state machine will bring the device into "FAILSAFE state (for details please refer to chapter State machine).

#### **Normal Operation**

A trigger signal within the "Long Open Window" will terminate the "Long Open Window" and start the "Closed Window". The "Closed Window" has a fixed duration for operation without invalid triggering.. During normal operation no valid trigger signal is allowed during the "Closed Window". If a valid trigger signal is received within the "Closed Window", the window watchdog recognizes "invalid WWD triggering". The "Closed Window" will be terminated with this invalid triggering and an "Open Window" will be started.

An "invalid WWD triggering" will increment the window watchdog failure counter by two. This is indicated by interrupt.

After the "Closed Window" has ended, the window watchdog starts an "Open Window".

Within the "Open Window" a valid trigger signal is expected. If a valid trigger signal is received within the "Open Window" the watchdog terminates the "Open Window" and starts the "Closed Window". "Valid WWD triggering" will decrement the window watchdog failure counter by one in case it is greater than zero, this is not indicated by interrupt.

If no valid triggering should be received during the "Open Window", the window watchdog recognizes "Invalid WWD triggering" and increments the window watchdog failure counter by two and a new "Open Window" is started. This is indicated by interrupt.

In normal operation, the watchdog continues to cycle between the "Open Window" and "Closed Window" as long as valid triggering is received.

### **Window watchdog output WWO**

The window watchdog output WWO is an internal signal: It is connected to the safe window watchdog failure counter. The value of WWO is either "Valid WWD triggering" or "Invalid WWD Triggering".

![](_page_2_Figure_9.jpeg)

**Figure 79 Watchdog state diagram**

#### Description:

- "Trigger" is either a SPI command to **WWDSCMD** register or a valid watchdog trigger at pin WDI
- "No Trigger" in the "Long open Window" is considered as "Invalid WWD triggering", the watchdog opens again a "Long Open Window"
- "Trigger" within the "Long Open Window" is considered as "Valid WWD triggering", the watchdog closes the "Long Open Window" and opens the "Closed Window"
- "Trigger" within the "Closed Window" is considered as "Invalid WWD triggering"

- "No Trigger" within the "Closed Window" moves the watchdog to the "Open Window", after the "Closed Window" has ended.
- "Trigger" within the "Open Window" is considered as "Valid WWD triggering", the watchdog closes the "Open Window" and opens the "Closed Window"
- "No Trigger" in the "Open Window" is considered as "Invalid WWD triggering",.

#### **Window watchdog trigger pin WDI**

The watchdog input pin WDI has an integrated pull-down current *I*WDI. The watchdog input WDI can transition to high within the "Closed Window" or during the following "Open Window".

#### **Valid Trigger Signal at WDI**

Watchdog input WDI is periodically sampled with a period of *T*SAM. A valid trigger signal is a falling edge from *V*WDI,high to *V*WDI,low. To improve immunity against noise or glitches on the WDI input, at least two high samples followed by two low samples are required for a valid trigger signal, the valid triggering is considered with the second consecutive sampling point measuring low signal. For example, if the first three samples (two high one low) of the trigger pulse at pin WDI are inside the "Closed Window" and only the fourth sample (the second low sample) is taken in the "Open Window" then the watchdog output WWO will indicate "valid WWD triggering".

#### **Invalid Triggering at WDI**

No trigger signal detected during the "Open Window" or a trigger signal detected during the "Closed Window", is considered invalid triggering. Watchdog output WDO indicates "invalid triggering" immediately after no valid trigger during the "Open Window" or immediately if a trigger signal is detected during the "Closed Window".

![](_page_3_Figure_10.jpeg)

**Figure 80 Valid and invalid trigger pulses at pin WDI**

## **15.2.1 Timing Diagrams**

#### **15.2.1.1 Normal operation: Correct triggering**

![](_page_4_Figure_3.jpeg)

**Figure 81 Normal operation: Correct triggering**

- 1. The "Long Open Window" starts in INIT state if the reset output of ROT (monitoring the microcontroller related voltages) turned high. In case the window watchdog was deactivated in SLEEP, the first Open Window starts with the transition from SLEEP state to WAKE state which is indicated by interrupt. The time of this first Open Window depends on the configured cycle time and is 600 ms (**WDCYC** = 1) or 60 ms (**WDCYC** = 0)
- 2. During the "Long Open Window" valid triggering of the WWD according to the configured trigger selection is expected. The maximum time of the "Long Open Window" is fixed, but it will be terminated as soon as a "Valid WWD triggering" is recognized.
- 3. The window watchdog will enter now the "Closed Window". After receiving this first valid trigger the device will be allowed to move from INIT to NORMAL state or from WAKE to NORMAL state.
- 4. The "Closed Window" has a fixed duration *t*WD,CW (can be determined by SPI command). It starts right after the valid trigger signal, that closes the "Open Window" or the "Long Open Window". During the "Closed Window" no trigger signal should be applied. A transition from low to high at the WDI pin is not detected and will not lead to a trigger event,
- 5. A valid trigger signal terminates the "Open Window" immediately, thus the time of the "Open Window" is variable and depending on the time the microcontrollers schedules the triggering. This is counted as a "Valid WWD triggering"

## **15.2.1.2 Fault operation: No trigger in open window after initialization**

![](_page_5_Figure_2.jpeg)

**Figure 82 Fault operation: No trigger in Open Window after initialization**

- 1. The initialization timeout and the long open window (LOW) do have the same typ. length. Usually this leads to the initialization timeout finishing at the slightly before or at same time as the LOW, which would skip the interrupt event (1). Even though due to the given accuracy, the missing valid triggering within the "Long Open Window" might lead to an interrupt event after the LOW has ended which is increasing the window watchdog failure counter by two.
- 2. The INIT state timer expires for the first time. As no valid triggering of the window watchdog was received during INIT state as expected, a so-called "Soft-Reset" will be issued: Pin ROT goes to zero, but the output voltages of the post regulators remain on. Additional information: In case the window watchdog should not be triggered correctly within the next "Long Open Window" of the following INIT phase, a "Hard-Reset" will be issued, which means pin ROT will go to zero and the output voltages will also be switched off. After a third invalid triggering during INIT phase the device will go into FAILSAFE state.
- 3. After the so-called "Soft-Reset" pin ROT turns high again after the power-on reset delay time *t*rd and the watchdog opens a "Long Open Window" to give the microcontroller the chance to trigger and synchronize to the watchdog period.
- 4. A valid triggering terminates the "Long Open Window", which makes the duration of the "Long Open Window" variable and depending on the triggering. This is counted as a "Valid WWD triggering" and a "Closed Window" is started. The window watchdog failure counter will be decremented by one without an interrupt issued.
- 5. The following "Closed Window" lasts for the time *t*WD,CW. Triggering within this time will be considered as an "Invalid WWD triggering".

## **15.2.1.3 Fault operation: No trigger in Open Window in steady state**

![](_page_6_Figure_2.jpeg)

**Figure 83 Fault operation: No trigger in Open Window in steady state**

- 1. A missing valid triggering within the "Open Window" leads after the window has ended to an "Invalid WWD triggering". This event is indicated by an interrupt, the window watchdog failure counter increases by two.
- 2. Having detected an "Invalid WWD triggering" the watchdog will start a new "Open Window" with duration *t*WD,OW to give the microcontroller the chance to trigger and synchronize to the watchdog period.
- 3. A valid triggering terminates the "Open Window", which makes the duration of the "Open Window" variable and depending on the triggering. This is counted as a "Valid WWD triggering" and a "Closed Window" is started. The window watchdog failure counter will be decremented by one without an interrupt issued. Additional informations: In case of multiple "Invalid WWD triggering" within the "Open Windows", the window watchdog failure counter would be incremented again by two until it reaches the configured threshold. In this case a reset will be issued.
- 4. The following "Closed Window" lasts for the time *t*WD,CW. Triggering within this time will be considered as an "Invalid WWD triggering".

The behavior of pin ROT is depending on the value of ΣWWO. In the example above it was assumed, that the invalid triggering will not lead to exceed the threshold ΣWWO.

## **15.2.1.4 Fault operation: False trigger in Closed Window after initialization**

![](_page_7_Figure_2.jpeg)

**Figure 84 Fault operation: False trigger in Closed Window after initialization**

- 1. A triggering during the "Closed Window" is indicated as "Invalid WWD triggering". This event is indicated by an interrupt and the window watchdog failure counter increases by two.
- 2. The "Closed Window" will be closed with the "Invalid WWD triggering". Originally it would last for the time *t*WD,CW. The false triggering terminates the "Closed Window" and starts an "Open Window" to give the micro processor the opportunity to synchronize to the window watchdog period.
- 3. Within this "Open Window" a valid triggering is expected. A valid triggering terminates the "Open Window", which makes the duration of the "Open Window" variable and depending on the triggering. This is counted as a "Valid WWD triggering" and a "Closed Window" is started. The window watchdog failure counter will be decremented by one without an interrupt issued.
- 4. The following "Closed Window" lasts for the time *t*WD,CW. Triggering within this time will be considered as an "Invalid WWD triggering".

The behavior of pin ROT is depending on the value of ΣWWO. In the example above it was assumed, that the invalid triggering will not lead to exceed the threshold ΣWWO.

## **15.2.1.5 Fault operation: False trigger in Closed Window in steady state**

![](_page_8_Figure_2.jpeg)

**Figure 85 Fault operation: False trigger in Closed Window**

- 1. A triggering during the "Closed Window" is indicated as "Invalid WWD triggering". This event is indicated by an interrupt and the window watchdog failure counter increases by two.
- 2. The "Closed Window" will be closed with the "Invalid WWD triggering". Originally it would last for the time *t*WD,CW. The false triggering terminates the "Closed Window" and starts an "Open Window" to give the micro processor the opportunity to synchronize to the window watchdog period.
- 3. Within this "Open Window" a valid triggering is expected. A valid triggering terminates the "Open Window", which makes the duration of the "Open Window" variable and depending on the triggering. This is counted as a "Valid WWD triggering" and a "Closed Window" is started. The window watchdog failure counter will be decremented by one without an interrupt issued.
- 4. The following "Closed Window" lasts for the time *t*WD,CW. Triggering within this time will be considered as an "Invalid WWD triggering".

The behavior of pin ROT is depending on the value of ΣWWO. In the example above it was assumed, that the invalid triggering will not lead to exceed the threshold ΣWWO.

## **15.2.2 Electrical characteristics**

**Table 25 Electrical Characteristics: Window watchdog function**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                        | Symbol     | Values |      |       | Unit | Note /                           | Number      |
|--------------------------------------------------|------------|--------|------|-------|------|----------------------------------|-------------|
|                                                  |            | Min.   | Typ. | Max.  |      | Test<br>Condition                |             |
| General timing parameters watchdog (WWD and FWD) |            |        |      |       |      |                                  |             |
| Watchdog cycle time                              | tCYCLE     | 94     | 100  | 106.5 | µs   | selectable by SPI<br>command     | P_15.2.2.1  |
| Watchdog cycle time, default<br>setting          | tCYCLE     | 940    | 1000 | 1065  | µs   | selectable by SPI<br>command     | P_15.2.2.2  |
| Long open window time                            | tLOW       | 564    | 600  | 639   | ms   | –                                | P_15.2.2.3  |
| Watchdog input WDI                               |            |        |      |       |      |                                  |             |
| Watchdog sampling time                           | tSAM       | 188    | 200  | 213   | µs   | –                                | P_15.2.2.4  |
| WDI valid high level                             | VWDI, high | 3.6    | –    | –     | V    | VWDI increasing,<br>VQUC = 5.0 V | P_15.2.2.5  |
| WDI valid low level                              | VWDI, low  | –      | –    | 0.8   | V    | VWDI decreasing,<br>VQUC = 5.0 V | P_15.2.2.6  |
| WDI hysteresis                                   | VWDI, hyst | –      | 350  | –     | mV   | VQUC = 5.0 V                     | P_15.2.2.7  |
| WDI valid high level                             | VWDI, high | 2.0    | –    | –     | V    | VWDI increasing,<br>VQUC = 3.3 V | P_15.2.2.8  |
| WDI valid low level                              | VWDI, low  | –      | –    | 0.8   | V    | VWDI decreasing,<br>VQUC = 3.3 V | P_15.2.2.9  |
| WDI hysteresis                                   | VWDI, hyst | –      | 160  | –     | mV   | VQUC = 3.3 V                     | P_15.2.2.10 |
| WDI pull-down current                            | IWDI       | –      | 150  | 330   | µA   | VWDI = VQUC                      | P_15.2.2.11 |
| WDI input capacitance                            | CWDI       | –      | 4    | 15    | pF   | 1)                               | P_15.2.2.12 |

<sup>1)</sup> Specified by design, not subject to production test

# **15.3 Functional Watchdog**

#### **Principle of Operation**

A functional or question/answer watchdog is integrated in the TLF35584 to monitor the microcontroller. In a steady state a question is generated (taken out of table), in parallel the so called heartbeat counter starts counting from zero. The heartbeat counter counts up, until the heartbeat period has ended. The duration of the heartbeat period is set to a default value, but can be adjusted via SPI command. The question consists of 4 bits, the expected answer consists of 4 responses of 8 bits each. The four responses shall be sent before the heartbeat period has ended. The last response shall be written to the synchronized response register to reset the heartbeat counter.

#### **Initialization**

The functional watchdog is off per default when the device is powered up for the first time. It can be enabled by SPI writing to **WDCFG0**.**FWDEN**.

### **Configuration**

The functional watchdog can be configured in INIT, NORMAL and WAKE state. "Configured" means:

- Modify the length of the heartbeat period by SPI command, depending on the needs of the application. (combination of cycle time **WDCYC** and number of cycles for heartbeat **WDHBTP**)
- The threshold for the functional watchdog failure counter overflow can defined by SPI

The heartbeat period is based on the cycle time *t*CYCLE specified in **Table 25**.

### **Normal Operation**

The question is taken out of the **Table 26**, the correct responses are listed in the same row. The sequence of responses must be kept and can be derived from the response counter **FWDSTAT0**.**FWDRSPC** before sending the response.

The response to the actual question defined in the table shall be composed by four subsequent response bytes. A correct response to the given question in **FWDSTAT0**.**FWDQUEST** register shall be done in the following way.

- The first three responses shall be written into **FWDRSP**
- The last response should be written into **FWDRSPSYNC** to reset the heartbeat timer

All four responses must be written before the heartbeat period expires.

If the complete response (32 bits) is correct and if the last response byte was sent with synchronized respond, the heartbeat counter will be reset and set to zero. If the complete answer (all four responses - 32 bits) is correct, it is regarded as "Valid FWD triggering", the functional watchdog error counter ΣFWO is decremented by 1. If the last response was sent with synchronized response, the heartbeat counter will be reset, but if the answer is wrong, this is regarded as "Invalid FWD triggering" and the functional watchdog error counter ΣFWO is incremented by 2.

An overflow of the functional watchdog error counter ΣFWO will trigger a "Move to INIT" event, reset the heartbeat counter and set the functional watchdog error counter ΣFWO to zero.

**Table 26 Functional watchdog response definition** 

| QUESTION | RESP3 | RESP2 | RESP1 | RESP0 |
|----------|-------|-------|-------|-------|
| 0        | FF    | 0F    | F0    | 00    |
| 1        | B0    | 40    | BF    | 4F    |
| 2        | E9    | 19    | E6    | 16    |
| 3        | A6    | 56    | A9    | 59    |
| 4        | 75    | 85    | 7A    | 8A    |
| 5        | 3A    | CA    | 35    | C5    |
| 6        | 63    | 93    | 6C    | 9C    |
| 7        | 2C    | DC    | 23    | D3    |
| 8        | D2    | 22    | DD    | 2D    |
| 9        | 9D    | 6D    | 92    | 62    |
| A        | C4    | 34    | CB    | 3B    |
| B        | 8B    | 7B    | 84    | 74    |
| C        | 58    | A8    | 57    | A7    |
| D        | 17    | E7    | 18    | E8    |
| E        | 4E    | BE    | 41    | B1    |
| F        | 01    | F1    | 0E    | FE    |

#### **Functional watchdog output FWO**

The functional watchdog output FWO is an internal signal: It is connected to the FWD failure counter. The value of the functional watchdog FWO output is either "Valid FWD triggering" or "Invalid FWD Triggering".

![](_page_12_Figure_1.jpeg)

Figure 86 Functional watchdog flowchart diagram

# **15.3.1 Timing Diagrams**

## **15.3.1.1 Normal operation: Correct triggering**

![](_page_13_Figure_3.jpeg)

**Figure 87 Normal operation: Correct triggering**

- 1. A new question is generated, in parallel the heartbeat counter starts counting up (It is assumed, that a "Valid FWD triggering" has happened before).
- 2. A correct response is received (RESP3)
- 3. A correct response is received (RESP2)
- 4. A correct response is received (RESP1)
- 5. A correct synchronized response is received (RESP0). All responses are correct, the sequence of responses is correct and the last synchronized response was received before the heartbeat counter overflowed. The heartbeat counter will be reset (set to zero). This is regarded as "Valid FWD triggering", the functional watchdog error counter ΣFWO is decremented by 1 (if the functional watchdog error counter value is higher than zero).
- 6. A new question is generated, in parallel the heartbeat counter starts counting up

## **15.3.1.2 Fault operation: Synchronization is missing**

![](_page_14_Figure_2.jpeg)

**Figure 88 Fault operation: Synchronization is missing**

- 1. A new question is generated, in parallel the heartbeat counter starts counting up (It is assumed, that a "Valid FWD triggering" has happened before).
- 2. A correct response is received (RESP3)
- 3. A correct response is received (RESP2)
- 4. A correct response is received (RESP1)
- 5. A correct response is received (RESP0), but not synchronized (written in wrong register). So far, all responses are correct, the sequence of responses is correct and the last not synchronized response was received before the heartbeat counter overflow occurred. The heartbeat counter will not be reset and continue to count. This is regarded as "Valid FWD triggering", the functional watchdog error counter ΣFWO is decremented by 1 (if the functional watchdog error counter value is higher than zero). A new question is generated.
- 6. The heartbeat counter is still counting up, waiting for the answer on the new question. Later in time the heartbeat counter will expire and an overflow occurs. This is regarded as "Invalid FWD triggering". The functional watchdog error counter ΣFWO is incremented by 2. The heartbeat counter is reset.
- 7. The heartbeat counter starts counting up. No new question is generated.

## **15.3.1.3 Fault operation: Answer is wrong**

![](_page_15_Figure_2.jpeg)

**Figure 89 Fault operation: Answer is wrong**

- 1. A new question is generated, in parallel the heartbeat counter starts counting up (It is assumed, that a "Valid FWD triggering" has happened before)
- 2. A correct response is received (RESP3)
- 3. A correct response is received (RESP2)
- 4. An incorrect response is received (RESP1)
- 5. A correct response is received (RESP0). The heartbeat counter will be reset (set to zero). The complete answer is not correct. This is regarded as "Invalid FWD triggering". The functional watchdog error counter ΣFWO is incremented by 2. The heartbeat counter is reset.
- 6. No new question is generated, but the heartbeat counter starts counting up.

Note: If i.e. RESP2 and RESP1 would be mixed, than both responses would be regarded as incorrect - the responses have to be sent in correct order.

## **15.3.1.4 Fault operation: Missing response**

![](_page_16_Figure_2.jpeg)

**Figure 90 Fault operation: Answer is not complete**

- 1. A new question is generated, in parallel the heartbeat counter starts counting up (It is assumed, that a "Valid FWD triggering" has happened before).
- 2. A correct response is received (RESP3)
- 3. A correct response is received (RESP2)
- 4. A response is missing (RESP1)
- 5. A correct response is received (RESP0). So the last response is not the last response but the second last due to the missing response (in this example RESP1). The functional watchdog will wait for all four responses to be written, while the heartbeat counter keeps on counting. There is no fixed time for all four responses, but they must be sent in correct order before the heartbeat counter expires.
- 6. The complete answer is not correct due to missing response RESP1. Although the last response is synchronized, the heartbeat counter will not be reset and continue counting up until an overflow occurs. This is regarded as "Invalid FWD triggering". The functional watchdog error counter ΣFWO is incremented by 2. The heartbeat counter is reset.
- 7. No new question is generated and the heartbeat counter starts counting up.