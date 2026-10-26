# Appendix E to Part 404—Content and Syntax for Papaha naumokua kea Ship Reporting System
Immediately upon crossing the reporting area boundary, notification should be sent as a direct e-mail to nwhi.notifications@noaa.gov in the prescribed format and data syntax shown. Use of batch message routing services which may delay receipt of a report should not be used. Failure to follow the exact format (e.g., extra information, extraneous characters, or double spacing) may cause the automated computer system to reject your report.
Note: Report transmission costs via INMARSAT-C will be assumed by NOAA.
E.1 Entry Notification Format
Immediately upon entering the Reporting Area, vessels required to participate must provide the following information.
Table E.1—Information required for entry notification
Telegraphy | Function | Information required | Example field text
System identifier | CORAL SHIPREP // | CORAL SHIPREP //
A | Ship | Vessel name/call sign/flag/IMO number/Federal documentation or State registration number if applicable // | A/OCEAN VOYAGER/C5FU8/BAHAMAS/IMO 9359165//
B | Date, time (UTC), and month of entry | A 6-digit group giving day of month (first two digits), hours and minutes (last four digits) in coordinated universal time, suffixed by the letter Z (indicating time in UTC), and three letters indicating month // | B/271107Z DEC//
C | Position | A 4-digit group giving latitude in degrees and minutes, suffixed with the letter N (indicating north), followed by a single /, and a five-digit group giving longitude in degrees and minutes, suffixed with the letter W (indicating west) // [Report in the World Geodetic System 1984 Datum (WGS-84)] | C/2728N/17356W//
E | True course | 3-digit number indicating true course // | E/180//
F | Speed in knots and tenths | 3-digit group indicating knots decimal tenths // | F/20.5//
I | Destination and estimated time of arrival | Name of port city/country/estimated arrival date and time group expressed as in (B) // | I/SEATTLE/USA/311230Z DEC//
L | Intended route through the reporting area | Route information should be reported as a direct rhumbline (RL) course through the reporting area and intended speed (expressed as in E and F) or a series of waypoints (WP). Each waypoint entry should be reported as latitude and longitude, expressed as in (C), and intended speed between waypoints (as in F) // (Note: As many "L" lines as needed may be used to describe the vessel's intended route.) | L/RL/215/20.5// -OR- L/WP/2734N/17352W/20.5// L/WP/2641N/17413W/20.5// L/WP/2605N/17530W/20.5//
O | Vessel draft in meters | Maximum present static draft reported in meters decimal centimeters // | O/11.50//
P | Categories of Hazardous Cargoes* | Classification Code (e.g. IMDG, IBC, IGC, INF) / and all corresponding Categories of Hazardous Cargoes (delimited by commas) // Note: If necessary, use a separate "P" line for each type of Classification Code | P/IMDG/1.4G,2.1,2.2,2.3,3,4.1,6.1,8,9//
Q | Defects or deficiencies** | Brief details of defects, damage, deficiencies or limitations that restrict maneuverability or impair normal navigation // (If none, enter the number zero.) | Q/Include details as required//
R | Pollution incident or goods lost overboard** | Description of pollution incident or goods lost overboard within the Monument, the Reporting Area, or the U.S. Exclusive Economic Zone//(If none, enter the number zero.) | R/0//
T | Contact information of ship's agent or owner | Name/address/and phone number of ship's agent or owner // | T/JOHN DOE/GENERIC SHIPPING COMPANY INC, 6101 ACME ROAD, ROOM 123, CITY, STATE, COUNTRY 12345/123-123-1234//
U | Ship size (length overall and gross tonnage) and type | Length overall reported in meters decimal centimeters/number of gross tons/type of ship (e.g. bulk carrier, chemical tanker, oil tanker, gas tanker, container, general cargo, fishing vessel, research, passenger, OBO, RORO) // | U/294.14/54592/CONTAINER SHIP//
W | Persons | Total number of persons on board // | W/15//
Table E.1 Notes *Categories of hazardous cargoes means goods classified in the International Maritime Dangerous Goods (IMDG) Code; substances classified in chapter 17 of the International Code for the Construction and Equipment of Ships Carrying Dangerous Chemicals in Bulk (IBC Code) and chapter 19 of the International Code for the Construction and Equipment of Ships Carrying Liquefied Gases in Bulk (IGC Code); oils as defined in MARPOL Annex I; noxious liquid substances as defined in MARPOL Annex II; harmful substances as defined in MARPOL Annex III; and radioactive materials specified in the Code for the Safe Carriage of the Irradiated Nuclear Fuel, Plutonium and High-Level Radioactive Wastes in Flasks on Board Ships (INF Code). **In accordance with the provisions of the MARPOL Convention, ships must report information relating to defects, damage, deficiencies or other limitations as well as, if necessary, information relating to pollution incidents or loss of cargo. Safety related reports must be provided to CORAL SHIPREP without delay should a ship suffer damage, failure or breakdown affecting the safety of the ship (Item Q), or if a ship makes a marked deviation from a route, course or speed previously advised (Item L). Pollution or cargo lost overboard must be reported without delay (Item R).
E.2 Prior Notification of Entry Format
Vessels of the United States less than 300 gross tonnage that are not equipped with onboard email capability must provide the following notification of entry at least 72 hrs, but no longer than 1 month, prior to entry date, utilizing the data syntax described above. Notification may be made via the following communication methods, listed in order of preference: Email [nwhi.notifications@noaa.gov]; fax [1-808-455-3093]; telephone [1-866-478-NWHI (6944)].
Table E.2—Information Required for Prior Notification
System identifier | PRIOR NOTICE //.
Items | A, B, C (as applicable), I, L, O, P (as applicable), Q, T, U, W.
E.3 Exit Notification Format
Immediately upon leaving the Reporting Area, vessels required to participate must provide the following information. Vessels of the United States less than 300 gross tonnage that are not equipped with onboard email capability must provide the following Exit Notification information within 12 hrs of leaving the Reporting Area. Notification may be made via the following communication methods, listed in order of preference: Email [nwhi.notifications@noaa.gov]; fax [1-808-455-3093]; telephone [1-866-478-NWHI (6944)].
Table E.3—Information Required for Exit Notification
Telegraphy | Function | Information required | Example field text
System identifier | CORAL SHIPREP // | CORAL SHIPREP//
A | Ship | Vessel name / call sign / flag / IMO number / Federal documentation or State registration number if applicable // | A/OCEAN VOYAGER/C5FU8/BAHAMAS/IMO9359165//
B | Date, time (UTC), and month of exit | A 6-digit group giving day of month (first two digits), hours and minutes (last four digits), suffixed by the letter Z indicating time in UTC, and three letters indicating month// | B/271657Z DEC//
C | Position | A 4-digit group giving latitude in degrees and minutes, suffixed with the letter N (indicating north), followed by a single //, and a five digit group giving longitude in degrees and minutes, suffixed with the letter W (indicating west) // [Report in the World Geodetic System 1984 Datum (WGS-84)] | C/2605N/17530W//
R | Pollution incident or goods lost overboard | Description of pollution incident or goods lost overboard within the Monument, the Reporting Area, or the U.S. Exclusive Economic Zone // (If none, enter the number zero) | R/0//
E.4 Example Entry Report
CORAL SHIPREP//
A/SEA ROVER/WFSU/USA/IMO 8674208/DOC 602011//
B/010915Z JUN//
C/2636N/17600W//
E/050//
F/20.0//
I/LOS ANGELES/USA/081215Z JUN//
L/RL/050/20.0//
O/10.90//
P/IMDG/3,4.1,6.1,8,9//
Q/0//
R/0//
T/JOHN DOE/CONTAINER SHIPPERS INC, 500 PORT ROAD, ROOM 123, LOS ANGELES, CA, USA 90050/213-123-1234//
U/199.90/27227/CONTAINER SHIP//
W/15//
E.5 Example Exit Report
CORAL SHIPREP//
A/SEA ROVER/WFSU/USA/IMO 8674208/DOC 602011//
B/011515Z JUN//
C/2747N/17416W//
R/0//
