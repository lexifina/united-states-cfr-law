# Appendix E to Part 360—Hold File Structure
This is the structure of the data file to provide information to the FDIC for each legal or collateral hold placed on a deposit account or sub-account. If data or information are not maintained or do not apply, a null value in the appropriate field should be indicated. The file will be in a tab-or pipe-delimited ASCII format. Each file name will contain the institution's FDIC Certificate Number, an indication that it is a hold data file type and the date of the extract. The files will be encrypted using an FDIC-supplied algorithm. The FDIC will transmit the encryption algorithm over FDICconnect.
Field name | Field description | Comments | Format
1. DP_Acct_Identifier | Account IdentifierThe primary field used to identify the account. This field may be the Account Number. | The Account Identifier may be composed of more than one physical data element. If multiple fields are required to identify the account, data should be placed in separate fields and the FDIC instructed how these fields are combined to uniquely identify the account | Character (25).
2. DP_Acct_Identifier—2 | Account Identifier—2 | | Character (25).
| If necessary, the second element used to identify the account
3. DP_Acct_Identifier—3 | Account Identifier—3 | | Character (25).
| If necessary, the third element used to identify the account
4. DP_Acct_Identifier—4 | Account Identifier—4 | | Character (25).
| If necessary, the fourth element used to identify the account
5. DP _Acct_Identifier—5 | Account Identifier—5 | | Character (25).
| If necessary, the fifth element used to identify the account
6. DP_Sub_Acct_Identifier | Sub-Account IdentifierIf available, the sub-account identifier for the account. | The Sub-Account Identifier may identify separate deposits tied to this account where there are different processing parameters such as interest rates or maturity dates, but all owners are the same. | Character (25).
7. HD_Hold_Amt | Hold Amount | | Decimal (14,2).
| Dollar amount of the hold
8. HD_Hold_Reason | Hold ReasonReason for the hold. Possible values are: | | Character (2).
| • LN = Loan Collateral Hold
| • LG = Court Order Hold
| • FD = FDIC hold
| • OT = Other (do not include daily operational type holds)
9. HD_Hold_Desc | Hold Description | | Character (255).
| Description of the hold available on the system
10. HD_Hold_Start_Dt | Hold Start DateThe date the hold was initiated. | | Date (YYYYMMDD).
11. HD_Hold_Exp_Dt | Hold Expiration DateThe date the hold is to expire. | | Date (YYYYMMDD)
