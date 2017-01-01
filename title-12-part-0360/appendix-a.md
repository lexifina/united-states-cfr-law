# Appendix A to Part 360—Non-Monetary Transaction File Structure
This is the structure of the data file the FDIC will provide to remove or add a FDIC hold for an individual account or sub-account. The file will be in a tab- or pipe-delimited ASCII format and provided through FDICconnect or Direct Connect. The file will be encrypted using an FDIC-supplied algorithm.
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
6. DP_Sub_Acct_Identifier | Sub-Account IdentifierIf available, the Sub-Account identifier for the account. | The Sub-Account Identifier may identify separate deposits tied to this account where there are different processing parameters such as interest rates or maturity dates, but all owners are the same | Character (25).
7. PH_Hold_Action | Hold ActionThe requested hold action to be taken for this account or sub-account. | | Character (1).
| Possible values are:
| • R = Remove
| • A = Add
8. PH_Hold_Amt | Hold Amount | | Decimal (14,2).
| Dollar amount of the FDIC hold to be removed or added
9. PH_Hold_Desc | Hold Description | | Character (225).
| FDIC hold to be removed or added
