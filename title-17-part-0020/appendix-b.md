# Appendix B to Part 20—Explanatory Guidance on Data Record Layouts
Record Layout Examples for § 20.3
The following example (in Tables 1, 2 and 3) covers reporting for a particular clearing organization. "Clearing Organization One" would report, for the 27th of September 2010, the following eleven unique data record submissions. Each data record submission represents a unique position, as indicated by § 20.3, held by a clearing member of Clearing Organization One. Paragraph (a) of § 20.3 broadly outlines the data elements that determine unique positions for reports on clearing member positions. Paragraphs (b) of § 20.3 present all of the data elements that should be submitted in reference to a particular data record for a particular clearing member (in Table 1). Paragraph (c) identifies data elements that would comprise end of day record data on cleared products (in Tables 2 and 3). Therefore, paragraphs (b) and (c) of § 20.3 present all of the data elements that should be submitted in reference to a particular data record.
Because CFTC designated Clearing Organization One (in this example) currently has two clearing members, "Clearing Member One" and "Clearing Member Two," positions cleared for these two distinct clearing members would be subdivided.
In the following example it is assumed that the clearing member accounts are either proprietary or customer (but not both) and therefore data record submissions do not have to be delineated by these account types. However, if clearing members did have both proprietary and customer accounts, then a clearing organization would have to further subdivide these clearing member data records by these two account types.
Clearing Member One currently has five positions with multiple cleared product IDs and futures equivalent months/years, and therefore these positions also constitute separate data records.
Clearing Member Two currently has six positions with the following varying characteristics: Cleared product IDs; futures equivalent months/years; commodity reference prices; swaption positions that involve both puts and calls; and multiple strike prices. Accordingly, these positions must be reported in separate data records. An illustration of how these records would appear is included in Table 1 below. Clearing Organization One would also have to report the corresponding swaption position deltas, strike prices, expiration dates, and settlement prices and swap settlement prices. An illustration of these submissions is included in Tables 2 and 3 below.
Table 1—Data Records Reported Under Paragraphs (a) and (b) of § 20.3
Data records | CFTC clearing org ID | Clearing org clearing member ID | Clearing org cleared product ID | Reporting day | Proprietary/customer account indicator | Futures equivalent month and year | Commodity reference price
Data record 1 | CCO_ID_1 | CM_ID_2 | CP_04 | 9/27/2010 | C | Nov-10 | NYMEX NY Harbor No.2.
Data record 2 | CCO_ID_1 | CM_ID_2 | CP_04 | 9/27/2010 | C | Oct-10 | NYMEX NY Harbor No.2.
Data record 3 | CCO_ID_1 | CM_ID_2 | CP_02 | 9/27/2010 | C | Nov-10 | NYMEX Henry Hub.
Data record 4 | CCO_ID_1 | CM_ID_2 | CP_02 | 9/27/2010 | C | Oct-10 | NYMEX Henry Hub.
Data record 5 | CCO_ID_1 | CM_ID_2 | CP_02 | 9/27/2010 | C | Nov-10 | NYMEX Henry Hub.
Data record 6 | CCO_ID_1 | CM_ID_2 | CP_02 | 9/27/2010 | C | Oct-10 | NYMEX Henry Hub.
Data record 7 | CCO_ID_1 | CM_ID_1 | CP_03 | 9/27/2010 | P | Mar-11 | NYMEX Light Sweet.
Data record 8 | CCO_ID_1 | CM_ID_1 | CP_03 | 9/27/2010 | P | Feb-11 | NYMEX Light Sweet.
Data record 9 | CCO_ID_1 | CM_ID_1 | CP_01 | 9/27/2010 | P | Mar-11 | NYMEX Light Sweet.
Data record 10 | CCO_ID_1 | CM_ID_1 | CP_01 | 9/27/2010 | P | Feb-11 | NYMEX Light Sweet.
Data record 11 | CCO_ID_1 | CM_ID_1 | CP_01 | 9/27/2010 | P | Jan-11 | NYMEX Light Sweet.
NDR | Yes | Yes | Yes | Yes | Yes | Yes | No.
Data records | Long swap position | Short swap position | Put/call indicator | Swaption expiration date | Swaption strike price | Non-delta adjusted long swaption position | Non-delta adjusted short swaption position
Data record 1 | 0 | 5000
Data record 2 | 0 | 2000
Data record 3 | | | C | 7/29/2011 | 5.59 | 2000 | 0
Data record 4 | | | C | 7/29/2011 | 5.59 | 18000 | 0
Data record 5 | | | P | 7/29/2011 | 5.50 | 100 | 30
Data record 6 | | | P | 7/29/2011 | 5.50 | 900 | 270
Data record 7 | 5000 | 0
Data record 8 | 5000 | 0
Data record 9 | 429 | 1286
Data record 10 | 2281 | 6843
Data record 11 | 1290 | 3871
NDR | No | No | Yes | Yes | Yes | No | No.
Note: The bottom row of Table 1 indicates whether data elements for which any difference in one of the elements constitutes a reason for a new data record (NDR).
Table 2—Example of Data Records Required Under § 20.3(c) for Cleared Swaption Products
Data records | CFTC clearing org ID | Clearing org cleared product ID | Reporting day | Futures equivalent month and year | Commodity reference price | Swaption expirationdate | Swaption strike price | Put/call indicator | Delta | Swaption daily settlement price
Data record 1 | CCO_ID_1 | CP_02 | 9/27/2010 | Nov-10 | NYMEX Henry Hub | 7/29/2011 | 5.59 | C | .5 | 6.25
Data record 2 | CCO_ID_1 | CP_02 | 9/27/2010 | Oct-10 | NYMEX Henry Hub | 7/29/2011 | 5.59 | C | .5 | 5.50
Data record 3 | CCO_ID_1 | CP_02 | 9/27/2010 | Nov-10 | NYMEX Henry Hub | 7/29/2011 | 5.50 | P | .2 | 4.53
Data record 4 | CCO_ID_1 | CP_02 | 9/27/2010 | Oct-10 | NYMEX Henry Hub | 7/29/2011 | 5.50 | P | .2 | 4.78
Table 3—Example of Data Records Required Under § 20.3(c) for Cleared Swap Products
Data records | CFTC clearing org ID | Clearing org cleared product ID | Reporting day | Futures equivalent month and year | Commodity reference price | Swap daily settlement price
Data record 1 | CCO_ID_1 | CP_04 | 9/27/2010 | Nov-10 | NYMEX NY Harbor No. 2 | 20.35
Data record 2 | CCO_ID_1 | CP_04 | 9/27/2010 | Oct-10 | NYMEX NY Harbor No. 2 | 10.50
Data record 3 | CCO_ID_1 | CP_03 | 9/27/2010 | Mar-11 | NYMEX Light Sweet | 15.00
Data record 4 | CCO_ID_1 | CP_03 | 9/27/2010 | Feb-11 | NYMEX Light Sweet | 21.00
Data record 5 | CCO_ID_1 | CP_01 | 9/27/2010 | Mar-11 | NYMEX Light Sweet | 17.50
Data record 6 | CCO_ID_1 | CP_01 | 9/27/2010 | Feb-11 | NYMEX Light Sweet | 21.65
Data record 7 | CCO_ID_1 | CP_01 | 9/27/2010 | Jan-11 | NYMEX Light Sweet | 12.50
First Record Layout Example for § 20.4:
This first example shows the data records generated under § 20.4 by a single reporting firm for report date September 27, 2011. Each data record represents a unique part of a reportable position in heating oil and natural gas by the reporting entity and its counterparties. Paragraph (b) of § 20.4 outlines the data elements that determine unique positions.
In this example, the reporting entity clears with one clearing organization and therefore the data records do not have to be delineated by clearing organization (there is a reportable position stemming from an uncleared transaction included as well). However, if the reporting entity in this example used multiple clearing organizations, then it would have to further subdivide its data submissions by each clearing organization.
The reporting entity reports fifteen records; six principal positions and nine counterparty positions. The reported positions constitute separate data records because they vary by the following characteristics: swap counterparties; futures equivalent months/years; clearing organization cleared products; swaptions that were either cleared or uncleared; commodity reference prices; and whether the trade was entered into on or off execution facilities. An illustration of how these records would be reported is included in Table 4 below.
For the calculation of notional values, assume for simplicity that the price of heating oil, for all contract months and for both reference prices, is $3/gal. Similarly, assume that the price of natural gas for all contract months is $4.25/MMBtu.
Note: The bottom two rows in Table 4 indicate whether, for uncleared and cleared swaps and swaptions, data elements for which any difference in one of the elements constitutes a reason for a new data record (NDR).
Table 4—Example of Data Records Reported Under § 20.4(c)
Data records | Commission reporting entity ID | Principal/counterparty position indicator | 102S Swap counterparty ID | Counterparty name | Reporting day | Clearing orgcleared product ID | Commodity code | Futuresequivalent month and year
Data record 1 | CRE_ID_1 | PRIN | | | 9/27/2011 | CPID_05 | HO | Jan-12
Data record 2 | CRE_ID_1 | COUNT | CP_01 | Energy Firm 1 | 9/27/2011 | CPID_05 | HO | Jan-12
Data record 3 | CRE_ID_1 | COUNT | CP_02 | Energy Firm 2 | 9/27/2011 | CPID_05 | HO | Jan-12
Data record 4 | CRE_ID_1 | PRIN | | | 9/27/2011 | CPID_04 | HO | Feb-12
Data record 5 | CRE_ID_1 | COUNT | CP_03 | Energy Firm 3 | 9/27/2011 | CPID_04 | HO | Feb-12
Data record 6 | CRE_ID_1 | PRIN | | | 9/27/2011 | CPID_04 | HO | Mar-12
Data record 7 | CRE_ID_1 | COUNT | CP_04 | ABC_Firm | 9/27/2011 | CPID_04 | HO | Mar-12
Data record 8 | CRE_ID_1 | PRIN | | | 9/27/2011 | CDIP_07 | NG | Mar-12
Data record 9 | CRE_ID_1 | COUNT | CP_05 | XYZ_Firm | 9/27/2011 | CDIP_07 | NG | Mar-12
Data record 10 | CRE_ID_1 | COUNT | CP_06 | WVU_Firm | 9/27/2011 | CDIP_07 | NG | Mar-12
Data record 11 | CRE_ID_1 | COUNT | CP_01 | Energy_Firm_1 | 9/27/2011 | CDIP_07 | NG | Mar-12
Data record 12 | CRE_ID_1 | PRIN | | | 9/27/2011 | CDIP_07 | NG | Mar-12
Data record 13 | CRE_ID_1 | COUNT | CP_07 | MNO_Firm | 9/27/2011 | CDIP_07 | NG | Mar-12
Data record 14 | CRE_ID_1 | PRIN | | | 9/27/2011 | UNCL | NG | Jan-12
Data record 15 | CRE_ID_1 | COUNT | CP_02 | Energy Firm 2 | 9/27/2011 | UNCL | NG | Jan-12
NDR Uncleared | Yes | Yes | Yes | No | Yes | N/A | No | Yes
NDR Cleared | Yes | Yes | Yes | No | Yes | Yes | No | Yes
Data records | Cleared/uncleared indicator | CFTC clearing org identifier | Commodity reference price | Execution facility | Long swap position | Short swap position
Data record 1 | C | CCO_ID_1 | Platts Oilgram Price Report for New York No. 2 (Barge) | EX1 | 200
Data record 2 | C | CCO_ID_1 | Platts Oilgram Price Report for New York No. 2 (Barge) | EX1 | | 50
Data record 3 | C | CCO_ID_1 | Platts Oilgram Price Report for New York No. 2 (Barge) | EX1 | | 150
Data record 4 | C | CCO_ID_1 | NYMEX NY Harbor No.2 | EX2 | 350
Data record 5 | C | CCO_ID_1 | NYMEX NY Harbor No.2 | EX2 | | 350
Data record 6 | C | CCO_ID_1 | NYMEX NY Harbor No.2 | EX1 | 100
Data record 7 | C | CCO_ID_1 | NYMEX NY Harbor No.2 | EX1 | | 100
Data record 8 | C | CCO_ID_1 | NYMEX Henry Hub | EX3 | 200 | 100
Data record 9 | C | CCO_ID_1 | NYMEX Henry Hub | EX3 | | 125
Data record 10 | C | CCO_ID_1 | NYMEX Henry Hub | EX3 | | 75
Data record 11 | C | CCO_ID_1 | NYMEX Henry Hub | EX3 | 100
Data record 12 | C | CCO_ID_1 | NYMEX Henry Hub | EX1
Data record 13 | C | CCO_ID_1 | NYMEX Henry Hub | EX1
Data record 14 | U | U | NYMEX Henry Hub | NOEX
Data record 15 | U | U | NYMEX Henry Hub | NOEX
NDR Uncleared | Yes | N/A | Yes | Yes | No | No
NDR Cleared | Yes | Yes | No | Yes | No | No
Data records | Put/callindicator | Swaptionexpiration date | Swaption strike price | Non-delta adjusted long swaption position | Non-delta adjusted short swaption position | Deltaadjusted long swaption position | Deltaadjusted short swaption position | Long swap or swaptionnotional value position | Short swap or swaptionnotional value position
Data record 1 | | | | | | | | $25,200,000
Data record 2 | | | | | | | | | $6,300,000
Data record 3 | | | | | | | | | $18,900,000
Data record 4 | | | | | | | | $44,100,000
Data record 5 | | | | | | | | | $44,100,000
Data record 6 | | | | | | | | $12,600,000
Data record 7 | | | | | | | | | $12,600,000
Data record 8 | | | | | | | | $8,500,000 | $4,250,000
Data record 9 | | | | | | | | | $5,312,500
Data record 10 | | | | | | | | | $3,187,500
Data record 11 | | | | | | | | $4,250,000
Data record 12 | C | 2/27/2012 | 4.00 | 100 | | 80 | | $3,400,000
Data record 13 | C | 2/27/2012 | 4.00 | | 100 | | 80 | | $3,400,000
Data record 14 | C | 12/27/2011 | 4.25 | 100 | | 95 | | $4,037,500
Data record 15 | C | 12/27/2011 | 4.25 | | 100 | | 95 | | $4,037,500
NDR Uncleared | Yes | Yes | Yes | No | No | No | No | No | No
NDR Cleared | Yes | Yes | Yes | No | No | No | No | No | No
Second Record Layout Example for § 20.4:
In this second example, the data records generated by § 20.4(c) are displayed for a hypothetical swap, as detailed in Example 1 of appendix A. In contrast to the above example, this second example of a § 20.4(c) data record is simplistic in that it displays a situation where the position records arise from a single swap transaction, in one commodity, with a single counterparty.
For the sake of this example, assume the swap dealer gained long exposure from the swap, and that the swap was cleared. The price of crude is assumed to be $100/bbl for all contract months on January 1 and $95/bbl for all contract months on January 2. An illustration of the data records generated for January 1, 2011 and January 2, 2011 as a result of this hypothetical swap can be found in Tables 5 and 6, respectively.
Table 5—Example of Data Records Reported Under § 20.4(c) for January 1, 2011 (Appx A, Example 1)
Data records | Commission reporting entity ID | Principal/counterparty position indicator | 102S swap counterparty ID | Counterparty Name | Reporting day | Clearing orgcleared product ID | Commodity code | Futures equivalent month and year
Data record 1 | SD_1 | PRIN | | | 1/1/2011 | CPID_03 | CL | Feb-11
Data record 2 | SD_1 | PRIN | | | 1/1/2011 | CPID_03 | CL | Mar-11
Data record 3 | SD_1 | PRIN | | | 1/1/2011 | CPID_03 | CL | Apr-11
Data record 4 | SD_1 | PRIN | | | 1/1/2011 | CPID_03 | CL | May-11
Data record 5 | SD_1 | PRIN | | | 1/1/2011 | CPID_03 | CL | Jun-11
Data record 6 | SD_1 | PRIN | | | 1/1/2011 | CPID_03 | CL | Jul-11
Data record 7 | SD_1 | PRIN | | | 1/1/2011 | CPID_03 | CL | Aug-11
Data record 8 | SD_1 | COUNT | CP_01 | Firm__1 | 1/1/2011 | CPID_03 | CL | Feb-11
Data record 9 | SD_1 | COUNT | CP_01 | Energy_Firm__1 | 1/1/2011 | CPID_03 | CL | Mar-11
Data record 10 | SD_1 | COUNT | CP_01 | Energy_Firm__1 | 1/1/2011 | CPID_03 | CL | Apr-11
Data record 11 | SD_1 | COUNT | CP_01 | Energy_Firm__1 | 1/1/2011 | CPID_03 | CL | May-11
Data record 12 | SD_1 | COUNT | CP_01 | Energy_Firm__1 | 1/1/2011 | CPID_03 | CL | Jun-11
Data record 13 | SD_1 | COUNT | CP_01 | Energy_Firm__1 | 1/1/2011 | CPID_03 | CL | Jul-11
Data record 14 | SD_1 | COUNT | CP_01 | Energy_Firm__1 | 1/1/2011 | CPID_03 | CL | Aug-11
Data records | Cleared/uncleared indicator | CFTC clearing org identifier | Commodity reference price | Execution facility | Longswap position | Shortswap position
Data record 1 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 73
Data record 2 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 103
Data record 3 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 93
Data record 4 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 103
Data record 5 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 99
Data record 6 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 103
Data record 7 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 27
Data record 8 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 73
Data record 9 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 103
Data record 10 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 93
Data record 11 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 103
Data record 12 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 99
Data record 13 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 103
Data record 14 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 27
Data records | Put/call indicator | Swaption expiration date | Swaption strike price | Non-delta adjusted long swaption position | Non-delta adjusted short swaption position | Delta adjusted long swaption position | Delta adjusted long swaption position | Long swap or swaption notional value position | Short swap or swaption notional value position
Data record 1 | | | | | | | | $7,300,000
Data record 2 | | | | | | | | $10,300,000
Data record 3 | | | | | | | | $9,300,000
Data record 4 | | | | | | | | $10,300,000
Data record 5 | | | | | | | | $9,900,000
Data record 6 | | | | | | | | $10,300,000
Data record 7 | | | | | | | | $2,700,000
Data record 8 | | | | | | | | | $7,300,000
Data record 9 | | | | | | | | | $10,300,000
Data record 10 | | | | | | | | | $9,300,000
Data record 11 | | | | | | | | | $10,300,000
Data record 12 | | | | | | | | | $9,900,000
Data record 13 | | | | | | | | | $10,300,000
Data record 14 | | | | | | | | | $2,700,000
Table 6—Example of Data Records Reported Under § 20.4(c) for January 2, 2011 (Appx A, Example 1)
Data records | Commission reporting entity ID | Principal/counterparty position indicator | 102S Swap counterparty ID | Counterparty name | Reporting day | Clearing orgcleared product ID | Commodity code | Futures equivalent month and year
Data record 1 | SD_1 | PRIN | | | 1/2/2011 | CPID_03 | CL | Feb-11
Data record 2 | SD_1 | PRIN | | | 1/2/2011 | CPID_03 | CL | Mar-11
Data record 3 | SD_1 | PRIN | | | 1/2/2011 | CPID_03 | CL | Apr-11
Data record 4 | SD_1 | PRIN | | | 1/2/2011 | CPID_03 | CL | May-11
Data record 5 | SD_1 | PRIN | | | 1/2/2011 | CPID_03 | CL | Jun-11
Data record 6 | SD_1 | PRIN | | | 1/2/2011 | CPID_03 | CL | Jul-11
Data record 7 | SD_1 | PRIN | | | 1/2/2011 | CPID_03 | CL | Aug-11
Data record 8 | SD_1 | COUNT | Counterparty__1 | Energy Firm | 1/2/2011 | CPID_03 | CL | Feb-11
Data record 9 | SD_1 | COUNT | Counterparty__1 | Energy Firm | 1/2/2011 | CPID_03 | CL | Mar-11
Data record 10 | SD_1 | COUNT | Counterparty__1 | Energy Firm | 1/2/2011 | CPID_03 | CL | Apr-11
Data record 11 | SD_1 | COUNT | Counterparty__1 | Energy Firm | 1/2/2011 | CPID_03 | CL | May-11
Data record 12 | SD_1 | COUNT | Counterparty__1 | Energy Firm | 1/2/2011 | CPID_03 | CL | Jun-11
Data record 13 | SD_1 | COUNT | Counterparty__1 | Energy Firm | 1/2/2011 | CPID_03 | CL | Jul-11
Data record 14 | SD_1 | COUNT | Counterparty__1 | Energy Firm | 1/2/2011 | CPID_03 | CL | Aug-11
Data records | Cleared/uncleared indicator | CFTC clearing org identifier | Commodity reference price | Execution facility | Long swap position | Short swap position
Data record 1 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 70
Data record 2 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 103
Data record 3 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 93
Data record 4 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 103
Data record 5 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 99
Data record 6 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 103
Data record 7 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | 27
Data record 8 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 70
Data record 9 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 103
Data record 10 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 93
Data record 11 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 103
Data record 12 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 99
Data record 13 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 103
Data record 14 | C | CCO_ID_1 | NYMEX Light Sweet | EX1 | | 27
Data records | Put/call indicator | Swaption expiration date | Swaption strike price | Non-delta adjusted long swaption position | Non-delta adjusted short swaption position | Delta adjusted long swaption position | Delta adjusted long swaption position | Long swap or swaption notional value position | Short swap or swaption notional value position
Data record 1 | | | | | | | | $6,650,000
Data record 2 | | | | | | | | $9,785,000
Data record 3 | | | | | | | | $8,835,000
Data record 4 | | | | | | | | $9,785,000
Data record 5 | | | | | | | | $9,405,000
Data record 6 | | | | | | | | $9,785,000
Data record 7 | | | | | | | | $2,565,000
Data record 8 | | | | | | | | | $6,650,000
Data record 9 | | | | | | | | | $9,785,000
Data record 10 | | | | | | | | | $8,835,000
Data record 11 | | | | | | | | | $9,785,000
Data record 12 | | | | | | | | | $9,405,000
Data record 13 | | | | | | | | | $9,785,000
Data record 14 | | | | | | | | | $2,565,000
