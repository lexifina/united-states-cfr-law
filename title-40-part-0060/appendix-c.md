# Appendix C to Part 60—Determination of Emission Rate Change
1. Introduction
1.1 The following method shall be used to determine whether a physical or operational change to an existing facility resulted in an increase in the emission rate to the atmosphere. The method used is the Student's t test, commonly used to make inferences from small samples.
2. Data
2.1 Each emission test shall consist of n runs (usually three) which produce n emission rates. Thus two sets of emission rates are generated, one before and one after the change, the two sets being of equal size.
2.2 When using manual emission tests, except as provided in § 60.8(b) of this part, the reference methods of appendix A to this part shall be used in accordance with the procedures specified in the applicable subpart both before and after the change to obtain the data.
2.3 When using continuous monitors, the facility shall be operated as if a manual emission test were being performed. Valid data using the averaging time which would be required if a manual emission test were being conducted shall be used.
3. Procedure
3.1 Subscripts a and b denote prechange and postchange respectively.
3.2 Calculate the arithmetic mean emission rate, E, for each set of data using Equation 1.
EC01JN92.292
Where:
E i = Emission rate for the i th run.
n = number of runs.
3.3 Calculate the sample variance, S 2, for each set of data using Equation 2.
EC01JN92.293
3.4 Calculate the pooled estimate, S p, using Equation 3.
EC01JN92.294
3.5 Calculate the test statistic, t, using Equation 4.
EC01JN92.295
4. Results
4.1 If E b>,E a and t>t′, where t′ is the critical value of t obtained from Table 1, then with 95% confidence the difference between E b and E a is significant, and an increase in emission rate to the atmosphere has occurred.
Table 1
Degrees of freedom (n a=n b−2) | t′ (95 percent confidence level)
2 | 2.920
3 | 2.353
4 | 2.132
5 | 2.015
6 | 1.943
7 | 1.895
8 | 1.860
For greater than 8 degrees of freedom, see any standard statistical handbook or text.
5.1 Assume the two performance tests produced the following set of data:
Test a | Test b
Run 1. 100 | 115
Run 2. 95 | 120
Run 3. 110 | 125
5.2 Using Equation 1—
E a = 100 + 95 + 110/3 = 102
E b = 115 + 120 + 125/3 = 120
5.3 Using Equation 2—
S a2 = (100−102) 2 + (95−102) 2 + (110−102) 2/3−1 = 58.5
S b2 = (115−120) 2 + (120−120) 2 + (125−120) 2/3−1 = 25
5.4 Using Equation 3—
S p = [(3 − 1)(58.5) + (3 + 1)(25) / 3 + 3 − 2]1/2 = 6.46
5.5 Using Equation 4—
EC01JN92.296
5.6 Since (n 1 + n 2 − 2) = 4, t′ = 2.132 (from Table 1). Thus since t>t′ the difference in the values of E a and E b is significant, and there has been an increase in emission rate to the atmosphere.
6. Continuous Monitoring Data
6.1 Hourly averages from continuous monitoring devices, where available, should be used as data points and the above procedure followed.
