# Appendix F to Part 360—Customer File Structure
This is the structure of the data file to provide to the FDIC information related to each customer who has an account or sub-account reported in the deposit data or sweep/automated credit account file. If data or information are not maintained or do not apply, a null value in the appropriate field should be indicated. The file will be in a tab-or pipe-delimited ASCII format. Each file name will contain the institution's FDIC Certificate Number, an indication that it is a customer file type and the date of the extract. The files will be encrypted using an FDIC-supplied algorithm. The FDIC will transmit the encryption algorithm over FDICconnect.
Note: Each record must contain the customer's name and permanent legal address. Fields 4-12 relate to the customer name for individuals only. Fields 13-14 relate to the customer name for entities other than individuals. Some systems provide for separate fields for name, street address, city, state, ZIP, and country, all of which are parsed out. Others systems may simply provide multiple lines for name, street address, city, state, ZIP, with no distinction. In this case, certain name and address data elements must be parsed and provided in the appropriate fields.
Field name | Field description | Comments | Format
1. CS_Cust_Identifier | Customer Identifier | | Character (25).
| The unique field used by the institution to identify the customer
2. CS_Tax_ID | Customer Tax ID Number | Hyphens are optional in this field | Character (11).
| The tax identification number on record for the customer |
3. CS_Tax_Code | Customer Tax ID Code | | Character (1).
| The type of the tax identification number of the customer. Possible values are:
| • S = Social Security Number
| • T = Federal Tax Identification Number
| • O = Other
4. CS_Name_Line—1 | Individual Customer Name Line 1 | | Character (100).
| If available, the free-form name narrative of the customer, first line
5. CS_Name_Line—2 | Individual Customer Name Line 2 | | Character (100).
| If available, the free-form name narrative of the customer, second line.
6. CS_Last_Name | Individual Customer Last NameFor individuals, the customer's last name. | This field is required if the data element is in the institution's records. If necessary, data should be parsed from fields 4 or 5 to obtain this element | Character (50).
7. CS_First_Name | Individual Customer First NameFor individuals, the customer's first name. | This field is required if the data element is in the institution's records. If necessary, data should be parsed from fields 4 or 5 to obtain this element | Character (50).
8. CS_Middle_Name | Individual Customer Middle NameFor individuals, the customer's middle name. | This field is required if the data element is in the institution's records. If necessary, data should be parsed from fields 4 or 5 to obtain this element | Character (50).
9. CS_Suffix | Individual Professional SuffixFor individuals, the suffix designating customer's academic, professional or honorary status, such as Esq., Ph.D., M.D., and D.D.S. | This field is required if the data element is in the institution's records. If necessary, data should be parsed from fields 4 or 5 to obtain this element | Character (20).
10. CS_Generation | Individual Generational SuffixFor individuals, the suffix designating the customer's generational status, such as Jr., Sr. or III. | This field is required if the data element is in the institution's records. If necessary, data should be parsed from fields 4 or 5 to obtain this element | Character (10).
11. CS_Prefix | Individual Customer PrefixFor individuals, the prefix of the customer, such as Rev., Dr., Mrs., Mr. or Ms. | This field is required if the data element is in the institution's records. If necessary, data should be parsed from fields 4 or 5 to obtain this element | Character (10).
12. CS_Birth_Dt | Individual Customer Birth Date | | Date (YYYYMMDD).
| For individuals, the customer's birth date
13. CS_Ent_Name_Line—1 | Entity Name Line 1 | | Character (100).
| For entities other than individuals, the free-form name narrative of the customer, first line
14. CS_Ent_Name_Line—2 | Entity Name Line 2 | | Character (100).
| If available for entities other than individuals, the free-form name narrative of the customer, second line
15. CS_Nar_Addr_Line—1 | Customer Address Line 1 | | Character (100).
| If available, the free-form permanent legal address narrative for the customer, line one
16. CS_Nar_Addr_Line—2 | Customer Address Line 2 | | Character (100).
| If available, the free-form permanent legal address narrative of the customer, line two
17. CS_Nar_Addr_Line—3 | Customer Address Line 3 | | Character (100).
| If available, the free-form permanent legal address narrative of the customer, line three
18. CS_Street_Address—1 | Street Address Line 1The permanent legal address of the customer, line one. | This field is required. If necessary, data should be parsed from fields 16 or 17 to obtain this element | Character (100).
19. CS_Street_Address—2 | Street Address Line 2The permanent legal address of the customer, line two. | This field is required. If necessary, data should be parsed from fields 16 or 17 to obtain this element | Character (100).
20. CS_City | CityThe city associated with the permanent legal address. | This field is required. If necessary, data should be parsed from fields 16 or 17 to obtain this element | Character (25).
21. CS_State | StateThe state abbreviation associated with the permanent legal address. | This field is required. If necessary, data should be parsed from fields 16 or 17 to obtain this element. Use a two-character state code (official U.S. Postal Service abbreviations) | Character (2).
22. CS_ZIP | ZIPThe ZIP + 4 code associated with the permanent legal address. | This field is required. If necessary, data should be parsed from fields 16 or 17 to obtain this element. If the "+ 4" code is not available, provide only the 5-digit ZIP code. Hyphens are optional in this field | Character (10).
23. CS_Country | CountryThe country associated with the permanent legal address. | This field is required. If necessary, data should be parsed from fields 16 or 17 to obtain this element. Provide the name of the country or the standard IRS country code | Character (10).
24. CS_Telephone | Customer Telephone Number | | Character (20).
| The telephone number on record for the customer
25. CS_Email | Customer Email Address | | Character (150).
| The e-mail address on record for the customer
