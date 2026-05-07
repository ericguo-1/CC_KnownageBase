# **13 SPI - Serial Peripheral Interface**

## **13.1 Introduction**

### **Main functions**

The serial peripheral interface bus or SPI bus is a synchronous serial data link that operates in full duplex mode. The TLF35584 communicates in slave mode where the master (µC) initiates the data frame. The TLF35584 should be addressed via a dedicated chip select line. This allows a connection of other slave devices to the SPI bus.

### **Data transmission**

To begin a communication, the µC first configures the clock, using a frequency less than or equal to the maximum frequency the TLF35584 supports. The µC pulls down the chip select for the TLF35584.

### **Functional description**

SPI basic access: All data on MOSI (pin SDI) is captured on the rising edge of SPI clock signal (pin SCL) and shifted on the falling edge of SPI clock signal (pin SCL). The same methodology needs to be applied in the SPI master for MISO (SDO). A read operation has to start with CMD-bit being 1'b0 and a write operation has to start with CMD-bit being 1'b1.

In case of a write operation is performed the written command to SDI is looped back to SDO.

The parity is calculated for the output data stream in case a read operation is performed. The data for the calculation consists of 1'b1, status [5:0] and rd\_data[7:0]. The parity bit is set to '1' if the number of '1' in the output data stream is odd, i.e.XOR function between all 15 bits to send out.

Parity is checked on write data. The parity is calculated on the incoming bit stream for the cmd bit, the six address bits and the eight data bits.

Configuration via SPI can be done anytime, if the state machine (FSM) is in INIT state, NORMAL state, WAKE state or SLEEP state. During SLEEP state the SPI has a decreased maximum clock frequency, for details please refer to **Table 19**.

SPI access timing can be found in the following diagram:

![](_page_0_Figure_14.jpeg)

**Figure 74 SPI - frame in normal mode**

SPI MISO:

- During write, data from MOSI is directly looped back, during read, the addressed register content will be provided in the very same SPI frame
- The cmd bit is always set to 1'b1. All other status bits are set to zero.

![](_page_1_Figure_3.jpeg)

**Figure 75 SPI - Timings**

### **Table 19 Electrical Characteristics: SPI - Timings**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                          | Symbol      | Values |      |               | Unit | Note /                                                                          | Number    |
|------------------------------------|-------------|--------|------|---------------|------|---------------------------------------------------------------------------------|-----------|
|                                    |             | Min.   | Typ. | Max.          |      | Test<br>Condition                                                               |           |
| CLK_SPI Operating<br>Frequency     | fSPI_clk    | –      | –    | 10            | MHz  | 1)                                                                              | P_13.1.1  |
| CLK_SPI Operating<br>Frequency     | fSPI_clk    | –      | –    | 1.5           | MHz  | SLEEP state                                                                     | P_13.1.2  |
| CLK Signal duty cycle              | DSCL        | 45     | 50   | 55            | %    |                                                                                 | P_13.1.3  |
| CLK_SPI Operating<br>Period        | tSPI_clk    | 100    | –    | –             | ns   |                                                                                 | P_13.1.4  |
| CLK_SPI High Time                  | tSPI_wsclkh | 45     | –    | –             | ns   |                                                                                 | P_13.1.5  |
| CLK_SPI Low Time                   | tSPI_wsclkl | 45     | –    | –             | ns   |                                                                                 | P_13.1.6  |
| CLK_SPI Fall Time                  | tSPI_clkf   | –      | –    | 0.1*tSPI_fact | [ns] | tSPI_fact<br>tSPI_clk<br>≤<br>;<br>tSPI_fact<br>100<br>ns<br>≤<br>≤<br>1<br>µs  | P_13.1.7  |
| CLK_SPI Rise Time                  | tSPI_clkr   | –      | –    | 0.1*tSPI_fact | [ns] | tSPI_fact<br>tSPI_clk<br>≤<br>;<br>tSPI_fact<br>100<br>ns<br>≤<br>≤<br>1<br>µs  | P_13.1.8  |
| CLK_SPI Lead Time                  | tSPI_lead   | 100    | –    | –             | ns   |                                                                                 | P_13.1.9  |
| CLK_SPI Lag Time                   | tSPI_lag    | 50     | –    | –             | ns   |                                                                                 | P_13.1.10 |
| SPI Chip Select (SCS)<br>Rise Time | tSPI_csr    | –      | –    | 0.2*tSPI_fact | [ns] | tSPI_fact<br>tSPI_lag<br>≤<br>;<br>tSPI_fact<br>50<br>ns<br>≤<br>≤<br>500<br>ns | P_13.1.11 |

**Table 19 Electrical Characteristics: SPI - Timings** (cont'd)

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                                    | Symbol   | Values |      |                        | Unit | Note /                                                                                                      | Number    |
|----------------------------------------------|----------|--------|------|------------------------|------|-------------------------------------------------------------------------------------------------------------|-----------|
|                                              |          | Min.   | Typ. | Max.                   |      | Test<br>Condition                                                                                           |           |
| SPI Chip Select (SCS)<br>Fall Time           | tSPI_csf | –      | –    | 0.2*tSPI_fact          | [ns] | tSPI_fact<br>tSPI_lead;<br>≤<br>tSPI_fact<br>100<br>ns<br>≤<br>≤<br>1<br>µs                                 | P_13.1.12 |
| SPI Data Input (SDI)<br>Setup                | tSPI_su  | 10     | –    | –                      | ns   |                                                                                                             | P_13.1.13 |
| SPI Data Input (SDI)<br>Hold Time            | tSPI_hi  | 10     | –    | –                      | ns   |                                                                                                             | P_13.1.14 |
| SPI Data Output (SDO)<br>Valid after CLK_SPI | tSPI_v   | –      | –    | (0.1*tSPI_fact)<br>+36 | [ns] | CSDO,load=<br>50<br>pF;<br>tSPI_fact<br>tSPI_clkf<br>≥<br>;<br>tSPI_fact<br>10<br>ns<br>≤<br>≤<br>100<br>ns | P_13.1.15 |
| SPI Write Propagation<br>Delay SDI to SDO    | tSPI_wpd | –      | –    | 35                     | ns   |                                                                                                             | P_13.1.16 |
| SPI Data Output (SDO)<br>Access              | tSPI_a   | –      | –    | 50                     | ns   | CSDO,load = 50<br>pF                                                                                        | P_13.1.17 |
| SPI Data Output (SDO)<br>Disable Time        | tSPI_dis |        | –    | 100                    | ns   | CSDO,load = 50<br>pF                                                                                        | P_13.1.18 |
| Sequential Transfer<br>Delay                 | tSPI_td  | 350    | –    | –                      | ns   |                                                                                                             | P_13.1.19 |
| Sequential Transfer<br>Delay                 | tSPI_td  | 2      | –    | –                      | µs   | SLEEP state                                                                                                 | P_13.1.20 |
| Frame duration (SCS<br>low)                  | tSPI_fl  |        | –    | 1.85                   | ms   |                                                                                                             | P_13.1.21 |

<sup>1)</sup> For max. achievable CLK\_SPI operating frequency, please consider the CLK\_SPI rise- and fall times (*t*SPI\_clkr and *t*SPI\_clkf).

#### SPI errors:

- Wrong parity bit during write, write data is ignored.
- Write to invalid address, write data is ignored.
- Wrong number of SPI clock cycles while SCS is low, write data is ignored, read data is provided by the device with each SPI clock cycle.
- Read from invalid address (all data bits zero returned on MISO for read data). For this case the parity bit is inverted/corrupted after complete calculation by the device.
- Invalid frame duration, write data is ignored and the output driver for SDO is turned off internally by the device after *t*SPI\_fl. Read data is provided with each SPI clock cycle as long as SCS is low for less than *t*SPI\_fl.
- If the number of SPI clock cycles is different than 16 and an invalid frame duration error is detected by the device, the invalid frame duration status flag is set and the wrong number of SPI clock cycle status flag is set.

In case of an SPI error occurs, an interrupt will be generated.

Interrupts on SPI errors are initiated only after SCS has been driven high or the frame time-out occurred.

## **13.2 SPI Write Access To Protected Registers**

Certain internal registers (**SYSPCFG0**, **SYSPCFG1**, **WDCFG0**, **WDCFG1**, **FWDCFG**, **WWDCFG0**, **WWDCFG1**) need to be protected against being overwritten accidently. The status of the protection can be checked by reading the **LOCK** bit in the register **PROTSTAT**.

Write access to these registers is only possible after a dedicated 32 bit UNLOCK sequence has been sent via SPI. The four bytes need to be send without any other SPI write access in between. Error in doing so will reset the sequence detection, i.e. a new UNLOCK sequence has to be send. An interrupt is generated and the number of successfully detected UNLOCK sequence bytes is set to zero if a write access to any other register then **PROTCFG** is detected in between. The access to the protected registers is possible in INIT, NORMAL and WAKE state.

The UNLOCK sequence consists of a 32-bit sequence of 4 consecutive bytes (1: 0xAB; 2:0xEF; 3:0x56; 4:0x12) which have to be sent with no other SPI write access in between. The correctness of every written byte can be checked by reading the register **PROTSTAT**. Once the UNLOCK sequence has been performed successfully, any protected configuration request register can be written. In order to ensure proper writing to the protected configuration request registers the microcontroller shall read back the register values and verify the correctness by checking data. The data bits written to the protected configuration request registers are send back inverted during read operation, that means the microcontroller can calculate an XOR of the register data read and expected. The results should be 0xFF in case of correct register data. The TLF35584 will not check the correctness of the values in the register.

All protected configuration request register values are captured by the respective functions only after a successful LOCK sequence has been performed. A successful LOCK sequence consists of a 32-bit sequence of 4 consecutive bytes (1: 0xDF; 2:0x34; 3:0xBE; 4:0xCA) which have to be send with no other SPI write access in between. The correctness of every written byte can be checked by reading the register **PROTSTAT**.

Error in doing so will reset the sequence detection, i.e. a new LOCK sequence has to be sent. In this case (any SPI write access in between LOCK sequence) an interrupt is generated.

Upon detection of a successful LOCK sequence the configuration registers and all internal functions are updated with the values from the protected configuration request registers. It is the responsibility of the uC to ensure all registers are configured properly by either writing a new value into a particular register or by reading back a register which is supposed to be unchanged. Partial reconfiguration of the protected registers, i.e. configuring just a single function and leaving other functions unchanged is not supported as with the successful LOCK sequence all protected configuration request registers are taken over into the configuration (**RSYSPCFG0**, **RSYSPCFG1**, **RWDCFG0**, **RWDCFG1**, **RFWDCFG**, **RWWDCFG0**, **RWWDCFG1**).

After the LOCK sequence an internal configuration time of max. 60 µs has to be considered to ensure that the new configuration is taken over.

#### Affected functions:

- All watchdog configuration registers for WWD and FWD.
- Enabling of WD while the device is in SLEEP state
- All Error pin monitoring configuration registers
- Enabling of Error pin monitoring while the FSM is in SLEEP
- A dedicated register to enable or disable the STDBY LDO
- Configuration of SS2 delay time failure events not leading to FAILSAFE state

Read access to any protected configuration request register is always possible.

## **13.3 SPI Write Initiated State Transition Request And Regulator Configuration**

A State machine transition can be initiated via SPI command(s). In case the state of any selectable voltage source (post regular) is expected to change for the next state, this information has to be sent together with the command into the same register. In case the setting for a particular voltage source (post regulator) is supposed to change but the state needs to be unchanged, the same approach can be applied. This basically means, the SPI command contains the current state of the FSM but a different setting for configurable voltage source (post regulator).

In order to request a state transition and/or a change of the LDO configuration the request data have to be written to two separated registers **DEVCTRL** and **DEVCTRLN** after each other consequently. The data written to DEVCTRLN have to be inverted bitwise compared to the data written to DEVCTRL. The request will be only accepted when the two registers are written consecutively after each other (first **DEVCTRL** and second **DEVCTRLN**) and will be taken over with the rising edge of the CS at the end of the second command. In case of an invalid request (wrong sequence or DEVCTRLN not inverted to DEVCTRL) it will be rejected, an interrupt is generated and the corresponding status flag (**NO\_OP**) is set. Incase of an invalid state transition

request according to the **State Machine** in **Chapter 11** the request is ignored without issuing an interrupt.

## **13.4 Registers Description**

### **Table 20 Abbreviations**

| Registers that are being reset only in case of a POR.                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Registers that are being reset only in case of STANDBY and a POR.                                                                                                             |
| Registers that are being reset only in case of FAILSAFE, STANDBY and a POR.                                                                                                   |
| Registers that are being reset in case of "Move to INIT" event, FAILSAFE, STANDBY and a<br>POR.                                                                               |
| Bits that are readable (read)                                                                                                                                                 |
| Bits that are readable and writable (read-write)                                                                                                                              |
| Bits that are readable and writable but protected by register PROTCFG (read-write<br>protected)                                                                               |
| Bits that are readable and to clear the bit you have to write a 1 to it. (read-write-1-to-clear).<br>Flag-bits are updated based on the occurred condition.                   |
| Bits that are readable and writable after writing the operation is triggered, once this is done<br>successfully the bit is cleared by hardware. (read-write-hardware-cleared) |
| Bits that are readable and writable, after the operation the bit is updated by hardware. (read<br>write-hardware-updated)                                                     |
|                                                                                                                                                                               |

### **Table 21 Register Address Space**

| Module       | Base Address | End Address | Note            |
|--------------|--------------|-------------|-----------------|
| BusInterface | 0H           | 3FH         | Slave interface |

### **Table 22 Register Overview**

| Register Short Name | Register Long Name                                          | Offset Address | Reset Value |  |
|---------------------|-------------------------------------------------------------|----------------|-------------|--|
| DEVCFG0             | Device configuration 0 *R2)                                 | 00H            | 08H         |  |
| DEVCFG1             | Device configuration 1 *R0)                                 | 01H            | 06H         |  |
| DEVCFG2             | Device configuration 2 *R2)                                 | 02H            | 00H         |  |
| PROTCFG             | Protection register *R2)                                    | 03H            | 00H         |  |
| SYSPCFG0            | Protected System configuration request 0 *R1)               | 04H            | 01H         |  |
| SYSPCFG1            | Protected System configuration request 1 *R2)               | 05H            | 00H         |  |
| WDCFG0              | Protected Watchdog configuration request 0 *R2)             | 06H            | 9BH         |  |
| WDCFG1              | Protected Watchdog configuration request 1 *R2)             | 07H            | 09H         |  |
| FWDCFG              | Protected Functional watchdog configuration<br>request *R2) | 08H            | 0BH         |  |
| WWDCFG0             | Protected Window watchdog configuration request<br>0 *R2)   | 09H            | 06H         |  |
| WWDCFG1             | Protected Window watchdog configuration request<br>1 *R2)   | 0AH            | 0BH         |  |
| RSYSPCFG0           | System configuration 0 status *R0)                          | 0BH            | 01H         |  |
| RSYSPCFG1           | System configuration 1 status *R3) 1)                       | 0CH            | 00H         |  |
| RWDCFG0             | Watchdog configuration 0 status *R3)                        | 0DH            | 9BH         |  |

**Table 22 Register Overview** (cont'd)

| Register Short Name | Register Long Name                                                | Offset Address | Reset Value |
|---------------------|-------------------------------------------------------------------|----------------|-------------|
| RWDCFG1             | Watchdog configuration 1 status *R3)                              | 0EH            | 09H         |
| RFWDCFG             | Functional watchdog configuration status *R3)                     | 0FH            | 0BH         |
| RWWDCFG0            | Window watchdog configuration 0 status *R3)                       | 10H            | 06H         |
| RWWDCFG1            | Window watchdog configuration 1 status *R3)                       | 11H            | 09H         |
| WKTIMCFG0           | Wake timer configuration 0 *R2)                                   | 12H            | 00H         |
| WKTIMCFG1           | Wake timer configuration 1 *R2)                                   | 13H            | 00H         |
| WKTIMCFG2           | Wake timer configuration 2 *R2)                                   | 14H            | 00H         |
| DEVCTRL             | Device control request *R2)                                       | 15H            | 00H         |
| DEVCTRLN            | Device control inverted request *R2)                              | 16H            | 00H         |
| WWDSCMD             | Window watchdog service command *R2)                              | 17H            | 00H         |
| FWDRSP              | Functional watchdog response command *R2)                         | 18H            | 00H         |
| FWDRSPSYNC          | Functional watchdog response command with<br>synchronization *R2) | 19H            | 00H         |
| SYSFAIL             | Failure status flags *R1)                                         | 1AH            | 00H         |
| INITERR             | Init error status flags *R2)                                      | 1BH            | 00H         |
| IF                  | Interrupt flags *R2)                                              | 1CH            | 00H         |
| SYSSF               | System status flags *R2)                                          | 1DH            | 00H         |
| WKSF                | Wakeup status flags *R2)                                          | 1EH            | 00H         |
| SPISF               | SPI status flags *R2)                                             | 1FH            | 00H         |
| MONSF0              | Monitor status flags 0 *R1)                                       | 20H            | 00H         |
| MONSF1              | Monitor status flags 1 *R1)                                       | 21H            | 00H         |
| MONSF2              | Monitor status flags 2 *R2)                                       | 22H            | 00H         |
| MONSF3              | Monitor status flags 3 *R1)                                       | 23H            | 00H         |
| OTFAIL              | Over temperature failure status flags *R1)                        | 24H            | 00H         |
| OTWRNSF             | Over temperature warning status flags *R2)                        | 25H            | 00H         |
| VMONSTAT            | Voltage monitor status *R2)                                       | 26H            | 00H         |
| DEVSTAT             | Device status *R2)                                                | 27H            | 00H         |
| PROTSTAT            | Protection status *R1)                                            | 28H            | 01H         |
| WWDSTAT             | Window watchdog status *R3)                                       | 29H            | 00H         |
| FWDSTAT0            | Functional watchdog status 0 *R3)                                 | 2AH            | 30H         |
| FWDSTAT1            | Functional watchdog status 1 *R3)                                 | 2BH            | 00H         |
| ABIST_CTRL0         | ABIST control0 *R2) 1)                                            | 2CH            | 00H         |
| ABIST_CTRL1         | ABIST control1 *R2)                                               | 2DH            | 00H         |
| ABIST_SELECT0       | ABIST select 0 *R2)                                               | 2EH            | 00H         |
| ABIST_SELECT1       | ABIST select 1 *R2)                                               | 2FH            | 00H         |
| ABIST_SELECT2       | ABIST select 2 *R2)                                               | 30H            | 00H         |
| GTM                 | Global testmode *R2)                                              | 3FH            | 02H         |
| BCK_FREQ_CHANGE     | Buck switching frequency change *R2)                              | 31H            | 00H         |

**Table 22 Register Overview** (cont'd)

| Register Short Name | Register Long Name         | Offset Address | Reset Value |
|---------------------|----------------------------|----------------|-------------|
| BCK_FRE_SPREAD      | Buck Frequency spread *R2) | 32H            | 00H         |
| BCK_MAIN_CTRL       | Buck main control *R2)     | 33H            | 00H         |

<sup>1)</sup> Reset class of single bits is different. See register for details.

The registers are addressed wordwise.

## **13.4.1 Device registers**

**Device configuration 0 \*R2)**

| DEVCFG0<br>Device configuration 0 *R2) |         |              | Offset<br>00H |   |   |       | Reset Value | 08H |  |
|----------------------------------------|---------|--------------|---------------|---|---|-------|-------------|-----|--|
|                                        | 7       | 6            | 5             | 4 | 3 | 2     | 1           | 0   |  |
|                                        | WKTIMEN | WKTIMCY<br>C | nu            |   |   | TRDEL |             |     |  |
|                                        | rw      | rw           |               |   |   | rw    |             |     |  |

| Field    | Bits | Type | Description                                                                                                                                                                                      |  |
|----------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| WKTIMEN  | 7    | rw   | Wake timer enable<br>0D<br>Wake timer disabled<br>1D<br>Wake timer enabled in SLEEP or STANDBY state<br>Reset: 0H                                                                                |  |
| WKTIMCYC | 6    | rw   | Wake timer cycle period<br>0D<br>10 us<br>1D<br>10 ms<br>Reset: 0H                                                                                                                               |  |
| nu       | 5:4  | none | Reset: 0H                                                                                                                                                                                        |  |
| TRDEL    | 3:0  | rw   | Transition delay into low power states<br>For STANDBY and SLEEP transition. Defined as a step of 100 us.<br>0D<br>100 us<br>1D<br>200 us<br>2D<br>300 us<br>D<br><br>15D<br>1600 us<br>Reset: 8H |  |

**Device configuration 1 \*R0)**

| DEVCFG1<br>Device configuration 1 *R0) |   |   |    | Offset<br>01H |   |   | Reset Value<br>06H |   |  |
|----------------------------------------|---|---|----|---------------|---|---|--------------------|---|--|
|                                        | 7 | 6 | 5  | 4             | 3 | 2 | 1                  | 0 |  |
|                                        |   |   | nu |               |   |   | RESDEL             |   |  |
|                                        |   |   |    |               |   |   | rw                 |   |  |

| Field  | Bits | Type | Description                                                                                                                                                  |
|--------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu     | 7:3  | none | Reset: 00H                                                                                                                                                   |
| RESDEL | 2:0  | rw   | Reset release delay time<br>0D<br>200 us<br>1D<br>400 us<br>2D<br>800 us<br>3D<br>1ms<br>4D<br>2 ms<br>5D<br>4 ms<br>6D<br>10 ms<br>7D<br>15 ms<br>Reset: 6H |

#### **Device configuration 2 \*R2)**

| DEVCFG2                     | Offset | Reset Value |
|-----------------------------|--------|-------------|
| Device configuration 2 *R2) | 02H    | 00H         |

| 7     | 6   | 5   | 4      | 3    | 2 | 1       | 0      |
|-------|-----|-----|--------|------|---|---------|--------|
| EVCEN | STU | FRE | CMONEN | CTHR |   | ESYNPHA | ESYNEN |
| r     | r   | r   | rw     | rw   |   | rw      | rw     |

| Field   | Bits | Type | Description                                                                                                                                                                                                                         |  |  |
|---------|------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| EVCEN   | 7    | r    | External core supply enable status<br>0D<br>External core supply disabled<br>1D<br>External core supply enabled<br>Reset: 0H                                                                                                        |  |  |
| STU     | 6    | r    | Step-up converter enable status<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 0H                                                                                                                                                     |  |  |
| FRE     | 5    | r    | Step-down converter frequency selection status<br>0D<br>Step-down converter runs on low frequency range<br>1D<br>Step-down converter runs on high frequency range<br>Reset: 0H                                                      |  |  |
| CMONEN  | 4    | rw   | QUC current monitor enable for transition to a low power state<br>For STANDBY and SLEEP transition. The setting is overwritten in<br>SLEEP as current monitoring is always enabled.<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 0H |  |  |
| CTHR    | 3:2  | rw   | QUC current monitoring threshold value<br>0D<br>10 mA<br>1D<br>30 mA<br>2D<br>60 mA<br>3D<br>100 mA<br>Reset: 0H                                                                                                                    |  |  |
| ESYNPHA | 1    | rw   | External synchronization output phase<br>0D<br>No phase shift<br>1D<br>180 phase shift<br>Reset: 0H                                                                                                                                 |  |  |
| ESYNEN  | 0    | rw   | Synchronization output for external switchmode regulator enable<br>0D<br>Disable<br>1D<br>Enable<br>Reset: 0H                                                                                                                       |  |  |

#### **Protection register \*R2)**

![](_page_10_Figure_2.jpeg)

| Field | Bits | Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------|------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KEY   | 7:0  | rw   | Protection key<br>Protection key register to request write access to protected registers.<br>Unlock: write 32-bit sequence of 4 consecutive bytes<br>(1: 0xAB 2:0xEF 3:0x56 4:0x12) to unlock access to protected registers.<br>Lock: write 32-bit sequence of 4 consecutive bytes<br>(1: 0xDF 2:0x34 3:0xBE 4:0xCA) to lock access to protected registers. All<br>configured values are applied to SSC and WD module after the lock. |
|       |      |      | ABH<br>Key 1 to unlock protected registers.<br>EFH<br>Key 2 to unlock protected registers.<br>56H<br>Key 3 to unlock protected registers.<br>12H<br>Key 4 to unlock protected registers.<br>DFH<br>Key 1 to lock protected registers.<br>34H<br>Key 2 to lock protected registers.<br>BEH<br>Key 3 to lock protected registers.<br>CAH<br>Key 4 to lock protected registers.<br>Reset: 00H                                            |

**Protected System configuration request 0 \*R1)**

| SYSPCFG0<br>Protected System configuration request 0<br>*R1) |   |   |    | Offset<br>04H |   |   | Reset Value<br>01H |
|--------------------------------------------------------------|---|---|----|---------------|---|---|--------------------|
| 7                                                            | 6 | 5 | 4  | 3             | 2 | 1 | 0                  |
|                                                              |   |   | nu |               |   |   | STBYEN             |
|                                                              |   |   |    |               |   |   | rwp                |

| Field  | Bits | Type | Description                                                                                                                          |
|--------|------|------|--------------------------------------------------------------------------------------------------------------------------------------|
| nu     | 7:1  | none | not used bits shall be written as 0 and will always return 1 upon read<br>Reset: 00H                                                 |
| STBYEN | 0    | rwp  | Request standby regulator QST enable<br>Valid for all device states except FAILSAFE.<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 1H |

#### **Protected System configuration request 1 \*R2)**

**SYSPCFG1 Offset Reset Value Protected System configuration request 1 \*R2) 05H 08H**

![](_page_12_Figure_3.jpeg)

| Field             | Bits | Type | Description                                                                                                                                                                                                              |
|-------------------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SS2DEL            | 7:5  | rwp  | Request safe state 2 delay<br>Applied for transitions from NORMAL to INIT, WAKE and SLEEP state.<br>0D<br>no delay<br>1D<br>10 ms<br>2D<br>50 ms<br>3D<br>100 ms<br>4D<br>250 ms<br>Reset: 0H                            |
| ERRSLPEN          | 4    | rwp  | Request ERR pin monitor functionality enable while the system is in<br>SLEEP<br>0D<br>ERR pin monitor is disabled in SLEEP<br>1D<br>ERR pin monitor can be active in SLEEP depending on ERREN bit<br>value.<br>Reset: 0H |
| ERREN<br>3<br>rwp |      |      | Request ERR pin monitor enable<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 1H                                                                                                                                           |
| ERRRECEN          | 2    | rwp  | Request ERR pin monitor recovery enable<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 0H                                                                                                                                  |
| ERRREC            | 1:0  | rwp  | Request ERR pin monitor recovery time<br>0D<br>1 ms<br>1D<br>2.5 ms<br>2D<br>5 ms<br>3D<br>10 ms<br>Reset: 0H                                                                                                            |

#### **Protected Watchdog configuration request 0 \*R2)**

| WDCFG0                                     | Offset | Reset Value |
|--------------------------------------------|--------|-------------|
| Protected Watchdog configuration request 0 | 06H    | 9BH         |
| *R2)                                       |        |             |

![](_page_13_Figure_3.jpeg)

| Field   | Bits | Type | Description                                                                                                                                                                                                              |
|---------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WWDETHR | 7:4  | rwp  | Request window watchdog error threshold<br>WWD error threshold to generate reset and enter into INIT state.<br>Reset: 9H                                                                                                 |
| WWDEN   | 3    | rwp  | Request window watchdog enable<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 1H                                                                                                                                           |
| FWDEN   | 2    | rwp  | Request functional watchdog enable<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 0H                                                                                                                                       |
| WWDTSEL | 1    | rwp  | Request window watchdog trigger selection<br>This is ignored when window watchdog is disabled.<br>0D<br>External WDI input used as a WWD trigger<br>1D<br>WWD is triggered by SPI write to WWDSCMD register<br>Reset: 1H |
| WDCYC   | 0    | rwp  | Request watchdog cycle time<br>0D<br>0,1 ms tick period<br>1D<br>1 ms tick period<br>Reset: 1H                                                                                                                           |

FWDETHR

rwp

### **Protected Watchdog configuration request 1 \*R2)**

nu WDSLPEN

| 7 | 6      | 5 | 4 | 3                                          | 2             | 1 | 0 |                    |
|---|--------|---|---|--------------------------------------------|---------------|---|---|--------------------|
|   |        |   |   |                                            |               |   |   |                    |
|   |        |   |   |                                            |               |   |   |                    |
|   |        |   |   |                                            |               |   |   |                    |
|   |        |   |   |                                            |               |   |   |                    |
|   |        |   |   |                                            |               |   |   |                    |
|   |        |   |   |                                            |               |   |   |                    |
|   |        |   |   |                                            |               |   |   |                    |
|   |        |   |   |                                            |               |   |   |                    |
|   | WDCFG1 |   |   | Protected Watchdog configuration request 1 | Offset<br>07H |   |   | Reset Value<br>09H |

rwp

| Field   | Bits | Type | Description                                                                                                                                                                                                                          |
|---------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu      | 7:5  | none | not used bits shall be written as 0 and will always return 1 upon read<br>Reset: 0H                                                                                                                                                  |
| WDSLPEN | 4    | rwp  | Request watchdog functionality enable while the device is in SLEEP<br>0D<br>Disabled<br>1D<br>Enabled, the WD will work based on individual configuration<br>(WWDEN & FWDEN) settings while the system is in SLEEP mode<br>Reset: 0H |
| FWDETHR | 3:0  | rwp  | Request functional watchdog error threshold<br>FWD error threshold to generate reset and enter into INIT state.<br>Reset: 9H                                                                                                         |

### **Protected Functional watchdog configuration request \*R2)**

**FWDCFG Offset Reset Value Protected Functional watchdog configuration request \*R2) 08H 0BH** 7 6 5 4 3 2 1 0 nu WDHBTP rwp

| Field | Bits | Type | Description                                                                         |
|-------|------|------|-------------------------------------------------------------------------------------|
| nu    | 7:5  | none | not used bits shall be written as 0 and will always return 1 upon read<br>Reset: 0H |

| Field  | Bits | Type | Description                                                                                                                                                                                                                            |
|--------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WDHBTP | 4:0  | rwp  | Request functional watchdog heartbeat timer period<br>Defined as a multiple of 50 watchdog cycles (RWDCFG0.WDCYC).<br>0D<br>50 wd cycles<br>1D<br>100 wd cycles<br>2D<br>150 wd cycles<br>D<br><br>31D<br>1600 wd cycles<br>Reset: 0BH |

### **Protected Window watchdog configuration request 0 \*R2)**

| WWDCFG0<br>Protected Window watchdog configuration<br>request 0 *R2) |   |    |   |   | Offset<br>09H |     |   | Reset Value<br>06H |  |
|----------------------------------------------------------------------|---|----|---|---|---------------|-----|---|--------------------|--|
|                                                                      | 7 | 6  | 5 | 4 | 3             | 2   | 1 | 0                  |  |
|                                                                      |   | nu |   |   |               | CW  |   |                    |  |
|                                                                      |   |    |   |   |               | rwp |   |                    |  |

| Field | Bits | Type | Description                                                                                                                                                                                                                    |
|-------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu    | 7:5  | none | not used bits shall be written as 0 and will always return 1 upon read<br>Reset: 0H                                                                                                                                            |
| CW    | 4:0  | rwp  | Request window watchdog closed window time<br>Defined as a multiple of 50 watchdog cycles (RWDCFG0.WDCYC).<br>0D<br>50 wd cycles<br>1D<br>100 wd cycles<br>2D<br>150 wd cycles<br>D<br><br>31D<br>1600 wd cycles<br>Reset: 06H |

#### **Protected Window watchdog configuration request 1 \*R2)**

| WWDCFG1<br>Protected Window watchdog configuration<br>request 1 *R2) |   |    |   |   | Offset<br>0AH |     |   | Reset Value<br>0BH |  |
|----------------------------------------------------------------------|---|----|---|---|---------------|-----|---|--------------------|--|
|                                                                      | 7 | 6  | 5 | 4 | 3             | 2   | 1 | 0                  |  |
|                                                                      |   | nu |   |   |               | OW  |   |                    |  |
|                                                                      |   |    |   |   |               | rwp |   |                    |  |

| Field | Bits | Type | Description                                                                                                                                                                                                                  |
|-------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu    | 7:5  | none | not used bits shall be written as 0 and will always return 1 upon read<br>Reset: 0H                                                                                                                                          |
| OW    | 4:0  | rwp  | Request window watchdog open window time<br>Defined as a multiple of 50 watchdog cycles (RWDCFG0.WDCYC).<br>0D<br>50 wd cycles<br>1D<br>100 wd cycles<br>2D<br>150 wd cycles<br>D<br><br>31D<br>1600 wd cycles<br>Reset: 0BH |

### **System configuration 0 status \*R0)**

| RSYSPCFG0<br>System configuration 0 status *R0) |   |   |    | Offset<br>0BH |   | Reset Value<br>01H |             |
|-------------------------------------------------|---|---|----|---------------|---|--------------------|-------------|
| 7                                               | 6 | 5 | 4  | 3             | 2 | 1                  | 0           |
|                                                 |   |   | nu |               |   |                    | STBYEN<br>r |

| Field  | Bits | Type | Description                                                                                                                                                                                   |
|--------|------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu     | 7:1  | none | Reset: 00H                                                                                                                                                                                    |
| STBYEN | 0    | r    | Standby regulator QST enable status<br>Current configuration of standby regulator QST enable.<br>Valid for all device states except FAILSAFE.<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 1H |

r

r

| RSYSPCFG1                          |        |   |   | Offset       |       |          | Reset Value |        |  |
|------------------------------------|--------|---|---|--------------|-------|----------|-------------|--------|--|
| System configuration 1 status *R3) |        |   |   | 0CH          |       |          | 08H         |        |  |
|                                    |        |   |   |              |       |          |             |        |  |
|                                    | 7      | 6 | 5 | 4            | 3     | 2        | 1           | 0      |  |
|                                    | SS2DEL |   |   | ERRSLPE<br>N | ERREN | ERRRECEN |             | ERRREC |  |

r

r

r

| Field    | Bits | Type | Description                                                                                                                                                                                                                                                                                                                                 |  |  |  |  |
|----------|------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| SS2DEL   | 7:5  | r    | Safe state 2 delay status<br>Current configuration of safe state 2 delay applied for transitions from<br>NORMAL to INIT, WAKE and SLEEP state.<br>Bits have different reset class than whole register. The Bits are reset<br>according to *R1)<br>0D<br>no delay<br>1D<br>10 ms<br>2D<br>50 ms<br>3D<br>100 ms<br>4D<br>250 ms<br>Reset: 0H |  |  |  |  |
| ERRSLPEN | 4    | r    | ERR pin monitor functionality enable status while the device is in<br>SLEEP<br>Current configuration of ERR pin monitor functionality enable for SLEEP.<br>0D<br>ERR pin monitor is disabled in SLEEP<br>1D<br>ERR pin monitor can be active in SLEEP depending on ERREN bit<br>value.<br>Reset: 0H                                         |  |  |  |  |
| ERREN    | 3    | r    | ERR pin monitor enable status<br>Current configuration of ERR pin monitor enable.<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 1H                                                                                                                                                                                                           |  |  |  |  |
| ERRRECEN | 2    | r    | ERR pin monitor recovery enable status<br>Current configuration of ERR pin monitor recovery enable.<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 0H                                                                                                                                                                                         |  |  |  |  |

<sup>1)</sup> Reset class of single bits is different. See register for details.

| Field  | Bits | Type | Description                                                                                                                                                             |
|--------|------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERRREC | 1:0  | r    | ERR pin monitor recovery time status<br>Current configuration of ERR pin monitor recovery time.<br>0D<br>1 ms<br>1D<br>2.5 ms<br>2D<br>5 ms<br>3D<br>10 ms<br>Reset: 0H |

### **Watchdog configuration 0 status \*R3)**

| RWDCFG0<br>Watchdog configuration 0 status *R3) |   |         |   |   | Offset<br>0DH |       |         | Reset Value<br>9BH |
|-------------------------------------------------|---|---------|---|---|---------------|-------|---------|--------------------|
|                                                 | 7 | 6       | 5 | 4 | 3             | 2     | 1       | 0                  |
|                                                 |   | WWDETHR |   |   | WWDEN         | FWDEN | WWDTSEL | WDCYC              |
| r                                               |   |         |   | r | r             | r     | r       |                    |

| Field   | Bits | Type | Description                                                                                                                                                                                                                                                                |  |  |  |  |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| WWDETHR | 7:4  | r    | Window watchdog error threshold status<br>Current configuration of WWD error threshold to generate reset and enter<br>into INIT state.<br>Reset: 9H                                                                                                                        |  |  |  |  |
| WWDEN   | 3    | r    | Window watchdog enable status<br>Current configuration of WWD enable.<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 1H                                                                                                                                                      |  |  |  |  |
| FWDEN   | 2    | r    | Functional watchdog enable status<br>Current configuration of FWD enable.<br>0D<br>Disabled<br>1D<br>Enabled<br>Reset: 0H                                                                                                                                                  |  |  |  |  |
| WWDTSEL | 1    | r    | Window watchdog trigger selection status<br>Current configuration of WWD trigger selection. This is ignored when<br>window watchdog is disabled.<br>0D<br>External WDI input used as a WWD trigger<br>1D<br>WWD is triggered by SPI write to WWDSCMD register<br>Reset: 1H |  |  |  |  |
| WDCYC   | 0    | r    | Watchdog cycle time status<br>Current configuration of watchdog cycle time.<br>0D<br>0,1 ms tick period<br>1D<br>1 ms tick period<br>Reset: 1H                                                                                                                             |  |  |  |  |

#### **Watchdog configuration 1 status \*R3)**

| RWDCFG1<br>Watchdog configuration 1 status *R3) |    |   |         | Offset<br>0EH |         |   | Reset Value<br>09H |
|-------------------------------------------------|----|---|---------|---------------|---------|---|--------------------|
| 7                                               | 6  | 5 | 4       | 3             | 2       | 1 | 0                  |
|                                                 | nu |   | WDSLPEN |               | FWDETHR |   |                    |
|                                                 |    |   | r       |               | r       |   |                    |

| Field   | Bits | Type | Description                                                                                                                                                                                                                                                                                        |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu      | 7:5  | none | Reset: 0H                                                                                                                                                                                                                                                                                          |
| WDSLPEN | 4    | r    | Watchdog functionality enable status while the device is in SLEEP<br>Current configuration of WD functionality enable for SLEEP.<br>0D<br>Disabled<br>1D<br>Enabled, the WD will work based on individual configuration<br>(WWDEN & FWDEN) settings while the system is in SLEEP mode<br>Reset: 0H |
| FWDETHR | 3:0  | r    | Functional watchdog error threshold status<br>Current configuration of FWD error threshold to generate reset and enter<br>into INIT state.<br>Reset: 9H                                                                                                                                            |

#### **Functional watchdog configuration status \*R3)**

| RFWDCFG |                                                  |    |   | Offset |     | Reset Value |   |     |  |
|---------|--------------------------------------------------|----|---|--------|-----|-------------|---|-----|--|
|         | Functional watchdog configuration status<br>*R3) |    |   |        | 0FH |             |   | 0BH |  |
|         | 7                                                | 6  | 5 | 4      | 3   | 2           | 1 | 0   |  |
|         |                                                  | nu |   |        |     | WDHBTP      |   |     |  |

| Field | Bits | Type | Description |
|-------|------|------|-------------|
| nu    | 7:5  | none |             |
|       |      |      | Reset: 0H   |

r

| Field  | Bits | Type | Description                                                                                                                                                                                                                                                                                  |
|--------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WDHBTP | 4:0  | r    | Functional watchdog heartbeat timer period status<br>Current configuration of FWD heartbeat timer period defined as a multiple<br>of 50 watchdog cycles (RWDCFG0.WDCYC).<br>0D<br>50 wd cycles<br>1D<br>100 wd cycles<br>2D<br>150 wd cycles<br>D<br><br>31D<br>1600 wd cycles<br>Reset: 0BH |

**Window watchdog configuration 0 status \*R3)**

| RWWDCFG0                                       | Offset | Reset Value |
|------------------------------------------------|--------|-------------|
| Window watchdog configuration 0 status<br>*R3) | 10H    | 06H         |

![](_page_20_Figure_4.jpeg)

r

| Field | Bits | Type | Description                                                                                                                                                                                                                                                                      |
|-------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu    | 7:5  | none | Reset: 0H                                                                                                                                                                                                                                                                        |
| CW    | 4:0  | r    | Window watchdog closed window time status<br>Current configuration of WWD closed window time defined as a multiple<br>of 50 watchdog cycles (RWDCFG0.WDCYC).<br>0D<br>50 wd cycles<br>1D<br>100 wd cycles<br>2D<br>150 wd cycles<br>D<br><br>31D<br>1600 wd cycles<br>Reset: 06H |

**Window watchdog configuration 1 status \*R3)**

| RWWDCFG1<br>*R3) |    | Window watchdog configuration 1 status |   | Offset<br>11H |    |   | Reset Value<br>0BH |  |
|------------------|----|----------------------------------------|---|---------------|----|---|--------------------|--|
| 7                | 6  | 5                                      | 4 | 3             | 2  | 1 | 0                  |  |
|                  | nu |                                        |   |               | OW |   |                    |  |
|                  |    |                                        |   |               | r  |   |                    |  |

| Field | Bits | Type | Description                                                                                                                                                                                                                                                                  |
|-------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu    | 7:5  | none | Reset: 0H                                                                                                                                                                                                                                                                    |
| OW    | 4:0  | r    | Window watchdog open window time status<br>Current configuration of WWD open window time defined as a multiple of<br>50 watchdog cycles (RWDCFG0.WDCYC).<br>0D<br>50 wd cycles<br>1D<br>100 wd cycles<br>2D<br>150 wd cycles<br>D<br><br>31D<br>1600 wd cycles<br>Reset: 0BH |

**Wake timer configuration 0 \*R2)**

| WKTIMCFG0<br>Wake timer configuration 0 *R2) |   |   |         | Offset<br>12H |   |   | Reset Value<br>00H |  |
|----------------------------------------------|---|---|---------|---------------|---|---|--------------------|--|
| 7                                            | 6 | 5 | 4       | 3             | 2 | 1 | 0                  |  |
|                                              |   |   | TIMVALL |               |   |   |                    |  |
|                                              |   |   | rw      |               |   |   |                    |  |

| Field   | Bits | Type | Description                                                                                                                            |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------------------|
| TIMVALL | 7:0  | rw   | Wake timer value lower bits<br>Bits (7:0) of wake time defined as a multiple of wake timer cycles<br>(DEVCFG0.WKTIMCYC).<br>Reset: 00H |

**Wake timer configuration 1 \*R2)**

| WKTIMCFG1<br>Wake timer configuration 1 *R2) |   |   | Offset<br>13H |   |   |   | Reset Value | 00H |
|----------------------------------------------|---|---|---------------|---|---|---|-------------|-----|
| 7                                            | 6 | 5 | 4             | 3 | 2 | 1 | 0           |     |
|                                              |   |   | TIMVALM       |   |   |   |             |     |
|                                              |   |   | rw            |   |   |   |             |     |

| Field   | Bits | Type | Description                                                                                                                              |
|---------|------|------|------------------------------------------------------------------------------------------------------------------------------------------|
| TIMVALM | 7:0  | rw   | Wake timer value middle bits<br>Bits (15:8) of wake time defined as a multiple of wake timer cycles<br>(DEVCFG0.WKTIMCYC).<br>Reset: 00H |

**Wake timer configuration 2 \*R2)**

| WKTIMCFG2<br>Wake timer configuration 2 *R2) |    |   | Offset<br>14H |         |   | Reset Value<br>00H |   |  |
|----------------------------------------------|----|---|---------------|---------|---|--------------------|---|--|
| 7                                            | 6  | 5 | 4             | 3       | 2 | 1                  | 0 |  |
|                                              |    |   |               | TIMVALH |   |                    |   |  |
|                                              | rw |   |               |         |   |                    |   |  |

| Field   | Bits | Type | Description                                                                                                                               |
|---------|------|------|-------------------------------------------------------------------------------------------------------------------------------------------|
| TIMVALH | 7:0  | rw   | Wake timer value higher bits<br>Bits (23:16) of wake time defined as a multiple of wake timer cycles<br>(DEVCFG0.WKTIMCYC).<br>Reset: 00H |

rwhc

#### **Device control request \*R2)**

rw

rw

rw

| DEVCTRL<br>Device control request *R2) |        |        |       |    | Offset<br>15H |   | Reset Value<br>00H |   |  |
|----------------------------------------|--------|--------|-------|----|---------------|---|--------------------|---|--|
|                                        |        |        |       |    |               |   |                    |   |  |
|                                        | 7      | 6      | 5     | 4  | 3             | 2 | 1                  | 0 |  |
|                                        | TRK2EN | TRK1EN | COMEN | nu | VREFEN        |   | STATEREQ           |   |  |

rw

| Field    | Bits | Type | Description                                                                                                                                                                                                                                                                                                                                    |
|----------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRK2EN   | 7    | rw   | Request tracker2 QT2 enable<br>0D<br>QT2 will be disabled after valid request<br>1D<br>QT2 will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                                    |
| TRK1EN   | 6    | rw   | Request tracker1 QT1 enable<br>0D<br>QT1 will be disabled after valid request<br>1D<br>QT1 will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                                    |
| COMEN    | 5    | rw   | Request communication ldo QCO enable<br>0D<br>QCO will be disabled after valid request<br>1D<br>QCO will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                           |
| nu       | 4    | none | Reset: 0H                                                                                                                                                                                                                                                                                                                                      |
| VREFEN   | 3    | rw   | Request voltage reference QVR enable<br>0D<br>QVR will be disabled after valid request<br>1D<br>QVR will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                           |
| STATEREQ | 2:0  | rwhc | Request for device state transition<br>Cleared to 000 by the HW after the request is processed. After writing a<br>new state value a user should not change the value before it's cleared by<br>HW.<br>7D<br>RESERVED<br>6D<br>RESERVED<br>5D<br>WAKE<br>4D<br>STANDBY<br>3D<br>SLEEP<br>2D<br>NORMAL<br>1D<br>INIT<br>0D<br>NONE<br>Reset: 0H |

#### **Device control inverted request \*R2)**

| DEVCTRLN |                                      |        |       |    | Offset |   | Reset Value |     |  |  |
|----------|--------------------------------------|--------|-------|----|--------|---|-------------|-----|--|--|
|          | Device control inverted request *R2) |        |       |    | 16H    |   |             | 00H |  |  |
|          |                                      |        |       |    |        |   |             |     |  |  |
|          | 7                                    | 6      | 5     | 4  | 3      | 2 | 1           | 0   |  |  |
|          | TRK2EN                               | TRK1EN | COMEN | nu | VREFEN |   | STATEREQ    |     |  |  |
|          | rw                                   | rw     | rw    |    | rw     |   | rwhc        |     |  |  |

| Field    | Bits | Type | Description                                                                                                                                                                                                                                                                                                                                    |
|----------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRK2EN   | 7    | rw   | Request tracker2 QT2 enable<br>1D<br>QT2 will be disabled after valid request<br>0D<br>QT2 will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                                    |
| TRK1EN   | 6    | rw   | Request tracker1 QT1 enable<br>1D<br>QT1 will be disabled after valid request<br>0D<br>QT1 will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                                    |
| COMEN    | 5    | rw   | Request communication ldo QCO enable<br>1D<br>QCO will be disabled after valid request<br>0D<br>QCO will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                           |
| nu       | 4    | none | Reset: 0H                                                                                                                                                                                                                                                                                                                                      |
| VREFEN   | 3    | rw   | Request voltage reference QVR enable<br>1D<br>QVR will be disabled after valid request<br>0D<br>QVR will be enabled after valid request<br>Reset: 0H                                                                                                                                                                                           |
| STATEREQ | 2:0  | rwhc | Request for device state transition<br>Cleared to 000 by the HW after the request is processed. After writing a<br>new state value a user should not change the value before it's cleared by<br>HW.<br>7D<br>NONE<br>6D<br>INIT<br>5D<br>NORMAL<br>4D<br>SLEEP<br>3D<br>STANDBY<br>2D<br>WAKE<br>1D<br>RESERVED<br>0D<br>RESERVED<br>Reset: 0H |

#### **Window watchdog service command \*R2)**

| WWDSCMD<br>Window watchdog service command *R2) |                 |   |    | Offset<br>17H |   |   |      | Reset Value<br>00H |
|-------------------------------------------------|-----------------|---|----|---------------|---|---|------|--------------------|
|                                                 | 7               | 6 | 5  | 4             | 3 | 2 | 1    | 0                  |
|                                                 | TRIG_ST<br>ATUS |   | nu |               |   |   | TRIG |                    |
|                                                 | r               |   |    |               |   |   |      | rw                 |

| Field           | Bits | Type | Description                                                                                                          |
|-----------------|------|------|----------------------------------------------------------------------------------------------------------------------|
| TRIG_STATU<br>S | 7    | r    | Last SPI trigger received<br>Reset: 0H                                                                               |
| nu              | 6:1  | none | Reset: 00H                                                                                                           |
| TRIG            | 0    | rw   | Window watchdog SPI trigger command<br>Read TRIG_STATUS bit first and write inverted value to TRIG bit.<br>Reset: 0H |

## **Functional watchdog response command \*R2)**

**FWDRSP Offset Reset Value Functional watchdog response command \*R2) 18H 00H**

![](_page_26_Figure_6.jpeg)

| Field  | Bits | Type | Description                                                                                           |
|--------|------|------|-------------------------------------------------------------------------------------------------------|
| FWDRSP | 7:0  | rw   | Functional watchdog response<br>Write functional watchdog response bytes to this field.<br>Reset: 00H |

**Functional watchdog response command with synchronization \*R2)**

|         | FWDRSPSYNC                |   |                                      |   | Offset |   | Reset Value |     |  |
|---------|---------------------------|---|--------------------------------------|---|--------|---|-------------|-----|--|
|         | with synchronization *R2) |   | Functional watchdog response command |   | 19H    |   |             | 00H |  |
|         | 7                         | 6 | 5                                    | 4 | 3      | 2 | 1           | 0   |  |
| FWDRSPS |                           |   |                                      |   |        |   |             |     |  |
|         |                           |   |                                      |   | rw     |   |             |     |  |

| Field   | Bits | Type | Description                                                                                                                                                                     |
|---------|------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FWDRSPS | 7:0  | rw   | Functional watchdog heartbeat synchronization response<br>Write the last functional watchdog response byte to this field to<br>synchronize/restart the heartbeat.<br>Reset: 00H |

rw1c

rw1c

#### **Failure status flags \*R1)**

rw1c

rw1c

| SYSFAIL<br>Failure status flags *R1) |       |          |   |    | Offset<br>1AH |       | Reset Value<br>00H |                |  |
|--------------------------------------|-------|----------|---|----|---------------|-------|--------------------|----------------|--|
|                                      | 7     | 6        | 5 | 4  | 3             | 2     | 1                  | 0              |  |
|                                      | INITF | ABISTERR |   | nu |               | VMONF | OTF                | VOLTSEL<br>ERR |  |

rw1c

| Field          | Bits | Type | Description                                                                                                                                                                                                                                    |  |  |  |  |
|----------------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| INITF          | 7    | rw1c | INIT failure flag<br>INIT failure due to the third INIT failure in row. i.e. The device restarts INIT<br>phase from FAILSAFE.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H          |  |  |  |  |
| ABISTERR       | 6    | rw1c | ABIST operation interrupted flag<br>ABIST interrupted by any fault/event which is not part of ABIST.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H                                   |  |  |  |  |
| nu             | 5:3  | none | Reset: 0H                                                                                                                                                                                                                                      |  |  |  |  |
| VMONF          | 2    | rw1c | Voltage monitor failure flag<br>Voltage monitor failure occured which lead to FAILSAFE.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags, read MONSF0, MONSF1<br>and MONSF3 for details<br>Reset: 0H |  |  |  |  |
| OTF            | 1    | rw1c | Over temperature failure flag<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags, read OTFAIL for details<br>Reset: 0H                                                                                 |  |  |  |  |
| VOLTSELER<br>R | 0    | rw1c | Double Bit error on voltage selection flag<br>Device entered FAILSAFE state due to internal voltage selection failure.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H                 |  |  |  |  |

#### **Init error status flags \*R2)**

| INITERR                      | Offset | Reset Value |
|------------------------------|--------|-------------|
| Init error status flags *R2) | 1BH    | 00H         |

| 7       | 6       | 5    | 4    | 3    | 2     | 1  | 0 |
|---------|---------|------|------|------|-------|----|---|
| HARDRES | SOFTRES | ERRF | FWDF | WWDF | VMONF | nu |   |
| rw1c    | rw1c    | rw1c | rw1c | rw1c | rw1c  |    |   |

| Field   | Bits | Type | Description                                                                                                                                                                                                                                              |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HARDRES | 7    | rw1c | Hard reset flag<br>Hard reset has been generated due to the second INIT failure in row. i.e.<br>The device restarts INIT phase for the 3rd time.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H |
| SOFTRES | 6    | rw1c | Soft reset flag<br>Soft reset has been generated due to the first INIT failure. i.e. The device<br>restarts INIT phase for the 2nd time.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H         |
| ERRF    | 5    | rw1c | MCU error monitor failure flag<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H                                                                                                                   |
| FWDF    | 4    | rw1c | Functional watchdog error counter overflow failure flag<br>Functional watchdog error counter reached the error threshold.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H                        |
| WWDF    | 3    | rw1c | Window watchdog error counter overflow failure flag<br>Window watchdog error counter reached the error threshold.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags<br>Reset: 0H                                |
| VMONF   | 2    | rw1c | Voltage monitor failure flag<br>Voltage monitor failure occured which lead to INIT.<br>0D<br>No fault, write 0 - no action<br>1D<br>Fault occurred, write 1 to clear the flags, read MONSF2 for details<br>Reset: 0H                                     |
| nu      | 1:0  | rw1c | Reset: 0H                                                                                                                                                                                                                                                |

#### **Interrupt flags \*R2)**

| IF                   | Offset | Reset Value |
|----------------------|--------|-------------|
| Interrupt flags *R2) | 1CH    | 00H         |

| 7       | 6     | 5    | 4    | 3    | 2    | 1    | 0    |  |
|---------|-------|------|------|------|------|------|------|--|
| INTMISS | ABIST | OTF  | OTW  | MON  | SPI  | WK   | SYS  |  |
| r       | rw1c  | rw1c | rw1c | rw1c | rw1c | rw1c | rw1c |  |

| Field   | Bits | Type | Description                                                                                                                                                                                                                                        |  |  |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| INTMISS | 7    | r    | Interrupt not serviced in time flag<br>Interrupt has not been serviced within tINT,TO time<br>0D<br>No interrupt timeout happened<br>1D<br>Interrupt timeout happened, cleared by hardware when all other<br>flags in IF are cleared.<br>Reset: 0H |  |  |
| ABIST   | 6    | rw1c | Requested ABIST operation performed flag<br>0D<br>No interrupt, write 0 - no action<br>1D<br>Interrupt flag active, write 1 to clear the flag<br>Reset: 0H                                                                                         |  |  |
| OTF     | 5    | rw1c | Over temperature failure interrupt flag<br>0D<br>No interrupt, write 0 - no action<br>1D<br>Interrupt flag active, write 1 to clear the flag, read OTFAIL for details<br>Reset: 0H                                                                 |  |  |
| OTW     | 4    | rw1c | Over temperature warning interrupt flag<br>0D<br>No interrupt, write 0 - no action<br>1D<br>Interrupt flag active, write 1 to clear the flag, read OTWRNSF for<br>details<br>Reset: 0H                                                             |  |  |
| MON     | 3    | rw1c | Monitor interrupt flag<br>0D<br>No interrupt, write 0 - no action<br>1D<br>Interrupt flag active, write 1 to clear the flag, read MONSF0,<br>MONSF1, MONSF2 and MONSF3 for details<br>Reset: 0H                                                    |  |  |
| SPI     | 2    | rw1c | SPI interrupt flag<br>0D<br>No interrupt, write 0 - no action<br>1D<br>Interrupt flag active, write 1 to clear the flag, read SPISF for details<br>Reset: 0H                                                                                       |  |  |
| WK      | 1    | rw1c | Wake interrupt flag<br>Only set if device generates an interrupt when leaving SLEEP state.<br>0D<br>No interrupt, write 0 - no action<br>1D<br>Interrupt flag active, write 1 to clear the flag, read WKSF for details<br>Reset: 0H                |  |  |

| Field | Bits | Type | Description                                                                                                                                                     |
|-------|------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SYS   | 0    | rw1c | System interrupt flag<br>0D<br>No interrupt, write 0 - no action<br>1D<br>Interrupt flag active, write 1 to clear the flag, read SYSSF for details<br>Reset: 0H |

### **System status flags \*R2)**

| SYSSF                    | Offset | Reset Value |
|--------------------------|--------|-------------|
| System status flags *R2) | 1DH    | 00H         |
|                          |        |             |
|                          |        |             |

| 7 | 6  | 5     | 4      | 3       | 2    | 1    | 0    |
|---|----|-------|--------|---------|------|------|------|
|   | nu | NO_OP | TRFAIL | ERRMISS | FWDE | WWDE | CFGE |
|   |    | rw1c  | rw1c   | rw1c    | rw1c | rw1c | rw1c |

| Field   | Bits | Type | Description                                                                                                                                                                                                                                                            |  |
|---------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| nu      | 7:6  | none | Reset: 0H                                                                                                                                                                                                                                                              |  |
| NO_OP   | 5    | rw1c | State transition request failure flag<br>Requested state transition via DEVCTRL & DEVCTRLN could not be<br>performed because of wrong protocol.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                           |  |
| TRFAIL  | 4    | rw1c | Transition to low power failed flag<br>Transition to low power failed either due to the QUC current monitor,<br>WAK high level or a rising edge on ENA during TRDEL time.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |  |
| ERRMISS | 3    | rw1c | MCU error miss status flag<br>Set only when SYSPCFG1.ERRRECEN='1'<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                                                                                         |  |
| FWDE    | 2    | rw1c | Functional watchdog error interrupt flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                                                                                                                  |  |

| Field | Bits | Type | Description                                                                                                                                                                                                                                                                                              |
|-------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WWDE  | 1    | rw1c | Window watchdog error interrupt flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                                                                                                                                                        |
| CFGE  | 0    | rw1c | Protected configuration double bit error flag<br>Double bit error occurred on protected configuration register.<br>Status registers shall be read in order to determine which configuration<br>has changed.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |

### **Wakeup status flags \*R2)**

| WKSF                     |   |    | Offset |       |       | Reset Value |     |     |  |
|--------------------------|---|----|--------|-------|-------|-------------|-----|-----|--|
| Wakeup status flags *R2) |   |    |        |       | 1EH   | 00H         |     |     |  |
|                          | 7 | 6  | 5      | 4     | 3     | 2           | 1   | 0   |  |
|                          |   | nu |        | WKSPI | WKTIM | CMON        | ENA | WAK |  |

rw1c

rw1c

rw1c

rw1c

rw1c

| Field | Bits | Type | Description                                                                                                                                                                                      |
|-------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu    | 7:5  | none | Reset: 0H                                                                                                                                                                                        |
| WKSPI | 4    | rw1c | Wakeup from SLEEP by SPI flag (GoToWAKE)<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                                            |
| WKTIM | 3    | rw1c | Wake timer wakeup flag<br>Bit will also be set if STANDBY state left because of wake timer expired.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |
| CMON  | 2    | rw1c | QUC current monitor threshold wakeup flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                                           |

| Field | Bits | Type | Description                                                                                                                                                                                   |
|-------|------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENA   | 1    | rw1c | ENA signal wakeup flag<br>Bit will also be set if FAILSAFE or STANDBY state left because of ENA.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |
| WAK   | 0    | rw1c | WAK signal wakeup flag<br>Bit will also be set if FAILSAFE or STANDBY state left because of WAK.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |

## **SPI status flags \*R2)**

| SPISF<br>SPI status flags *R2) |   |    | Offset<br>1FH |      |      | Reset Value<br>00H |      |      |  |
|--------------------------------|---|----|---------------|------|------|--------------------|------|------|--|
|                                | 7 | 6  | 5             | 4    | 3    | 2                  | 1    | 0    |  |
|                                |   | nu |               | LOCK | DURE | ADDRE              | LENE | PARE |  |
|                                |   |    |               | rw1c | rw1c | rw1c               | rw1c | rw1c |  |

| Field | Bits | Type | Description                                                                                                                                                                          |
|-------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu    | 7:5  | none | Reset: 0H                                                                                                                                                                            |
| LOCK  | 4    | rw1c | LOCK or UNLOCK procedure error flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                                     |
| DURE  | 3    | rw1c | SPI frame duration error flag<br>SCS low for more than 2 ms.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                            |
| ADDRE | 2    | rw1c | SPI address invalid flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                                                |
| LENE  | 1    | rw1c | SPI frame length invalid flag<br>Number of detected SPI clock cycles different than 16.<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |

#### **SPI - Serial Peripheral Interface**

| Field | Bits | Type | Description                                                                                                              |
|-------|------|------|--------------------------------------------------------------------------------------------------------------------------|
| PARE  | 0    | rw1c | SPI frame parity error flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |

#### **Monitor status flags 0 \*R1)**

| MONSF0                      | Offset | Reset Value |
|-----------------------------|--------|-------------|
| Monitor status flags 0 *R1) | 20H    | 00H         |

| 7      | 6      | 5      | 4     | 3       | 2      | 1    | 0      |  |
|--------|--------|--------|-------|---------|--------|------|--------|--|
| TRK2SG | TRK1SG | VREFSG | COMSG | VCORESG | STBYSG | UCSG | PREGSG |  |
| rw1c   | rw1c   | rw1c   | rw1c  | rw1c    | rw1c   | rw1c | rw1c   |  |

| Field   | Bits | Type | Description                                                                                                                                    |
|---------|------|------|------------------------------------------------------------------------------------------------------------------------------------------------|
| TRK2SG  | 7    | rw1c | Tracker2 short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H              |
| TRK1SG  | 6    | rw1c | Tracker1 short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H              |
| VREFSG  | 5    | rw1c | Voltage reference short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H     |
| COMSG   | 4    | rw1c | Communication LDO short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H     |
| VCORESG | 3    | rw1c | Core voltage short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H          |
| STBYSG  | 2    | rw1c | Standby LDO short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H           |
| UCSG    | 1    | rw1c | uC LDO short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                |
| PREGSG  | 0    | rw1c | Pre-regulator voltage short to ground status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |

#### **Monitor status flags 1 \*R1)**

| MONSF1                      | Offset | Reset Value |
|-----------------------------|--------|-------------|
| Monitor status flags 1 *R1) | 21H    | 00H         |

| 7      | 6      | 5      | 4     | 3       | 2      | 1    | 0      |  |
|--------|--------|--------|-------|---------|--------|------|--------|--|
| TRK2OV | TRK1OV | VREFOV | COMOV | VCOREOV | STBYOV | UCOV | PREGOV |  |
| rw1c   | rw1c   | rw1c   | rw1c  | rw1c    | rw1c   | rw1c | rw1c   |  |

| Field   | Bits | Type | Description                                                                                                                                 |
|---------|------|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| TRK2OV  | 7    | rw1c | Tracker2 over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H              |
| TRK1OV  | 6    | rw1c | Tracker1 over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H              |
| VREFOV  | 5    | rw1c | Voltage reference over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H     |
| COMOV   | 4    | rw1c | Communication LDO over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H     |
| VCOREOV | 3    | rw1c | Core voltage over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H          |
| STBYOV  | 2    | rw1c | Standby LDO over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H           |
| UCOV    | 1    | rw1c | uC LDO over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                |
| PREGOV  | 0    | rw1c | Pre-regulator voltage over voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |

#### **Monitor status flags 2 \*R2)**

| MONSF2                      | Offset | Reset Value |
|-----------------------------|--------|-------------|
| Monitor status flags 2 *R2) | 22H    | 00H         |

| 7      | 6      | 5      | 4     | 3       | 2      | 1    | 0      |  |
|--------|--------|--------|-------|---------|--------|------|--------|--|
| TRK2UV | TRK1UV | VREFUV | COMUV | VCOREUV | STBYUV | UCUV | PREGUV |  |
| rw1c   | rw1c   | rw1c   | rw1c  | rw1c    | rw1c   | rw1c | rw1c   |  |

| Field   | Bits | Type | Description                                                                                                                                  |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------|
| TRK2UV  | 7    | rw1c | Tracker2 under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H              |
| TRK1UV  | 6    | rw1c | Tracker1 under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H              |
| VREFUV  | 5    | rw1c | Voltage reference under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H     |
| COMUV   | 4    | rw1c | Communication LDO under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H     |
| VCOREUV | 3    | rw1c | Core voltage under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H          |
| STBYUV  | 2    | rw1c | Standby LDO under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H           |
| UCUV    | 1    | rw1c | uC LDO under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                |
| PREGUV  | 0    | rw1c | Pre-regulator voltage under voltage status flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |

#### **Monitor status flags 3 \*R1)**

| MONSF3                      | Offset | Reset Value |
|-----------------------------|--------|-------------|
| Monitor status flags 3 *R1) | 23H    | 00H         |

| 7      | 6       | 5      | 4      | 3 | 2  | 1 | 0      |
|--------|---------|--------|--------|---|----|---|--------|
| BIASHI | BIASLOW | BG12OV | BG12UV |   | nu |   | VBATOV |
| rw1c   | rw1c    | rw1c   | rw1c   |   |    |   |        |

| Field   | Bits | Type | Description                                                                                                                                                        |
|---------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BIASHI  | 7    | rw1c | Bias current too high flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                            |
| BIASLOW | 6    | rw1c | Bias current too low flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                             |
| BG12OV  | 5    | rw1c | Bandgap comparator over voltage condition flag<br>(VBG1 ≥ VBG2 + 4%)<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H  |
| BG12UV  | 4    | rw1c | Bandgap comparator under voltage condition flag<br>(VBG1 ≤ VBG2 - 4%)<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |
| nu      | 3:1  | none | Reset: 0H                                                                                                                                                          |
| VBATOV  | 0    | rw1c | Supply voltage VSx over voltage flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                                  |

#### **Over temperature failure status flags \*R1)**

| OTFAIL<br>Over temperature failure status flags *R1) |      |   |    |      | Offset<br>24H |   |      | Reset Value<br>00H |  |
|------------------------------------------------------|------|---|----|------|---------------|---|------|--------------------|--|
|                                                      | 7    | 6 | 5  | 4    | 3             | 2 | 1    | 0                  |  |
|                                                      | MON  |   | nu | COM  | nu            |   | UC   | PREG               |  |
|                                                      | rw1c |   |    | rw1c |               |   | rw1c | rw1c               |  |

| Field | Bits | Type | Description                                                                                                                          |
|-------|------|------|--------------------------------------------------------------------------------------------------------------------------------------|
| MON   | 7    | rw1c | Monitoring over temperature flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H        |
| nu    | 6:5  | none | Reset: 0H                                                                                                                            |
| COM   | 4    | rw1c | Communication LDO over temperature flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |
| nu    | 3:2  | none | Reset: 0H                                                                                                                            |
| UC    | 1    | rw1c | uC LDO over temperature flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H            |
| PREG  | 0    | rw1c | Pre-regulator over temperature flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H     |

#### **Over temperature warning status flags \*R2)**

| OTWRNSF                                    | Offset | Reset Value |
|--------------------------------------------|--------|-------------|
| Over temperature warning status flags *R2) | 25H    | 00H         |

| 7 | 6  | 5    | 4    | 3  | 2     | 1    | 0    |
|---|----|------|------|----|-------|------|------|
|   | nu | VREF | COM  | nu | STDBY | UC   | PREG |
|   |    | rw1c | rw1c |    | rw1c  | rw1c | rw1c |

| Field                                                                                                                                   | Bits | Type                                      | Description                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu                                                                                                                                      | 7:6  | none                                      | Reset: 0H                                                                                                                                                   |
| VREF<br>5<br>rw1c<br>Voltage reference over load flag<br>(over current for more than 1ms)<br>0D<br>Write 0 no action<br>1D<br>Reset: 0H |      | Event detected, write 1 to clear the flag |                                                                                                                                                             |
| COM                                                                                                                                     | 4    | rw1c                                      | Communication LDO over temperature warning flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                |
| nu                                                                                                                                      | 3    | none                                      | Reset: 0H                                                                                                                                                   |
| STDBY                                                                                                                                   | 2    | rw1c                                      | Standby LDO over load flag<br>(over current for more than 1ms)<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H |
| UC                                                                                                                                      | 1    | rw1c                                      | uC LDO over temperature warning flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                           |
| PREG                                                                                                                                    | 0    | rw1c                                      | Pre-regulator over temperature warning flag<br>0D<br>Write 0 - no action<br>1D<br>Event detected, write 1 to clear the flag<br>Reset: 0H                    |

#### **Voltage monitor status \*R2)**

| VMONSTAT                    | Offset | Reset Value |
|-----------------------------|--------|-------------|
| Voltage monitor status *R2) | 26H    | 00H         |

| 7      | 6      | 5      | 4     | 3       | 2      | 1  | 0 |
|--------|--------|--------|-------|---------|--------|----|---|
| TRK2ST | TRK1ST | VREFST | COMST | VCOREST | STBYST | nu |   |
| r      | r      | r      | r     | r       | r      |    |   |

| Field   | Bits | Type | Description                                                                                                                |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------|
| TRK2ST  | 7    | r    | Tracker2 voltage ready status<br>0D<br>Voltage is out of range or not enabled<br>1D<br>Voltage is OK<br>Reset: 0H          |
| TRK1ST  | 6    | r    | Tracker1 voltage ready status<br>0D<br>Voltage is out of range or not enabled<br>1D<br>Voltage is OK<br>Reset: 0H          |
| VREFST  | 5    | r    | Voltage reference voltage ready status<br>0D<br>Voltage is out of range or not enabled<br>1D<br>Voltage is OK<br>Reset: 0H |
| COMST   | 4    | r    | Communication LDO voltage ready status<br>0D<br>Voltage is out of range or not enabled<br>1D<br>Voltage is OK<br>Reset: 0H |
| VCOREST | 3    | r    | Core voltage ready status<br>0D<br>Voltage is out of range or not enabled<br>1D<br>Voltage is OK<br>Reset: 0H              |
| STBYST  | 2    | r    | Standby LDO voltage ready status<br>0D<br>Voltage is out of range or not enabled<br>1D<br>Voltage is OK<br>Reset: 0H       |
| nu      | 1:0  | none | Reset: 0H                                                                                                                  |

#### **Device status \*R2)**

| DEVSTAT            | Offset | Reset Value |
|--------------------|--------|-------------|
| Device status *R2) | 27H    | 00H         |

| 7      | 6      | 5     | 4      | 3      | 2 | 1     | 0 |
|--------|--------|-------|--------|--------|---|-------|---|
| TRK2EN | TRK1EN | COMEN | STBYEN | VREFEN |   | STATE |   |
| r      | r      | r     | r      | r      |   | r     |   |

| Field  | Bits | Type | Description                                                                                                                                             |
|--------|------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRK2EN | 7    | r    | Tracker2 voltage enable status<br>0D<br>Voltage is disabled<br>1D<br>Voltage is enabled<br>Reset: 0H                                                    |
| TRK1EN | 6    | r    | Tracker1 voltage enable status<br>0D<br>Voltage is disabled<br>1D<br>Voltage is enabled<br>Reset: 0H                                                    |
| COMEN  | 5    | r    | Communication LDO enable status<br>0D<br>Voltage is disabled<br>1D<br>Voltage is enabled<br>Reset: 0H                                                   |
| STBYEN | 4    | r    | Standby LDO enable status<br>0D<br>Voltage is disabled<br>1D<br>Voltage is enabled<br>Reset: 0H                                                         |
| VREFEN | 3    | r    | Reference voltage enable status<br>0D<br>Voltage is disabled<br>1D<br>Voltage is enabled<br>Reset: 0H                                                   |
| STATE  | 2:0  | r    | Device state<br>7D<br>RESERVED<br>6D<br>RESERVED<br>5D<br>WAKE<br>4D<br>STANDBY<br>3D<br>SLEEP<br>2D<br>NORMAL<br>1D<br>INIT<br>0D<br>NONE<br>Reset: 0H |

#### **Protection status \*R1)**

| PROTSTAT<br>Protection status *R1) |   |   |   | Offset |   |   | Reset Value |   |     |
|------------------------------------|---|---|---|--------|---|---|-------------|---|-----|
|                                    |   |   |   | 28H    |   |   |             |   | 01H |
|                                    |   |   |   |        |   |   |             |   |     |
|                                    | 7 | 6 | 5 | 4      | 3 | 2 | 1           | 0 |     |
|                                    |   |   |   |        |   |   |             |   |     |

| 7      | 6      | 5      | 4      | 3 | 2  | 1 | 0    |  |
|--------|--------|--------|--------|---|----|---|------|--|
| KEY4OK | KEY3OK | KEY2OK | KEY1OK |   | nu |   | LOCK |  |
| r      | r      | r      | r      |   |    |   | r    |  |

| Field  | Bits | Type | Description                                                                                                                                 |
|--------|------|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| KEY4OK | 7    | r    | Key4 ok status<br>Information about validity of the 4th received protection key byte<br>0D<br>Key not valid<br>1D<br>Key valid<br>Reset: 0H |
| KEY3OK | 6    | r    | Key3 ok status<br>Information about validity of the 3rd received protection key byte<br>0D<br>Key not valid<br>1D<br>Key valid<br>Reset: 0H |
| KEY2OK | 5    | r    | Key2 ok status<br>Information about validity of the 2nd received protection key byte<br>0D<br>Key not valid<br>1D<br>Key valid<br>Reset: 0H |
| KEY1OK | 4    | r    | Key1 ok status<br>Information about validity of the 1st received protection key byte<br>0D<br>Key not valid<br>1D<br>Key valid<br>Reset: 0H |
| nu     | 3:1  | none | Reset: 0H                                                                                                                                   |
| LOCK   | 0    | r    | Protected register lock status<br>0D<br>Access is unlocked<br>1D<br>Access is locked<br>Reset: 1H                                           |

**Window watchdog status \*R3)**

| WWDSTAT<br>Window watchdog status *R3) |    |   |   | Offset<br>29H |         |   | Reset Value<br>00H |  |
|----------------------------------------|----|---|---|---------------|---------|---|--------------------|--|
| 7                                      | 6  | 5 | 4 | 3             | 2       | 1 | 0                  |  |
|                                        | nu |   |   |               | WWDECNT |   |                    |  |
|                                        |    |   |   |               | r       |   |                    |  |

| Field   | Bits | Type | Description                                       |
|---------|------|------|---------------------------------------------------|
| nu      | 7:4  | none | Reset: 0H                                         |
| WWDECNT | 3:0  | r    | Window watchdog error counter status<br>Reset: 0H |

**Functional watchdog status 0 \*R3)**

r

|                                   | FWDSTAT0 |              |     |         | Offset |     |          | Reset Value |  |
|-----------------------------------|----------|--------------|-----|---------|--------|-----|----------|-------------|--|
| Functional watchdog status 0 *R3) |          |              | 2AH |         |        | 30H |          |             |  |
|                                   |          |              |     |         |        |     |          |             |  |
|                                   | 7        | 6            | 5   | 4       | 3      | 2   | 1        | 0           |  |
|                                   | nu       | FWDRSPO<br>K |     | FWDRSPC |        |     | FWDQUEST |             |  |

r

r

| Field    | Bits | Type | Description                                                                                                                                                 |
|----------|------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nu       | 7    | none | Reset: 0H                                                                                                                                                   |
| FWDRSPOK | 6    | r    | Functional watchdog response check error status<br>0D<br>Response message is wrong<br>1D<br>All received bytes in response message are correct<br>Reset: 0H |
| FWDRSPC  | 5:4  | r    | Functional watchdog response counter value<br>Reset: 3H                                                                                                     |
| FWDQUEST | 3:0  | r    | Functional watchdog question<br>Reset: 0H                                                                                                                   |

#### **Functional watchdog status 1 \*R3)**

| FWDSTAT1 | Functional watchdog status 1 *R3) |    |   | Offset<br>2BH | Reset Value<br>00H |   |   |  |  |
|----------|-----------------------------------|----|---|---------------|--------------------|---|---|--|--|
| 7        | 6                                 | 5  | 4 | 3             | 2                  | 1 | 0 |  |  |
|          |                                   | nu |   |               | FWDECNT            |   |   |  |  |
|          |                                   |    |   |               | r                  |   |   |  |  |

| Field   | Bits | Type | Description                                          |
|---------|------|------|------------------------------------------------------|
| nu      | 7:4  | none | Reset: 0H                                            |
| FWDECNT | 3:0  | r    | Functional watchdog error counter value<br>Reset: 0H |

#### **ABIST control 0 \*R2)**

| ABIST_CTRL0         | Offset | Reset Value |
|---------------------|--------|-------------|
| ABIST control0 *R2) | 2CH    | 00H         |
|                     |        |             |

![](_page_46_Figure_3.jpeg)

| Field  | Bits | Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                           |  |  |  |  |  |
|--------|------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|
| STATUS | 7:4  | r    | ABIST global error status<br>ABIST status information after requested operation has been performed,<br>information shall only be considered valid, once START bit is cleared.<br>Bits have different reset class than whole register. The Bits are reset<br>according to *R1).<br>5D<br>Selected ABIST operation performed with no errors<br>10D<br>Selected ABIST operation performed with errors, check respective<br>SELECT registers<br>Reset: 0H |  |  |  |  |  |
| INT    | 3    | rw   | Safety path selection<br>Select whether safe state or interrupt related comparator shall be tested.<br>0D<br>safe state related comparators shall be tested<br>1D<br>interrupt related comparators shall be tested<br>Reset: 0H                                                                                                                                                                                                                       |  |  |  |  |  |
| SINGLE | 2    | rw   | ABIST Sequence selection<br>Select whether a single comparator shall be tested or all comparators in<br>predefined sequence<br>0D<br>Predefined sequence<br>1D<br>Single comparator test<br>Reset: 0H                                                                                                                                                                                                                                                 |  |  |  |  |  |
| PATH   | 1    | rw   | Full path test selection<br>Select the path which should be covered by ABIST operation<br>0D<br>Comparator only<br>1D<br>Comparator and corresponding deglitching logic, shall be selected<br>in case contribution to respective safety measure needs to be<br>tested<br>Reset: 0H                                                                                                                                                                    |  |  |  |  |  |
| START  | 0    | rwhc | Start ABIST operation<br>The ABIST operation itself will be started. This bit is cleared after ABIST<br>operation has been performed<br>0D<br>Operation done<br>1D<br>Start operation<br>Reset: 0H                                                                                                                                                                                                                                                    |  |  |  |  |  |

rw

rw

#### **ABIST control 1 \*R2)**

| ABIST_CTRL1<br>ABIST control1 *R2) |   |  |   |  | Offset<br>2DH |    |   |  |   |  | Reset Value<br>00H |                  |         |  |
|------------------------------------|---|--|---|--|---------------|----|---|--|---|--|--------------------|------------------|---------|--|
|                                    | 7 |  | 6 |  | 5             |    | 4 |  | 3 |  | 2                  | 1                | 0       |  |
|                                    |   |  |   |  |               | nu |   |  |   |  |                    | ABIST_C<br>LK_EN | OV_TRIG |  |

| Field            | Bits | Type | Description                                                                                                             |
|------------------|------|------|-------------------------------------------------------------------------------------------------------------------------|
| nu               | 7:2  | none | Reset: 00H                                                                                                              |
| ABIST_CLK_<br>EN | 1    | rw   | ABIST clock check enable<br>Select ABIST clock to check its functionality<br>0D<br>Disable<br>1D<br>Enable<br>Reset: 0H |
| OV_TRIG          | 0    | rw   | Overvoltage trigger for secondary internal monitor enable<br>0D<br>Disable<br>1D<br>Enable<br>Reset: 0H                 |

#### **ABIST select 0 \*R2)**

| ABIST_SELECT0       | Offset | Reset Value |
|---------------------|--------|-------------|
| ABIST select 0 *R2) | 2EH    | 00H         |

| 7      | 6      | 5      | 4     | 3       | 2      | 1    | 0      |
|--------|--------|--------|-------|---------|--------|------|--------|
| TRK2OV | TRK1OV | VREFOV | COMOV | VCOREOV | STBYOV | UCOV | PREGOV |
| rwhu   | rwhu   | rwhu   | rwhu  | rwhu    | rwhu   | rwhu | rwhu   |

| Field   | Bits | Type | Description                                                                                                                                                                                                                                 |
|---------|------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TRK2OV  | 7    | rwhu | Select TRK2 OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H         |
| TRK1OV  | 6    | rwhu | Select TRK1 OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H         |
| VREFOV  | 5    | rwhu | Select VREF OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H         |
| COMOV   | 4    | rwhu | Select COM OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H          |
| VCOREOV | 3    | rwhu | Select Core voltage OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H |
| STBYOV  | 2    | rwhu | Select Standby LDO OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H  |
| UCOV    | 1    | rwhu | Select uC LDO OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H       |

| Field  | Bits | Type | Description                                                                                                                                                                                                                                  |
|--------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PREGOV | 0    | rwhu | Select Pre-regulator OV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H |

#### **ABIST select 1 \*R2)**

| ABIST_SELECT1       | Offset | Reset Value |
|---------------------|--------|-------------|
| ABIST select 1 *R2) | 2FH    | 00H         |

| 7      | 6      | 5      | 4     | 3       | 2      | 1    | 0      |
|--------|--------|--------|-------|---------|--------|------|--------|
| TRK2UV | TRK1UV | VREFUV | COMUV | VCOREUV | STBYUV | UCUV | PREGUV |
| rwhu   | rwhu   | rwhu   | rwhu  | rwhu    | rwhu   | rwhu | rwhu   |

| Field   | Bits | Type | Description                                                                                                                                                                                                                          |  |
|---------|------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TRK2UV  | 7    | rwhu | Select TRK2 UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H  |  |
| TRK1UV  | 6    | rwhu | Select TRK1 UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this voltage<br>Reset: 0H     |  |
| VREFUV  | 5    | rwhu | Select VREF UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H  |  |
| COMUV   | 4    | rwhu | Select COM UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H   |  |
| VCOREUV | 3    | rwhu | Select VCORE UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H |  |

| Field  | Bits | Type | Description                                                                                                                                                                                                                                  |  |
|--------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| STBYUV | 2    | rwhu | Select STBY UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H          |  |
| UCUV   | 1    | rwhu | Select uC UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H            |  |
| PREGUV | 0    | rwhu | Select pre regulator UV comparator for ABIST operation<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H |  |

### **ABIST select 2 \*R2)**

| ABIST_SELECT2       | Offset | Reset Value |
|---------------------|--------|-------------|
| ABIST select 2 *R2) | 30H    | 00H         |

| 7      | 6       | 5      | 4      | 3     | 2  | 1 | 0      |
|--------|---------|--------|--------|-------|----|---|--------|
| BIASHI | BIASLOW | BG12OV | BG12UV | INTOV | nu |   | VBATOV |
| rwhu   | rwhu    | rwhu   | rwhu   | rwhu  |    |   | rwhu   |

| Field   | Bits | Type | Description                                                                                                                                                                                                                                        |  |
|---------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| BIASHI  | 7    | rwhu | Select bias current too high<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H                                 |  |
| BIASLOW | 6    | rwhu | Select bias current too low<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H                                  |  |
| BG12OV  | 5    | rwhu | Select bandgap comparator OV condition<br>(VBG1 ≥ VBG2 + 4%)<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H |  |

| Field  | Bits | Type | Description                                                                                                                                                                                                                                        |  |
|--------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| BG12UV | 4    | rwhu | Select bandgap comparator UV condition<br>(VBG1 ≤ VBG2 - 4%)<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H |  |
| INTOV  | 3    | rwhu | Select internal supply OV condition<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H                          |  |
| nu     | 2:1  | none | Reset: 0H                                                                                                                                                                                                                                          |  |
| VBATOV | 0    | rwhu | Select supply VSx overvoltage<br>0D<br>Not selected<br>1D<br>Selected, bit will be cleared upon successful ABIST operation on<br>comparator, bit will be set in case of ABIST fail for this comparator<br>Reset: 0H                                |  |

### **Global testmode \*R2)**

![](_page_51_Figure_3.jpeg)

| Field | Bits | Type | Description                                                                                              |
|-------|------|------|----------------------------------------------------------------------------------------------------------|
| nu    | 7:2  | none | Reset: 00H                                                                                               |
| NTM   | 1    | r    | Test mode inverted status<br>0D<br>Device is in test mode<br>1D<br>Device is in normal mode<br>Reset: 1H |
| TM    | 0    | r    | Test mode status<br>0D<br>Device is in normal mode<br>1D<br>Device is in test mode<br>Reset: 0H          |

## **13.4.2 Buck registers**

**Buck switching frequency change \*R2)**

![](_page_52_Figure_3.jpeg)

| Field            | Bits | Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
|------------------|------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| nu               | 7:3  | none | Reset: 00H                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |
| BCK_FREQ_<br>SEL | 2:0  | rw   | BUCK switching frequency change<br>For hi and low switching mode. New value needs to be validated via<br>data_valid procedure<br>Change buck frequency by approx4.5% from fOSC,step-down<br>7D<br>Change buck frequency by approx3.0% from fOSC,step-down<br>6D<br>Change buck frequency by approx1.5% from fOSC,step-down<br>5D<br>4D<br>No change<br>Change buck frequency by approx. +4.5% from fOSC,step-down<br>3D<br>Change buck frequency by approx. +3.0% from fOSC,step-down<br>2D<br>Change buck frequency by approx. +1.5% from fOSC,step-down<br>1D<br>0D<br>No Change<br>Reset: 0H |  |  |

**Buck Frequency spread \*R2)**

![](_page_53_Figure_2.jpeg)

| Field<br>Bits<br>Type<br>Description |     |    |                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------|-----|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FRE_SP_THR                           | 7:0 | rw | Spread spectrum<br>Select the percentage of frequency spread(+/-). The mean frequency is<br>reduced by the percentage as well keeping the maximum frequency at<br>the nominal frequency selected by FRE.<br>00H<br>No spread<br>2BH<br>1%<br>55H<br>2%<br>80H<br>3%<br>AAH<br>4%<br>D5H<br>5%<br>FFH<br>6%<br>Reset: 00H |

**Buck main control \*R2)**

| BCK_MAIN_CTRL<br>Buck main control *R2) |                |   |   | Offset<br>33H |    |   | Reset Value<br>00H |  |
|-----------------------------------------|----------------|---|---|---------------|----|---|--------------------|--|
| 7                                       | 6              | 5 | 4 | 3             | 2  | 1 | 0                  |  |
| BUSY                                    | DATA_VA<br>LID |   |   |               | nu |   |                    |  |
| r                                       | rw             |   |   |               |    |   |                    |  |

| Field | Bits | Type | Description                                                                                        |
|-------|------|------|----------------------------------------------------------------------------------------------------|
| BUSY  | 7    | r    | DATA_VALID parameter update ready status<br>0D<br>update done<br>1D<br>update ongoing<br>Reset: 0H |

#### **SPI - Serial Peripheral Interface**

| Field      | Bits | Type | Description                                                                                                                                                                                                                                              |
|------------|------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DATA_VALID | 6    | rw   | Enable buck update<br>Update Command to load new parameter for stepdown regulator (after<br>configuration write 1 to update and write 0 after BUSY flag is cleared to<br>proceed operation)<br>0D<br>No action<br>1D<br>Load new parameters<br>Reset: 0H |
| nu         | 5:0  | none | Reset: 00H                                                                                                                                                                                                                                               |

## **13.5 Electrical Characteristics**

**Table 23 Electrical Characteristics: SPI signals**

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                         | Symbol     | Values |      |      | Unit | Note /                              | Number    |
|-----------------------------------|------------|--------|------|------|------|-------------------------------------|-----------|
|                                   |            | Min.   | Typ. | Max. |      | Test<br>Condition                   |           |
| Pin SCS, Chip Select              |            |        |      |      |      |                                     |           |
| Chip select valid high level      | VSCS, hi   | 3.6    | –    | –    | V    | VSCS increasing,<br>VQUC = 5.0<br>V | P_13.5.1  |
| Chip select valid low level       | VSCS, lo   | –      | –    | 0.8  | V    | VSCS decreasing,<br>VQUC = 5.0<br>V | P_13.5.2  |
| Chip select hysteresis            | VSCS, hyst | –      | 350  | –    | mV   | VQUC = 5.0<br>V                     | P_13.5.3  |
| Chip select valid high level      | VSCS, hi   | 2.0    | –    | –    | V    | VSCS increasing,<br>VQUC = 3.3<br>V | P_13.5.4  |
| Chip select valid low level       | VSCS, lo   | –      | –    | 0.8  | V    | VSCS decreasing,<br>VQUC = 3.3<br>V | P_13.5.5  |
| Chip select hysteresis            | VSCS, hyst | –      | 160  | –    | mV   | VQUC = 3.3<br>V                     | P_13.5.6  |
| Chip select pull-up current       | ISCS       | -175   | -120 | –    | µA   | VSCS = 0<br>V                       | P_13.5.7  |
| Chip select input capacitance     | CSCS       | –      | 4    | 15   | pF   | 1)                                  | P_13.5.8  |
| Pin SCL, Clock                    |            |        |      |      |      |                                     |           |
| Clock signal valid high level     | VSCL, hi   | 3.6    | –    | –    | V    | VSCL increasing,<br>VQUC = 5.0<br>V | P_13.5.9  |
| Clock signal valid low level      | VSCL, lo   | –      | –    | 0.8  | V    | VSCL decreasing,<br>VQUC = 5.0<br>V | P_13.5.10 |
| Clock hysteresis                  | VSCL, hyst | –      | 350  | –    | mV   | VQUC = 5.0<br>V                     | P_13.5.11 |
| Clock signal valid high level     | VSCL, hi   | 2.0    | –    | –    | V    | VSCL increasing,<br>VQUC = 3.3 V    | P_13.5.12 |
| Clock signal valid low level      | VSCL, lo   | –      | –    | 0.8  | V    | VSCL decreasing,<br>VQUC = 3.3 V    | P_13.5.13 |
| Clock hysteresis                  | VSCL, hyst | –      | 160  | –    | mV   | VQUC = 3.3<br>V                     | P_13.5.14 |
| Clock signal pull-down<br>current | ISCL       | –      | 150  | 330  | µA   | VSCL = VQUC                         | P_13.5.15 |
| Clock input capacitance           | CSCL       | –      | 4    | 15   | pF   | 1)                                  | P_13.5.16 |
| Pin SDI, Data Input, MOSI         |            |        |      |      |      |                                     |           |
| Data input valid high level       | VSDI, hi   | 3.6    | –    | –    | V    | VSDI increasing,<br>VQUC = 5.0 V    | P_13.5.17 |
| Data input valid low level        | VSDI, lo   | –      | –    | 0.8  | V    | VSDI decreasing,<br>VQUC = 5.0 V    | P_13.5.18 |
| Data input hysteresis             | VSDI, hyst | –      | 350  | –    | mV   | VQUC = 5.0<br>V                     | P_13.5.19 |
| Data input valid high level       | VSDI, hi   | 2.0    | –    | –    | V    | VSDI increasing,<br>VQUC = 3.3 V    | P_13.5.20 |

**Table 23 Electrical Characteristics: SPI signals** (cont'd)

*V*VS =6.0 V to 40 V, *T*<sup>j</sup> = -40°C to +150°C, all voltages with respect to ground, positive current flowing into pin (unless otherwise specified)

| Parameter                               | Symbol          | Values |      |      | Unit | Note /                           | Number    |
|-----------------------------------------|-----------------|--------|------|------|------|----------------------------------|-----------|
|                                         |                 | Min.   | Typ. | Max. |      | Test<br>Condition                |           |
| Data input valid low level              | VSDI, lo        | –      | –    | 0.8  | V    | VSDI decreasing,<br>VQUC = 3.3 V | P_13.5.21 |
| Data input hysteresis                   | VSDI, hyst      | –      | 160  | –    | mV   | VQUC = 3.3<br>V                  | P_13.5.22 |
| Data input signal pull-down<br>current  | ISDI            | –      | 150  | 330  | µA   | VSDI = VQUC                      | P_13.5.23 |
| Data input capacitance                  | CSDI            | –      | 4    | 15   | pF   | 1)                               | P_13.5.24 |
| Pin SDO, Data Output, MISO              |                 |        |      |      |      |                                  |           |
| Data output high level<br>TLF35584xxVS1 | VSDO, hi        | 4.0    | –    | –    | V    | VQUC = 5.0 V,<br>ISDO = -9<br>mA | P_13.5.25 |
| Data output low level<br>TLF35584xxVS1  | VSDO, lo        | –      | –    | 0.7  | V    | VQUC = 5.0 V<br>ISDO = 7<br>mA   | P_13.5.26 |
| Data output high level<br>TLF35584xxVS2 | VSDO, hi        | 2.3    | –    | –    | V    | VQUC = 3.3 V<br>ISDO = -7<br>mA  | P_13.5.27 |
| Data output low level<br>TLF35584xxVS2  | VSDO, lo        | –      | –    | 0.7  | V    | VQUC = 3.3 V<br>ISDO = 5.5<br>mA | P_13.5.28 |
| Data output rise time 1)                | tSDO, rise      | –      | –    | 25   | ns   | CSDO,load = 50<br>pF             | P_13.5.29 |
| Data output fall time 1)                | tSDO, fall      | –      | –    | 25   | ns   | CSDO,load = 50<br>pF             | P_13.5.30 |
| Data output tristate<br>capacitance     | CSDO, tri       | –      | 4    | 15   | pF   | 1)                               | P_13.5.31 |
| Data output tristate leakage            | ISDO, tr, leaki | -10    | –    | 10   | µA   | –                                | P_13.5.32 |

<sup>1)</sup> Specified by design, not subject to production test