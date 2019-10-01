# Appendix C to Part 370—Credit Balance Processing File Structure
A covered institution's IT system should be able to produce a file in the format below that can be used to calculate deposit insurance coverage for deposits resulting from credit balances on accounts for debt owed to the covered institution ("credit balances"). This file format is derived from the "Broker Submission File Format" found in the FDIC's "Deposit Broker's Processing Guide," supplemented by the "Addendum to the Deposit Broker's Processing Guide" used for Part 370 alternative recordkeeping entity processing. The file format below identifies fields that are not applicable for processing credit balances. These fields should be null while also maintaining the pipe delimiters. Additional information regarding the FDIC's Deposit Broker's Processing Guide for part 370 covered institutions may be found at https://www.fdic.gov/deposit/deposits/brokers/part-370-appendix.html
Field name | Description | Null valueallowed? (Y/N)
01 Broker Number | Not applicable | Y.
02 Account Number | Account number of account holding pending payments or other items for refunds of credit balances | N.
03 Customer Account Number | Assigned customer account number | N.
04 CUSIP | Not applicable | Y.
05 Tax ID | Taxpayer identification number of the account holder | N.
06 Tax ID Code | Code indicates corporate (TIN) or personal tax identification number (SSN) | N.
07 Name | Full name of credit balance owner | N.
08 Name 2 | Name 2 | Y.
09 Address 1 | Address line 1 as it appears on the credit balance owner's statement | N.
10 Address 2 | Address line 2 as it appears on the credit balance owner's statement | Y.
11 Address 3 | Address line 3 as it appears on the credit balance owner's statement | Y.
12 City | Address city as it appears on the credit balance owner's statement | N.
13 State | State postal abbreviation as it appears on the credit balance owner's statement | Y.
14 Zip/Postal | The zip/postal code associated with the credit balance owner's address at it appears on the credit balance owner's statement. For United States zip codes, use the United States Postal Service ZIP+4 standard. For international zip codes follow that standard format of that country | N.
15 Country | Country code as it appears on the credit balance owner's statement | N.
16 Province | Province as it appears on the credit balance owner's statement | Y.
17 IRA Code | Not applicable | Y.
18 Credit Balance | Credit balance of the account as of the institution failure date | N.
19 Sub-broker Indicator | Not applicable | Y.
20 Deposit Account Ownership Category | Account ownership right and capacity | N.
21 Transactional Flag | Not applicable | Y.
22 Retained Interest | Not applicable | Y.
23 Amount of Overfunding | Not applicable | Y.
24 Account Participant Full Name | Not applicable | Y.
25 Account Participant Type | Not applicable | Y.
26 Amount of Account Participant's Non-contingent Interests | Not applicable | Y.
27 Amount of Account Participant's Contingent Interests | Not applicable | Y.
28 Account Participant's Government-Issued ID | Not applicable | Y.
29 Account Participant's Government-Issued ID Type | Not applicable | Y.
