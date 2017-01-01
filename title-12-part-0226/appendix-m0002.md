# Appendix M2 to Part 226—Sample Calculations of Repayment Disclosures
The following is an example of how to calculate the minimum payment repayment estimate, the minimum payment total cost estimate, the estimated monthly payment for repayment in 36 months, the total cost estimate for repayment in 36 months, and the savings estimate for repayment in 36 months using the guidance in Appendix M1 to this part where three annual percentage rates apply (where one of the rates is a promotional APR), the total outstanding balance is $1000, and the minimum payment formula is 2 percent of the outstanding balance or $20, whichever is greater. The following calculation is written in SAS code.
data one;
/*
Note: pmt01 = estimated monthly payment to repay balance in 36 months sumpmts36 = sum of payments for repayment in 36 months
month = number of months to repay total balance if making only minimum payments
pmt = minimum monthly payment
fc = monthly finance charge
sumpmts = sum of payments for minimum payments
*/
* inputs;
* annual percentage rates; apr1 = 0.0; apr2 = 0.17; apr3 = 0.21; * insert in ascending order;
* outstanding balances; cbal1 = 500; cbal2 = 250; cbal3 = 250;
* dollar minimum payment; dmin = 20;
* percent minimum payment; pmin = 0.02; * (0.02 + perrate);
* promotional rate information;
* last month for promotional rate; expm = 6; * = 0 if no promotional rate;
* regular rate; rrate =.17; * = 0 if no promotional rate;
array apr(3); array perrate(3);
days = 365/12; * calculate days in month;
* calculate estimated monthly payment to pay off balances in 36 months, and total cost of repaying balance in 36 months;
array xperrate(3);
do I = 1 to 3;
xperrate(I) = (apr(I)/365)*days; * calculate periodic rate;
end;
if expm gt 0 then xperrate1a = (expm/36) * xperrate1 + (1 - (expm/36)) * (rrate/365) * days; else xperrate1a = xperrate1;
tbal = cbal1 + cbal2 + cbal3;
perrate36 = (cbal1 * xperrate1a + cbal2 * xperrate2 + cbal3 * xperrate3) / (cbal1 + cbal2 + cbal3);
* months to repay; dmonths = 36;
* initialize counters for sum of payments for repayment in 36 months; Sumpmts36 = 0;
pvaf = (1 - (1 + perrate36) ** -dmonths) / perrate36; * calculate present value of annuity factor;
pmt01 = round(tbal/pvaf,0.01); * calculate monthly payment for designated number of months;
sumpmts36 = pmt01 * 36;
* calculate time to repay and total cost of making minimum payments each month;
* initialize counter for months, and sum of payments;
month = 0;
sumpmts = 0;
do I = 1 to 3;
perrate(I) = (apr(I) / 365) * days; * calculate periodic rate;
end;
put perrate1 = perrate2 = perrate3 =;
eins:
month = month + 1; * increment month counter;
pmt = round(pmin*tbal,0.01); * calculate payment as percentage of balance;
if month ge expm and expm ne 0 then perrate1 = (rrate / 365) * days;
if pmt lt dmin then pmt = dmin; * set dollar minimum payment;
array xxxbal(3); array cbal(3);
do I = 1 to 3;
xxxbal(I) = round(cbal(I) * (1 + perrate(I)),0.01);
end;
fc = xxxbal1 + xxxbal2 + xxxbal3 − tbal;
if pmt gt (tbal + fc) then do;
do I = 1 to 3;
if cbal(I) gt 0 then pmt = round(cbal(I) * (1 + perrate(I)),0.01); * set final payment amount;
end;
end;
if pmt le xxxbal1 then do;
cbal1 = xxxbal1 − pmt;
cbal2 = xxxbal2;
cbal3 = xxxbal3;
end;
if pmt gt xxxbal1 and xxxbal2 gt 0 and pmt le (xxxbal1 + xxxbal2) then do;
cbal2 = xxxbal2 − (pmt − xxxbal1);
cbal1 = 0;
cbal3 = xxxbal3;
end;
if pmt gt xxxbal2 and xxxbal3 gt 0 then do;
cbal3 = xxxbal3 − (pmt − xxxbal1 − xxxbal2);
cbal2 = 0;
end;
sumpmts = sumpmts + pmt; * increment sum of payments;
tbal = cbal1 + cbal2 + cbal3; * calculate new total balance;
* print month, balance, payment amount, and finance charge;
put month = tbal = cbal1 = cbal2 = cbal3 = pmt = fc =;
if tbal gt 0 then go to eins; * go to next month if balance is greater than zero;
* initialize total cost savings;
savtot = 0;
savtot = round(sumpmts,1) − round (sumpmts36,1);
* print number of months to repay debt if minimum payments made, final balance (zero), total cost if minimum payments made, estimated monthly payment for repayment in 36 months, total cost for repayment in 36 months, and total savings if repaid in 36 months;
put title = '';
put title = 'number of months to repay debt if minimum payment made, final balance, total cost if minimum payments made, estimated monthly payment for repayment in 36 months, total cost for repayment in 36 months, and total savings if repaid in 36 months';
put month = tbal = sumpmts = pmt01 = sumpmts36 = savto t =;
put title = '';
run;
