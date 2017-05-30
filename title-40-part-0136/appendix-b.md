# Appendix B to Part 136—Definition and Procedure for the Determination of the Method Detection Limit—Revision 1.11
Definition
The method detection limit (MDL) is defined as the minimum concentration of a substance that can be measured and reported with 99% confidence that the analyte concentration is greater than zero and is determined from analysis of a sample in a given matrix containing the analyte.
Scope and Application
This procedure is designed for applicability to a wide variety of sample types ranging from reagent (blank) water containing analyte to wastewater containing analyte. The MDL for an analytical procedure may vary as a function of sample type. The procedure requires a complete, specific, and well defined analytical method. It is essential that all sample processing steps of the analytical method be included in the determination of the method detection limit.
The MDL obtained by this procedure is used to judge the significance of a single measurement of a future sample.
The MDL procedure was designed for applicability to a broad variety of physical and chemical methods. To accomplish this, the procedure was made device- or instrument-independent.
Procedure
1. Make an estimate of the detection limit using one of the following:
(a) The concentration value that corresponds to an instrument signal/noise in the range of 2.5 to 5.
(b) The concentration equivalent of three times the standard deviation of replicate instrumental measurements of the analyte in reagent water.
(c) That region of the standard curve where there is a significant change in sensitivity, i.e., a break in the slope of the standard curve.
(d) Instrumental limitations.
It is recognized that the experience of the analyst is important to this process. However, the analyst must include the above considerations in the initial estimate of the detection limit.
2. Prepare reagent (blank) water that is as free of analyte as possible. Reagent or interference free water is defined as a water sample in which analyte and interferent concentrations are not detected at the method detection limit of each analyte of interest. Interferences are defined as systematic errors in the measured analytical signal of an established procedure caused by the presence of interfering species (interferent). The interferent concentration is presupposed to be normally distributed in representative samples of a given matrix.
3. (a) If the MDL is to be determined in reagent (blank) water, prepare a laboratory standard (analyte in reagent water) at a concentration which is at least equal to or in the same concentration range as the estimated method detection limit. (Recommend between 1 and 5 times the estimated method detection limit.) Proceed to Step 4.
(b) If the MDL is to be determined in another sample matrix, analyze the sample. If the measured level of the analyte is in the recommended range of one to five times the estimated detection limit, proceed to Step 4.
If the measured level of analyte is less than the estimated detection limit, add a known amount of analyte to bring the level of analyte between one and five times the estimated detection limit.
If the measured level of analyte is greater than five times the estimated detection limit, there are two options.
(1) Obtain another sample with a lower level of analyte in the same matrix if possible.
(2) The sample may be used as is for determining the method detection limit if the analyte level does not exceed 10 times the MDL of the analyte in reagent water. The variance of the analytical method changes as the analyte concentration increases from the MDL, hence the MDL determined under these circumstances may not truly reflect method variance at lower analyte concentrations.
4. (a) Take a minimum of seven aliquots of the sample to be used to calculate the method detection limit and process each through the entire analytical method. Make all computations according to the defined method with final results in the method reporting units. If a blank measurement is required to calculate the measured level of analyte, obtain a separate blank measurement for each sample aliquot analyzed. The average blank measurement is subtracted from the respective sample measurements.
(b) It may be economically and technically desirable to evaluate the estimated method detection limit before proceeding with 4a. This will: (1) Prevent repeating this entire procedure when the costs of analyses are high and (2) insure that the procedure is being conducted at the correct concentration. It is quite possible that an inflated MDL will be calculated from data obtained at many times the real MDL even though the level of analyte is less than five times the calculated method detection limit. To insure that the estimate of the method detection limit is a good estimate, it is necessary to determine that a lower concentration of analyte will not result in a significantly lower method detection limit. Take two aliquots of the sample to be used to calculate the method detection limit and process each through the entire method, including blank measurements as described above in 4a. Evaluate these data:
(1) If these measurements indicate the sample is in desirable range for determination of the MDL, take five additional aliquots and proceed. Use all seven measurements for calculation of the MDL.
(2) If these measurements indicate the sample is not in correct range, reestimate the MDL, obtain new sample as in 3 and repeat either 4a or 4b.
5. Calculate the variance (S2) and standard deviation (S) of the replicate measurements, as follows:
EC15NO91.208
where:
Xι; i = 1 to n, are the analytical results in the final method reporting units obtained from the n sample aliquots and Σ refers to the sum of the X values from i = l to n.
6. (a) Compute the MDL as follows:
MDL = t(n-1,1- α = 0.99) (S)
where:
MDL = the method detection limit
t(n-1,1- α =.99) = the students' t value appropriate for a 99% confidence level and a standard deviation estimate with n-1 degrees of freedom. See Table.
S = standard deviation of the replicate analyses.
(b) The 95% confidence interval estimates for the MDL derived in 6a are computed according to the following equations derived from percentiles of the chi square over degrees of freedom distribution (χ2/df).
LCL = 0.64 MDL
UCL = 2.20 MDL
where: LCL and UCL are the lower and upper 95% confidence limits respectively based on seven aliquots.
7. Optional iterative procedure to verify the reasonableness of the estimate of the MDL and subsequent MDL determinations.
(a) If this is the initial attempt to compute MDL based on the estimate of MDL formulated in Step 1, take the MDL as calculated in Step 6, spike the matrix at this calculated MDL and proceed through the procedure starting with Step 4.
(b) If this is the second or later iteration of the MDL calculation, use S2 from the current MDL calculation and S2 from the previous MDL calculation to compute the F-ratio. The F-ratio is calculated by substituting the larger S2 into the numerator S2 A and the other into the denominator S2 B. The computed F-ratio is then compared with the F-ratio found in the table which is 3.05 as follows: if S2 A/S2 B<3.05, then compute the pooled standard deviation by the following equation:
EC15NO91.209
if S2 A/S2 B>3.05, respike at the most recent calculated MDL and process the samples through the procedure starting with Step 4. If the most recent calculated MDL does not permit qualitative identification when samples are spiked at that level, report the MDL as a concentration between the current and previous MDL which permits qualitative identification.
(c) Use the Spooled as calculated in 7b to compute The final MDL according to the following equation:
MDL = 2.681 (Spooled)
where 2.681 is equal to t(12,1− α=.99).
(d) The 95% confidence limits for MDL derived in 7c are computed according to the following equations derived from precentiles of the chi squared over degrees of freedom distribution.
LCL = 0.72 MDL
UCL = 1.65 MDL
where LCL and UCL are the lower and upper 95% confidence limits respectively based on 14 aliquots.
Tables of Students' t Values at the 99 Percent Confidence Level
Number of replicates | Degrees of freedom (n-1) | tcn-1,.99)
7 | 6 | 3.143
8 | 7 | 2.998
9 | 8 | 2.896
10 | 9 | 2.821
11 | 10 | 2.764
16 | 15 | 2.602
21 | 20 | 2.528
26 | 25 | 2.485
31 | 30 | 2.457
61 | 60 | 2.390
00 | 00 | 2.326
Reporting
The analytical method used must be specifically identified by number or title ald the MDL for each analyte expressed in the appropriate method reporting units. If the analytical method permits options which affect the method detection limit, these conditions must be specified with the MDL value. The sample matrix used to determine the MDL must also be identified with MDL value. Report the mean analyte level with the MDL and indicate if the MDL procedure was iterated. If a laboratory standard or a sample that contained a known amount analyte was used for this determination, also report the mean recovery.
If the level of analyte in the sample was below the determined MDL or exceeds 10 times the MDL of the analyte in reagent water, do not report a value for the MDL.
