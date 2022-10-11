# Appendix Y1 to Subpart B of Part 430—Uniform Test Method for Measuring the Energy Consumption of Battery Chargers
Note: Manufacturers must use the results of testing under this appendix Y1 to determine compliance with any amended standards for battery chargers provided in § 430.32 that are published after September 8, 2022. Representations related to energy or water consumption must be made in accordance with the appropriate appendix that applies (i.e., appendix Y or appendix Y1) when determining compliance with the relevant standard. Manufacturers may also use appendix Y1 to certify compliance with amended standards, published after September 8, 2022, prior to the applicable compliance date for those standards.
1. Scope
This appendix provides the test requirements used to measure the energy consumption of battery chargers, including fixed-location wireless chargers designed for charging batteries with less than 100 watt-hour battery energy and open-placement wireless chargers, operating at either DC or United States AC line voltage (nominally 115V at 60Hz). This appendix also provides the test requirements used to measure the energy efficiency of uninterruptible power supplies as defined in section 2 of this appendix that utilize the standardized National Electrical Manufacturer Association (NEMA) plug, 1–15P or 5–15P, as specified in ANSI/NEMA WD 6–2016 (incorporated by reference, see § 430.3) and have an AC output. This appendix does not provide a method for testing back-up battery chargers.
2. Definitions
The following definitions are for the purposes of explaining the terminology associated with the test method for measuring battery charger energy consumption. 1
1 For clarity on any other terminology used in the test method, please refer to IEEE 1515–2000, (Sources for information and guidance, see § 430.4).
2.1. Active mode or charge mode is the state in which the battery charger system is connected to the main electricity supply, and the battery charger is delivering current, equalizing the cells, and performing other one-time or limited-time functions in order to bring the battery to a fully charged state.
2.2. Active power or real power (P) means the average power consumed by a unit. For a two terminal device with current and voltage waveforms i(t) and v(t), which are periodic with period T, the real or active power P is:
ER08SE22.003
2.3. Ambient temperature is the temperature of the ambient air immediately surrounding the unit under test.
2.4. Apparent power (S) is the product of root-mean-square (RMS) voltage and RMS current in volt-amperes (VA).
2.5. Batch charger is a battery charger that charges two or more identical batteries simultaneously in a series, parallel, series-parallel, or parallel-series configuration. A batch charger does not have separate voltage or current regulation, nor does it have any separate indicators for each battery in the batch. When testing a batch charger, the term "battery" is understood to mean, collectively, all the batteries in the batch that are charged together. A charger can be both a batch charger and a multi-port charger or multi-voltage charger.
2.6. Battery or battery pack is an assembly of one or more rechargeable cells and any integral protective circuitry intended to provide electrical energy to a consumer product, and may be in one of the following forms:
(a) Detachable battery (a battery that is contained in a separate enclosure from the consumer product and is intended to be removed or disconnected from the consumer product for recharging); or
(b) Integral battery (a battery that is contained within the consumer product and is not removed from the consumer product for charging purposes). The word "intended" in this context refers to whether a battery has been designed in such a way as to permit its removal or disconnection from its associated consumer product.
2.7. Battery energy is the energy, in watt-hours, delivered by the battery under the specified discharge conditions in the test procedure.
2.8. Battery maintenance mode or maintenance mode, is a subset of standby mode in which the battery charger is connected to the main electricity supply and the battery is fully charged, but is still connected to the charger.
2.9. Battery rest period is a period of time between discharge and charge or between charge and discharge, during which the battery is resting in an open-circuit state in ambient air.
2.10. C-Rate (C) is the rate of charge or discharge, calculated by dividing the charge or discharge current by the nameplate battery charge capacity of the battery. For example, a 0.2 C-rate would result in a charge or discharge period of 5 hours.
2.11. Cradle is an electrical interface between an integral battery product and the rest of the battery charger designed to hold the product between uses.
2.12. Energy storage system is a system consisting of single or multiple devices designed to provide power to the UPS inverter circuitry.
2.13. Equalization is a process whereby a battery is overcharged, beyond what would be considered "normal" charge return, so that cells can be balanced, electrolyte mixed, and plate sulfation removed.
2.14. Instructions or manufacturer's instructions means the documentation packaged with a product in printed or electronic form and any information about the product listed on a website maintained by the manufacturer and accessible by the general public at the time of the test. It also includes any information on the packaging or on the product itself. "Instructions" also includes any service manuals or data sheets that the manufacturer offers to independent service technicians, whether printed or in electronic form.
2.15. Measured charge capacity of a battery is the product of the discharge current in amperes and the time in decimal hours required to reach the specified end-of-discharge voltage.
2.16. Manual on-off switch is a switch activated by the user to control power reaching the battery charger. This term does not apply to any mechanical, optical, or electronic switches that automatically disconnect mains power from the battery charger when a battery is removed from a cradle or charging base, or for products with non-detachable batteries that control power to the product itself.
2.17. Multi-port charger means a battery charger that charges two or more batteries (which may be identical or different) simultaneously. The batteries are not connected in series or in parallel but with each port having separate voltage and/or current regulation. If the charger has status indicators, each port has its own indicator(s). A charger can be both a batch charger and a multi-port charger if it is capable of charging two or more batches of batteries simultaneously and each batch has separate regulation and/or indicator(s).
2.18. Multi-voltage charger is a battery charger that, by design, can charge a variety of batteries (or batches of batteries, if also a batch charger) that are of different nameplate battery voltages. A multi-voltage charger can also be a multi-port charger if it can charge two or more batteries simultaneously with independent voltages and/or current regulation.
2.19. Normal mode is a mode of operation for a UPS in which:
(a) The AC input supply is within required tolerances and supplies the UPS,
(b) The energy storage system is being maintained at full charge or is under recharge, and
(c) The load connected to the UPS is within the UPS's specified power rating.
2.20. Off mode is the condition, applicable only to units with manual on-off switches, in which the battery charger:
(a) Is connected to the main electricity supply;
(b) Is not connected to the battery; and
(c) All manual on-off switches are turned off.
2.21. Nameplate battery voltage is specified by the battery manufacturer and typically printed on the label of the battery itself. If there are multiple batteries that are connected in series, the nameplate battery voltage of the batteries is the total voltage of the series configuration—that is, the nameplate voltage of each battery multiplied by the number of batteries connected in series. Connecting multiple batteries in parallel does not affect the nameplate battery voltage.
2.22. Nameplate battery charge capacity is the capacity, claimed by the battery manufacturer on a label or in instructions, that the battery can store, usually given in ampere-hours (Ah) or milliampere-hours (mAh) and typically printed on the label of the battery itself. If there are multiple batteries that are connected in parallel, the nameplate battery charge capacity of the batteries is the total charge capacity of the parallel configuration, that is, the nameplate charge capacity of each battery multiplied by the number of batteries connected in parallel. Connecting multiple batteries in series does not affect the nameplate charge capacity.
2.23. Nameplate battery energy capacity means the product (in watts-hours (Wh)) of the nameplate battery voltage and the nameplate battery charge capacity.
2.24. No-battery mode is a subset of standby mode and means the condition in which:
(a) The battery charger is connected to the main electricity supply;
(b) The battery is not connected to the charger; and
(c) For battery chargers with manual on-off switches, all such switches are turned on.
2.25. Reference test load is a load or a condition with a power factor of greater than 0.99 in which the AC output socket of the UPS delivers the active power (W) for which the UPS is rated.
2.26. Standby mode means the condition in which the battery charge is either in maintenance mode or no battery mode as defined in this appendix.
2.27. Total harmonic distortion (THD), expressed as a percent, is the root mean square (RMS) value of an AC signal after the fundamental component is removed and interharmonic components are ignored, divided by the RMS value of the fundamental component.
2.28. Uninterruptible power supply or UPS means a battery charger consisting of a combination of convertors, switches and energy storage devices (such as batteries), constituting a power system for maintaining continuity of load power in case of input power failure.
2.28.1. Voltage and frequency dependent UPS or VFD UPS means a UPS that produces an AC output where the output voltage and frequency are dependent on the input voltage and frequency. This UPS architecture does not provide corrective functions like those in voltage independent and voltage and frequency independent systems.
Note to 2.28.1: VFD input dependency may be verified by performing the AC input failure test in Section 6.2.2.7 of IEC 62040–3 Ed. 2.0 (incorporated by reference, see § 430.3) and observing that, at a minimum, the UPS switches from normal mode of operation to battery power while the input is interrupted.
2.28.2. Voltage and frequency independent UPS, or VFI UPS, means a UPS where the device remains in normal mode producing an AC output voltage and frequency that is independent of input voltage and frequency variations and protects the load against adverse effects from such variations without depleting the stored energy source.
Note to 2.28.2: VFI input dependency may be verified by performing the steady state input voltage tolerance test and the input frequency tolerance test in Sections 6.4.1.1 and 6.4.1.2 of IEC 62040–3 Ed. 2.0 respectively, and observing that, at a minimum, the UPS produces an output voltage and frequency within the specified output range when the input voltage is varied by ±10 percent of the rated input voltage and the input frequency is varied by ±2 percent of the rated input frequency.
2.28.3. Voltage independent UPS or VI UPS means a UPS that produces an AC output within a specific tolerance band that is independent of under-voltage or over-voltage variations in the input voltage without depleting the stored energy source. The output frequency of a VI UPS is dependent on the input frequency, similar to a voltage and frequency dependent system.
Note to 2.28.3: VI input dependency may be verified by performing the steady state input voltage tolerance test in Section 6.4.1.1 of IEC 62040–3 Ed. 2.0 and ensuring that the UPS remains in normal mode with the output voltage within the specified output range when the input voltage is varied by ±10% of the rated input voltage.
2.29. Unit under test (UUT) in this appendix refers to the combination of the battery charger and battery being tested.
2.30. Wireless charger is a battery charger that can charge batteries inductively.
2.30.1. Fixed-location wireless charger is an inductive wireless battery charger that incorporates a physical receiver locating feature (e.g., by physical peg, cradle, locking mechanism, magnet, etc.) to repeatably align or orient the position of the receiver with respect to the transmitter.
2.30.2. Open-placement wireless charger is an inductive wireless charger that does not incorporate a physical receiver locating feature (e.g., by a physical peg, cradle, locking mechanism, magnet etc.) to repeatably align or orient the position of the receiver with respect to the transmitter.
3. Testing Requirements for all Battery Chargers Other Than Uninterruptible Power Supplies and Open-Placement Wireless Chargers
3.1. Standard Test Conditions
3.1.1. General
The values that may be measured or calculated during the conduct of this test procedure have been summarized for easy reference in Table 3.1.1 of this appendix.
Table 3.1.1—List of Measured or Calculated Values
Name of measured or calculated value | Reference
1. Duration of the Charge and Maintenance Modes test | Section 3.3.2.
2. Battery Discharge Energy (E batt) | Section 3.3.8.
3. Initial time and power (W) of the input current of connected battery | Section 3.3.6.
4. Active and Maintenance Modes Energy Consumption | Section 3.3.6.
5. Maintenance Mode Power (P m) | Section 3.3.9.
6. Active mode Energy Consumption (E a) | Section 3.3.10.
7. No-Battery Mode Power (P nb) | Section 3.3.11.
8. Off Mode Power (P off) | Section 3.3.12.
9. Standby Mode Power (P sb) | Section 3.3.13.
3.1.2. Verifying Accuracy and Precision of Measuring Equipment
Any power measurement equipment utilized for testing must conform to the uncertainty and resolution requirements outlined in Section 4, "General conditions for measurement", as well as Annexes B, "Notes on the measurement of low-power modes", and D, "Determination of uncertainty of measurement", of IEC 62301 (incorporated by reference, see § 430.3).
3.1.3. Setting Up the Test Room
All tests, battery conditioning, and battery rest periods shall be carried out in a room with an air speed immediately surrounding the UUT of ≤0.5 m/s. The ambient temperature shall be maintained at 20 °C ± 5 °C throughout the test. There shall be no intentional cooling of the UUT such as by use of separately powered fans, air conditioners, or heat sinks. The UUT shall be conditioned, rested, and tested on a thermally non-conductive surface. When not undergoing active testing, batteries shall be stored at 20 °C ± 5 °C.
3.1.4. Verifying the UUT's Input Voltage and Input Frequency
(a) If the UUT is intended for operation on AC line-voltage input in the United States, it shall be tested at 115 V at 60 Hz. If the UUT is intended for operation on AC line-voltage input but cannot be operated at 115 V at 60 Hz, it shall not be tested.
(b) If a battery charger is powered by a low-voltage DC or AC input and the manufacturer packages the battery charger with an external power supply ("EPS"), test the battery charger using the packaged EPS; if the battery charger does not include a pre-packaged EPS, then test the battery charger with an EPS sold and recommended by the manufacturer; if the manufacturer does not recommend an EPS that it sells, test the battery charger with an EPS that the manufacturer recommends for use in the manufacturer materials. The input reference source shall be 115 V at 60 Hz. If the EPS cannot be operated with AC input voltage at 115 V at 60 Hz, the charger shall not be tested.
(c) If a battery charger is designed for operation only on DC input voltage and if the provisions of section 3.1.4.(b) of this appendix do not apply, test the battery charger with an external power supply that minimally complies with the applicable energy conservation standard and meets the external power supply parameters specified by the battery charger manufacturer. The input voltage shall be within ±1 percent of the battery charger manufacturer specified voltage.
(d) If the input voltage is AC, the input frequency shall be within ±1 percent of the specified frequency. The THD of the input voltage shall be ≤2 percent, up to and including the 13th harmonic. The crest factor of the input voltage shall be between 1.34 and 1.49.
(e) If the input voltage is DC, the AC ripple voltage (RMS) shall be:
(1) ≤0.2 V for DC voltages up to 10 V; or
(2) ≤2 percent of the DC voltage for DC voltages over 10 V.
3.2. Unit Under Test Setup Requirements
3.2.1. General Setup
(a) The battery charger system shall be prepared and set up in accordance with the manufacturer's instructions, except where those instructions conflict with the requirements of this test procedure. If no instructions are given, then factory or "default" settings shall be used, or where there are no indications of such settings, the UUT shall be tested in the condition as it would be supplied to an end user.
(b) If the battery charger has user controls to select from two or more charge rates (such as regular or fast charge) or different charge currents, the test shall be conducted at the fastest charge rate that is recommended by the manufacturer for everyday use, or, failing any explicit recommendation, the factory-default charge rate. If the charger has user controls for selecting special charge cycles that are recommended only for occasional use to preserve battery health, such as equalization charge, removing memory, or battery conditioning, these modes are not required to be tested. The settings of the controls shall be listed in the report for each test.
3.2.2. Selection and Treatment of the Battery Charger
The UUT, including the battery charger and its associated battery, shall be new products of the type and condition that would be sold to a customer. If the battery is lead-acid chemistry and the battery is to be stored for more than 24 hours between its initial acquisition and testing, the battery shall be charged before such storage.
3.2.3. Selection of Batteries To Use for Testing
(a) For chargers with integral batteries, the battery packaged with the charger shall be used for testing. For chargers with detachable batteries, the battery or batteries to be used for testing will vary depending on whether there are any batteries packaged with the battery charger.
(1) If batteries are packaged with the charger, batteries for testing shall be selected from the batteries packaged with the battery charger, according to the procedure in section 3.2.3(b) of this appendix.
(2) If no batteries are packaged with the charger, but the instructions specify or recommend batteries for use with the charger, batteries for testing shall be selected from those recommended or specified in the instructions, according to the procedure in section 3.2.3(b) of this appendix.
(3) If no batteries are packaged with the charger and the instructions do not specify or recommend batteries for use with the charger, batteries for testing shall be selected from any that are suitable for use with the charger, according to the procedure in section 3.2.3(b) of this appendix.
(b)(1) From the detachable batteries specified in section 3.2.3.(a) of this appendix, use Table 3.2.1 of this appendix to select the batteries to be used for testing, depending on the type of battery charger being tested. The battery charger types represented by the rows in the table are mutually exclusive. Find the single applicable row for the UUT, and test according to those requirements. Select only the single battery configuration specified for the battery charger type in Table 3.2.1 of this section.
(2) If the battery selection criteria specified in Table 3.2.1 of this appendix results in two or more batteries or configurations of batteries of different chemistries, but with equal voltage and capacity ratings, determine the maintenance mode power, as specified in section 3.3.9 of this appendix, for each of the batteries or configurations of batteries, and select for testing the battery or configuration of batteries with the highest maintenance mode power.
(c) A charger is considered as:
(1) Single-capacity if all associated batteries have the same nameplate battery charge capacity (see definition) and, if it is a batch charger, all configurations of the batteries have the same nameplate battery charge capacity.
(2) Multi-capacity if there are associated batteries or configurations of batteries that have different nameplate battery charge capacities.
(d) The selected battery or batteries will be referred to as the "test battery" and will be used through the remainder of this test procedure.
Table 3.2.1—Battery Selection for Testing
Type of charger | Multi-voltage | Multi-port | Multi-capacity | Tests to perform | Battery selection (from all configurations of all associated batteries)
No | No | No | Any associated battery.
No | No | Yes | Highest charge capacity battery.
No | Yes | Yes or No | Use all ports. Use the maximum number of identical batteries with the highest nameplate battery charge capacity that the charger can accommodate.
Yes | No | No | Highest voltage battery.
Yes | Yes to either or both | Use all ports. Use the battery or configuration of batteries with the highest individual voltage. If multiple batteries meet this criteria, then use the battery or configuration of batteries with the highest total nameplate battery charge capacity at the highest individual voltage.
3.2.4. Limiting Other Non-Battery-Charger Functions
(a) If the battery charger or product containing the battery charger does not have any additional functions unrelated to battery charging, this section may be skipped.
(b) Any optional functions controlled by the user and not associated with the battery charging process (e.g., the answering machine in a cordless telephone charging base) shall be switched off. If it is not possible to switch such functions off, they shall be set to their lowest power-consuming mode during the test.
(c) If the battery charger takes any physically separate connectors or cables not required for battery charging but associated with its other functionality (such as phone lines, serial or USB connections, Ethernet, cable TV lines, etc.), these connectors or cables shall be left disconnected during the testing.
(d) Any manual on-off switches specifically associated with the battery charging process shall be switched on for the duration of the charge, maintenance, and no-battery mode tests, and switched off for the off mode test.
3.2.5. Accessing the Battery for the Test
(a) The technician may need to disassemble the end-use product or battery charger to gain access to the battery terminals for the Battery Discharge Energy Test in section 3.3.8 of this appendix. If the battery terminals are not clearly labeled, the technician shall use a voltmeter to identify the positive and negative terminals. These terminals will be the ones that give the largest voltage difference and are able to deliver significant current (0.2 C or 1/hr) into a load.
(b) All conductors used for contacting the battery must be cleaned and burnished prior to connecting in order to decrease voltage drops and achieve consistent results.
(c) Manufacturer's instructions for disassembly shall be followed, except those instructions that:
(1) Lead to any permanent alteration of the battery charger circuitry or function;
(2) Could alter the energy consumption of the battery charger compared to that experienced by a user during typical use, e.g., due to changes in the airflow through the enclosure of the UUT; or
(3) Conflict requirements of this test procedure.
(d) Care shall be taken by the technician during disassembly to follow appropriate safety precautions. If the functionality of the device or its safety features is compromised, the product shall be discarded after testing.
(e) Some products may include protective circuitry between the battery cells and the remainder of the device. If the manufacturer provides a description for accessing the connections at the output of the protective circuitry, these connections shall be used to discharge the battery and measure the discharge energy. The energy consumed by the protective circuitry during discharge shall not be measured or credited as battery energy.
(f) If any of the following conditions specified in sections 3.2.5.(f)(1) to 3.2.5.(f)(3) of this appendix are applicable, preventing the measurement of the Battery Discharge Energy and the Charging and Maintenance Mode Energy, a manufacturer must submit a petition for a test procedure waiver in accordance with § 430.27:
(1) Inability to access the battery terminals;
(2) Access to the battery terminals destroys charger functionality; or
(3) Inability to draw current from the test battery.
3.2.6. Determining Charge Capacity for Batteries With No Rating
(a) If there is no rating for the battery charge capacity on the battery or in the instructions, then the technician shall determine a discharge current that meets the following requirements. The battery shall be fully charged and then discharged at this constant-current rate until it reaches the end-of-discharge voltage specified in Table 3.3.2 of this appendix. The discharge time must be not less than 4.5 hours nor more than 5 hours. In addition, the discharge test (section 3.3.8 of this appendix) (which may not be starting with a fully-charged battery) shall reach the end-of-discharge voltage within 5 hours. The same discharge current shall be used for both the preparations step (section 3.3.4 of this appendix) and the discharge test (section 3.3.8 of this appendix). The test report shall include the discharge current used and the resulting discharge times for both a fully-charged battery and for the discharge test.
(b) For this section, the battery is considered as "fully charged" when either: it has been charged by the UUT until an indicator on the UUT shows that the charge is complete; or it has been charged by a battery analyzer at a current not greater than the discharge current until the battery analyzer indicates that the battery is fully charged.
(c) When there is no capacity rating, a suitable discharge current must generally be determined by trial and error. Since the conditioning step does not require constant-current discharges, the trials themselves may also be counted as part of battery conditioning.
3.3. Test Measurement
The test sequence to measure the battery charger energy consumption is summarized in Table 3.3.1 of this appendix, and explained in detail in this appendix. Measurements shall be made under test conditions and with the equipment specified in sections 3.1 and 3.2 of this appendix.
Table 3.3.1—Test Sequence
Step/description | Equipment needed | Data taken? | Test battery | Charger | Battery analyzer or constant- current load | AC power meter | Thermometer (for flooded lead-acid battery chargers only)
1. Record general data on UUT; Section 3.3.1 | Yes | X | X |
2. Determine Active and Maintenance Modes Test duration; Section 3.3.2 | No | | |
3. Battery conditioning; Section 3.3.3 | No | X | X | X
4. Prepare battery for Active Mode test; Section 3.3.4 | No | X | X |
5. Battery rest period; Section 3.3.5 | No | X | | | | X
6. Conduct Active and Maintenance Modes Test; Section 3.3.6 | Yes | X | X | | X
7. Battery Rest Period; Section 3.3.7 | No | X | | | | X
8. Battery Discharge Energy Test; Section 3.3.8 | Yes | X | | X
9. Determine the Maintenance Mode Power; Section 3.3.9 | Yes | X | X | | X
10. Determine Active Charge Energy; Section 3.3.10 | Yes | X | X | | X
11. Conduct No-Battery Mode Test; Section 3.3.11 | Yes | | X | | X
12. Conduct Off Mode Test; Section 3.3.12 | Yes | | X | | X
13. Calculating Standby Mode Power; Section 3.3.13 | Yes | | | | |
3.3.1. Recording General Data on the UUT
The technician shall record:
(a) The manufacturer and model of the battery charger;
(b) The presence and status of any additional functions unrelated to battery charging;
(c) The manufacturer, model, and number of batteries in the test battery;
(d) The nameplate battery voltage of the test battery;
(e) The nameplate battery charge capacity of the test battery; and
(f) The nameplate battery charge energy of the test battery.
(g) The settings of the controls, if battery charger has user controls to select from two or more charge rates.
3.3.2. Determining the Duration of the Charge and Maintenance Modes Test
(a) The charge and maintenance modes test, described in detail in section 3.3.6 of this appendix, shall be 24 hours in length or longer, as determined by the items in sections 3.3.2.(a)(1) to 3.3.2.(a)(3) of this appendix. Proceed in order until a test duration is determined. In case when the battery charger does not enter its true battery maintenance mode, the test shall continue until 5 hours after the true battery maintenance mode has been captured.
(1) If the battery charger has an indicator to show that the battery is fully charged, that indicator shall be used as follows: if the indicator shows that the battery is charged after 19 hours of charging, the test shall be terminated at 24 hours. Conversely, if the full-charge indication is not yet present after 19 hours of charging, the test shall continue until 5 hours after the indication is present.
(2) If there is no indicator, but the manufacturer's instructions indicate that charging this battery or this capacity of battery should be complete within 19 hours, the test shall be for 24 hours. If the instructions indicate that charging may take longer than 19 hours, the test shall be run for the longest estimated charge time plus 5 hours.
(3) If there is no indicator and no time estimate in the instructions, but the charging current is stated on the charger or in the instructions, calculate the test duration as the longer of 24 hours or:
ER08SE22.004
(b) If none of section 3.3.2.(a) applies, the duration of the test shall be 24 hours.
3.3.3. Battery Conditioning
(a) No conditioning is to be done on lithium-ion batteries. The test technician shall proceed directly to battery preparation, section 3.3.4 of this appendix, when testing chargers for these batteries.
(b) Products with integral batteries will have to be disassembled per the instructions in section 3.2.5 of this appendix, and the battery disconnected from the charger for discharging.
(c) Batteries of other chemistries that have not been previously cycled are to be conditioned by performing two charges and two discharges, followed by a charge, as sections 3.3.3.(c)(1) to 3.3.3.(c)(5) of this appendix. No data need be recorded during battery conditioning.
(1) The test battery shall be fully charged for the duration specified in section 3.3.2 of this appendix or longer using the UUT.
(2) The test battery shall then be fully discharged using either:
(i) A battery analyzer at a rate not to exceed 1 C, until its average cell voltage under load reaches the end-of-discharge voltage specified in Table 3.3.2 of this appendix for the relevant battery chemistry; or
(ii) The UUT, until the UUT ceases operation due to low battery voltage.
(3) The test battery shall again be fully charged per step in section 3.3.3(c)(1) of this appendix.
(4) The test battery shall again be fully discharged per step in section 3.3.3(c)(2) of this appendix.
(5) The test battery shall be again fully charged per step in section 3.3.3(c)(1) of this appendix.
(d) Batteries of chemistries, other than lithium-ion, that are known to have been through at least two previous full charge/discharge cycles shall only be charged once per step in section 3.3.3(c)(5) of this appendix.
3.3.4. Preparing the Battery for Charge Testing
Following any conditioning prior to beginning the battery charge test (section 3.3.6 of this appendix), the test battery shall be fully discharged to the end of discharge voltage prescribed in Table 3.3.2 of this appendix, or until the UUT circuitry terminates the discharge.
3.3.5. Resting the Battery
The test battery shall be rested between preparation and the battery charge test. The rest period shall be at least one hour and not exceed 24 hours. For batteries with flooded cells, the electrolyte temperature shall be less than 30 °C before charging, even if the rest period must be extended longer than 24 hours.
3.3.6. Testing Active Charge Mode and Battery Maintenance Mode
(a) The Active Charge and Battery Maintenance Modes test measures energy consumed during charge mode and some time spent in the maintenance mode of the UUT. Functions required for battery conditioning that happen only with some user-selected switch or other control shall not be included in this measurement. (The technician shall manually turn off any battery conditioning cycle or setting.) Regularly occurring battery conditioning or maintenance functions that are not controlled by the user will, by default, be incorporated into this measurement.
(b) During the measurement period, input power values to the UUT shall be recorded at least once every minute.
(1) If possible, the technician shall set the data logging system to record the average power during the sample interval. The total energy is computed as the sum of power samples (in watts) multiplied by the sample interval (in hours).
(2) If this setting is not possible, then the power analyzer shall be set to integrate or accumulate the input power over the measurement period and this result shall be used as the total energy.
(c) The technician shall follow these steps:
(1) Ensure that the user-controllable device functionality not associated with battery charging and any battery conditioning cycle or setting are turned off, as instructed in section 3.2.4 of this appendix;
(2) Ensure that the test battery used in this test has been conditioned, prepared, discharged, and rested as described in sections 3.3.3. through 3.3.5. of this appendix;
(3) Connect the data logging equipment to the battery charger;
(4) Record the start time of the measurement period, and begin logging the input power;
(5) Connect the test battery to the battery charger within 3 minutes of beginning logging. For integral battery products, connect the product to a cradle or EPS within 3 minutes of beginning logging;
(6) After the test battery is connected, record the initial time and power (W) of the input current to the UUT. These measurements shall be taken within the first 10 minutes of active charging;
(7) Record the input power for the duration of the "Maintenance Mode Test" period, as determined by section 3.3.2. of this appendix. The actual time that power is connected to the UUT shall be within ±5 minutes of the specified period; and
(8) Disconnect power to the UUT, terminate data logging, and record the final time.
3.3.7. Resting the Battery
The test battery shall be rested between charging and discharging. The rest period shall be at least 1 hour and not more than 4 hours, with an exception for flooded cells. For batteries with flooded cells, the electrolyte temperature shall be less than 30 °C before charging, even if the rest period must be extended beyond 4 hours.
3.3.8. Battery Discharge Energy Test
(a) If multiple batteries were charged simultaneously, the discharge energy (E batt) is the sum of the discharge energies of all the batteries.
(1) For a multi-port charger, batteries that were charged in separate ports shall be discharged independently.
(2) For a batch charger, batteries that were charged as a group may be discharged individually, as a group, or in sub-groups connected in series and/or parallel. The position of each battery with respect to the other batteries need not be maintained.
(b) During discharge, the battery voltage and discharge current shall be sampled and recorded at least once per minute. The values recorded may be average or instantaneous values.
(c) For this test, the technician shall follow these steps:
(1) Ensure that the test battery has been charged by the UUT and rested according to the procedures prescribed in sections 3.3.6 and 3.3.7 of this appendix.
(2) Set the battery analyzer for a constant discharge rate and the end-of-discharge voltage in Table 3.3.2 of this appendix for the relevant battery chemistry.
(3) Connect the test battery to the analyzer and begin recording the voltage, current, and wattage, if available from the battery analyzer. When the end-of-discharge voltage is reached or the UUT circuitry terminates the discharge, the test battery shall be returned to an open-circuit condition. If current continues to be drawn from the test battery after the end-of-discharge condition is first reached, this additional energy is not to be counted in the battery discharge energy.
(d) If not available from the battery analyzer, the battery discharge energy (in watt-hours) is calculated by multiplying the voltage (in volts), current (in amperes), and sample period (in hours) for each sample, and then summing over all sample periods until the end-of-discharge voltage is reached.
Table 3.3.2—Required Battery Discharge Rates and End-of-Discharge Battery Voltages
Battery chemistry | Discharge rate (C) | End-of- discharge voltage* (volts per cell)
Valve-Regulated Lead Acid (VRLA) | 0.2 | 1.75
Flooded Lead Acid | 0.2 | 1.70
Nickel Cadmium (NiCd) | 0.2 | 1.0
Nickel Metal Hydride (NiMH) | 0.2 | 1.0
Lithium-ion (Li-Ion) | 0.2 | 2.5
Lithium-ion Polymer | 0.2 | 2.5
Lithium Iron Phosphate | 0.2 | 2.0
Rechargeable Alkaline | 0.2 | 0.9
Silver Zinc | 0.2 | 1.2
*If the presence of protective circuitry prevents the battery cells from being discharged to the end-of-discharge voltage specified, then discharge battery cells to the lowest possible voltage permitted by the protective circuitry.
3.3.9. Determining the Maintenance Mode Power
After the measurement period is complete, the technician shall determine the average maintenance mode power consumption (P m) by examining the power-versus-time data from the charge and maintenance mode test and:
(a) If the maintenance mode power is cyclic or shows periodic pulses, compute the average power over a time period that spans a whole number of cycles and includes at least the last 4 hours.
(b) Otherwise, calculate the average power value over the last 4 hours.
3.3.10. Determining the Active Charge Energy
After the measurement period is complete, the technician shall determine the total active charge energy (E a) by examining the power-versus-time data from the charge and maintenance mode test and:
(a) First determine when the battery charger enters maintenance mode by examining the power-versus-time data to identify when the input power enters either a steady state or a cyclic state with average power for that period being the same as the maintenance mode power determined in section 3.3.9. of this appendix.
(b) The accumulated energy or the average input power, integrated over the test period from the initial recorded input time up until when the battery charger enters maintenance mode would be the active charge energy, E a.
3.3.11. No-Battery Mode Energy Consumption Measurement
The no-battery mode measurement depends on the configuration of the battery charger, as follows:
(a) Conduct a measurement of no-battery power consumption while the battery charger is connected to the power source. Disconnect the battery from the charger, allow the charger to operate for at least 30 minutes, and record the power (i.e., watts) consumed as the time series integral of the power consumed over a 10-minute test period, divided by the period of measurement. If the battery charger has manual on-off switches, all must be turned on for the duration of the no-battery mode test.
(b) No-battery mode may also apply to products with integral batteries, as follows:
(1) If the product uses a cradle and/or adapter for power conversion and charging, then "disconnecting the battery from the charger" will require disconnection of the end-use product, which contains the batteries. The other enclosures of the battery charging system will remain connected to the main electricity supply, and no-battery mode power consumption will equal that of the cradle and/or adapter alone.
(2) If the product is powered through a detachable AC power cord and contains integrated power conversion and charging circuitry, then only the cord will remain connected to mains, and no-battery mode power consumption will equal that of the AC power cord (i.e., zero watts).
(3) If the product contains integrated power conversion and charging circuitry but is powered through a non-detachable AC power cord or plug blades, then no part of the system will remain connected to mains, and no-battery mode measurement is not applicable.
3.3.12. Off Mode Energy Consumption Measurement
The off mode measurement depends on the configuration of the battery charger, as follows:
(a) If the battery charger has manual on-off switches, record a measurement of off mode energy consumption while the battery charger is connected to the power source. Remove the battery from the charger, allow the charger to operate for at least 30 minutes, and record the power (i.e., watts) consumed as the time series integral of the power consumed over a 10-minute test period, divided by the period of measurement, with all manual on-off switches turned off. If the battery charger does not have manual on-off switches, record that the off mode measurement is not applicable to this product.
(b) Off mode may also apply to products with integral batteries, as follows:
(1) If the product uses a cradle and/or adapter for power conversion and charging, then "disconnecting the battery from the charger" will require disconnection of the end-use product, which contains the batteries. The other enclosures of the battery charging system will remain connected to the main electricity supply, and off mode power consumption will equal that of the cradle and/or adapter alone.
(2) If the product is powered through a detachable AC power cord and contains integrated power conversion and charging circuitry, then only the cord will remain connected to mains, and off mode power consumption will equal that of the AC power cord (i.e., zero watts).
(3) If the product contains integrated power conversion and charging circuitry but is powered through a non-detachable AC power cord or plug blades, then no part of the system will remain connected to mains, and off mode measurement is not applicable.
3.3.13. Standby Mode Power
The standby mode power (P sb) is the summation power of battery maintenance mode power (P m) and no-battery mode power (P nb).
4. Testing Requirements for Uninterruptible Power Supplies
4.1. Standard Test Conditions
4.1.1. Measuring Equipment
(a) The power or energy meter must provide true root mean square (r.m.s) measurements of the active input and output measurements, with an uncertainty at full rated load of less than or equal to 0.5 percent at the 95 percent confidence level notwithstanding that voltage and current waveforms can include harmonic components. The meter must measure input and output values simultaneously.
(b) All measurement equipment used to conduct the tests must be calibrated within the measurement equipment manufacturer specified calibration period by a standard traceable to International System of Units such that measurements meet the uncertainty requirements specified in section 4.1.1(a) of this appendix.
4.1.2. Test Room Requirements
All portions of the test must be carried out in a room with an air speed immediately surrounding the UUT of ≤0.5 m/s in all directions. Maintain the ambient temperature in the range of 20.0 °C to 30.0 °C, including all inaccuracies and uncertainties introduced by the temperature measurement equipment, throughout the test. No intentional cooling of the UUT, such as by use of separately powered fans, air conditioners, or heat sinks, is permitted. Test the UUT on a thermally non-conductive surface.
4.1.3. Input Voltage and Input Frequency
The AC input voltage and frequency to the UPS during testing must be within 3 percent of the highest rated voltage and within 1 percent of the highest rated frequency of the device.
4.2. Unit Under Test Setup Requirements
4.2.1. General Setup
Configure the UPS according to Section J.2 of Annex J of IEC 62040–3 Ed. 2.0 with the following additional requirements:
(a) UPS Operating Mode Conditions. If the UPS can operate in two or more distinct normal modes as more than one UPS architecture, conduct the test in its lowest input dependency as well as in its highest input dependency mode where VFD represents the lowest possible input dependency, followed by VI and then VFI.
(b) Energy Storage System. The UPS must not be modified or adjusted to disable energy storage charging features. Minimize the transfer of energy to and from the energy storage system by ensuring the energy storage system is fully charged (at the start of testing) as follows:
(1) If the UUT has a battery charge indicator, charge the battery for 5 hours after the UUT has indicated that it is fully charged.
(2) If the UUT does not have a battery charge indicator but the user manual shipped with the UUT specifies a time to reach full charge, charge the battery for 5 hours longer than the time specified.
(3) If the UUT does not have a battery charge indicator or user manual instructions, charge the battery for 24 hours.
(c) DC output port(s). All DC output port(s) of the UUT must remain unloaded during testing.
4.2.2. Additional Features
(a) Any feature unrelated to maintaining the energy storage system at full charge or delivery of load power (e.g., LCD display) shall be switched off. If it is not possible to switch such features off, they shall be set to their lowest power-consuming mode during the test.
(b) If the UPS takes any physically separate connectors or cables not required for maintaining the energy storage system at full charge or delivery of load power but associated with other features (such as serial or USB connections, Ethernet, etc.), these connectors or cables shall be left disconnected during the test.
(c) Any manual on-off switches specifically associated with maintaining the energy storage system at full charge or delivery of load power shall be switched on for the duration of the test.
4.3. Test Measurement and Calculation
Efficiency can be calculated from either average power or accumulated energy.
4.3.1. Average Power Calculations
If efficiency calculation are to be made using average power, calculate the average power consumption (P avg) by sampling the power at a rate of at least 1 sample per second and computing the arithmetic mean of all samples over the time period specified for each test as follows:
ER08SE22.005
Where:
P avg = average power
P i = power measured during individual measurement (i)
n = total number of measurements
4.3.2. Steady State
Operate the UUT and the load for a sufficient length of time to reach steady state conditions. To determine if steady state conditions have been attained, perform the following steady state check, in which the difference between the two efficiency calculations must be less than 1 percent:
(a)(1) Simultaneously measure the UUT's input and output power for at least 5 minutes, as specified in section 4.3.1 of this appendix, and record the average of each over the duration as P avg_in and P avg_out, respectively; or,
(2) Simultaneously measure the UUT's input and output energy for at least 5 minutes and record the accumulation of each over the duration as E in and E out, respectively.
(b) Calculate the UUT's efficiency, Eff 1, using one of the following two equations:
(1)
ER08SE22.006
Where:
Eff is the UUT efficiency
P avg_out is the average output power in watts
P avg_in is the average input power in watts
(2)
ER08SE22.007
Where:
Eff is the UUT efficiency
E out is the accumulated output energy in watt-hours
E in in the accumulated input energy in watt-hours
(c) Wait a minimum of 10 minutes.
(d) Repeat the steps listed in paragraphs (a) and (b) of section 4.3.2 of this appendix to calculate another efficiency value, Eff 2.
(e) Determine if the product is at steady state using the following equation:
ER08SE22.008
If the percentage difference of Eff 1 and Eff 2 as described in the equation, is less than 1 percent, the product is at steady state.
(f) If the percentage difference is greater than or equal to 1 percent, the product is not at steady state. Repeat the steps listed in paragraphs (c) to (e) of section 4.3.2 of this appendix until the product is at steady state.
4.3.3. Power Measurements and Efficiency Calculations
Measure input and output power of the UUT according to Section J.3 of Annex J of IEC 62040–3 Ed. 2.0, or measure the input and output energy of the UUT for efficiency calculations with the following exceptions:
(a) Test the UUT at the following reference test load conditions, in the following order: 100 percent, 75 percent, 50 percent, and 25 percent of the rated output power.
(b) Perform the test at each of the reference test loads by simultaneously measuring the UUT's input and output power in Watts (W), or input and output energy in Watt-Hours (Wh) over a 15 minute test period at a rate of at least 1 Hz. Calculate the efficiency for that reference load using one of the following two equations:
(1)
ER08SE22.009
Where:
Eff n % = the efficiency at reference test load n %
P avg_out n % = the average output power at reference load n %
P avg_in n % = the average input power at reference load n %
(2)
ER08SE22.010
Where:
Eff n % = the efficiency at reference test load n %
E out n % = the accumulated output energy at reference load n %
E in n % = the accumulated input energy at reference load n %
4.3.4. UUT Classification
Optional Test for determination of UPS architecture. Determine the UPS architecture by performing the tests specified in the definitions of VI, VFD, and VFI (sections 2.28.1 through 2.28.3 of this appendix).
4.3.5. Output Efficiency Calculation
(a) Use the load weightings from Table 4.3.1 to determine the average load adjusted efficiency as follows:
Eff avg = (t 25 % × Eff | 25 %) + (t 50 % × Eff | 50 %) + (t 75 % × Eff | 75 %) + (t 100 % × Eff | 100 %)
Where:
Eff avg = the average load adjusted efficiency
t n % = the portion of time spent at reference test load n % as specified in Table 4.3.1
Eff | n % = the measured efficiency at reference test load n %
Table 4.3.1—Load Weightings
| Rated output power (W) | UPS architecture | Portion of time spent at reference load | 25% | 50% | 75% | 100%
P ≤ 1500 W | VFD | 0.2 | 0.2 | 0.3 | 0.3
| VI or VFI | 0 * | 0.3 | 0.4 | 0.3
P > 1500 W | VFD, VI, or VFI | 0 * | 0.3 | 0.4 | 0.3
* Measuring efficiency at loading points with 0 time weighting is not required.
(b) Round the calculated efficiency value to one tenth of a percentage point.
5. Testing Requirements for Open-Placement Wireless Chargers
5.1. Standard Test Conditions and UUT Setup Requirements
The technician will set up the testing environment according to the test conditions as specified in sections 3.1.2, 3.1.3, and 3.1.4 of this appendix. The unit under test will be configurated according to section 3.2.1 and all other non-battery charger related functions will be turned off according to section 3.2.4.
5.2. Active Mode Test
[Reserved]
5.3. No-Battery Mode Test
(a) Connect the UUT to mains power and place it in no-battery mode by ensuring there are no foreign objects on the charging surface (i.e., without any load).
(b) Monitor the AC input power for a period of 5 minutes to assess the stability of the UUT. If the power level does not drift by more than 1percent from the maximum value observed, the UUT is considered stable.
(c) If the AC input power is not stable, follow the specifications in Section 5.3.3. of IEC 62301 for measuring average power or accumulated energy over time for the input. If the UUT is stable, record the measurements of the AC input power over a 5-minute period.
(d) Power consumption calculation. The power consumption of the no-battery mode is equal to the active AC input power (W).
