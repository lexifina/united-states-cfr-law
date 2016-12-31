# Appendix A to Subpart R of Part 431—Uniform Test Method for the Measurement of Energy Consumption of the Components of Envelopes of Walk-In Coolers and Walk-In Freezers
1.0 Scope
This appendix covers the test requirements used to measure the energy consumption of the components that make up the envelope of a walk-in cooler or walk-in freezer.
2.0 Definitions
The definitions contained in § 431.302 are applicable to this appendix.
3.0 Additional Definitions
3.1 Automatic door opener/closer means a device or control system that "automatically" opens and closes doors without direct user contact, such as a motion sensor that senses when a forklift is approaching the entrance to a door and opens it, and then closes the door after the forklift has passed.
3.2 Core region means the part of the panel that is not the edge region.
3.3 Edge region means a region of the panel that is wide enough to encompass any framing members and edge effects. If the panel contains framing members (e.g. a wood frame) then the width of the edge region must be as wide as any framing member plus 2 in. ±0.25 in. If the panel does not contain framing members then the width of the edge region must be 4 in ±0.25 in. For walk-in panels that utilize vacuum insulated panels (VIP) for insulation, the width of the edge region must be the lesser of 4.5 in. ±1 in. or the maximum width that does not cause the VIP to be pierced by the cutting device when the edge region is cut.
3.4 Surface area means the area of the surface of the walk-in component that would be external to the walk-in. For example, for panel, the surface area would be the area of the side of the panel that faces the outside of the walk-in. It would not include edges of the panel that are not exposed to the outside of the walk-in.
3.5 Rating conditions means, unless explicitly stated otherwise, all conditions shown in Table A.1. For installations where two or more walk-in envelope components share any surface(s), the "external conditions" of the shared surface(s) must reflect the internal conditions of the adjacent walk-in. For example, if a walk-in component divides a walk-in freezer from a walk-in cooler, then the internal conditions are the freezer rating conditions and the external conditions are the cooler rating conditions.
3.6 Percent time off (PTO) means the percent of time that an electrical device is assumed to be off.
Table A.1—Temperature Conditions
Internal Temperatures (cooled space within the envelope)
Cooler Dry Bulb Temperature | 35 °F.
Freezer Dry Bulb Temperature | −10 °F.
External Temperatures (space external to the envelope)
Freezer and Cooler Dry Bulb Temperatures | 75 °F.
Subfloor Temperatures
Freezer and Cooler Dry Bulb Temperatures | 55 °F.
4.0 Calculation Instructions
4.1 Display Panels
(a) Calculate the U-factor of the display panel in accordance with section 5.3 of this appendix, Btu/h-ft2- °F.
(b) Calculate the display panel surface area, as defined in section 3.4 of this appendix, Adp, ft2, with standard geometric formulas or engineering software.
(c) Calculate the temperature differential, ΔTdp, °F, for the display panel, as follows:
ER09JN11.003
Where:
TDB,ext,dp = dry-bulb air external temperature, °F, as prescribed in Table A.1; and
TDB,int,dp = dry-bulb air temperature internal to the cooler or freezer, °F, as prescribed in Table A.1.
(d) Calculate the conduction load through the display panel, Qcond-dp, Btu/h, as follows:
ER09JN11.004
Where:
Adp = surface area of the walk-in display panel, ft2;
ΔTdp = temperature differential between refrigerated and adjacent zones, °F; and
Udp = thermal transmittance, U-factor, of the display panel in accordance with section 5.3 of this appendix, Btu/h-ft2- °F.
(e) Select Energy Efficiency Ratio (EER), as follows:
(1) For coolers, use EER = 12.4 Btu/W-h
(2) For freezers, use EER = 6.3 Btu/W-h
(f) Calculate the total daily energy consumption, Edp, kWh/day, as follows:
ER09JN11.005
Where:
Qcond, dp = the conduction load through the display panel, Btu/h; and EER = EER of walk-in (cooler or freezer), Btu/W-h.
4.2 [Reserved]
4.3 [Reserved]
4.4 Display Doors
4.4.1 Conduction Through Display Doors
(a) Calculate the U-factor of the door in accordance with section 5.3 of this appendix, Btu/h-ft2- °F
(b) Calculate the surface area, as defined in section 3.4 of this appendix, of the display door, Add, ft2, with standard geometric formulas or engineering software.
(c) Calculate the temperature differential, ΔTdd, °F, for the display door as follows:
ER09JN11.020
Where:
TDB,ext, dd = dry-bulb air temperature external to the display door, °F, as prescribed in Table A.1; and
TDB,int, dd = dry-bulb air temperature internal to the display door, °F, as prescribed in Table A.1.
(d) Calculate the conduction load through the display doors, Qcond-dd, Btu/h, as follows:
ER09JN11.021
Where:
ΔTdd = temperature differential between refrigerated and adjacent zones, °F;
Add = surface area walk-in display doors, ft2; and
Udd = thermal transmittance, U-factor of the door, in accordance with section 5.3 of this appendix, Btu/h-ft2- °F.
4.4.2 Direct Energy Consumption of Electrical Component(s) of Display Doors
Electrical components associated with display doors could include, but are not limited to: heater wire (for anti-sweat or anti-freeze application); lights (including display door lighting systems); control system units; and sensors.
(a) Select the required value for percent time off (PTO) for each type of electricity consuming device, PTOt (%)
(1) For lights without timers, control system or other demand-based control, PTO = 25 percent. For lighting with timers, control system or other demand-based control, PTO = 50 percent.
(2) For anti-sweat heaters on coolers (if included): Without timers, control system or other demand-based control, PTO = 0 percent. With timers, control system or other demand-based control, PTO = 75 percent. For anti-sweat heaters on freezers (if included): Without timers, control system or other auto-shut-off systems, PTO = 0 percent. With timers, control system or other demand-based control, PTO = 50 percent.
(3) For all other electricity consuming devices: Without timers, control system, or other auto-shut-off systems, PTO = 0 percent. If it can be demonstrated that the device is controlled by a preinstalled timer, control system or other auto-shut-off system, PTO = 25 percent.
(b) Calculate the power usage for each type of electricity consuming device, Pdd-comp,u,t, kWh/day, as follows:
ER09JN11.022
Where:
u = the index for each of type of electricity-consuming device located on either (1) the interior facing side of the display door or within the inside portion of the display door, (2) the exterior facing side of the display door, or (3) any combination of (1) and (2). For purposes of this calculation, the interior index is represented by u = int and the exterior index is represented by u = ext. If the electrical component is both on the interior and exterior side of the display door then u = int. For anti-sweat heaters sited anywhere in the display door, 75 percent of the total power is be attributed to u = int and 25 percent of the total power is attributed to u = ext;
t = index for each type of electricity consuming device with identical rated power;
Prated,u,t = rated power of each component, of type t, kW;
PTOu,t = percent time off, for device of type t, %; and
nu,t = number of devices at the rated power of type t, unitless.
(c) Calculate the total electrical energy consumption for interior and exterior power, Pdd-tot, int (kWh/day) and Pdd-tot, ext (kWh/day), respectively, as follows:
ER09JN11.023
Where:
t = index for each type of electricity consuming device with identical rated power;
Pdd-comp,int, t = the energy usage for an electricity consuming device sited on the interior facing side of or in the display door, of type t, kWh/day; and
Pdd-comp,ext, t = the energy usage for an electricity consuming device sited on the external facing side of the display door, of type t, kWh/day.
(d) Calculate the total electrical energy consumption, Pdd-tot, (kWh/day), as follows:
ER09JN11.024
Where:
Pdd-tot,int = the total interior electrical energy usage for the display door, kWh/day; and
Pdd-tot,ext = the total exterior electrical energy usage for the display door, kWh/day.
4.4.3 Total Indirect Electricity Consumption Due to Electrical Devices
(a) Select Energy Efficiency Ratio (EER), as follows:
(1) For coolers, use EER = 12.4 Btu/Wh
(2) For freezers, use EER = 6.3 Btu/Wh
(b) Calculate the additional refrigeration energy consumption due to thermal output from electrical components sited inside the display door, Cdd-load, kWh/day, as follows:
ER09JN11.025
Where:
EER = EER of walk-in cooler or walk-in freezer, Btu/W-h; and
Pdd-tot,int = The total internal electrical energy consumption due for the display door, kWh/day.
4.4.4 Total Display Door Energy Consumption
(a) Select Energy Efficiency Ratio (EER), as follows:
(1) For coolers, use EER = 12.4 Btu/W-h
(2) For freezers, use EER = 6.3 Btu/W-h
(b) Calculate the total daily energy consumption due to conduction thermal load, Edd, thermal, kWh/day, as follows:
ER09JN11.026
Where:
Qcond, dd = the conduction load through the display door, Btu/h; and
EER = EER of walk-in (cooler or freezer), Btu/W-h.
(c) Calculate the total energy, Edd,tot, kWh/day,
ER09JN11.027
Where:
Edd, thermal = the total daily energy consumption due to thermal load for the display door, kWh/day;
Pdd-tot = the total electrical load, kWh/day; and
Cdd-load = additional refrigeration load due to thermal output from electrical components contained within the display door, kWh/day.
4.5 Non-Display Doors
4.5.1 Conduction Through Non-Display Doors
(a) Calculate the surface area, as defined in section 3.4 of this appendix, of the non-display door, And, ft2, with standard geometric formulas or with engineering software.
(b) Calculate the temperature differential of the non-display door, ΔTnd, °F, as follows:
ER09JN11.028
Where:
TDB,ext, nd = dry-bulb air external temperature, °F, as prescribed by Table A.1; and
TDB,int, nd = dry-bulb air internal temperature, °F, as prescribed by Table A.1. If the component spans both cooler and freezer spaces, the freezer temperature must be used.
(c) Calculate the conduction load through the non-display door: Qcond-nd, Btu/h,
ER09JN11.029
Where:
ΔTnd = temperature differential across the non-display door, °F;
Und = thermal transmittance, U-factor of the door, in accordance with section 5.3 of this appendix, Btu/h-ft2- °F; and
And = area of non-display door, ft2.
4.5.2 Direct Energy Consumption of Electrical Components of Non-Display Doors
Electrical components associated with a walk-in non-display door comprise any components that are on the non-display door and that directly consume electrical energy. This includes, but is not limited to, heater wire (for anti-sweat or anti-freeze application), control system units, and sensors.
(a) Select the required value for percent time off for each type of electricity consuming device, PTOt (%)
(1) For lighting without timers, control system or other demand-based control, PTO = 25 percent. For lighting with timers, control system or other demand-based control, PTO = 50 percent.
(2) For anti-sweat heaters on coolers (if included): Without timers, control system or other demand-based control, PTO = 0 percent. With timers, control system or other demand-based control, PTO = 75 percent. For anti-sweat heaters on freezers (if included): Without timers, control system or other auto-shut-off systems, PTO = 0 percent. With timers, control system or other demand-based control, PTO = 50 percent.
(3) For all other electricity consuming devices: Without timers, control system, or other auto-shut-off systems, PTO = 0 percent. If it can be demonstrated that the device is controlled by a preinstalled timer, control system or other auto-shut-off system, PTO = 25 percent.
(b) Calculate the power usage for each type of electricity consuming device, Pnd-comp,u,t, kWh/day, as follows:
ER09JN11.030
Where:
u = the index for each of type of electricity-consuming device located on either (1) the interior facing side of the display door or within the inside portion of the display door, (2) the exterior facing side of the display door, or (3) any combination of (1) and (2). For purposes of this calculation, the interior index is represented by u = int and the exterior index is represented by u = ext. If the electrical component is both on the interior and exterior side of the display door then u = int. For anti-sweat heaters sited anywhere in the display door, 75 percent of the total power is be attributed to u = int and 25 percent of the total power is attributed to u = ext;
t = index for each type of electricity consuming device with identical rated power;
Prated,u,t = rated power of each component, of type t, kW;
PTOu,t = percent time off, for device of type t, %; and
nu,t = number of devices at the rated power of type t, unitless.
(c) Calculate the total electrical energy consumption for interior and exterior power, Pnd-tot, int (kWh/day) and Pnd-tot, ext (kWh/day), respectively, as follows:
ER09JN11.031
Where:
t = index for each type of electricity consuming device with identical rated power;
Pnd-comp,int, t = the energy usage for an electricity consuming device sited on the internal facing side or internal to the non-display door, of type t, kWh/day; and
Pnd-comp,ext, t = the energy usage for an electricity consuming device sited on the external facing side of the non-display door, of type t, kWh/day. For anti-sweat heaters,
(d) Calculate the total electrical energy consumption, Pnd-tot, kWh/day, as follows:
ER09JN11.032
Where:
Pnd-tot,int = the total interior electrical energy usage for the non-display door, of type t, kWh/day; and
Pnd-tot,ext = the total exterior electrical energy usage for the non-display door, of type t, kWh/day.
4.5.3 Total Indirect Electricity Consumption Due to Electrical Devices
(a) Select Energy Efficiency Ratio (EER), as follows:
(1) For coolers, use EER = 12.4 Btu/Wh
(2) For freezers, use EER = 6.3 Btu/Wh
(b) Calculate the additional refrigeration energy consumption due to thermal output from electrical components associated with the non-display door, Cnd-load, kWh/day, as follows:
ER09JN11.033
Where:
EER = EER of walk-in cooler or freezer, Btu/W-h; and
Pnd-tot,int = the total interior electrical energy consumption for the non-display door, kWh/day.
4.5.4 Total Non-Display Door Energy Consumption
(a) Select Energy Efficiency Ratio (EER), as follows:
(1) For coolers, use EER = 12.4 Btu/W-h
(2) For freezers, use EER = 6.3 Btu/W-h
(b) Calculate the total daily energy consumption due to thermal load, End, thermal, kWh/day, as follows:
ER09JN11.034
Where:
Qcond-nd = the conduction load through the non-display door, Btu/hr; and
EER = EER of walk-in (cooler or freezer), Btu/W-h.
(c) Calculate the total energy, End,tot, kWh/day, as follows:
ER09JN11.035
Where:
End, thermal = the total daily energy consumption due to thermal load for the non-display door, kWh/day;
Pnd-tot = the total electrical energy consumption, kWh/day; and
Cnd-load = additional refrigeration load due to thermal output from electrical components contained on the inside face of the non-display door, kWh/day.
5.0 Test Methods and Measurements
5.1-5.2 [Reserved]
5.3 U-factor of Doors and Display Panels
(a) Follow the procedure in NFRC 100, (incorporated by reference; see § 431.303), exactly, with these exceptions:
(1) The average surface heat transfer coefficient on the cold-side of the apparatus shall be 30 Watts per square-meter-Kelvin (W/m2*K) ±5%. The average surface heat transfer coefficient on the warm-side of the apparatus shall be 7.7 Watts per square-meter-Kelvin (W/m2*K) ±5%.
(2) Cold-side conditions:
(i) Air temperature of 35 °F (1.7 °C) for cooler doors and −10 °F (−23.3 °C) for freezer doors
(ii) Mean inside radiant temperature must be the same as shown in section 5.3(a)(2)(i), above.
(3) Warm-side conditions
(i) Air temperature of 75 °F (23.9 °C)
(ii) Mean outside radiant temperature must be the same as section 5.3(a)(3)(i), above.
(4) Direct solar irradiance = 0 W/m2 (Btu/h-ft2).
(b) Required Test Measurements
(i) Display Doors and Display Panels
1. Thermal Transmittance: Udd
(ii) Non-Display Door
1. Thermal Transmittance: Und
At 81 FR 95803, Dec. 28, 2016, Appendix A to Subpart R of Part 431 was amended by removing and reserving sections 3.2 and 3.3; revising section 3.4; redesignating sections 3.5 and 3.6 as sections 3.6 and 3.7; adding section 3.5; revising newly redesignated section 3.6; and revising Table A.1, effective Jan. 27, 2017. For the convenience of the user, the added and revised text is set forth as follows:
Appendix A to Subpart R of Part 431—Uniform Test Method for the Measurement of Energy Consumption of the Components of Envelopes of Walk-In Coolers and Walk-In Freezers
3.2 [Reserved]
3.3 [Reserved]
3.4 Surface area means the area of the surface of the walk-in component that would be external to the walk-in cooler or walk-in freezer as appropriate.
3.5 Rated power means the electricity consuming device's power as specified on the device's nameplate. If the device does not have a nameplate or such nameplate does not list the device's power, then the rated power must be read from the device's product data sheet.
3.6 Rating conditions means, unless explicitly stated otherwise, all conditions shown in Table A.1 of this section.
Table A.1—Temperature Conditions
|
Internal Temperatures (cooled space within the envelope)
Cooler Dry Bulb Temperature | 35 °F
Freezer Dry Bulb Temperature | −10 °F
External Temperatures (space external to the envelope)
Freezer and Cooler Dry Bulb Temperatures | 75 °F.
