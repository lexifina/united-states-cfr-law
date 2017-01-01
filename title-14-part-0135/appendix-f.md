# Appendix F to Part 135—Airplane Flight Recorder Specification
The recorded values must meet the designated range, resolution and accuracy requirements during static and dynamic conditions. Dynamic condition means the parameter is experiencing change at the maximum rate attainable, including the maximum rate of reversal. All data recorded must be correlated in time to within one second.
Parameters | Range | Accuracy (sensor input) | Seconds per sampling interval | Resolution | Remarks
1. Time or Relative Time Counts 1 | 24 Hrs, 0 to 4095 | ±0.125% Per Hour | 4 | 1 sec | UTC time preferred when available. Counter increments each 4 seconds of system operation.
2. Pressure Altitude | −1000 ft to max certificated altitude of aircraft. + 5000 ft | ±100 to ±700 ft (see table, TSO C124a or TSO C51a) | 1 | 5′ to 35″ | Data should be obtained from the air data computer when practicable.
3. Indicated airspeed or Calibrated airspeed | 50 KIAS or minimum value to Max Vso≢ and Vso to 1.2 V.D | ±5% and ±3% | 1 | 1 kt | Data should be obtained from the air data computer when practicable.
4. Heading (Primary flight crew reference) | 0−360° and Discrete "true" or "mag" | ±2° | 1 | 0.5° | When true or magnetic heading can be selected as the primary heading reference, a discrete indicating selection must be recorded.
5. Normal Acceleration (Vertical) 9 | −3g to + 6g | ±1% of max range excluding datum error of ±5% | 0.125 | 0.004g
6. Pitch Attitude | ±75% | ±2° | 1 or 0.25 for airplanes operated under § 135.152(j) | 0.5° | A sampling rate of 0.25 is recommended.
7. Roll Attitude 2 | ±180° | ±2° | 1 or 0.5 0.5 airplanes operated under § 135.152(j) | 0.5° | A sampling rate of 0.5 is recommended.
8. Manual Radio Transmitter Keying or CVR/DFDR synchronization reference | On-Off (Discrete)None | | 1 | | Preferably each crew member but one discrete acceptable for all transmission provided the CVR/FDR system complies with TSO C124a CVR synchronization requirements (paragraph 4.2.1 ED-55).
9. Thrust/Power on each engine—primary flight crew reference | Full Range Forward | ±2% | 1 (per engine) | 0.3% of full range | Sufficient parameters (e.g. EPR, N1 or Torque, NP) as appropriate to the particular engine being recorded to determine power in forward and reverse thrust, including potential overspeed condition.
10. Autopilot Engagement | Discrete "on" or "off" | | 1 | |
11. Longitudinal Acceleration | ±1g | ±1.5% max. range excluding datum error of ±5% | 0.25 | 0.004g. |
12a. Pitch control(s) position (nonfly-by-wire systems) 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 or 0.25 for airplanes operated under § 135.152(j) | 0.5% of full range | For airplanes that have a flight control breakaway capability that allows either pilot to operate the controls independently, record both control inputs. The control inputs may be sampled alternately once per second to produce the sampling interval of 0.5 or 0.25, as applicable.
12b. Pitch control(s) position (fly-by-wire systems) 3 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 or 0.25 for airplanes operated under § 135.152(j) | 0.2% of full range
13a. Lateral control position(s) (nonfly-by-wire) 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 or 0.25 for airplanes operated under § 135.152(j) | 0.2% of full range | For airplanes that have a flight control breakaway capability that allows either pilot to operate the controls independently, record both control inputs. The control inputs may be sampled alternately once per second to produce the sampling interval of 0.5 or 0.25, as applicable.
13b. Lateral control position(s) (fly-by-wire) 4 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 or 0.25 for airplanes operated under § 135.152(j) | 0.2% of full range
14a. Yaw control position(s) (nonfly-by-wire) 5 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 | 0.3% of full range | For airplanes that have a flight control breakaway capability that allows either pilot to operate the controls independently, record both control inputs. The control inputs may be sampled alternately once per second to produce the sampling of 0.5 or 0.25, as applicable.
14b. Yaw control position(s) (fly-by-wire) 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 | 0.2% of full range
15. Pitch control surface(s) position 6 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 or 0.25 for airplanes operated under § 135.152(j). | 0.3% of full range | For airplanes fitted with multiple or split surfaces, a suitable combination of inputs is acceptable in lieu of recording each surface separately. The control surfaces may be sampled alternately to produce the sampling interval of 0.5 or 0.25, as applicable.
16. Lateral control surface(s) position 7 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 or 0.25 for airplanes operated under § 135.152(j) | 0.2% of full range | A suitable combination of surface position sensors is acceptable in lieu of recording each surface separately. The control surfaces may be sampled alternately to produce the sampling interval of 0.5 or 0.25, as applicable.
17. Yaw control surface(s) position 8 18 | Full Range | ±2° unless higher accuracy uniquely required | 0.5 | 0.2% of full range | For airplanes with multiple or split surfaces, a suitable combination of surface position sensors is acceptable in lieu of recording each surface separately. The control surfaces may be sampled alternately to produce the sampling interval of 0.5.
18. Lateral Acceleration | ±1g | ±1.5% max. range excluding datum error of ±5% | 0.25 | 0.004g
19. Pitch Trim Surface Position | Full Range | ±3° Unless Higher Accuracy Uniquely Required | 1 | 0.6% of full range
20. Trailing Edge Flap or Cockpit Control Selection 10 | Full Range or Each Position (discrete) | ±3° or as Pilot's Indicator | 2 | 0.5% of full range | Flap position and cockpit control may each be sampled alternately at 4 second intervals, to give a data point every 2 seconds.
21. Leading Edge Flap or Cockpit Control Selection 11 | Full Range or Each Discrete Position | ±3° or as Pilot's Indicator and sufficient to determine each discrete position | 2 | 0.5% of full range | Left and right sides, of flap position and cockpit control may each be sampled at 4 second intervals, so as to give a data point to every 2 seconds.
22. Each Thrust reverser Position (or equivalent for propeller airplane) | Stowed, In Transit, and reverse (Discrete) | | 1 (per engine | | Turbo-jet—2 discretes enable the 3 states to be determinedTurbo-prop—1 discrete
23. Ground Spoiler Position or Speed Brake Selection 12 | Full Range or Each Position (discrete) | ±2° Unless Higher Accuracy Uniquely Required | 1 or 0.5 for airplanes operated under § 135.152(j) | 0.5% of full range
24. Outside Air Temperature or Total Air Temperature 13 | −50 °C to + 90 °C | ±2 °C | 2 | 0.3 °C
25. Autopilot/Autothrottle/AFCS Mode and Engagement Status | A suitable combination of discretes | | 1 | | Discretes should show which systems are engaged and which primary modes are controlling the flight path and speed of the aircraft.
26. Radio Altitude 14 | −20 ft to 2,500 ft | ±2 ft or ±3% Whichever is Greater Below 500 ft and ±5% Above 500 ft | 1 | 1 ft + 5% above 500 ft | For autoland/category 3 operations. Each radio altimeter should be recorded, but arranged so that at least one is recorded each second.
27. Localizer Deviation, MLS Azimuth, or GPS Lateral Deviation | ±400 Microamps or available sensor range as installed ±62° | As installed ±3% recommended. | 1 | 0.3% of full range | For autoland/category 3 operations. Each system should be recorded but arranged so that at least one is recorded each second. It is not necessary to record ILS and MLS at the same time, only the approach aid in use need be recorded.
28. Glideslope Deviation, MLS Elevation, or GPS Vertical Deviation | ±400 Microamps or available sensor range as installed0.9 to + 30° | As installed ±3% recommended | 1 | 0.3% of full range | For autoland/category 3 operations. Each system should be recorded but arranged so that at least one is recorded each second. It is not necessary to record ILS and MLS at the same time, only the approach aid in use need be recorded.
29. Marker Beacon Passage | Discrete "on" or "off" | | 1 | | A single discrete is acceptable for all markers.
30. Master Warning | Discrete | | 1 | | Record the master warning and record each "red" warning that cannot be determined from other parameters or from the cockpit voice recorder.
31. Air/ground sensor (primary airplane system reference nose or main gear) | Discrete "air" or "ground" | | 1 (0.25 recommended.)
32. Angle of Attack (If measured directly) | As installed | As installed | 2 or 0.5 for airplanes operated under § 135.152(j) | 0.3% of full range | If left and right sensors are available, each may be recorded at 4 or 1 second intervals, as appropriate, so as to give a data point at 2 seconds or 0.5 second, as required.
33. Hydraulic Pressure Low, Each System | Discrete or available sensor range, "low" or "normal" | ±5% | 2 | 0.5% of full range. |
34. Groundspeed | As installed | Most Accurate Systems Installed | 1 | 0.2% of full range. |
35. GPWS (ground proximity warning system) | Discrete "warning" or "off" | | 1 | | A suitable combination of discretes unless recorder capacity is limited in which case a single discrete for all modes is acceptable.
36. Landing Gear Position or Landing gear cockpit control selection | Discrete | | 4 | | A suitable combination of discretes should be recorded.
37. Drift Angle 15 | As installed | As installed | 4 | 0.1°
38. Wind Speed and Direction | As installed | As installed | 4 | 1 knot, and 1.0°. |
39. Latitude and Longitude | As installed | As installed | 4 | 0.002°, or as installed | Provided by the Primary Navigation System Reference. Where capacity permits latitude/longitude resolution should be 0.0002°.
40. Stick shaker and pusher activation | Discrete(s) "on" or "off" | | 1 | | A suitable combination of discretes to determine activation.
41. Windshear Detection | Discrete "warning" or "off" | | 1.
42. Throttle/power lever position 16 | Full Range | ±2% | 1 for each lever | 2% of full range | For airplanes with non-mechanically linked cockpit engine controls.
43. Additional Engine Parameters | As installed | As installed | Each engine each second | 2% of full range | Where capacity permits, the preferred priority is indicated vibration level, N2, EGT, Fuel Flow, Fuel Cut-off lever position and N3, unless engine manufacturer recommends otherwise.
44. Traffic Alert and Collision Avoidance System (TCAS) | Discretes | As installed | 1 | | A suitable combination of discretes should be recorded to determine the status of—Combined Control, Vertical Control, Up Advisory, and down advisory. (ref. ARINC Characteristic 735 Attachment 6E, TCAS VERTICAL RA DATA OUTPUT WORD.)
45. DME 1 and 2 Distance | 0-200 NM; | As installed | 4 | 1 NM | 1 mile.
46. Nav 1 and 2 Selected Frequency | Full range | As installed | 4 | | Sufficient to determine selected frequency.
47. Selected barometric setting | Full Range | ±5% | (1 per 64 sec.) | 0.2% of full range.
48. Selected altitude | Full Range | ±5% | 1 | 100 ft.
49. Selected speed | Full Range | ±5% | 1 | 1 knot.
50. Selected Mach | Full Range | ±5% | 1 | .01.
51. Selected vertical speed | Full Range | ±5% | 1 | 100 ft./min.
52. Selected heading | Full Range | ±5% | 1 | 1°.
53. Selected flight path | Full Range | ±5% | 1 | 1°. |
54. Selected decision height | Full Range | ±5% | 64 | 1 ft.
55. EFIS display format | Discrete(s) | | 4 | | Discretes should show the display system status (e.g., off, normal, fail, composite, sector, plan, nav aids, weather radar, range, copy.
56. Multi-function/Engine Alerts Display format | Discrete(s) | | 4 | | Discretes should show the display system status (e.g., off, normal, fail, and the identity of display pages for emergency procedures, need not be recorded.
57. Thrust comand 17 | Full Range | ±2% | 2 | 2% of full range
58. Thrust target | Full Range | ±2% | 4 | 2% of full range.
59. Fuel quantity in CG trim tank | Full Range | ±5% | (1 per 64 sec.) | 1% of full range.
60. Primary Navigation System Reference | Discrete GPS, INS, VOR/DME, MLS, Loran C, Omega, Localizer Glidescope | | 4 | | A suitable combination of discretes to determine the Primary Navigation System reference.
61. Ice Detection | Discrete "ice" or "no ice" | | 4.
62. Engine warning each engine vibration | Discrete | | 1.
63. Engine warning each engine over temp. | Discrete | | 1.
64. Engine warning each engine oil pressure low | Discrete | | 1.
65. Engine warning each engine over speed | Discrete | | 1.
66. Yaw Trim Surface Position | Full Range | ±3% Unless Higher Accuracy Uniquely Required | 2 | 0.3% of full range.
67. Roll Trim Surface Position | Full Range | ±3% Unless Higher Accuracy Uniquely Required | 2 | 0.3% of full range.
68. Brake Pressure (left and right) | As installed | ±5% | 1 | | To determine braking effort applied by pilots or by autobrakes.
69. Brake Pedal Application (left and right) | Discrete or Analog "applied" or "off" | ±5% (Analog) | 1 | | To determine braking applied by pilots.
70. Yaw or sideslip angle | Full Range | ±5% | 1 | 0.5°.
71. Engine bleed valve position | Discrete "open" or "closed" | | 4.
72. De-icing or anti-icing system selection | Discrete "on" or "off" | | 4.
73. Computed center of gravity | Full Range | ±5% | (1 per 64 sec.) | 1% of full range.
74. AC electrical bus status | Discrete "power" or "off" | | 4 | | Each bus.
75. DC electrical bus status | Discrete "power" or "off" | | 4 | | Each bus.
76. APU bleed valve position | Discrete "open" or "closed" | | 4.
77. Hydraulic Pressure (each system) | Full range | ±5% | 2 | 100 psi.
78. Loss of cabin pressure | Discrete "loss" or "normal" | | 1.
79. Computer failure (critical flight and engine control systems) | Discrete "fail" or "normal" | | 4.
80. Heads-up display (when an information source is installed) | Discrete(s) "on" or "off" | | 4.
81. Para-visual display (when an information source is installed) | Discrete(s) "on" or "off" | | 1.
82. Cockpit trim control input position—pitch | Full Range | ±5% | 1 | 0.2% of full range | Where mechanical means for control inputs are not available, cockpit display trim positions should be recorded.
83. Cockpit trim control input position—roll | Full Range | ±5% | 1 | 0.7% of full range | Where mechanical means for control inputs are not available, cockpit display trim position should be recorded.
84. Cockpit trim control input position—yaw | Full Range | ±5% | 1 | 0.3% of full range | Where mechanical means for control input are not available, cockpit display trim positions should be recorded.
85. Trailing edge flap and cockpit flap control position | Full Range | ±5% | 2 | 0.5% of full range | Trailing edge flaps and cockpit flap control position may each be sampled alternately at 4 second intervals to provide a sample each 0.5 second.
86. Leading edge flap and cockpit flap control position | Full Range or Discrete | ±5% | 1 | 0.5% of full range.
87. Ground spoiler position and speed brake selection | Full Range or Discrete | ±5% | 0.5 | 0.3% of full range
88. All cockpit flight control input forces (control wheel, control column, rudder pedal) 18 | Full Range Control wheel ±70 lbs. Control column ±85 lbs. Rudder pedal ±165 lbs | ±5° | 1 | 0.3% of full range | For fly-by-wire flight control systems, where flight control surface position is a function of the displacement of the control input device only, it is not necessary to record this parameter. For airplanes that have a flight control breakaway capability that allows either pilot to operate the control independently, record both control force inputs. The control force inputs may be sampled alternately once per 2 seconds to produce the sampling interval of 1.
1 For A300 B2/B4 airplanes, resolution = 6 seconds.
2 For A330/A340 series airplanes, resolution = 0.703°.
3 For A318/A319/A320/A321 series airplanes, resolution = 0.275% (0.088°>0.064°). For A330/A340 series airplanes, resolution = 2.20% (0.703°>0.064°).
4 For A318/A319/A320/A321 series airplanes, resolution = 0.22% (0.088°>0.080°). For A330/A340 series airplanes, resolution = 1.76% (0.703°>0.080°).
5 For A330/A340 series airplanes, resolution = 1.18% (0.703°>0.120°).
6 For A330/A340 series airplanes, resolution = 0.783% (0.352°>0.090°).
7 For A330/A340 series airplanes, aileron resolution = 0.704% (0.352°>0.100°). For A330/A340 series airplanes, spoiler resolution = 1.406% (0.703°>0.100°).
8 For A330/A340 series airplanes, resolution = 0.30% (0.176°>0.12°). For A330/A340 series airplanes, seconds per sampling interval = 1.
9 For B-717 series airplanes, resolution =.005g. For Dassault F900C/F900EX airplanes, resolution =.007g.
10 For A330/A340 series airplanes, resolution = 1.05% (0.250°>0.120°).
11 For A330/A340 series airplanes, resolution = 1.05% (0.250°>0.120°). For A300 B2/B4 series airplanes, resolution = 0.92% (0.230°>0.125°).
12 For A330/A340 series airplanes, spoiler resolution = 1.406% (0.703°>0.100°).
13 For A330/A340 series airplanes, resolution = 0.5 °C.
14 For Dassault F900C/F900EX airplanes, Radio Altitude resolution = 1.25 ft.
15 For A330/A340 series airplanes, resolution = 0.352 degrees.
16 For A318/A319/A320/A321 series airplanes, resolution = 4.32%. For A330/A340 series airplanes, resolution is 3.27% of full range for throttle lever angle (TLA); for reverse thrust, reverse throttle lever angle (RLA) resolution is nonlinear over the active reverse thrust range, which is 51.54 degrees to 96.14 degrees. The resolved element is 2.8 degrees uniformly over the entire active reverse thrust range, or 2.9% of the full range value of 96.14 degrees.
17 For A318/A319/A320/A321 series airplanes, with IAE engines, resolution = 2.58%.
18 For all aircraft manufactured on or after December 6, 2010, the seconds per sampling interval is 0.125. Each input must be recorded at this rate. Alternately sampling inputs (interleaving) to meet this sampling interval is prohibited.
