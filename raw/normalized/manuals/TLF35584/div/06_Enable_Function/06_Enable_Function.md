# 6 Pre Regulators

#### 6.1 Introduction

The pre regulator is mandatory to maintain a stabilized and constant intermediate circuit voltage to supply the following post regulators. It consists of two independent regulators: A step up converter with an external power stage in front to maintain a minimum input voltage to the following step down converter.

The step up converter can be deactivated (if not needed) by connecting pin STU to ground. Leaving pin STU open activates the step up regulator.

The step down regulator frequency can be preset by leaving pin FRE open for the high switching frequency range or connecting to GND for the low switching frequency range.

The step down converter is constantly on, providing a stabilized intermediate circuit voltage  $V_{\rm PREREG}$  to supply the following post regulators. The step up converter is connected directly to the input voltage  $V_{\rm Bat}$ . It only operates during low input voltage condition (i.e. cranking) when the input voltage drops below the threshold  $V_{\rm PRE\_REG,boost,UV}$ , to maintain an input voltage high enough for the following step down regulator. Low input voltage condition means, that the input voltage at pin VSx is too low to provide an intermediate circuit voltage  $V_{\rm PREREG}$  within the specified limits. An internal comparator connected to the input voltage path detects the threshold when to turn on the step up converter. In case the input voltage is above the step up converter output voltage (threshold for switching on the step up converter), this regulator is deactivated by the internal comparator. An internal logic switches the step up converter on (and off again) whenever it is needed.

![](_page_0_Figure_7.jpeg)

Figure 7 Principle pre regulator stage

# **6.2 Step Up Regulator**

### **6.2.1 Functional description**

The asynchronous step up pre regulator provides a higher output voltage than the input voltage when operating. This will be the case whenever the supply voltage should be too low to allow nominal values at the post regulator outputs. The boost pre regulator output voltage will be well below the nominal supply (battery) voltage to make sure, that he only operates during low input voltage conditions.

If the step up feature should not be necessary for the application, the external power elements (Mosfet, diode) could be skipped, the filter elements might be adjusted to the application requirements.

![](_page_1_Figure_5.jpeg)

**Figure 8 Step Up Regulator**

# **6.2.2 Electrical characteristics**

**Table 7 Electrical Characteristics: Step up regulator**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                   | Symbol                      | Values |      |      | Unit | Note /                               | Number     |
|---------------------------------------------|-----------------------------|--------|------|------|------|--------------------------------------|------------|
|                                             |                             | Min.   | Typ. | Max. |      | Test<br>Condition                    |            |
| Step up pre regulator                       |                             |        |      |      |      |                                      |            |
| Pre regulator boost output<br>voltage       | VPRE_REG,boo<br>st          | 7.00   | 7.5  | 8.00 | V    | –                                    | P_6.2.2.1  |
| Threshold external sense<br>resistor for OC | VRSH-RSL                    | 190    | 210  | 230  | mV   | –                                    | P_6.2.2.2  |
| Low side sense input current                | IRSL                        | -120   | -60  | -30  | µA   | VRSL<br>=0V                          | P_6.2.2.3  |
| High side sense input current               | IRSH                        | -45    | -30  | -15  | µA   | tested at VRSH<br>=0V                | P_6.2.2.4  |
| Input under voltage threshold               | VPRE_REG,boo<br>st,UV       | 8      | 8.3  | 8.6  | V    | –                                    | P_6.2.2.5  |
| Input under voltage threshold<br>hysteresis | VPRE_REG,boo<br>st,UV, hyst | 80     | –    | 200  | mV   | –                                    | P_6.2.2.6  |
| Gate driver peak sourcing<br>current        | IDRG,SRC                    | –      | 130  | –    | mA   | 1)                                   | P_6.2.2.7  |
| Gate driver peak sinking<br>current         | IDRG,SNK                    | –      | 100  | –    | mA   | 1)                                   | P_6.2.2.8  |
| Gate driver output rise time                | tR,DRG                      | 12     | –    | 150  | ns   | 10% to 90%<br>CDRG<br>=<br>470<br>pF | P_6.2.2.9  |
| Gate driver output fall time                | tF,DRG                      | 12     | –    | 150  | ns   | 90% to 10%<br>CDRG<br>=<br>470<br>pF | P_6.2.2.10 |
| Gate driver output voltage                  | VDRG                        | 4.5    | 5    | 5.5  | V    | –                                    | P_6.2.2.11 |
| Maximum Duty Cycle                          | DMAX                        | 75     | 95   | –    | %    | –                                    | P_6.2.2.12 |
| Blanking time                               | tBlank                      |        | 240  |      | ns   | –                                    | P_6.2.2.13 |

<sup>1)</sup> Specified by design, not subject to production test.

# **6.3 Step Down Regulator**

### **6.3.1 Functional description**

The synchronous step down pre regulator is continuously in operation providing a stable intermediate circuit voltage to supply the following post regulators. The internal power stage consists of synchronous P-channel (high side) and N-channel (low side) Mosfets. For startup a soft start function is implemented.

The regulation loop operates in voltage mode.

Under normal load conditions the regulator operates in Pulse Width Modulation (PWM). Under light load conditions it will operate in Pulse Frequency Modulation (PFM) to minimize the internal current consumption (only in SLEEP state, not in NORMAL, WAKE or INIT state).

The output filter of the step down regulator has to be sized to ensure a maximum output voltage ripple of 100 mV in order to be in line with the PSRR specified for the post regulators.

![](_page_3_Figure_7.jpeg)

**Figure 9 Step Down Regulator**