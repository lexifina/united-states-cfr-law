# Appendix IV to Part 264—Cochran's Approximation to the Behrens-Fisher Students' t-test
Using all the available background data (nb readings), calculate the background mean (Xb) and background variance (sb2). For the single monitoring well under investigation (nm reading), calculate the monitoring mean (Xm) and monitoring variance (sm2).
For any set of data (X1, X2,..., Xn) the mean is calculated by:
and the variance is calculated by:
where "n" denotes the number of observations in the set of data.
The t-test uses these data summary measures to calculate a t-statistic (t*) and a comparison t-statistic (tc). The t* value is compared to the tc value and a conclusion reached as to whether there has been a statistically significant change in any indicator parameter.
The t-statistic for all parameters except pH and similar monitoring parameters is:
If the value of this t-statistic is negative then there is no significant difference between the monitoring data and background data. It should be noted that significantly small negative values may be indicative of a failure of the assumption made for test validity or errors have been made in collecting the background data.
The t-statistic (tc), against which t* will be compared, necessitates finding tb and tm from standard (one-tailed) tables where,
tb = t-tables with (nb−1) degrees of freedom, at the 0.05 level of significance.
tm = t-tables with (nm−1) degrees of freedom, at the 0.05 level of significance.
Finally, the special weightings Wb and Wm are defined as:
and so the comparison t-statistic is:
The t-statistic (t*) is now compared with the comparison t-statistic (tc) using the following decision-rule:
If t* is equal to or larger than tc, then conclude that there most likely has been a significant increase in this specific parameter.
If t* is less than tc, then conclude that most likely there has not been a change in this specific parameter.
The t-statistic for testing pH and similar monitoring parameters is constructed in the same manner as previously described except the negative sign (if any) is discarded and the caveat concerning the negative value is ignored. The standard (two-tailed) tables are used in the construction tc for pH and similar monitoring parameters.
If t* is equal to or larger than tc, then conclude that there most likely has been a significant increase (if the initial t* had been negative, this would imply a significant decrease). If t* is less than tc, then conclude that there most likely has been no change.
A further discussion of the test may be found in Statistical Methods (6th Edition, Section 4.14) by G. W. Snedecor and W. G. Cochran, or Principles and Procedures of Statistics (1st Edition, Section 5.8) by R. G. D. Steel and J. H. Torrie.
Standard T—Tables 0.05 Level of Significance
Degrees of freedom | t-values (one-tail) | t-values (two-tail)
1 | 6.314 | 12.706
2 | 2.920 | 4.303
3 | 2.353 | 3.182
4 | 2.132 | 2.776
5 | 2.015 | 2.571
6 | 1.943 | 2.447
7 | 1.895 | 2.365
8 | 1.860 | 2.306
9 | 1.833 | 2.262
10 | 1.812 | 2.228
11 | 1.796 | 2.201
12 | 1.782 | 2.179
13 | 1.771 | 2.160
14 | 1.761 | 2.145
15 | 1.753 | 2.131
16 | 1.746 | 2.120
17 | 1.740 | 2.110
18 | 1.734 | 2.101
19 | 1.729 | 2.093
20 | 1.725 | 2.086
21 | 1.721 | 2.080
22 | 1.717 | 2.074
23 | 1.714 | 2.069
24 | 1.711 | 2.064
25 | 1.708 | 2.060
30 | 1.697 | 2.042
40 | 1.684 | 2.021
Adopted from Table III of "Statistical Tables for Biological, Agricultural, and Medical Research" (1947, R. A. Fisher and F. Yates).
