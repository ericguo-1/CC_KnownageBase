# **5 Wake Function**

# **5.1 Introduction**

The TLF35584 is automatically turned on when connected to a battery (Power-On-Reset POR) and moves into INIT-state, where the device will be configured. After successful configuration, the device will be sent to NORMAL state via SPI command. From NORMAL or WAKE state, the device can be sent to a low power state (SLEEP or STANDBY) via SPI commands. The WAK and ENA signal are external triggers to leave the low power states (or the FAILSAFE state).

### **Wake (pin WAK - level triggered) / Enable (pin ENA - edge triggered)**

The WAK and ENA input pins are battery voltage level capable. A signal, with a voltage higher than VWAK,hi applied at pin WAK for *t*WAK,min represents a valid Wake-Signal. A positive going edge at pin ENA with a rise time *t*ENA,rise represents a valid Wake-Signal as well.

A valid Wake-Signal will bring the device from STANDBY to INIT state, from SLEEP to WAKE state or from FAILSAFE to INIT state.

A low signal VWAK,lo at pin WAK as well as a negative going edge at pin ENA will have no impact on the state machine and will not initiate a transition between states.

In case a valid Wake-Signal is detected during the transition phase from NORMAL to SLEEP state, the device will initiate a transition to WAKE state and generate an interrupt.

In case a valid Wake-Signal is detected during the transition phase from NORMAL to STANDBY state, the device will initiate a transition to INIT state and a Reset (ROT) will be generated.

Before sending a SPI transition command, pin ENA doesn't have to be brought below VENA,thrlo. Even if pin ENA is high (above VENA,thrhi), the SPI transition command will still send the device into SLEEP or STANDBY state.

For further details please refer to **Chapter 11 State Machine**.

![](_page_0_Figure_12.jpeg)

**Figure 4 Principle of the enable function**

# **5.2 Electrical Characteristics Enable Signal**

![](_page_1_Figure_2.jpeg)

**Figure 5 Valid enable signal**

### **Table 5 Electrical Characteristics: Enable signal**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                           | Symbol     | Values |      |      | Unit | Note /            | Number  |
|-------------------------------------|------------|--------|------|------|------|-------------------|---------|
|                                     |            | Min.   | Typ. | Max. |      | Test<br>Condition |         |
| Enable EN                           |            |        |      |      |      |                   |         |
| Enable upper threshold              | VENA,thrhi | –      | –    | 2.00 | V    | VENAincreasing    | P_5.2.1 |
| Enable lower threshold              | VENA,thrlo | 0.8    | –    | –    | V    | VENA decreasing   | P_5.2.2 |
| Enable threshold hysteresis         | VENA,hyst  | –      | 400  | –    | mV   | -                 | P_5.2.3 |
| Enable signal, rise time            | tENA,rise  | –      | –    | 10   | µs   | –                 | P_5.2.4 |
| Enable signal, minimum high<br>time | tENA,high  | 20     | –    | –    | µs   | –                 | P_5.2.5 |
| Enable high input current           | IENA,hi    | –      | 8    | 11   | µA   | VENA = 16 V       | P_5.2.6 |
| Enable low input current            | IENA,lo    | –      | 0.1  | 2    | µA   | VENA = 0.5 V      | P_5.2.7 |

### **5.3 Electrical Characteristics Wake Signal**

![](_page_2_Figure_2.jpeg)

**Figure 6 Valid wake signal**

#### **Table 6 Electrical Characteristics: Wake signal**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                   | Symbol    | Values |      |      | Unit | Note /            | Number  |
|-----------------------------|-----------|--------|------|------|------|-------------------|---------|
|                             |           | Min.   | Typ. | Max. |      | Test<br>Condition |         |
| Wake/Inhibit                |           |        |      |      |      |                   |         |
| Wake upper threshold        | VWAK,hi   | –      | –    | 2.00 | V    | VWAK increasing   | P_5.3.1 |
| Wake lower threshold        | VWAK,lo   | 0.8    | –    | –    | V    | VWAK decreasing   | P_5.3.2 |
| Wake signal hysteresis      | VWAK,hyst | –      | 400  | –    | mV   | –                 | P_5.3.3 |
| Wake signal, minimum length | tWAK,min  | 40     | –    | –    | µs   | –                 | P_5.3.4 |
| Wake high input current     | IWAK,hi   | –      | 8    | 11   | µA   | VWAK = 5.0V       | P_5.3.5 |
| Wake low input current      | IWAK,lo   | –      | 0.1  | 2    | µA   | VWAK = 0.5V       | P_5.3.6 |

# **5.4 Typical Performance Characteristics**

### **Enable Input Threshold Voltage** *V***ENA,th versus Junction Temperature** *T***<sup>j</sup>**

![](_page_3_Figure_3.jpeg)

# **Wake Input Threshold Voltage** *V***WAK,th versus Junction Temperature** *T***<sup>j</sup>**

![](_page_3_Figure_5.jpeg)