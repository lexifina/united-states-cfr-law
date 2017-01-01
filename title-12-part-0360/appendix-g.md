# Appendix G to Part 360—Deposit-Customer Join File Structure
This is the structure of the data file to provide to the FDIC information necessary to link the records in the deposit and customer files. If data or information are not maintained or do not apply, a null value in the appropriate field should be indicated. The file will be in a tab- or pipe-delimited ASCII format. Each file name will contain the institution's FDIC Certificate Number, an indication that it is a join file type and the date of the extract. The files will be encrypted using an FDIC-supplied algorithm. The FDIC will transmit the encryption algorithm over FDICconnect.
The deposit-customer join file will have one or more records for each deposit account, depending on the number of relationships to each account. A simple individual account, for example, will be associated with only one record in the deposit-customer join file indicating the owner of the account. A joint account with two owners will be associated with two records in the deposit-customer join file, one for each owner. The deposit-customer join file will contain other records associated with a deposit account to designate, among other things, beneficiaries, custodians, trustees and agents. This methodology allows the FDIC to know all of the possible relationships for an individual account and also whether a single customer is involved in many accounts.
Field name | FDIC field description | Comments | Format
1. CS_Cust_Identifier | Customer Identifier | | Character (25).
| The unique field used by the institution to identify the customer
2. DP_Acct_Identifier | Account IdentifierThe primary field used to identify the account. This field may be the Account Number. | The Account Identifier may be composed of more than one physical data element. If multiple fields are required to identify the account, the data should be placed in separate fields and the FDIC instructed how these fields are combined to uniquely identify the account | Character (25).
3. DP_Acct_Identifier—2 | Account Identifier—2 | | Character (25).
| If necessary, the second element used to identify the account
4. DP_Acct_Identifier—3 | Account Identifier—3 | | Character (25).
| If necessary, the third element used to identify the account
5. DP_Acct_Identifier—4 | Account Identifier—4 | | Character (25).
| If necessary, the fourth element used to identify the account
6. DP_Acct_Identifier—5 | Account Identifier—5 | | Character (25).
| If necessary, the fifth element used to identify the account
7. DP_Sub_Acct_Identifier | Sub-Account IdentifierIf available, the sub-account identifier for the account. | The Sub-Account Identifier may identify separate deposits tied to this account where there are different processing parameters such as interest rates or maturity dates, but all owners are the same | Character (25).
8. CS_Rel_Code | Relationship CodeThe code indicating how the customer is related to the account. Possible values are: • ADM = Administrator. • AGT = Agent/Representative. • ATF = Attorney For. • AUT = Authorized Signer. | Institutions must map their relationship codes to the codes in the list to the left. If the institution maintains more relationships they must supply the additional relationship codes being utilized along with the code definition | Character (5).
| • BNF = Beneficiary
| • CSV = Conservator
| • CUS = Custodian
| • DBA = Doing Business As
| • EXC = Executor
| • GDN = Guardian
| • MIN = Minor
| • PRI = Primary Owner
| • SEC = Secondary Owner(s)
| • TTE = Trustee
9. CS_Bene_Code | Beneficiary Type CodeIf the customer is considered a beneficiary, the type of account associated with this customer. Possible values are: | This includes beneficiaries on retirement accounts, trust accounts, minor accounts, and payable-on-death accounts | Character (1).
| • I = IRA
| • T = Trust—Irrevocable
| • R = Trust—Revocable
| • M = Uniform Gift to Minor
| • P = Payable on Death
| • O = Other
