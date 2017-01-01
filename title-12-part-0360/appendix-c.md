# Appendix C to Part 360—Deposit File Structure
This is the structure for the data file to provide deposit data to the FDIC. If data or information are not maintained or do not apply, a null value in the appropriate field should be indicated. The file will be in a tab-or pipe-delimited ASCII format. Each file name will contain the institution's FDIC Certificate Number, an indication that it is a deposit file type and the date of the extract. The files will be encrypted using an FDIC-supplied algorithm. The FDIC will transmit to the covered institution the encryption algorithm over FDICconnect.
The total deposit balances and the number of deposit accounts in each deposit file must be reconciled to the subsidiary system control totals.
The FDIC intends to fully utilize a covered institution's understanding of its customers and the data maintained around deposit accounts. Should additional information be available to the covered institution to help the FDIC more quickly complete its insurance determination process, it may add this information to the end of this data file. Should additional data elements be provided, a complete data dictionary for these elements must be supplied along with a description of how this information could be best used to establish account ownership or insurance category.
The deposit data elements provide information specific to deposit account balances and account data. The sequencing of these elements, their physical data structures and the field data format and field length must be provided to the FDIC along with the data structures identified below.
A header record will also be required at the beginning of this file. This record will contain the number of accounts to be included in this file, the maximum number of characters contained in largest account title field maintained within the deposit file and the maximum number of characters contained in largest address field maintained within the deposit file.
Note: Each record must contain the account title/name and current account statement mailing address. Fields 17-33 relate to the account name and address information. Some systems provide for separate fields for account title/name, street address, city, state, ZIP, and country, all of which are parsed out. Others systems may simply provide multiple lines for name, street address, city, state, ZIP, with no distinction. Populate fields that best fit the system's data, either fields 17-27 or fields 28-33.
Field name | Field description | Comments | Format
1. DP_Acct_Identifier | Account IdentifierThe primary field used to identify the account. This field may be the Account Number. | The Account Identifier may be composed of more than one physical data element. If multiple fields are required to identify the account, data should be placed in separate fields and the FDIC instructed how these fields are combined to uniquely identify the account. | Character (25).
2. DP_Acct_Identifier—2 | Account Identifier—2If necessary, the second element used to identify the account. | | Character (25).
3. DP_Acct_Identifier—3 | Account Identifier—3If necessary, the third element used to identify the account. | | Character (25).
4. DP_Acct_Identifier—4 | Account Identifier—4If necessary, the fourth element used to identify the account. | | Character (25).
5. DP_Acct_Identifier—5 | Account Identifier—5If necessary, the fifth element used to identify the account. | | Character (25).
6. DP_Sub_Acct_Identifier | Sub-Account IdentifierIf available, the sub-account identifier for the account. | The Sub-Account Identifier may identify separate deposits tied to this account where there are different processing parameters such as interest rates or maturity dates, but all owners are the same. | Character (25).
7. DP_Bank_No | Bank NumberThe bank number assigned to the deposit account. | | Character (15).
8. DP_Tax_ID | Tax IDThe tax identification number maintained on the account. | For consumer accounts, typically, this would be the primary account holder's social security number ("SSN"). For business accounts it would be the federal tax identification number ("TIN"). Hyphens are optional in this field. | Character (15).
9. DP_Tax_Code | Tax ID CodeThe type of the tax identification number. Possible values are: • S = Social Security Number. • T = Federal Tax Identification Number. • O = Other. | Generally deposit systems have flags or indicators set to indicate whether the number is an SSN or TIN. | Character (1).
10. DP_Branch | Branch NumberThe branch or office associated with the account. | In lieu of a branch number this field may represent a specialty department or division. | Character (15).
11. DP_Cost_Center | Cost Center or G/L CodeThe identifier used for organization reporting or ownership of the account. Insert null value if the cost center is not carried in the deposit record. | This field ties to the general ledger accounts. | Character (20).
12. DP_Dep_Type | Deposit Type IndicatorThe type of deposit by office location. Possible values are: • D = Deposit (Domestic). • F = Foreign Deposit. | A deposit—also called a "domestic deposit"—includes only deposit liabilities payable in the United States, typically those deposits maintained in a domestic office of an insured depository institution, as defined in section 3(l) of the Federal Deposit Insurance Act (12 U.S.C. 1813(l)). A foreign deposit is a deposit liability in a foreign branch payable solely at a foreign branch or branches. | Character (1).
13. DP_Currency_Type | Currency TypeThe ISO 4217 currency code. | | Character (3).
14. DP_Ownership_Ind | Customer Ownership IndicatorThe type of ownership at the account level. Possible values are: • S = Single. • J = Joint Account. • P = Partnership account. • C = Corporation. • B = Brokered Deposits. • I = IRA Accounts. • U = Unincorporated Association. • R = Revocable Trust. • IR = Irrevocable Trust. • G = Government Accounts. • E = Employee Benefit Plan Accounts. • O = Other. | Single: Accounts owned by an individual and those accounts held as Minor Accounts, Estate Accounts, Non-Minor Custodian/Guardian Accounts, Attorney in Fact Accounts and Sole Proprietorships Joint Account: Accounts owned by two or more individuals, but does not include the ownership of a Payable on Death Account or Trust Account. Partnership Account: Accounts owned by a Partnership Corporation: Accounts owned by a Corporation (e.g. Inc., L.L.C., or P.C.). Brokered Deposits: Accounts placed by a deposit broker who acts as an intermediary for the actual owner or sub-broker. IRA Accounts: Accounts for which the owner has the right to direct how the funds are invested including Keoghs and other Self-Directed Retirement Accounts. | Character (2).
| | Unincorporated Association: An account owned by an association of two or more persons formed for some religious, educational, charitable, social or other non-commercial purpose.
| | Revocable Trusts: Including PODs and formal revocable trusts (e.g. Living Trusts, Intervivos Trusts or Family Trusts).
| | Irrevocable Trusts: Accounts held by a trust established by statute or written trust in which the grantor relinquishes all power to revoke the trust.
| | Government Accounts: Accounts owned by a government entity (e.g. City, State, County or Federal government entities and their sub-divisions).
| | Employee Benefit Plan: Accounts established by the administrator of an Employee Benefit Plan including defined contribution, defined benefit and employee welfare plans.
| | Other Accounts: Accounts owned by an entity not described above.
15. DP_Prod_Cat | Product CategoryThe product classification. Possible values are: | Product Category is sometimes referred to as "application type" or "system type". | Character (3).
| • DDA = Non-Interest Bearing Checking accounts.
| • NOW = Interest Bearing Checking accounts.
| • MMA = Money Market Deposit Accounts.
| • SAV = Other savings accounts.
| • CDS = Time Deposit accounts and Certificate of Deposit accounts, including any accounts with specified maturity dates that may or may not be renewable.
16. DP_Stat_Code | Status CodeStatus or condition of the account. Possible values are: | | Character (1).
| • O = Open.
| • D = Dormant.
| • I = Inactive.
| • E = Escheatment.
| • A = Abandoned.
| • C = Closing.
| • R = Restricted/Frozen/Blocked.
17. DP_Acct_Title—1 | Account Title Line 1Account styling or titling of the account. | These data will be used to identify the owners and beneficiaries of the account. | Character (100).
18. DP_Acct_Title—2 | Account Title Line 2If available, the second account title line. | | Character (100).
19. DP_Acct_Title—3 | Account Title Line 3If available, the third account title line. | | Character (100).
20. DP_Acct_Title—4 | Account Title Line 4If available, the fourth account title line. | | Character (100).
21. DP_Street_Add_Ln—1 | Street Address Line 1The current account statement mailing address of record. | | Character (100).
22. DP_Street_Add_Ln—2 | Street Address Line 2If available, the second mailing address line. | | Character (100).
23. DP_Street_Add_Ln—3 | Street Address Line 3If available, the third mailing address line. | | Character (100).
24. DP_City | CityThe city associated with the mailing address. | | Character (50).
25. DP_State | StateThe state abbreviation associated with the mailing address. | Use a two-character state code (official U.S. Postal Service abbreviations). | Character (2).
26. DP_ZIP | ZIPThe ZIP + 4 code associated with the mailing address. | If the "+ 4" code is not available provide only the 5-digit ZIP code. Hyphens are optional in this field. | Character (10).
27. DP_Country | CountryThe country associated with the mailing address. | Provide the country name or the standard IRS country code. | Character (10).
28. DP_NA_Line—1 | Name/Address Line 1Alternate name/address format for the current account statement mailing address of record, first line. | Fields 28-33 are to be used if address data are not parsed to populate Fields 17-27. | Character (100).
29. DP_NA_Line—2 | Name/Address Line 2Alternate name/address format, second line. | | Character (100).
30. DP_NA_Line—3 | Name/Address Line 3Alternate name/address format, third line. | | Character (100).
31. DP_NA_Line—4 | Name/Address Line 4Alternate name/address format, fourth line. | | Character (100).
32. DP_NA_Line—5 | Name/Address Line 5Alternate name/address format, fifth line. | | Character (100).
33. DP_NA_Line—6 | Name/Address Line 6Alternate name/address format, sixth line. | | Character (100).
34. DP_Cur_Bal | Current BalanceThe current balance in the account at the end of business on the effective date of this file. | This balance should not be reduced by float or holds. For CDs and time deposits, the balance should reflect the principal balance plus any interest paid and available for withdrawal not already included in the principal (do not include accrued interest). The total of all current balances in this file should reconcile to the total deposit trial balance totals or other summary reconciliation of deposits performed by the institution. | Decimal (14,2).
35. DP_Int_Rate | Interest RateThe current interest rate in effect for interest bearing accounts. | Interest rate should be expressed in decimal format, i.e., 2.0% should be represented as 0.020000000. | Decimal (10,9).
36. DP_Acc_Int | Accrued InterestThe amount of interest that has been earned but not yet paid to the account as of the date of the file. | | Decimal (14,2).
37. DP_Lst_Int_Pd | Date Last Interest PaidThe date through which interest was last paid to the account. | | Date (YYYYMMDD).
38. DP_Lst_Deposit | Date Last DepositThe date of the last deposit transaction posted to the account. | For example, a deposit that included checks and/or cash. | Date (YYYYMMDD).
39. DP_Int_Term_No | Interest Term NumberThe number of months in the current interest term. | | Decimal (3,0).
40. DP_Nxt_Mat | Date of Next MaturityFor CD and time deposit accounts, the next date the account is to mature. | For non-renewing CDs that have matured and are waiting to be redeemed this date may be in the past. | Date (YYYYMMDD).
41. DP_Open_DT | Account Open DateThe date the account was opened. | If the account had previously been closed and re-opened, this should reflect the most recent re-opened date. | Date (YYYYMMDD).
42. DP_Sweep_Code | Sweep Code | | Character (1).
| Indicates if the account is a sweep account. Possible values are:
| • Y = Yes.
| • N = No.
43. DP_Hold_To_Post | Full Hold on the account: Indicator if all postings to this account are restricted. Possible values are: | | Character (1).
| • Y = Yes.
| • N = No.
44. DP_Issue_Val_Amt | Issued Value AmountThe value of the current CD when issued. | For CDs only. | Decimal (14,2).
45. DP_Int_CD_Cde | Type of Interest for CD | For CDs only. | Character (1).
| Possible values are:
| • C = Rate Change Allowed.
| • N = Rate Change Not Allowed.
| • R = Change Rate to Default at Renewal.
| • T = Rate Change Allowed Only During the Term.
46. DP_IRA_Cde | IRA CodeThe type of IRA. Possible values are: • C = Corporate Retirement • E = Educational IRA. • I = IRA Account. • K = Keogh Account. • R = Roth IRA Account. • S = SEP Account. • T = Transitional Roth IRA. • V = Versa Account. • H = Health Savings Account. | Optional code field to be used if available to help further identify the types of IRA accounts. | Character (1).
47. DP_Deposit_Class_Type | Deposit Class TypeThe deposit class. Possible values are: | The institution may also use more or fewer class types. | Character (10).
| • RTL = Retail.
| • FED = Federal government.
| • STATE = State government.
| • COMM = Commercial.
| • CORP = Corporate.
| • BANK = Bank Owned.
| • DUE TO = Other Banks.
48. DP_Product_Class_Cde | Deposit Class CodesThe deposit class codes. Possible values are: RTL • 1 = Payable on Death. • 2 = Individual. • 3 = Living Trust—Intervivos or Family. • 4 = Irrevocable Trust (includes Educational IRAs). • 5 = Estate. • 6 = Attorney in Fact. • 7 = Minor—(includes all variations of Uniform Gifts to Minor Accounts). • 8 = Bankruptcy Personal. • 9 = Pre-Need Burial. • 10 = Escrow. • 11 = Representative Payee/Beneficiary. • 12 = Sole Proprietorship. • 13 = Joint. • 14 = Non-Minor Custodian/Guardian. • 15 = Other Retail. | These Product Class codes are used in conjunction with the Deposit Class Types in field 51. This field is to be used in concert with fields 12 and 13 identified above to enable the financial institution to capture more detailed information concerning account types. It is the intent of the FDIC to have the financial institution map its detailed account types to the codes identified in this field. The institution may also use additional codes, but in this event the institution must supply the detailed description and code value for each additional code used. If no additional account product type detail is available then this field should be left blank. | Character (2).
| FED• 16 = FHA. • 17 = Federal Government. STATE • 18 = City. • 19 = State. • 20 = County, Clerk of Court. • 21 = Other State. COMMERCIAL • 22 = Business Escrow. • 23 = Bankruptcy. • 24 = Club. • 25 = Church. • 26 = Unincorporated Association. • 27 = Unincorporated Non-Profit. • • 28 = Other Commercial. CORPORATION • 29 = Business Trust. • 30 = Business Agent. • 31 = Business Guardian. • 32 = Incorporated Association. • 33 = Incorporated Non-Profit. • 33 = Incorporated Non-Profit. • 34 = Corporation. • 35 = Corporate Partnership. • 36 = Corporate Partnership Trust. • 37 = Corporate Agent. • 38 = Corporate Guardian. • 39 = Pre-Need Funeral Trust. • 40 = Limited Liability Incorporation. • 41 = LLC partnership. • 42 = Lawyer Trust. • 43 = Realtor Trust. • 44 = Other Corporation. BANK • 45 = Certified & Official Checks, Money Orders, Loan Disbursements Checks, and Expense Checks. • 46 = ATM Settlement. • 47 = Other Bank Owned Accounts. DUE TO (Other Banks) • 48 = Due to U.S. Banks. • 49 = Due to U.S. Branches of Foreign Banks. • 50 = Due to Other Depository Institutions. • 51 = Due to Foreign Banks. • 52 = Due to Foreign Branches of U.S. banks. • 53 = Due to Foreign Governments and Official Institutions.
