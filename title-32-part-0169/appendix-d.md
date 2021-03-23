# Appendix D to Part 169 a —Commercial Activities Management Information System (CAMIS)
Each DoD Component shall create and manage their CAMIS data base. The CAMIS data base shall have a comprehensive edit check on all input data in the computerized system. All data errors in the CAMIS data base shall be corrected as they are found by the established edit check program. The data elements described in this appendix represents the DoD minimum requirements.
On approval of a full cost comparison, a simplified cost comparison, or a direct conversion CA, the DoD Component shall create the initial entry using the data elements in part I for full cost comparisons and data elements in part II for all other conversions. Within 30 days of the end of each quarter the DoD Component shall submit a floppy diskette. Data files must be in American Standard Code Information Interchange text file format on a MicroSoft-Disk Operating System formatted 3.5 inch floppy diskette. Provide submissions in the Defense Utility Energy Reporting System format. The data shall be submitted in the Director, Installations Management (D,IM), 400 Army Navy Drive, Room 206, Arlington, VA 22202-2884 at least 60 days prior to the end of the quarter. The D,IM shall use the automated data to update the CAMIS. If the DoD Component is unable to provide data in an automated format, the D,IM shall provide quarterly printouts of cost comparison records (CCR) and conversion and/or comparison records (DCSCCR) that may be annotated and returned within 30 days of the end of each quarter to the D,IM. The D,IM then shall use the annotated printouts to update the CAMIS.
Part I—Cost Comparison
The record for each cost comparison is divided into six sections. Each of these sections contains information provided by the DoD Components. The first five sections are arranged in a sequence of milestone events occurring during a cost comparison. Each section is completed immediately following the completion of the milestone event. These events are as follows:
1. Cost comparison is approved by DoD Component.
2. Solicitation is issued.
3. In-house and contractor costs are compared.
4. Contract is awarded/solicitation is canceled.
5. Contract starts.
The events are used as milestones because upon their completion some elements of significant information concerning the cost comparison become known.
A sixth section is utilized for CCRs that result in award of a contract. This section contains data elements on contract cost and information on subsequent contract actions during the second and third year of contract operation.
The data elements that comprise these six sections are defined in this enclosure.
Part II—Direct Conversions and Simplified Cost Comparisons
The record for each direct conversion and simplified cost comparison is divided into six sections. Each of the first five sections is completed immediately following the completion of the following events:
1. DoD Component approves CA action.
2. The solicitation is issued.
3. In-house and contractor costs are compared.
4. Contract is awarded or solicitation is canceled.
5. Contract starts.
A sixth section is utilized for tracking historical data after the direct conversion or simplified cost comparison is completed. This section contains data elements on contracts and cost information during the second and third performance period. The data elements that comprise the six sections in part II, of this Appendix, are defined in the CAMIS Entry and Update Instruction, Part II—Direct Conversions and Simplified Cost Comparisons.
Camis Entry and Update Instructions
Part I—Cost Comparisons
The bracketed number preceding each definition in sections one through five is the DoD data element number. All date fields should be in the format MMDDYY (such as, June 30, 1983 = 063083).
Section One
Event: DoD Component Approves Conducting a Cost Comparison
All entries in this section of CCR shall be submitted by DoD Components on the first quarter update after approving the start of a cost comparison.
These entries shall be used to establish the CCR and to identify the geographical, organizational, political, and functional attributes of the activity (or activities) undergoing cost comparison as well as to provide an initial estimate of the manpower associated with the activity (or activities). The initial estimate of the manpower in this section of the CCR will be in all cases those manpower figures identified in the correspondence approving the start of the cost comparison.
DoD Components shall enter the following data elements to establish a CCR:
[1] Cost Comparison Number. The number assigned by the DoD Component to uniquely identify a specific cost comparison. The first character of the cost comparison number must be a letter designating DoD Component as noted in data element [3], below. The cost comparison number may vary in length from five to ten characters, of which the second and subsequent may be alpha or numeric and assigned under any system desired by the DoD Component.
[2] Announcement and/or approval date. Date Congress is notified when required by 10 U.S.C. 2461, of this part or date DoD Component approves studies being performed by 45 or fewer DoD civilian employees.
[3] DOD Component Code. Use the following codes to identify the Military Service or Defense Agency conducting the cost comparison:
A—Department of the Army
B—Defense Mapping Agency
C—Strategic Defense Initiatives Organization
D—Civilian Health and Medical Program of the Uniformed Services (CHAMPUS) [3D1]
E—Defense Advanced Research Projects Agency
F—Department of the Air Force
G—National Security Agency/Central Security Service
H—Defense Nuclear Agency
J—Joint Chiefs of Staff (including the Joint Staff, Unified and Specified Commands, and Joint Service Schools)
K—Defense Information Systems Agency (DISA)
L—Defense Intelligence Agency
M—United States Marine Corps
N—United States Navy
R—Defense Contract Audit Agency
S—Defense Logistics Agency
T—Defense Security Assistance Agency
V—Defense Investigative Service
W—Uniform Services University of the Health Sciences
X—Inspector General, Department of Defense
Y—On Site Inspection Agency (OSIA)
2—Defense Finance & Accounting Service (DFAS)
3—Defense Commissary Agency (DeCA)
4—Defense Technical Information Center (DTIC)
5—U.S. Army Corps of Engineers (USACE) Civil Works
[4] Command code. The code established by the DoD Component headquarters to identify the command responsible for operating the commercial activity undergoing cost comparison.
[5] Installation code. The code established by the DoD Component headquarters to identify the installation where the CA(s) under cost comparison is and/or are located physically. Two or more codes (for cost comparison packages encompassing more than one installation) should be separated by commas.
[6] State code. A two-position numeric code for the State (Data element reference ST-GA.) or U.S. Territory (FIPS 55-2), as shown in attachment 1 to appendix B to this part, where element [5] is located. Two or more codes shall be separated by commas.
[7] Congressional District (CD). Number of the congressional district(s) where [5] is located. If representatives are elected "at large," enter "01" in this data element; for a delegate or resident commissioner (such as, District of Columbia or Puerto Rico) enter "98." If the installation is located in two or more CDs, all CDs should be entered and separated by commas.
[8] [Reserved]
[9] Title of Cost Comparison. The title that describes the commercial activity(s) under cost comparision (for instance, "Facilities Engineering Package," "Installation Bus Service," or "Motor Pool"). Use a clear title, not acronyms of function codes in this data element.
[10] DOD Functional Area Code(s). The four of five alpha/numeric character designators listed in Appendix A of this part that describe the type of CA undergoing cost comparison. There would be one code for a single CA or possible several codes for a large cost comparison package. A series of codes shall be separated by commas.
[11] Prior Operation Code. A single alpha character that identifies the mode of operation for the activity at the time the cost comparison is started. Despite the outcome of the cost comparison, this code does not change. The coding as as follows:
I—In-house
C—Contract
N—New requirement
E—Expansion
[12] Cost Comparison Status Code. A single alpha character that identifies the current status of the cost comparison. Enter one of the following codes:
P—In progress
C—Complete
X—Canceled. The CCR shall be excluded from future updates.
Z—Consolidated. The cost comparison has been consolidated with one or more other cost comparisons into a single cost comparison package. The CCR for the cost comparison that has been consolidated shall be excluded from future updates. (See data element [15].)
B—Broken out. The cost comparison package has been broken into two or more separate cost comparisons. The previous CCR shall be excluded from future updates. (See data element [15].)
[13] Announcement—personnel estimate civilian, and [14] announcement—personnel estimate military. The number of civilian and military personnel allocated to the CAs undergoing cost comparison when the cost comparison is approved by the DoD Component or announced to Congress. This number in all cases shall be those personnel figures identified in the correspondence announcing the start of a cost comparison and will include authorized positions, temporaries, and borrowed labor. The number is used to give a preliminary estimate of the size of the activity.
[15] Revised and/or original cost comparison number. When a consolidation occurs, create a new CCR containing the attributes of the consolidated cost comparison. In the CCR of each cost comparison being consolidated, enter the cost comparison number of the new CCR in this data element and code "Z" in data element [12] of this attachment. In the new CCR, this data element should be blank and data element [12] of this attachment should denote the current status of the cost comparison. Once the consolidation has occurred, only the new CCR requires future updates. When a single cost comparison is being broken into multiple cost comparisons, create a new CCR for each cost comparison broken out from the original cost comparison. Each new CCR shall contain its own unique set of attributes; in data element [15] of this attachment enter the cost comparison number of the original cost comparison from which each was derived, and in data element [12] of this attachment enter the current status of each cost comparison. For the original cost comparison, data element [15] of this attachment, should be blank and data element [12] of this attachment should have a code "B" entry. Only the derivative record entries require future updates. When a consolidation or a breakout occurs, an explanatory remark shall be entered in data element [57] of this attachment (such as, "part of SW region cost comparison," or, "separated into three cost comparisons").
Section Two
Event: The Solicitation is Issued
The entries in this section of the CCR provide information on the personnel authorized to perform the workload in the PWS, the number of workyears used to accomplish the workload in the PWS, and the type and kind of solicitation.
The DoD Component shall enter the following data elements at the first quarterly update subsequent to the issuance of the solicitation:
[17] [Reserved]
[18] Solicitation-Type Code. A one-character alpha designator that identifies the type of solicitation used to obtain contract bids or offers. Use either the CBD as the source document or information received from the contracting officer for this entry. Solicitations under section 8(a) of the Small Business Act are negotiated. Enter one of the following codes:
S—Sealed Bid
N—Negotiated
[19] Solicitation Kind Code. A one-character (or two-character, if "W" suffix is used) alpha designator indicating whether the competition for the contract has been limited to a specific class of bidders or offerors. Use either the CBD as the source document or information received from the contracting officer to enter one of the following codes:
A—Restrict to small business
B—Small Business Administration 8(a) Set Aside
C—Javits-Wagner-O'Day Act (JWOD)
D—Other mandatory sources
U—Unrestricted
W—(optional suffix) Unrestricted after initial restriction
[20] Current Authorized Civilians and [21] Current Authorized Military. The number of civilian and military authorizations allocated on the DoD Component's manpower documents to perform the work described in the PWS. This number refines the initial authorization estimate (section one, data elements [13] and [14]).
[22] Baseline Annual Workyears Civilian and [23] Baseline Annual Workyears Military. The number of annual workyears it has taken to perform the work described by the PWS before the DoD Component conducts the MEO study of the in-house organizations; do not include contract monitor requirements. Military workyears include assigned, borrowed, diverted, and detailed personnel.
An annual workyear is the use of 2,087 hours (including authorized leave and paid time off for training). For example, when full-time employees whose work is completely within the PWS are concerned, "one workyear" normally is comparable to "one employee" or two part-time employees, each working 1,043 hours in a fiscal year. Also include in this total the workyears for full-time employees who do not work on a full-time basis on the work described by the PWS. For example, some portion of the workload is performed by persons from another work center who are used on an "as needed" basis. Their total hours performing this workload is 4,172 hours. This would be reflected as two workyears. Less than one-half year of effort should be rounded down, and one-half year or more should be rounded up.
These workyear figures shall be the baseline for determining the manpower savings identified by the management study.
Section Three
Event: The In-House and the Contractor Costs of Operation are Compared
The entries in this section provide information on the date of the cost comparison (initial decision), the preliminary results, the number of bids or offers received, and the costing method used in the cost comparison.
The DoD Component shall enter the following data elements in the first quarterly update subsequent to the date of the comparison of in-house and contractor costs (date of initial decision):
[24] Scheduled Initial Decision Date. Date the initial decision is scheduled at the start of a cost comparison.
[24A] Actual Initial Decision Date. Date the initial decision is announced. The initial decision is based on the apparent low bid or offer and is subject to preaward surveys and resolution of all appeals and protests. In a sealed bid procurement, the initial decision is announced at bid opening. In a negotiated procurement, the initial decision is announced when the cost comparison is made between the in-house estimate and the proposal of the selected offeror.
[25] Cost Comparison Preliminary Results Code. A one-character alpha designator indicating the results of the cost comparison as announced by the contracting officer at the time the bids or offers are compared. The entries are limited to two possibilities:
I—In-house
C—Contract
[26]-[27] [Reserved]
Section Four
Event: The Contracting Officer Either Awards the Contract or Commercial Activity Cancels the Solicitation
The entries in this section identify the final result, information on the contract, the in-house bid, and costing information from the cost comparison record.
The DoD Component shall enter the following data elements in the first quarterly update subsequent to the date the contracting officer either awards a contract or cancels the solicitation:
[28] Contract Award/Solicitation Commercial Activity Cancellation Date. For conversions to contract, this is the date a contract was awarded in a sealed bid solicitation or the date the contractor was authorized to proceed on a conditional award contract in a negotiated solicitation. For retentions in-house, this is the date the solicitation was canceled (when the contracting officer publishes an amendment to the solicitation canceling it).
[29] Cost Comparison Final Result Code. A one-character alpha designator identifying the final result of the comparison between in-house and contractor costs; the contracting officer either awards the contract or cancels the solicitation. Enter one of the following codes:
I—In-house
C—Contract
[30] Decision Rationale Code. A one-character alpha designator that identifies the rationale for awarding a contract or canceling the solicitation. The work shall be performed in-house or by contractor, based on cost, or the work shall be performed in-house because no satisfactory commercial source was available (no bids or offers were received or the preaward survey resulted in the determination that no commercial sources were responsive or responsible). Enter one of the following codes:
C—Cost
N—No satisfactory commercial source
O—Other
[31] [Reserved]
[31a] Prime Contractor Size. Enter one of the following
S—Small or small/disadvantaged business
L—Large business
[32] MEO Workyears. The number of annual workyears it takes to perform the work described in the PWS after the MEO study has been conducted. Do not include the minimum cost differential (line 14 in CCF or line 16 in the ENCR CCF) in the computation of any of these data elements.
For data elements [33] through [36], enter all data after all adjustments required by appeals board decisions. Do not include the minimum cost differential (line 31 old CCF or line 14 new CCF or line 16 new ENRC form) in the computation of any of these data elements. If a valid cost comparison was not conducted (that is, all bidders or offerors disqualified, no bids or offers received, etc.) do not complete data elements [33] through [36]. Explain lack of valid cost data in data element [57], DOD Component Comments.
[33] First Performance Period. Expressed in months, the length of time covered by the contract. Do not include any option periods.
[34] Cost Comparison Period. Expressed in months, the total period of operation covered by the cost comparison; this is the period used as the basis for data elements [35] and [36], below.
[35] Total in-house Cost ($000). Enter the total cost of in-house performance in thousands of dollars, rounded to the nearest thousand. This is the total of line 6 of the new CCF or line 8 of the ENCR CCF. An entry is required although the activity remains in-house due to absence of a satisfactory commercial source.
[36] Total Contract Cost ($000). Enter the total cost of contract performance in thousands of dollars, rounded to the nearest thousand. This is the total of line 13 of the CCF or line 15 of the ENCR CCF.
[37] Scheduled Contract or MEO Start Date. Date the contract and/or MEO was scheduled to start at the beginning of a cost comparison.
Section Five
Event: The Contract/MEO Starts
The entries in this section identify the contract or MEO start date and the personnel actions taken as a result of the cost comparison.
The DoD Component shall enter the following data elements in the first quarterly update subsequent to the start of the contract:
[38] Contract/MEO Start Date. The actual date the contractor began operation of the contract or the Government implements the MEO.
[39] Permanent Employees Reassigned to Equivalent Positions. The number of permanent employees who were reassigned to positions of equivalent grade as of the contract start date.
[40] Permanent Employee Changed To Lower Positions. The number of permanent employees who were reassigned to lower grade positions as of the contract start date.
[41] Employees Taking Early Retirement. The number of employees who took early retirement as of the contract start date.
[42] Employees Taking Normal Retirement. The number of employees who took normal retirement as of the contract start date.
[43] Permanent Employees Separated. The number of permanent employees who were separated from Federal employment as of the contract start date.
[44] Temporary Employees Separated. The number of temporary employees who were separated from Federal employment as of the contract start date.
[45] Employees Entitled to Severance Pay. The estimated number of employees entitled to severance pay on their separation from Federal employment as of the contract start date.
[46] Total Amount of Severance Entitlements ($000). The total estimated amount of severance to be paid to all employees, in thousands of dollars, rounded to the nearest thousand, as of the contract start date.
[47] Number Of Employees Hired by The Contractor. The number of estimated DoD civilian employees (full-time or otherwise) that will be hired by the contractors, or their subcontractors, at the contract start date.
Administrative Appeal
[48] Filed. Were administrative appeals filed?
N—No
Y—Yes
[49] Source. Who filed the appeal?
B—Both
C—Contractor
I—In-house
[50] Result. Were the appeals finally upheld? (If both appealed, explain result in data element [57], of this section).
N—No
P—Still in progress
Y—Yes
GAO Protest
[51] Filed. Was a protest filed with GAO?
N—No
Y—Yes
[52] Source. Who filed the protest?
B—Both
C—Contractor
I—In-house
[53] Result. Was the protest finally upheld? (Explain result in data element [57], below).
N—No
P—Still in progress
Y—Yes
Arbitration
[54] Requested. Was there a request for arbitration?
N—No
Y—Yes
[55] Result. Was the case found arbitrable? (Explain result in data element [57], below).
N—No
P—Still in progress
Y—Yes
General Information
+ [56] Total Staff-Hours Expended. Enter the estimated number of staff-hours expended by the installation for the cost comparison. Include direct and indirect hours expended from the time of PWS until a final decision is made.
+ [56a] Estimated Cost Of Conducting The Cost Comparison. Enter the estimated cost of the total staff-hours identified in data element [56] of this section non-labor (travel, reproduction costs, etc.) associated with the cost comparision.
+ Data elements [56] and [56A] will only be completed by DoD Components that are participating in the pilot test of these data elements.
[57] DoD Component Comments. Enter comments, as required, to explain situations that affect the conduct of the cost comparision. Where appropriate, precede each comment with the CAMIS data element being referenced.
[58] Effective Date. "As of" date of the most current update for the cost comparison. This data element will be completed by the DMDC.
[59] (Leave blank, for DoD computer program use).
Section Six
Event: Quarter Following Contract and/or Option Renewal
The entries in this section identify original costs, savings, information on subsequent performance periods and miscellaneous contract data. The DoD Component shall enter the following data elements in the first quarterly update annually.
[60] Original Cost of Function(s) ($000). The estimated total cost of functions before to development of an MEO in thousands of dollars, rounded to the nearest thousand for the base year and option years. (Begin entry when study began for data element [2] after 1 October 1989).
[60A] Estimated Dollar Savings ($000). The DoD Component's estimated savings from the cost comparison for the base year plus option years, in thousands of dollars, rounded to the nearest thousand, for either in-house or contract performance. Documentation will be available at the DoD Component level. (Begin entry after 1 October 1989).
[61] Contract Or In-House Bid First Performance Period ($000). For studies resulting in continued in-house performance, enter the total in-house cost (Line 6 from the CCF) for the first performance period. For studies resulting in conversion to contract performance, enter the contract price (Line 7 from the CCF) for the first performance period. Figures shall be shown in thousands of dollars, rounded to the nearest thousand.
[61A] Actual Contract or In-House Costs First Performance Period ($000). Enter the actual first performance period contract cost including all change orders (Plus changes in the scope of work) or actual in-house performance cost including changes in the scope of work, in thousands of dollars, rounded to the nearest thousand. No entry is required for actual in-house performance during the second and third performance periods.
[61B] Adjusted Contract Costs First Performance Period ($000). Enter an adjusted first performance period contract cost that includes actual DoL wage increases and costs for omissions and/or errors in the original PWS, but exclude new requirement costs and their associated wage increases, in thousands of dollars, rounded to the nearest thousand. (Begin entry after 1 October 1989).
[61C] Adjusted In-House Costs First Performance Period ($000). Enter the total first performance period in-house cost of the MEO, including civil service pay increases, but excluding increases associated with new mission requirements not included in the original scope of work of the function. Show costs in thousands of dollars, rounded to the nearest thousand. Entry is required even if the function went to contract. (Begin entry after 1 October 1989).
[62] Contract Or In-House Bid Second Performance Period ($000). For studies resulting in continued in-house performance, enter the total in-house cost (Line 6 from the CCF) for the second performance period. For studies resulting in conversion to contract performance, enter the contract price (Line 7 from the CCF) for the second performance period. Figures shall be shown in thousands of dollars, rounded to the nearest thousand.
[62A] Actual Contract Costs Second Performance Period ($000). Enter the actual second performance period contract cost including all change orders (Plus changes in the scope of work), in thousands of dollars, rounded to the nearest thousand. No entry is required when the function remained in-house.
[62B] Adjusted Contract Costs Second Performance Period ($000). Enter an adjusted second performance period contract cost that includes actual DoL wage increases and costs for omissions and/or errors in the original PWS, but exclude new requirement costs and their associated wage increases, in thousands of dollars, rounded to the nearest thousand. (Begin entry after 1 October 1989).
[62] Adjusted In-House Costs Second Performance Period ($000). Enter the total second performance period in-house cost of the MEO, including civil service pay increases, but excluding increases associated with new mission requirements not included in the original scope of work of the function. Show costs in thousands of dollars, rounded to the nearest thousand. Entry is required even if the function went to contract. (Begin entry after 1 October 1989).
[63] Contract Or In-house Bid Third Performance Period ($000). For studies resulting in continued in-house performance, enter the total in-house cost (Line 6 from the CCF) for the third performance period. For studies resulting in conversion to contract performance, enter the contract price (Line 7 from the CCF) for the third performance period. Figures shall be shown in thousands of dollars, rounded to the nearest thousand.
[63A] Actual Contract Costs Third Performance Period ($000). Enter the actual third performance period contract cost including all change orders (Plus changes in the scope of work), in thousands of dollars, rounded to the nearest thousand. No entry is required when the function remained in-house.
[63B] Adjusted Contract Costs Third Performance Period ($000). Enter an adjusted third performance period contract cost that includes actual DoL wage increases and costs for omissions and/or errors in the original PWS, but exclude new requirement costs and their associated wage increases, in thousands of dollars, rounded to the nearest thousand (Begin entry after 1 October 1989).
[63C] Adjusted In-House Costs Third Performance Period ($000). Enter the total third performance period in-house cost of the MEO, including civil service pay increases, but excluding increases associated with new mission requirements not included in the original scope of work of the function. Show costs in thousands of dollars, rounded to the nearest thousand. Entry is required even if the function went to contract (Begin entry after 1 October 1989).
[64] Contractor Change. Enter one of the following alpha designators to indicate whether the contract for the second or third performance period has changed from the original contractor.
N—No, the contractor has not changed.
Y—Yes, the contractor has changed.
Data elements [65] through [66] of this section are not required if the answer to [64] of this section is no (N).
[65] New Contractor Size (If data element [66] of this section contains the alpha designator "I" or "R," no entry is required).
L—New contractor is large business.
S—New contractor is small and/or small disadvantaged business.
[66] Reason For Change. DoD Components shall enter one of the following designators listed in this section, followed by the last two digits of the fiscal year which the change occurred.
C—Contract workload consolidated with other existing contract workload.
D—New contractor takes over because original contractor defaults.
I—Returned in-house because original contractor defaults within 12 months of start date and in-house bid is the next lowest.
N—New contractor replaced original contractor because Government opted not to renew contract in option years.
R—Returned in-house temporarily pending resolicitation due to contract default, etc.
U—Contract workload consolidated into a larger (umbrella) cost comparison.
X—Other-function either returned in-house or eliminated because of base closure, realignment, budget reduction or other change in requirements.
[67] Contract Administration Staffing. The actual number of contract administration personnel hired to administer the contract.
Camis Entry and Update Instruction
Part II—Direct Conversions and Simplified Cost Comparisons
The bracketed number preceding each definition in sections One through six of this section, is the DoD data element number. All date fields should be in the format YYMMDD (Data element reference DA-FA).
Section One
Event: DoD Component Approves the CA Action
All entries in this section of the DCSCCR record shall be submitted by DoD Components on the first quarter update after approving the start of a cost comparison. These entries shall be used to establish the DCSCCR and to identify the geographical, organizational, political, and functional attributes of the activity (or activities) undergoing conversion and/or comparison as well as to provide an initial estimate of the manpower associated with the activity (or activities). The initial estimate of the personnel in this section of the DCSCCR will be, in all cases, those personnel figures identified in the correspondence approving the start of the conversion and/or comparison. DoD Components shall enter the following data elements to establish a DCSCCR:
[1] Direct Conversion/Simplified Cost Comparison Number. The number assigned by the DoD Component to uniquely identify a specific conversion and/or comparison. The first character of the conversion and/or comparison number must be a letter designating the DoD Component as noted in data element [3] of this section. The conversion and/or comparison number may vary in length from five to ten characters, of which the second and subsequent may be alpha or numeric and assigned under any system desired by the DoD Component.
[2] Approval Date. The date has simplified cost comparison or direct conversion was approved.
[3] DoD Component Code. Use the following codes to identify the Military Service or Defense Agency and/or Field Activity conducting the cost comparison:
A—Department of the Army
B—Defense Mapping Agency (DMA)
D—Civilian Health and Medical Program of the Uniformed Services (CHAMPUS) [3D1]
D—Washington Headquarters Service (WHS) [3D2]
F—Department of the Air Force
G—National Security Agency/Central Security Service (NSA/CSS)
H—Defense Nuclear Agency (DNA)
J—Joint Chiefs of Staff (JCS) (including the Joint Staff, Unified and Specified Commands, and Joint Service Schools)
K—Defense Information Systems Agency (DISA)
L—Defense Intelligence Agency (DIA)
M—United States Marine Corps (USMC)
N—United States Navy (USN)
R—Defense Contract Audit Agency (DCAA)
S—Defense Logistics Agency (DLA)
T—Defense Security Assistance Agency (DSAA)
V—Defense Investigative Service (DIS)
W—Uniformed Services University of the Health Sciences (USUHS)
Y—On Site Inspection Agency (OSIA)
2—Defense Finance & Accounting Service (DFAS)
3—Defense Commissary Agency (DeCA)
4—Defense Technical Information Center (DTIC)
5—U.S. Army Corps of Engineers (USACE) Civil Works
[4] Command code. The code established by the DoD Component headquarters to identify the command responsible for operating the commercial activity undergoing cost comparison.
[5] Installation code. The code established by the DoD Component headquarters to identify the installation where the CA(s) under cost comparison is and/or are located physically. Two or more codes (for cost comparison packages encompassing more than one installation) should be separated by commas.
[6] State Code. A two-position numeric code for the State (Data element reference ST-GA.) or U.S. Territory (FIPS 55-2), as shown in attachment 1 to appendix B of this part, where element [5] is located. Two or more codes shall be separated by commas.
[7] Congressional District (CD). Number of the CDs where [5] of this section, is located. If representatives are elected "at large," enter "01" in this data element; for a delegate or resident commissioner (i.e., District of Columbia or Puerto Rico) enter "98." If the installation is located in two or more CDs, all CDs should be entered and separated by commas.
[8] (Leave blank)
[9] Title of Conversion and/or Comparison. The title that describes the CA(s) under conversion/comparison (for instance, "Facilities Engineering Package", "Installation Bus Service," or "Motor Pool"). Use a clear title, not acronyms or function codes in this data element.
[10] DoD Functional Area Code(s). The four- or five-alpha and/or numeric character designators listed in appendix A of this part that describes the type of CA undergoing conversion and/or comparison. This would be one code for a single CA or possibly several codes for a large cost comparison package. A series of codes shall be separated by commas.
[11] Prior Operation Code. A single alpha character that identifies the mode of operation for the activity at the time the conversion and/or comparison is started. Despite the outcome of the conversion and/or comparison, this code does not change. The coding is as follows:
C—Contract
E—Expansion
I—In-house
N—New requirement
[12] Conversion and/or Comparison Status Code. A single alpha character that identifies the current status of the conversion and/or comparison. Enter one of the following codes:
B—Broken out. The cost comparison package has been broken into two or more separate cost comparisons. The previous DCSCCR shall be excluded from future updates. (See data element [15] of this section.)
C—Complete
P—In progress
X—Canceled. The DCSCCR shall be excluded from future updates.
Z—Consolidated. The cost comparison has been consolidated with one or more other cost comparisons into a single cost comparison package. The DCSCCR for the cost comparison that has been consolidated shall be excluded from future updates. (See data element [15] of this section.)
[13] Announcement—personnel estimate civilian, and [14] announcement—personnel estimate military. The number of civilian and military personnel allocated to the CAs undergoing conversion and/or comparison at the time the start of the conversion and/or comparison is approved. This number is all cases shall be those personnel figures identified when the conversion and/or comparison was approved and will include authorized positions, temporaries, and borrowed labor. The number is used to give a preliminary estimate of the size of the activity.
[15] Revised and/or original cost comparison number. When a consolidation occurs, create a new DCSCCR containing the attributes of the consolidated conversion and/or comparison. In the DCSCCR of each conversion and/or comparison being consolidated, enter the conversion and/or comparison number of the new DCSCCR in this data element and code "Z" in data element [12] of this section. In the new DCSCCR, this data element should be blank and data element [12] of this section should denote the current status of the conversion and/or comparison. Once the consolidation has occurred, only the new DCSCCR requires future updates.
When a single conversion and/or comparison is being broken into multiple conversion and/or comparisons, create a new DCSCCR for each conversion and/or comparison broken out from the original conversion and/or comparison. Each new DCSCCR shall contain its own unique set of attributes; in data element [15] of this section enter the conversion and/or comparison number of the original conversion and/or comparison from which each was derived, and in data element [12] of this section enter the current status of each conversion and/or comparison. For the original conversion and/or comparison, data element [15] of this section should be blank and data element [12] of this section should have a code "B" entry. Only the derivative record entries require future updates.
When a consolidation or a breakout occurs, an explanatory remark shall be entered in data element [56] of this section (such as, "part of SW region cost comparison," or, "separated into three cost comparisons").
[16] (Leave blank)
Section Two
Event: The Solicitation is Issued
The entries in this section of the DCSCCR provide information on the personnel authorized to perform the workload in the PWS, the number of workyears used to accomplish the workload in the PWS, and the type and kind of solicitation.
The DoD Component shall enter the following data elements at the first quarterly update subsequent to the issuance of the solicitation:
[17] (Leave blank)
[18] Solicitation-Type code. A one-character alpha designator that identifies the type of solicitation used to obtain contract bids or offers. Use either the CBD as the source document or information received from the contracting officer for this entry. Solicitations under section 8(a) of "The Small Business Act" are negotiated. Enter one of the following codes:
N—Negotiated
S—Sealed Bid
[19] Solicitation-Kind code. A one-character (or two-character, if "W" suffix is used) alpha designator indicating whether the competition for the contract has been limited to a specific class of bidders or offerors. Use either the CBD as the source document or information received from the contracting officer to enter one of the following codes:
A—Restrict to small business
B—Small Business Administration 8(a) Set Aside
C—"Javits-Wagner-O'Day Act" (JWOD)
D—Other mandatory sources
U—Unrestricted
W—(Optional suffix) Unrestricted after initial restriction
[20] Current Authorized Civilians, and [21] Current Authorized Military. The number of civilian and military authorizations allocated on the DoD Component's manpower documents to perform the work described in the PWS. This number refines the initial authorization estimate (section one, data elements [13] and [14] of this section).
[22] Baseline Annual Workyears Civilian, and [23] Baseline Annual Workyears Military. The number of annual workyears it has taken to perform the work described by the PWS before the DoD Component conducts the MEO analysis of the in-house organization. Do not include contract monitor requirements. Military workyears include assigned, borrowed, diverted, and detailed personnel. Less than one-half a year of effort should be rounded down, and one-half a year or more should be rounded up. These workyear figures shall be the baseline for determining the personnel savings identified by the most efficient organization analysis.
Section Three
Event: The In-House And The Contractor Costs Of Operations Are Compared
The entries in this section provide information on the date of the conversion and/or comparison (initial decision), the preliminary results, the number of bids or offers received, and the costing method used in the conversion and/or comparison.
The DoD Component shall enter the following data elements in the first quarterly update subsequent to the date of the comparison of in-house and contractor costs (date of initial decision):
[24] Scheduled Initial Decision Date. Date the initial decision is scheduled at the start of a conversion and/or comparison
[24A] Actual Initial Decision Date. Date the initial decision is announced. The initial decision is based on the apparent low bid or offer and is subject to preaward surveys and resolution of all appeals and protests. In a sealed bid procurement, the initial decision is announced at bid opening. In a negotiated procurement, the initial decision is announced when the cost comparison is made between the in-house estimate and the proposal of the selected offeror. In a conversion, the initial decision is announced when the in-house cost estimate is evaluated against proposed contractor proposals.
[25] Cost Comparison Preliminary Results Code. A one-character alpha designator indicating the results of the cost comparison as announced by the contracting officer at the time of the comparison (No entry required for a direct conversion). The entries are limited to two possibilities:
C—Contract
I—In-house
[26] (Leave blank)
[27] (Leave blank)
Section Four
Event: The Contracting Officer Either Awards The Contract or Cancels The Solicitation
The entries in this section identify the final result, information on the contract, the in-house bid, and costing information from the direct conversion and/or simplified cost comparison fact sheet.
The DoD Component shall enter the following data elements in the first quarterly update subsequent to the date the contracting officer either awards a contract or cancels the solicitation:
[28] Contract Award or Solicitation Cancellation Date. For conversions to contract, this is the date a contract was awarded in a sealed bid solicitation or the date the contractor was authorized to proceed on a conditional award contract in a negotiated solicitation. For retentions in-house, this is the date the solicitation was canceled (when the contracting officer publishes an amendment to cancel the solicitation).
[29] Cost Comparison Final Result Code. A one-character alpha designator identifying the final result of the comparison between in-house and contractor costs; the contracting officer either awards the contract or cancels the solicitation. Enter one of the following codes:
C—Contract
I—In-house
[30] Decision Rationale Code. A one-character alpha designator that identifies the rationale for awarding a contract or canceling the solicitation. The work shall be performed in-house or by contractor based on cost, for other than cost, or the work shall be performed in-house because no satisfactory commercial source was available (no bids or offers were received or the pre-award survey resulted in the determination that no commercial sources were responsive or responsible). Enter one of the following codes:
C—Cost
N—No satisfactory commercial source
O—Other
[31] (Leave blank)
[31A] Prime Contractor Size. Enter one of the following:
L—Large business
S—Small or small and/or disadvantaged business
[32] MEO Workyears. The number of annual workyears it takes to perform the work described in the PWS after the MEO analysis has been conducted. This entry will be equal to the number of annual workyears in the in-house bid (No entry required for a direct conversion).
For data elements [33] through [36] of this section enter all data after all adjustments required by appeal board decisions. Do not include minimum cost differential in the computation of any of these data elements. If a valid conversion and/or comparison was not conducted (i.e., all bidders or offerors disqualified, no bids or offers received, etc.) do not complete data elements [33], [34] and [36] of this section. Explain lack of valid cost data in data element [56], "DoD Component Comments" of this section.
[33] First Performance Period. Expressed in months, the length of time covered by the contract. Do not include any option periods.
[34] Conversion and/or Comparison Period. Expressed in months, the total period of operation covered by the conversion or cost comparison; this is the period used as the basis for data elements [35] and [36] of this section.
[35] Total In-House Cost ($000). Enter the total estimated cost of in-house performance for the base year plus option years, in thousands of dollars, rounded to the nearest thousand. An entry is required although the activity remains in-house due to absence of a satisfactory commercial source (No entry required for a direct conversion).
[36] Total Contract Cost ($000). Enter the total estimated cost of contract performance for the base year plus option years, in thousands of dollars, rounded to the nearest thousand.
[37] Scheduled Contract or MEO Start Date. Date the contract and/or MEO was scheduled to start at the beginning of a conversion and/or comparison.
Section Five
Event: The Contract MEO Starts.
The entries in this section identify the contract or MEO start date and the personnel actions taken as a result of the conversion and/or comparison.
The DoD Component shall enter the following data elements in the first quarterly update subsequent to the start of the contract:
[38] Contract and/or MEO Start Date. The actual date the contractor began operation of the contract or the Government implements the MEO.
[39] Permanent Employees Reassigned to Equivalent Positions. The number of permanent employees who were reassigned to positions of equivalent grade as of the contract start date.
[40] Permanent Employees Changed to Lower Positions. The number of permanent employees who were reassigned to lower grade positions as of the contract start date.
[41] Employees Taking Early Retirement. The number of employees who took early retirement as of the contract start date.
[42] Employees Taking Normal Retirement. The number of employees who took normal retirement as of the contract start date.
[43] Permanent Employees Separated. The number of permanent employees who were separated from Federal employment as of the contract start date.
[44] Temporary Employees Separated. The number of temporary employees who were separated from Federal employment as of the contract start date.
[45] Employees Entitled to Severance Pay. The estimated number of employees entitled to severance pay on their separation from Federal employment as of the contract start date.
[46] Total Amount of Severance Entitlements ($000). The total estimated amount of severance to be paid to all employees, in thousands of dollars, rounded to the nearest thousand, as of the contract start date.
[47] Number of Employees Hired by the Contractor. The number of estimated DoD civilian employees (full-time or otherwise) that will be hired by the contractors, or their subcontractors, at the contract start date.
Administrative Appeal
[48] Filed. Were administrative appeals filed?
N—No
Y—Yes
[49] Source. Who filed the appeal?
B—Both
C—Contractor
I—In-House
[50] Result. Were the appeals finally upheld? (if both appealed, explain result in data element [56] of this section).
N—No
P—Still in Progress
Y—Yes
GAO Protest
[51] Filed. Was a protest filed with GAO?
N—No
Y—Yes
[52] Source. Who filed the protest?
B—Both
C—Contractor
I—In-House
[53] Result. Was the protest finally upheld? (explain result in data element [56], of this section).
N—No
P—Still in Progress
Y—Yes
Arbitration
[54] Requested. Was there a request for arbitration?
N—No
Y—Yes
[55] Result. Was the case found arbitrable? (explain result in data element [56], of this section).
N—No
P—Still in Progress
Y—Yes
General Information
[56] DoD Component Comments. Enter comments, as required, to explain situations that affect the conduct of the conversion and/or comparison. Where appropriate, precede each comment with the CAMIS data element being referenced.
[57] Effective Date. "As of" date of the most current update for the conversion and/or comparison. This data element will be completed by the DMDC.
[58] (Leave blank, for DoD computer program use).
Section Six
Event: Quarter Following Contract and/or Option Renewal
The entries in this section identify information on subsequent performance periods and miscellaneous contract data. The DoD Component shall enter the following data elements in the first quarterly update annually:
[59] Actual Contract Cost First Performance Period ($000). Enter the actual contractor cost for the first performance period, in thousands of dollars, rounded to the nearest thousand.
[60] Actual Contract Cost Second Performance Period ($000). Enter the actual contractor cost for the second performance period, in thousands of dollars, rounded to the nearest thousand.
[61] Actual Contract Cost Third Performance Period ($000). Enter the actual contractor cost for the third performance period, in thousands of dollars, rounded to the nearest thousand.
[62] Contractor Change. Enter one of the following alpha designators to indicate whether the contractor for the second or third performance period has changed from the original contractor.
N—No, the contractor has not changed
Y—Yes, the contractor has changed
Data elements [63] through [64] of this section are not required if the answer to [62] of this section is no (N).
[63] New Contractor Size. (If data element [64] of this section contains the alpha designator "I" or "R," no entry is required)
L—New contractor is large business
S—New contractor is small and/or small disadvantaged business.
[64] Reason For Change. DoD Components shall enter one of the following designators listed in the following, followed by the last two digits of the FY in which the change occurred.
C—Contract workload consolidated with other existing contract workload.
D—New contractor takes over because original contractor defaults.
I—Returned in-house because of original contractor defaults; etc., within 6 months of start date and in-house bid is the next lowest.
N—New contractor replaced original contractor because Government opted not to renew contract in option years.
R—Returned in-house temporarily pending resolicitation due to contract default, etc.
U—Contract workload consolidated with other existing contract workload.
X—Other-Function either returned in-house or eliminated because of base closure, realignment, budget reduction or other change in requirements.
[65] Contract Administration Staffing. The actual number of contract administration personnel hired to administer the contract.
