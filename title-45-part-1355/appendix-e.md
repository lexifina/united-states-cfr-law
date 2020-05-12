# Appendix E to Part 1355—Data Standards
This amendment was further delayed until Oct. 1, 2022, at 85 FR 28410, May 12, 2020.
All data submissions will be evaluated to determine the completeness and internal consistency of the data. Four types of assessments will be conducted on both the foster care and adoption data submissions. The results of these assessments will determine the applicability of a substantial noncompliance determination with the title IV-E plan.
The four types of assessments are:
• Comparisons of the detailed data to summary data;
• Internal consistency checks of the detailed data;
• An assessment of the status of missing data; and
• Timeliness, an assessment of how current the submitted data are.
A. Foster Care
1. Summary Data Elements Submission Standards
A summary file must accompany the Detailed Data Elements submission. Both transmissions must be sent through electronic means (see appendix C for details). This summary will be used to verify basic counts of records on the detailed data received.
a. The summary file must be a discrete file separate from the semi-annual reporting period detailed data file. The record layout for the summary file is included in appendix D. section A.2.c. All data must be included. If the value for a numeric field is zero, zero must be entered.
b. The Department will develop a second summary file by computing the values from the detailed data file received from the title IV-E agency. The two summary files (the one submitted by the title IV-E agency and the one created during Federal processing) will be compared, field by field. If the two files match, further validation of the detailed data elements will commence. If the two summary files do not match, we will assume that there has been an error in transmission and will request a retransmission from the title IV-E agency within 24 hours of the time the title IV-E agency has been notified. In addition, a log of these occurrences will be kept as a means of cataloging problems and offering suggestions on improved procedures.
2. Detailed Data File Submission Standards
a. Internal Consistency Validations.
Internal consistency validations involve evaluating the logical relationships between data elements in a detailed record. For example, a child cannot be discharged from foster care before he or she has been removed from his or her home. Thus, the Date of Latest Removal From Home data element must be a date prior to the Date of Discharge. If this is not the case, an internal inconsistency will be detected and an "error" indicated in the detailed data file.
A number of data elements have "if applicable" contingency relationships with other data elements in the detailed record. For example, if the Foster Family Structure has only a single parent, then the appropriate sex of the Single Female/Male element in the "Year of Birth" and "Race/Origin" elements must be completed and the "non-applicable" fields for these elements are to be filled with zero's or, for dates, left blank.
The internal consistency validations that will be performed on the foster care detailed data are as follows:
(1) The Local Agency must be the county or a county equivalent unit which has responsibility for the case. The 5 digit Federal Information Processing Standard (FIPS) or other ACF assigned code must be used.
(2) If Date of Latest Removal From Home (Element 21) is less than nine months prior to the Report Period Ending Date (Element 2) then the Date of Most Recent Periodic Review (Element 5) may be left blank.
(3) If Date of Latest Removal From Home (Element 21) is greater than nine months from Report Date (Element 2) then the Date of Most Recent Periodic Review (Element 5) must not be more than nine months prior to the Report Date (Element 2).
(4) If a child is identified as having a disability(ies) (Element 10), at least one Type of Disability Condition (Elements 11-15) must be indicated. Enter a zero (0) for disabilities that do not apply.
(5) If the Total Number of Removals From Home to Date (Element 19) is one (1), the Date Child was Discharged From Last Foster Care Episode (Element 20) must be blank.
(6) If the Total Number of Removals From Home to Date (Element 19) is two or more, then the Date Child was Discharged From Last Foster Care Episode (Element 20) must not be blank.
(7) If Date Child was Discharged From Last Foster Care Episode (Element 20) exists, then this date must be a date prior to the Date of Latest Removal From Home (Element 21).
(8) The Date of Latest Removal From Home (Element 21) must be prior to the Date of Placement in Current Foster Care Setting (Element 23).
(9) At least one element between elements 26 and 40 must be answered by selecting a "1". Enter a zero (0) for conditions that do not apply.
(10) If Current Placement Setting (Element 41) is a value that indicates that the child is not in a foster family or a pre-adoptive home, then elements 49-55 must be zero (0).
(11) At least one element between elements 59 and 65 must be answered by selecting a "1". Enter a zero for sources that do not apply.
(12) If the answer to the question, "Has this child ever been adopted?" (Element 16) is "1" (Yes), then the question, "How old was the child when the adoption was legalized?" (Element 17) must have an answer from "1" to "5."
(13) If the Date of Most Recent Periodic Review (Element 5) is not blank, then Manner of Removal From Home for Current Placement Episode (Element 25) cannot be option 3, "Not Yet Determined."
(14) If Reason for Discharge (Element 58) is option 3, "Adoption," then Parental Rights Termination dates (Elements 46 and 47) must not be blank.
(15) If the Date of Latest Removal From Home (Element 21) is present, the Date of Latest Removal From Home Transaction Date (Element 22) must be present and must be later than or equal to the Date of Latest Removal From Home (Element 21).
(16) If the Date of Discharge From Foster Care (Element 56) is present, the Date of Discharge From Foster Care Transaction Date (Element 57) must be present and must be later than or equal to the Date of Discharge From Foster Care (Element 56).
(17) If the Date of Discharge From Foster Care (Element 56) is present, it must be after the Date of Latest Removal From Home (Element 21).
(18) In Elements 8, 52, and 54, race categories ("a" through "e") and "f. Unable to Determine" cannot be coded "0," for it does not apply. If any of the race categories apply and are coded as "1" then "f. Unable to Determine" cannot also apply.
b. Out-of-Range Standards.
Out-of-range standards relate to the occurrence of values in response to data elements that exceed, either positively or negatively, the acceptable range of responses to the question. For example, if the acceptable responses to the element, Sex of the Adoptive Child, is "1" for a male and "2" for a female, but the datum provided in the element is "3," this represents an out-of-range response situation.
Out-of-range comparisons will be made for all elements. The acceptable values are described in Appendix A, Section I.
3. Missing Data Standards
The term "missing data" refers to instances where data for an element are required but are not present in the submission. Data elements with values of "Unable to Determine," "Not Yet Determined" or which are not applicable, are not considered missing.
a. In addition, the following situations will result in converting data values to a missing data status:
(1) Data elements whose values fail internal consistency validations as outlined in A.2.a.(1)-(18) above, and
(2) Data elements whose values are out-of-range.
b. The maximum amount of allowable missing data is dependent on the data elements as described below:
(1) No Missing Data.
The data for the elements listed below must be present in all records in the submission. If any record contains missing data for any of these elements, the entire submission will be considered missing and processing will not proceed.
Element No. | Element name
01 | Title IV-E agency.
02 | Report date.
03 | Local agency FIPS code or other ACF assigned code.
04 | Record number.
(2) Less Than Ten Percent Missing Data.
The data for the elements listed below cannot have ten percent or more missing data without incurring a finding of substantial noncompliance with the title IV-E plan.
Element No. | Element description
05 | Date of most recent periodic, review.
06 | Child's date of birth.
07 | Child's sex.
08 | Child's race.
09 | Child's Hispanic or Latino Ethnicity.
10 | Does child have a disability(ies)?
11-15 | Type of disability (at least one must be selected).
16 | Has child been adopted?
17 | How old was child when adoption was legalized?
18 | Date of first removal from home.
19 | Total number of removals from home to date.
20 | Date child was discharged from last foster care.
21 | Date of latest removal from home.
22 | Removal transaction date.
23 | Date of placement in current foster care setting.
24 | Number of previous placement settings during this removal episode.
25 | Manner of removal from home for current placement episode.
26-40 | Actions or conditions associated with child's removal (at least one must be selected).
41 | Current placement setting.
42 | Out of State/Tribal service area placement.
43 | Most recent case plan goal.
44 | Caretaker family structure.
45 | Year of birth of 1st principal caretaker.
46 | Year of birth of 2nd principal caretaker.
47 | Date of mother's parental rights termination.
48 | Legal or putative father parental rights termination date.
49 | Foster family structure.
50 | Year of birth of 1st foster caretaker.
51 | Year of birth of 2nd foster caretaker.
52 | Race of 1st foster caretaker.
53 | Hispanic or Latino Ethnicity of 1st foster caretaker.
54 | Race of 2nd foster caretaker.
55 | Hispanic or Latino Ethnicity of 2nd foster caretaker.
56 | Date of discharge from foster care.
57 | Foster care discharge transaction date.
58 | Reason for discharge.
59-65 | Sources of Federal support/assistance for child (at least one must be selected).
66 | Amount of monthly foster care payment (regardless of source).
c. Determination of substantial noncompliance with the title IV-E plan.
Missing data are a major factor in determining substantial noncompliance with the title IV-E plan.
(1) Selection Rules.
All data elements will be used in calculating missing data unless one of the following limiting rules applies to the detailed case record.
(a) If Date of Latest Removal From Home (Element 21) and the Date of Discharge From Foster Care (Element 56) is less than 30 days, then the following date elements are the only ones to be used in evaluating the missing data provisions for purposes of a determination of substantial noncompliance with the title IV-E plan:
Elements
1 to 4
6 to 9
21 and 22
41 and 42
56 to 58
(b) If Date of Latest Removal From Home (Element 18) is prior to October 1, 1995, then the following data elements are the only ones to be used in evaluating the missing data provisions for purposes of a determination of substantial noncompliance with the title IV-E plan:
Elements
1 to 4
6 to 9
21 and 22
41 and 43
56 to 58
(2) Determination of substantial noncompliance with the title IV-E plan.
The percentage calculation will be performed for each data element. The total number of detailed records that are included by the selection rules in 3.c.(1), will serve as the denominator. The number of missing data occurrences for each element will serve as the numerator. The result will be multiplied by one hundred. The determination of substantial noncompliance with the title IV-E plan is made when any one element's missing data percentage is ten percent or greater.
4. Timeliness of Foster Care Data Reports
Title IV-E agencies are required to submit reports within 45 calendar days after the end of the semi-annual reporting period.
Computer generated transaction dates indicate the date when key foster care events are entered into the title IV-E agency's computer system. The intent of these transaction dates is to ensure that information about the status of children in foster care is recorded and, thus, reported in a timely manner.
a. Date of Latest Removal From Home.
The Date of Latest Removal From Home Transaction Date (Element 22) must not be more than 60 days after the Date of Latest Removal From Home (Element 21) event.
b. The Date of Discharge From Foster Care Transaction Data (Element 57) must not be more than 60 days after the Date of Discharge From Foster Care (Element 56) event.
For purposes of a determination of substantial noncompliance with the title IV-E plan, ninety percent of the records in a detailed data submission, must indicate that:
(1) The difference between the Date of Latest Removal From Home Transaction Date (Element 22) and the Date of Latest Removal From Home (Element 21) event is 60 days or less;
and, where applicable,
(2) The difference between the Date of Discharge From Foster Care Transaction Date (Element 57), and the Date of Discharge From Foster Care (Element 56) event is 60 days or less.
B. Adoption
1. Summary Data Elements File Submission Standards
A summary file must accompany the detailed Data Elements File submission. Both files must be sent through electronic means (see appendix C for details). This summary will be used to verify the completeness of the Detailed Data File submission received.
a. The summary file should be a discrete file separate from the semi-annual reporting period detailed data file. The record layout for the summary file is included in appendix D, section B.2.c. All data must be included. If the value for a numeric field is zero, zero must be entered.
b. The Department will develop a second summary file by computing the values from the detailed data file received from the title IV-E agency. The two summary files (the one submitted by the title IV-E agency and the one created during Federal processing) will be compared, field by field. If the two files match, further validation of the detailed data elements will commence. (See section B.2 below.) If the two summary files do not match, we will assume that there has been an error in transmission and will request a retransmission from the title IV-E agency within 24 hours of the time the title IV-E agency has been notified. In addition, a log of these occurrences will be kept as a means of cataloging problems and offering suggestions on improved procedures.
2. Detailed Data Elements File Submission Standards
a. Internal Consistency Validations
Internal consistency validations involve evaluating the logical relationships between data elements in a detailed record. For example, an adoption cannot be finalized until parental rights have been terminated. Thus, the dates of Mother/Father Termination of Parental Rights, elements must be present and the dates must be prior to the "Date Adoption Legalized." If this is not the case, an internal inconsistency will be detected and an "error" indicated in the detailed data file.
A number of data elements have "if applicable" contingency relationships with other data elements in the detailed record. For example, if the Adoptive Parent is single, then the appropriate sex of the single female/male element in the "Family Structure," "Year of Birth" and "Race/Origin" elements must be completed and the "non-applicable" fields for these elements are to be filled with zeros or left blank.
The internal consistency validations that will be performed on the adoption detailed data are as follows:
(1) The Child's Date of Birth (Element 5) must be later than both the Mother's and Father's Year of Birth (Elements 16 and 17) unless either of these is unknown.)
(2) If the title IV-E agency has determined that the child is a special needs child (Element 9), then "the primary basis for determining that this child has special needs" (Element 10) must be completed. If "the primary basis for determining that this child has special needs" (Element 10) is answered by option "4," then at least one element between Elements 11-15, "Type of Disability," must be selected. Enter a zero (0) for disabilities that do not apply.
(3) Dates of Parental Rights Termination (Elements 19 and 20) must be completed and must be prior to the Date Adoption Legalized (Element 21).
(4) If "Is a monthly financial subsidy being paid for this child" (Element 35) is answered negatively, "2", then Element 36 must be zero (0) and "Is the subsidy paid under Title IV-E adoption assistance" (Element 37) must be a "2".
(5) If the "Child Was Placed By" (Element 34) is answered with option 1, "Public Agency," then the question, "Did the title IV-E Agency Have any Involvement in This Adoption" (Element 4) must be "1".
(6) If the "Relationship of Adoptive Parent(s) to the Child," "Foster Parent of Child" (Element 31) is selected, then the question, "Did the title IV-E Agency Have any Involvement in This Adoption" (Element 4) must be "1".
(7) If "Is a monthly financial subsidy being paid for this child?" (Element 35) answered "1," then the question, "Did the title IV-E Agency Have any Involvement in This Adoption" (Element 4) must be "1."
(8) If the "Family Structure" (Element 22) is option 3, Single Female, then the Mother's Year of Birth (Element 23), the "Adoptive Mother's Race" (Element 25) and "Hispanic or Latino Ethnicity" (Element 26) must be completed. Similarly, if the "Family Structure" (Element 22) is option 4, Single Male, then the Father's Year of Birth (Element 24), the Adoptive Father's Race" (Element 27) and "Hispanic or Latino Ethnicity" (Element 28) must be completed. If the "Family Structure" (Element 22) is option 1 or 2, then both Mother's and Father's "Year of Birth," "Race" and "Hispanic or Latino Ethnicity" must be completed.
(9) In Elements 7, 25, and 27, race categories ("a" through "e") and "f. Unable to Determine" cannot be coded "0," for it does not apply. If any of the race categories apply and are coded as "1" then "f. Unable to Determine" cannot also apply.
b. Out-of-Range Standards
Out-of-range standards relate to the occurrence of values in response to data elements that exceed, either positively or negatively, the acceptable range of responses to the question. For example, if the acceptable response to the element, Sex of the Adoptive Child, is "1" for a male and "2" for a female, but the datum provided in the element is "3," this represents an out-of-range response situation.
Out-of-range comparisons will be made for all elements. The acceptable values are described in appendix B, section I.
3. Missing Data Standards
The term "missing data" refers to instances where data for an element are required but are not present in the submission. Data elements with values of "Unable to Determine," "Other" or which are not applicable, are not considered missing.
a. In addition, the following situations will result in converting data values to a missing data status:
(1) Data elements whose values fail internal consistency validations as outlined in 2.a.(1)-(9) above, and
(2) Data elements whose values are out-of-range.
b. The maximum amount of allowable missing data is dependent on the data elements as described below.
(1) No Missing Data.
The data for the elements listed below must be present in all records in the submission. If any record contains missing data for any of these elements, the entire submission will be considered missing and processing will not proceed.
Element No. | Element name
01 | Title IV-E agency.
02 | Report date.
03 | Record number.
04 | Did the title IV-e agency have any involvement in this adoption?
(2) Less Than Ten Percent Missing Data
The data for the elements listed below cannot have ten percent or more missing data without incurring a determination of substantial noncompliance with the title IV-E plan.
Element No. | Element name
05 | Child's date of birth.
06 | Child's sex.
07 | Child's race.
08 | Is the child of Hispanic or Latino ethnicity?
09 | Does child have special needs?
10 | Indicate the primary basis for determining that the child has special needs. (If Element 09 is yes, you must answer this question.)
11-15 | Type of special need (at least one must be selected.)
16 | Mother's year of birth.
17 | Father's year of birth.
18 | Was mother married at time of child's birth?
19 | Date of mother's termination of parental rights.
20 | Date of father's termination of parental rights.
21 | Date adoption legalized.
22 | Adoptive parent(s)' family structure.
23 | Mother's year of birth.
24 | Father's year of birth.
25 | Adoptive mother's race.
26 | Hispanic or Latino ethnicity of mother.
27 | Adoptive father's race.
28 | Hispanic or Latino ethnicity of father.
29-32 | Relationship of adoptive parent(s) to child (at least one must be selected.)
33 | Child placed from.
34 | Child placed by.
35 | Is a monthly financial subsidy paid for this child?
36 | If yes, the monthly amount is?
37 | Is the child receiving Title IV-E adoption assistance? (If Element 35 is a "1" (Yes) an answer to this question is required.)
c. Determination of substantial noncompliance with the title IV-E plan.
Missing data are a major factor in determining substantial noncompliance with the title IV-E plan.
(1) Selection Rules.
Only the adoption records with a "1" (Yes) answer in Element 4, "Did the title IV-E Agency have any Involvement in this adoption" will be subject to a determination of substantial noncompliance with the title IV-E plan.
(2) Determination of substantial noncompliance with the title IV-E plan.
The percentage calculation will be performed for each data element. The total number of detailed records will serve as the denominator and the number of missing data occurrences for each element will serve as the numerator. The result will be multiplied by one hundred. The determination of substantial noncompliance with the title IV-E plan is made when any one element's missing data percentage is ten percent or greater.
4. Timeliness of Adoption Reports
The title IV-E agency is required to submit reports within 45 calendar days after the end of the semi-annual reporting period.
For determinations of substantial noncompliance with the title IV-E plan purposes, however, no specific timeliness of data standards apply. Data on adoptions should be submitted as promptly after finalization as possible.
The desired approach to reporting adoption data is that adoptions should be reported during the reporting period in which the adoption is legalized. Or, at the title IV-E agency's option, they can be reported in the following reporting period if the adoption is legalized within the last 60 days of the reporting period.
Negative reports must be submitted for any semi-annual period in which no adoptions have been legalized.
