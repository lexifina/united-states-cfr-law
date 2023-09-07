# Appendix C to Part 39—Daily Reporting Data Fields
A. Daily Cash Flow Reporting
Field name | Description | House & customer origin | Individual customer account
Common Fields (Daily Cash Flow Reporting)
Total Message Count | The total number of reports included in the file | M | M
FIXML Message Type | Financial Information eXchange Markup Language (FIXML) account summary report type | M | M
Sender ID | The CFTC-issued derivatives clearing organization (DCO) identifier | M | M
To ID | Indicate "CFTC" | M | M
Message Transmit Datetime | The date and time the file is transmitted | M | M
Report ID | A unique identifier assigned by the Commodity Futures Trading Commission (CFTC) to each clearing member report | M | M
Report Date | The business date of the information being reported | M | M
Base Currency | Base currency referenced throughout report; provide exchange rate against this currency | M | M
Report Time (Message Create Time) | The report "as of" or information cut-off time | M | M
DCO Identifier | CFTC-assigned identifier for a DCO | M | M
Clearing Participant Identifier | DCO-assigned identifier for a particular clearing member | M | M
Clearing Participant Name | The name of the clearing member | M | M
Fund Segregation Type | Clearing fund segregation type | M | M
Clearing Participant LEI | Legal entity identifier (LEI) for a particular clearing member per International Organization for Standardization (ISO) 17442 | C | C
Clearing Participant LEI Name | The LEI name associated with the clearing member LEI | C | C
Customer Position Identifier | Proprietary identifier for a particular customer position account | C | N/A
Customer Position Name | The name associated with the customer position identifier | M | N/A
Customer Position Account Type | Type of account used for reporting | C | N/A
Customer LEI | LEI for a particular customer; provide if available | N/A | C
Customer LEI Name | The LEI name associated with the customer position LEI | N/A | C
Margin Account | Margin account identifier | M | N/A
Customer Margin Name | The name associated with the customer margin identifier | N/A | C
Unique Margin Identifier | A single field that uniquely identifies the margin account. This field is used to identify associated positions | M | M
Customer Margin Identifier | Proprietary identifier for a particular customer | N/A | M
Customer Margin Account Type | Account type indicator | N/A | M
Futures and Options (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Concentration Risk | Risk factor component to capture costs associated with the liquidation of a large position | C | C
Delivery Margin | Margin collected to cover delivery risk | C | N/A
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons | M | M
Liquidity Risk | Risk component to capture bid/offer costs associated with the liquidation of a large portfolio. | C | C
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date | M | N/A
Total Margin | The total margin requirement for the origin. This margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | N/A
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin | M | N/A
Market Move Risk | Margin amount associated with market move risk | C | C
Margin Savings | The margin savings amount for the clearing member where there is a cross-margining agreement with another DCO | C | N/A
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C | C
Net Option Value | The credit or debit amount based on the long or short options positions | C | C
Backdated Profit and Loss | The profit and loss (P&L) attributed to positions added that were novated on a prior date | O | N/A
Day Trading Profit and Loss | The P&L attributed to the day's trades | C | N/A
Position Profit and Loss | The P&L of the previous day's position with today's price movement | C | N/A
Total Profit and Loss | Unrealized P&L or mark-to-market value of position(s) including change in mark to market (Total P&L = Position P&L + Day Trading P&L + Backdated P&L) | M | N/A
Customer Margin Omnibus Parent | The margin identifier for the omnibus account associated with the customer margin identifier. (Conditional on reported customer position being part of a separately reported omnibus account position.) | N/A | C
Commodity Swaps (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons | M | M
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date | M | N/A
Total Margin | The total margin requirement for the origin. This margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | M
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin | M | N/A
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C | N/A
Net Cash Flow | Net cash flow recognized on report date (with actual settlements occurring according to the currency's settlement conventions). E.g., profit/loss, price alignment interest, cash payments (fees, coupons, etc.) | C | N/A
Backdated Profit and Loss | The P&L attributed to positions added that were novated on a prior date | C | N/A
Day Trading Profit and Loss | The P&L attributed to the day's trades | C | N/A
Position Profit and Loss | The P&L of the previous day's position with today's price movement | C | N/A
Total Profit and Loss | Unrealized P&L or mark to market value of position(s) including change in mark to market (Total P&L = Position P&L + Day Trading P&L + Backdated P&L) | M | N/A
Credit Default Swaps (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Concentration Risk | Risk factor component to capture costs associated with the liquidation of a large position | C | C
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons | M | M
Liquidity Risk | Risk component to capture bid/offer costs associated with the liquidation of a large portfolio. | C | C
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date | M | N/A
Total Margin | The total margin requirement for the origin. This margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | C
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin | M | N/A
Spread Response Risk | Risk factor component associated with credit spread level changes and credit term structure shape changes | C | C
Systemic Risk | Risk factor component to capture parallel shift of credit spreads | C | C
Curve Risk | Risk factor that captures curve shifts based on portfolio | C | C
Index Spread Risk | Risk factor component associated with risks due to widening/tightening spreads of credit default swap (CDS) indices relative to each other | C | C
Sector Risk | Risk factor component to capture sector risk | C | C
Jump to Default Risk | Risk factor component to capture most extreme up/down move of a reference entity | C | C
Basis Risk | Risk factor component to capture basis risk between index and index constituent reference entities | C | C
Interest Rate Risk | Risk factor component associated with parallel shift movements in interest rates | C | C
Jump to Health Risk | Risk factor component to capture extreme narrowing of credit spreads of a reference entity; also known as "idiosyncratic risk" | C | C
Other Risk | Any other risk factors included in the margin model | C | C
Recovery Rate Sensitivity Risk | Risk factor component to capture fluctuations of recovery rate assumptions | C | C
Wrong Way Risk | Risk that occurs when exposure to a counterparty is adversely correlated with the credit quality of that counterparty. It arises when default risk and credit exposure increase together | C | C
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C | N/A
Initial Coupon | Amount of coupon premium amount accrued from the start of the current coupon period through the trade date. (Indicate gross pay/collect amounts.) | O | N/A
Upfront Payment | The difference in market value between the standard coupon and the market spread as well as the coupon accrued through the trade date. (Indicate gross pay/collect amounts.) | O | N/A
Trade Cash Adjustment | Additional cash amount on trades. (Indicate gross pay/collect amounts.) | C | N/A
Quarterly Coupon | Regular payment of quarterly coupon premium amounts. (Indicate gross pay/collect amounts.) | O | N/A
Credit Event Payments | Cash settlement of credit events. (Indicate gross pay/collect amounts.) | C | N/A
Accrued Coupon | Coupon obligation from the first day of the coupon period through the current clearing trade date. The sum of accrued coupon for each position in the clearing member's portfolio (by origin). | M | N/A
Final Mark to Market | Determined by marking the end-of-day position from par (100%) to the end-of-day settlement price | M | N/A
Backdated Profit and Loss | The P&L attributed to positions added that were novated on a prior date | C | N/A
Day Trading Profit and Loss | The P&L attributed to the day's trades | C | N/A
Position Profit and Loss | The P&L of the previous day's position with today's price movement | C | N/A
Total Profit and Loss | Unrealized P&L or mark-to-market value of position(s) including change in mark to market (Total P&L = Position P&L + Day Trading P&L + Backdated P&L) | M | N/A
Previous Accrued Coupon | Previous day's accrued coupon | M | N/A
Previous Mark to Market | Previous day's mark to market | M | N/A
Price Alignment Interest | To minimize the impact of daily cash variation margin payments on the pricing of swaps, the DCO will charge interest on cumulative variation margin received and pay interest on cumulative variation margin paid | M | N/A
Foreign Exchange (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons. | M | M
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date | M | N/A
Total Margin | The total margin requirement for the origin. This margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | M
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin | M | N/A
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Other Payments | Includes any upfront and/or final/settlement payments made/received for the trade date. (Indicate gross pay/collect amounts.) | M | N/A
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C | N/A
Price Alignment Interest | To minimize the impact of daily cash variation margin payments on the pricing of swaps, the DCO will charge interest on cumulative variation margin received and pay interest on cumulative variation margin paid | M | N/A
Backdated Profit and Loss | The P&L attributed to positions added that were novated on a prior date | C | N/A
Day Trading Profit and Loss | The P&L attributed to the day's trades | C | N/A
Position Profit and Loss | The P&L of the previous day's position with today's price movement | C | N/A
Total Profit and Loss | Unrealized P&L or mark-to-market value of position(s) including change in mark to market (Total P&L = Position P&L + Day Trading P&L + Backdated P&L) | M | N/A
Interest Rate Swaps (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons | M | M
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date | M | N/A
Total Margin | The total margin requirement for the origin. This margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | M
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin | M | N/A
Cross-Margined Products Profit/Loss | P&L resulting from changes in value due to changes in the futures price. This P&L should only include changes to the cross-margined futures in the account | C | N/A
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C | N/A
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Other Payments | Includes any upfront and/or final/settlement payments made/received for the trade date. (Indicate gross pay/collect amounts.) | C | N/A
Net Coupon Payment | Net amount of any coupon cash flows recognized on report date but actually occurring on currency's settlement convention date. (Indicate gross pay/collect amounts.) | M | N/A
Net Present Value | Net present value (NPV) of all positions by currency | M | N/A
Net Present Value Previous | Previous day's NPV by currency | M | N/A
PV of Other Payments | Includes the present value of any upfront and/or final/settlement payments that will be settled after the report date. Only include amounts that are affecting the NPV of current trades | M | N/A
Price Alignment Interest | To minimize the impact of daily cash variation margin payments on the pricing of swaps, the DCO will charge interest on cumulative variation margin received and pay interest on cumulative variation margin paid | M | N/A
Accrued Coupon | Coupon obligation from the first day of the coupon period through the current clearing trade date. The sum of accrued coupon for each position in the clearing member's portfolio (by origin) | M | N/A
Backdated Profit and Loss | The P&L attributed to positions added that were novated on a prior date | C | N/A
Day Trading Profit and Loss | The P&L attributed to the day's trades | C | N/A
Position Profit and Loss | The P&L of the previous day's position with today's price movement | C | N/A
Total Profit and Loss | Unrealized P&L or mark-to-market value of position(s) including change in mark to market (Total P&L = Position P&L + Day Trading P&L + Backdated P&L). | M | N/A
Equity Cross Margin (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons resulting from liquidity/concentration charges | M | M
Liquidity Risk | Risk component to capture bid/offer costs associated with the liquidation of a large portfolio | C | C
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date. | M | N/A
Total Margin | The total margin requirement for the origin. This margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | N/A
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin. | M | N/A
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C | N/A
Net Option Value | The credit or debit amount based on the long or short options positions | C | C
Backdated Profit and Loss | The P&L attributed to positions added that were novated on a prior date. | C | N/A
Day Trading Profit and Loss | The P&L attributed to the day's trades | C | N/A
Position Profit and Loss | The P&L of the previous day's position with today's price movement | C | N/A
Total Profit and Loss | Unrealized P&L or mark to market value of position(s) including change in mark to market (Total P&L = Position P&L + Day Trading P&L + Backdated P&L) | M | N/A
Consolidated (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons | M | N/A
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date | M | N/A
Total Margin | The consolidated non-U.S. margin requirement for the origin. The consolidated non-U.S. margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | N/A
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin | M | N/A
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C | N/A
Backdated Profit and Loss | The P&L attributed to positions added that were novated on a prior date | C | N/A
Day Trading Profit and Loss | The P&L attributed to the day's trades | C | N/A
Position Profit and Loss | The P&L of the previous day's position with today's price movement | C | N/A
Total Profit and Loss | Unrealized P&L or mark-to-market value of position(s) including change in mark to market (Total P&L = Position P&L + Day Trading P&L + Backdated P&L) | M | N/A
Exempt DCO (Daily Cash Flow Reporting)
Additional Margin | Any additional margin required in excess of initial margin. For example, this figure should include any liquidity/concentration charge if the charge is not included in the initial margin | M | N/A
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons | M | N/A
Margin Calls | Any outstanding margin call that has been issued but not collected as of the end of the trade date | M | N/A
Total Margin | The U.S. person margin requirement for the origin by currency contribution. If the traded currency's swaps (i.e., JY) offset risk of other currencies, include an amount of zero for that currency. This margin requirement should include the initial margin requirement plus any additional margin required by the DCO | M | N/A
Variation Margin | Variation margin should include the net sum of all cash flows between the DCO and clearing members by origin | M | N/A
Collateral on Deposit | The collateral on deposit for an origin. This amount should include all collateral after all haircuts that have been deposited to cover the total margin requirement | M | N/A
Mark-to-Market | Determined by marking the end of day position(s) from par (100%) to the end of day settlement price | M | N/A
M = mandatory C = conditional O = optional.
B. Daily Position Reporting
Field name | Description | Use
Common Fields (Daily Position Reporting)
Total Message Count | The total number of reports included in the file | M
FIXML Message Type | FIXML account summary report type | M
Sender ID | The CFTC-issued DCO identifier | M
To ID | Indicate "CFTC" | M
Message Transmit Datetime | The date and time the file is transmitted | M
Report ID | A unique identifier assigned by the CFTC to each clearing member report | M
Report Date | The business date of the information being reported | M
Base Currency | Base currency referenced throughout report; provide exchange rate against this currency | M
Report Time (Message Create Time) | The report "as of" or information cut-off time | M
Message Event | The event source being reported | M
Market Segment ID | Market segment associated with the position report | M
DCO Identifier | CFTC-assigned identifier for a DCO | M
Clearing Participant Identifier | DCO-assigned identifier for a particular clearing member | M
Clearing Participant Name | The name of the clearing member | M
Fund Segregation Type | Clearing fund segregation type | M
Clearing Participant LEI | LEI for a particular clearing member | C
Clearing Participant LEI Name | The LEI name associated with the clearing member LEI | C
Customer Position Identifier | Proprietary identifier for a particular customer position account | C
Customer Position Name | The name associated with the customer position identifier | M
Customer Position Account Type | Type of account used for reporting | C
Customer Position LEI | LEI for a particular customer; must be provided when available | C
Customer Position LEI Name | The LEI name associated with the Customer Position LEI | C
Customer Margin Identifier | Proprietary identifier for a particular customer | C
Customer Margin Name | The name associated with the customer margin identifier | C
Unique Margin Identifier | A single field that uniquely identifies the margin account. This field is used to identify associated positions | M
Futures and Options (Daily Position Reporting)
Settlement Price/Currency | Settlement price, prior settlement price, settlement currency, and final settlement date | M
Cross-Margin Entity | Name of the entity associated with a cross-margined account | C
Exchange Commodity Code | Contract commodity code issued by the exchange; e.g., ticker symbol, the human recognizable trading identifier | M
Clearing Commodity Code | Registered commodity clearing identifier. The code is for the contract as if it was traded in the form it is cleared. For example, if the contract was traded as a spread but cleared as an outright, the outright symbol should be used | M
Product Type | Indicates the type of product with which the security is associated | C
Security Type | Indicates type of security | M
Maturity Month Year | Month and year of the maturity | M
Maturity Date | The date on which the principal amount becomes due | C
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
Asset Subtype | Provides a more specific description of the asset type | C
Security Group (Sector) | A name assigned to a group of related instruments which may be concurrently affected by market events and actions | C
Unit Leverage Factor | The multiplier needed to convert a change of one point of the quoted index into local currency P&L for a 1-unit long position | M
Units | Unit of measure | M
Settlement Method | Method of settlement | C
Exchange Identifier (MIC) | Exchange where the instrument is traded, per ISO 10383 | M
Security Description | Used to provide a textual description of a financial instrument | M
Unique Product Identifier | A single field that uniquely identifies a given product. All positions with this identifier will have the same price | M
Alternate Product Identifier—Spread Underlying Long | When a contract represents a differential between two products, the product code that represents the long position in the spread for long position in the combined contract | C
Alternate Product Identifier—Spread Underlying Short | When a contract represents a differential between two products, the product code that represents the long position in the spread for short position in the combined contract | C
Last Trading Date | The last day of trading in a futures contract | M
First Notice Date | The first date on which delivery notices are issued | C
Position (Long) | Long position size. If a position is quoted in a unit of measure (UOM) different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
Position (Short) | Short position size. If a position is quoted in a UOM different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
Settlement FX Info | Settlement price foreign exchange conversion rate | M
Change in Settlement Price | The quoted price change between the prior trading day's settlement and today's settlement | M
Unit Currency P&L | The local currency P&L between the prior trading day's settlement and today's settlement for a 1-unit long position | M
Outright Initial Margin | Initial margin for the position as if it were a stand-alone outright position | C
Option Exercise Style | Exercise style | C
Option Strike Price | Option strike price | C
Option Put/Call Indicator | Option type | C
Underlying Settlement Price/Currency | Settlement price, prior settlement price, settlement currency, and final settlement date | C
Underlying Exchange Commodity Code | Underlying Contract code issued by the exchange | C
Underlying Clearing Commodity Code | Registered commodity clearing identifier. The code is for the contract as if it was traded in the form it is cleared. For example, if the contract was traded as a spread but cleared as an outright, the outright symbol should be used | C
Underlying Product Type | Indicates the type of product the security is associated with | C
Underlying Security Type | Indicator which identifies the underlying derivative type | C
Underlying Security Group (Sector) | A name assigned to a group of related instruments which may be concurrently affected by market events and actions | C
Underlying Maturity Month Year | Month and year of the maturity | C
Underlying Maturity Date | The date on which the principal amount becomes due | C
Underlying Asset Class | The underlying broad asset category for assessing risk exposure | C
Underlying Asset Subclass | The subcategory description of the asset class | C
Underlying Asset Type | Provides a more specific description of the asset subclass | C
Underlying Asset Subtype | Provides a more specific description of the asset type. | C
Underlying Exchange Code (MIC) | Exchange where the underlying instrument is traded | C
Underlying Security Description | Textual description of a financial instrument | C
Unique Underlying Product Code | A single field that is the result of concatenating relevant fields that create a unique product ID that is associated with a unique price | C
Primary Options Exchange Code—Implied Volatility Quote | This field identifies the main options chain for the future that provides the implied volatility quote | C
DELTA | Delta is the measure of how the option's value varies with changes in the underlying price | C
Implied Volatility | The implied volatility and quotation style for the contract, typically in natural log percent or index points | C
Customer Margin Omnibus Parent | The margin identifier for the omnibus account associated with the customer margin identifier. (Conditional on reported customer position being part of a separately reported omnibus account position) | C
Commodity Swaps (Daily Position Reporting)
Settlement Price/Currency | Settlement price, prior settlement price, settlement currency, and final settlement date | M
Exchange Commodity Code | Contract commodity code issued by the exchange; e.g., ticker symbol, the human recognizable trading identifier | M
Clearing Commodity Code | Registered commodity clearing identifier. The code is for the contract as if it was traded in the form it is cleared. For example, if the contract was traded as a spread but cleared as an outright, the outright symbol should be used | M
Product Type | Indicates the type of product with which the security is associated | C
Security Group (Sector) | A name assigned to a group of related instruments which may be concurrently affected by market events and actions | C
Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to 17 CFR 45.7 | O
Maturity Month Year | Month and year of the maturity | M
Maturity Date | The date on which the principal amount becomes due | C
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
Unit Leverage Factor | The multiplier needed to convert a change of one point of the quoted index into local currency P&L for a 1-unit long position | C
Minimum Tick | Minimum price tick increment | C
Units | Unit of measure | M
Settlement Method | Swap settlement method | C
Exchange Identifier (MIC) | Exchange where the instrument is traded | M
Security Description | Used to provide a textual description of a financial instrument | C
Security Type | Indicates type of security | M
Position (Long) | Long position size. If a position is quoted in a UOM different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
Position (Short) | Short position size. If a position is quoted in a UOM different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
Net Cash Flow | Net cash flow recognized on report date (with actual settlements occurring according to the currency's settlement conventions). E.g., profit/loss, price alignment interest, cash payments (fees, coupons, etc.) | C
Settlement FX Info | Settlement price foreign exchange conversion rate | M
Universal (or Unique) Swap Identifier | Universal (or Unique) Swap Identifier (USI) namespace and USI. The USI namespace and the USI should be separated by a pipe "|" character | M
Option Exercise Style | Exercise style | C
Option Put/Call Indicator | Option type | M
Option Strike Price | Option strike price | M
Underlying Settlement Price/Currency | Settlement price, prior settlement price, settlement currency, and final settlement date | M
Underlying Exchange Commodity Code | Underlying Contract code issued by the exchange | C
Underlying Clearing Commodity Code | Registered commodity clearing identifier. The code is for the contract as if it was traded in the form it is cleared. For example, if the contract was traded as a spread but cleared as an outright, the outright symbol should be used | M
Underlying Product Type | Indicates the type of product the security is associated with | C
Underlying Security Group (Sector) | A name assigned to a group of related instruments which may be concurrently affected by market events and actions | C
Underlying Maturity Month Year | Month and year of the maturity | M
Underlying Maturity Date | The date on which the principal amount becomes due | C
Underlying Asset Class | The underlying broad asset category for assessing risk exposure | M
Underlying Asset Subclass | The subcategory description of the asset class | C
Underlying Asset Type | Provides a more specific description of the asset subclass | C
Underlying Exchange Code (MIC) | Exchange where the underlying instrument is traded | M
Underlying Security Type | Indicates type of security | M
Underlying Security Description | Textual description of a financial instrument | C
DELTA | Delta is the measure of how the option's value varies with changes in the underlying price | C
Credit Default Swaps (Daily Position Reporting)
Settlement Price/Currency | Settlement price, prior settlement price, settlement currency, and final settlement date | M
Exchange Security Identifier | Contract code issued by the exchange | O
Redcode | The code assigned to the CDS by Markit that identifies the referenced entity or the index, series and version. (Underlying instrument is required for Security Type = SWAPTION.) | M
Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to Commission regulation 17 CFR 45.7 | O
Security Type | Indicator which identifies the derivative type | M
Restructuring Type | This field is used if the index has been restructured due to a credit event | M
Seniority Type | The class of debt | M
Maturity Date | The date on which the principal amount becomes due | C
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
Reference Entity Type (Sector) | Specifies the type of reference entity for first-to-default CDS basket contracts. The Markit sector code should be provided when available | M
Coupon Rate | The coupon rate associated with this CDS transaction stated in Basis Points | M
Security Description (Reference Entity) | Name of CDS index or single-name or sovereign debt | M
Recovery Factor | The assumed recovery rate used to determine the CDS price | O
Position (Long) | Long position size. If a position is quoted in a UOM different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
Position (Short) | Short position size. If a position is quoted in a UOM different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
5 YR Equivalent Notional | The five-year equivalent notional amount for each risk factor/reference entity CDS contract | M
Accrued Coupon | Coupon obligation from the first day of the coupon period through the current clearing trade date | M
Profit and Loss | Unrealized P&L or mark to market value of position(s) including change in mark to market plus change in accrued coupon plus change in unsettled upfront fees. Does not include cash flows related to quarterly coupon payments, credit event payments, or price alignment interest | M
Credit Exposure (CS01) | The credit exposure of the swap at a given point in time. CS01 = Spread DV01 = "dollar" value of a basis point = In currency (not percentage) terms, the change in fair value of the leg, transaction, position, or portfolio (as appropriate) commensurate with a 1 basis point (0.01 percent) instantaneous, hypothetical increase in the related credit spread curves. CS01/Spread DV01 may refer to non-dollar currencies and related curves. From the DCO's point of view: positive CS01 = gain in value resulting from 1 basis point increase, negative CS01 = loss of value resulting from 1 basis point increase | C
Mark to Market | Determined by marking the end of day position(s) from par (100%) to the end of day settlement price | M
Price Value of a Basis Point (PV01) | Change in P&L of a position given a one basis point move in CDS spread value. May also be referred to as DV01, Sprd DV01 | M
Previous Accrued Coupon | Previous day's accrued coupon | M
Previous Mark to Market | Previous day's mark to market | M
Universal (or Unique) Swap Identifier | Universal (or Unique) Swap Identifier (USI) namespace and USI. The USI namespace and the USI should be separated by a pipe "|" character | O
Option Strike Price | Option strike price | C
Settlement Method | Method of settlement | C
Option Exercise Style | Exercise style | C
Option Put/Call Indicator | Option type | C
Option Type | Specifies the option type | C
Option Start Date | The option adjusted start date | C
Option Expiration Date—Adjusted | The CDS option adjusted expiration date | C
Underlying Exchange Security Identifier | The underlying contract alias used by outside vendors to uniquely identify the contract | O
Underlying Clearing Security Identifier (Red Code) | The underlying code assigned to the CDS by Markit that identifies the referenced entity or the index, series and version | C
Underlying Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to Commission regulation 17 CFR 45.7 | O
Underlying Security Type | Indicator which identifies the underlying derivative type | C
Underlying Restructuring Type | This field is used if the underlying index has been restructured due to a credit event | C
Underlying Seniority Type | The underlying class of debt | C
Underlying Maturity Date | The date on which the principal amount becomes due | C
Underlying Asset Class | The underlying broad asset category for assessing risk exposure | C
Underlying Asset Subclass | The subcategory description of the asset class | C
Underlying Asset Type | Provides a more specific description of the asset subclass | C
Underlying Reference Entity Type (Sector) | Specifies the type of underlying reference entity for first-to-default CDS basket contracts | C
Underlying Coupon Rate | The underlying coupon rate associated with this CDS transaction stated in basis points | C
Underlying Security Description | Textual description of a financial instrument | C
Underlying Recovery Factor | The assumed recovery rate used to determine the underlying CDS price | C
DELTA | Delta is the measure of how the option's value varies with changes in the underlying price | M
GAMMA | Gamma is the rate of change for delta with respect to the underlying asset's price | M
RHO | Rho measures the sensitivity of an option's price to a variation in the risk-free interest rate | M
THETA | Theta is the rate at which an option loses value as time passes | M
VEGA | Vega is the measurement of an option's sensitivity to changes in the volatility of the underlying asset | M
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C
Option Premium Date | Date swaption premium is paid | C
Foreign Exchange (Daily Position Reporting)
Settle Date | Settle date of the position | M
Settlement Price/Fixing Currency | Settlement price of the position | M
Discount Factor | Discount factor for the position. Use the factor for the Mark to Market (MTM) currency | M
Valuation Date | Valuation date of the position | M
Delivery Date | Delivery date of the position | M
Clearing Security Identifier | Code assigned by the DCO for a particular contract | M
Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to Commission regulation 17 CFR 45.7 | O
Security Type | Registered commodity clearing identifier. (Underlying instrument is required for Security Type = FXOPT | FXNDO.) | M
Maturity Month Year | Month and year of the maturity | C
Maturity Date (Expiration) | Specifies date of maturity (a calendar date). Used for FXFWD/FXNDF. For non-deliverable forwards (NDFs), this represents the fixing date of the contract | C
Maturity Time (Expiration) | The contract expiration time. (Used for FXFWD/FXNDF.) | C
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
Valuation Method | Specifies the type of valuation method applied | C
Security Description | Used to provide a textual description of a financial instrument | C
Foreign Exchange Type | Identifies the type of FX contract. Use Typ = 7 for direct FX (e.g., EUR/USD). Use Typ = 16 for NDFWD contracts (e.g., THB/INR settled in USD) | M
Currency One | Specifies the first or only reference currency of the trade | M
Currency Two | Specifies the second reference currency of the trade | M
Quote Basis | For foreign exchange quanto option feature | M
Fixed Rate | (FXFWD or FXNDF only). Specifies the forward FX rate alternative | C
Spot Rate | Specifies the FX spot rates the first or only reference currency of the trade | C
Forward Points | (FXFWD or FXNDF only) The interest rate differential in basis points between the base and quote currencies in a forward rate quote. May be a negative value. (The number of basis points added to or subtracted from the current spot rate of a currency pair to determine the forward rate for delivery on a specific value date.) | C
Delivery Type Indicator | Delivery type indicator | M
Position—Long | Gross long position. An affirmative zero value should be reported for the long position. (Both long and short positions are required.) For FXNDF use Typ = DLV for settlement currency | M
Position—Short | Gross short position. An affirmative zero value should be reported for the short position. (Both long and short positions are required.) For FXNDF use Typ = DLV for settlement currency | M
Final Mark to Market | Mark to market which includes the discount factor | M
Dollar Value of a Basis Point (DV01)—Long Currency | The dollar value of a one basis point change (DV01) in the yield of the underlying security and that of the hedging vehicle | M
Dollar Value of a Basis Point (DV01)—Short Currency | The dollar value of a one basis point change (DV01) in the yield of the underlying security and that of the hedging vehicle | M
Net Cash Flow | Net cash flow recognized on report date (with actual settlements occurring according to the currency's settlement conventions). E.g., profit/loss, price alignment interest, cash payments (fees, coupons, etc.) | M
Undiscounted Mark to Market | Mark to market, which does not include the discount factor | M
Price Alignment Interest | To minimize the impact of daily cash variation margin payments on the pricing of swaps, the DCO will charge interest on cumulative variation margin received and pay interest on cumulative variation margin paid | M
Universal (or Unique) Swap Identifier | Universal (or Unique) Swap Identifier (USI) namespace and USI. The USI namespace and the USI should be separated by a pipe "|" character | M
Option Put/Call Indicator | Option type | C
Strike Rate | Option strike rate | C
Option Exercise Style | Exercise style | C
Option Cut Name | The code by which the expiry time is known in the market | C
Underlying Settlement Price/Fixing Currency | Settlement price for the position. (Underlying settlement is required for FXOPT, FXNDO.) | C
Underlying Exchange Security Code | Security code issued by the exchange; e.g., ticker symbol, the human recognizable trading identifier | C
Underlying Clearing Security Identifier | Code assigned by the DCO for the underlying contract | C
Underlying Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to Commission regulation 17 CFR 45.7 | O
Underlying Security Type | Indicator which identifies the underlying derivative | C
Underlying Maturity Month Year | Month and year of the maturity | C
Underlying Maturity Date (Expiration) | For FXFWD/FXNDF, the date on which the principal amount becomes due. For NDFs, this represents the fixing date of the contract | C
Underlying Exchange Identifier (MIC) | Exchange where the underlying instrument is traded | C
Underlying Security Description | Textual description of a financial instrument | C
Option Long/Short Indicator | Indicates whether the option is short or long | C
Option Expiration | Adjusted option expiration date | C
Notional Long/Short | FX currency notional long or short | M
Implied Volatility | The implied volatility and quotation style for the contract, typically in natural log percent or index points | C
DELTA | Delta is the measure of how the option's value varies with changes in the underlying price | M
GAMMA | Gamma is the rate of change for delta with respect to the underlying asset's price | M
RHO | Rho measures the sensitivity of an option's price to a variation in the risk-free interest rate | M
THETA | Theta is the rate at which an option loses value as time passes | M
VEGA | Vega is the measurement of an option's sensitivity to changes in the volatility of the underlying asset | M
Option Premium MTM | Premium mark to market, which includes the discount factor | C
Interest Rate Swaps (Daily Position Reporting)
Cleared Date | Date on which the trade was cleared at the DCO | M
Position Status | Position status: active, or terminated. Terminated positions should only be reported on the day of termination | M
DCO Pays Indicator | Indicate which cash flow the DCO pays | M
DCO Receives Indicator | Indicate which cash flow the DCO receives | M
Clearing Participant Pays Indicator | Indicate which cash flow the clearing member pays | M
Clearing Participant Receives Indicator | Indicate which cash flow the clearing member receives | M
Clearing Security Identifier | Code assigned by the DCO for a particular contract | M
Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to Commission regulation 17 CFR 45.7 | O
Security Type | Registered commodity clearing identifier | M
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
Swap Class | The classification or type of swap | M
Swap Subclass | The sub-classification or notional schedule type of the swap | C
Security Description | Used to provide a textual description of a financial instrument | M
Leg Type | Identifies if the leg is fixed or floating | M
Leg Notional | Notional amount associated with leg | M
Leg Notional Currency | Currency of the leg's notional amount | M
Leg Start Date Adj Bus Day Conv | If start date falls on a weekend or holiday, value defines how to adjust actual start date | C
Leg Start Date | Leg's effective date | M
Leg Maturity Date Adj Bus Day Conv | If the maturity date falls on a weekend or holiday, value defines how to adjust actual maturity date | C
Leg Maturity Date | The date on which the leg's principal amount becomes due | M
Leg Maturity Date Adj Calendar | Regarding the maturity date, this specifies which dates are considered holidays | C
Leg Calculation Period Adjusted Business Day Convention | If a date defining the calculation period falls on a holiday, this adjusts the actual dates based on the definition of the input | C
Leg Calculation Frequency | Calculation frequency, also known as the compounding frequency for compounded swaps | M
Leg First Reg Per Start Date | If there is a beginning stub, this indicates the date when the usual payment periods will begin | C
Leg Last Reg Per End Date | If there is an ending stub, this indicates the date when the usual payment periods will end | C
Leg Roll Conv | Indicates the day of the month when the payment is made | C
Leg Calc Per Adj Calendar | Regarding the calculation period, this specifies which dates are considered holidays | C
Leg Daycount | Defines how interest is accrued/calculated | C
Leg Comp Method | If payments are made on one timeframe but calculations are made on a shorter timeframe, this describes how to compound interest | C
Leg Pay Adj Bus Day Conv | If cash flow pay or receive date falls on a weekend or holiday, value defines actual date payment is made | C
Leg Pay Frequency | Frequency at which payments are made | M
Leg Pay Relative To | Payment relative to the beginning or end of the period | C
Leg Payment Lag | Number of business days after payment due date on which the payment is actually made | C
Leg Pay Adj Calendar | Regarding dates on which cash flow payments/receipts are scheduled, this specifies which dates are considered holidays | C
Leg Reset Relative To | Specifies whether reset dates are determined with respect to each adjusted calculation period start date or adjusted calculation period end date | C
Leg Reset Date Adj Bus Day Conv | Business day convention to apply to each reset date if the reset date falls on a holiday | C
Leg Reset Frequency | Frequency at which resets occur. If the Leg Reset Frequency is greater than the calculation per frequency, more than 1 reset date should be established for each calculation per frequency and some form of rate averaging is applicable | C
Leg Fixing Date Bus Day Conv | Business day convention to apply to each fixing date if the fixing date falls on a holiday | C
Leg Fixing Date Offset | Specifies the fixing date relative to the reset date in terms of a business days offset | C
Leg Fixing Day Type | The type of days to use to find the fixing date (i.e., business days, calendar days, etc.) | C
Leg Reset Date Adj Calendar | Regarding reset dates, this specifies which dates are considered holidays | C
Leg Fixing Date Calendar | Regarding the fixing date, this specifies which dates are considered holidays | C
Leg Fixed Rate or Amount | Only populate if Leg1 is Type "Fixed". This should be expressed in decimal form (e.g., 4% should be input as ".04") | C
Leg Index | If Stream is floating rate, this gives the index applicable to the floating rate | C
Leg Index Tenor | For the floating rate leg, the tenor of the leg. For the fixed rate leg, NULL | C
Leg Spread | Describes if there is a spread (typically an add-on) applied to the coupon rate | C
Leg Pmt Sched Notional | Variable notional swap notional values | C
Leg Initial Stub Rate | The interest rate applicable to the Initial Stub Period in decimal form (e.g., 4% should be input as ".04") | C
Leg Initial Stub Rate Index 1 | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the first index | C
Leg Initial Stub Rate Index 2 Tenor | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the second index | C
Leg Final Stub Rate | The interest rate applicable to the final stub period in decimal form (e.g., 4% should be input as ".04") | C
Leg Final Stub Rate Index 1 | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the first index | C
Leg Final Stub Rate Index 2 Tenor | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the second index | C
Accrued Coupon (Interest) | Net accrued coupon amount since the last payment in the leg currency. If reported by leg, indicate the associated stream (leg) description (e.g., "FIXED/FLOAT," "FLOAT1/FLOAT2") | M
Profit/Loss | Profit/loss resulting from changes in value due to changes in underlying curve movements or floating index rate resets. This should exclude impacts to NPVs from extraneous cash flows (price alignment interest, fees, and coupons) | M
Leg Current Period Rate | If leg is a floating leg, this indicates the current rate used to calculate the next floating Leg coupon in decimal form (e.g., 4% should be input as ".04") | M
Leg Coupon Payment | Coupon amount for T + 1 in the leg currency. This should reflect the net cash flow that will actually occur on the following business day. Negative number indicates that a payment was made | M
Dollar Value of Basis Point (DV01) | Change in value in USD if the relevant pricing curve is shifted up by 1 basis point. DV01 = "dollar" value of a basis point in currency (not percentage) terms, the change in fair value of the leg, transaction, position, or portfolio (as appropriate) commensurate with a 1 basis point (0.01 percent) instantaneous, hypothetical increase in the related zero-coupon curves. DV01 may refer to non-dollar currencies and related curves. From the DCO's point of view: positive DV01 = profit/gain resulting from 1 basis point increase, negative DV01 = loss resulting from 1 basis point increase | M
Net Cash Flow | Net cash flow recognized on report date (with actual settlements occurring according to the currency's settlement conventions). E.g., Profit/Loss, price alignment interest, cash payments (fees, coupons, etc.) | M
Net Present Value | Net present value (NPV) of all positions by currency | M
Present Value of Other Payments | Includes the present value of any upfront and/or final/settlement payments that will be settled after the report date. Only include amounts that are affecting the NPV of current trades | M
Net Present Value Previous | Previous day's NPV by currency | C
Price Alignment Interest | To minimize the impact of daily cash variation margin payments on the pricing of swaps, the DCO will charge interest on cumulative variation margin received and pay interest on cumulative variation margin paid | M
Other Payments | Includes any upfront and/or final/settlement payments made/received for the trade date. (Indicate gross pay/collect amounts.) | C
Universal (or Unique) Swap Identifier | Universal (or Unique) Swap Identifier (USI) namespace and USI. The USI namespace and the USI should be separated by a pipe "|" character | C
Leg Initial Exchange | Amount of any exchange of cash flow at initiation of trade being cleared | C
Leg Initial Exchange Date | Date that the initial exchange is set to occur | C
Leg Final Exchange | Amount of any exchange of cash flow at maturity of trade | C
Leg Final Exchange Date | Date that the final exchange is set to occur | C
Option Exercise Style | Exercise style | C
Option Type | Specifies the option type | C
Option Start Date | The option adjusted start date | C
Option Adjusted Expiration Date | The IRS swaption adjusted expiration date | C
Option Buy/Sell Indicator | Indicates the buyer or seller of a swap stream | C
Underlying Clearing Security Identifier | Code assigned by the DCO for the underlying contract | C
Underlying Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to 17 CFR 45.7 | C
Underlying Security Type | Indicator which identifies the underlying derivative | C
Underlying Asset Class | The underlying broad asset category for assessing risk exposure | C
Underlying Asset Subclass | The subcategory description of the asset class | C
Underlying Asset Type | Provides a more specific description of the asset subclass | C
Underlying Swap Class | The classification or type of swap | C
Underlying Swap Subclass | The sub-classification or notional schedule type of the swap | C
Underlying Security Description | Textual description of a financial instrument | C
Underlying Security Leg Type | Identifies if the leg is fixed or floating | C
Underlying Security Leg Notional | Notional amount associated with leg | C
Underlying Security Leg Currency | Currency of this leg's notional amount | C
Underlying Security Leg Index | If stream is floating rate, this gives the index applicable to the floating rate | C
Underlying Security Leg Index Tenor | For the floating rate leg, the tenor of the leg. For the fixed rate leg, NULL | C
Underlying Security Leg Fixed Rate Or Amount | Only populate if Leg1 is type "Fixed". This should be in decimal form (e.g., 4% should be input as ".04") | C
Underlying Security Leg Spread | Indicates whether there is a spread (typically an add-on) applied to the coupon rate | C
DELTA | Delta is the measure of how the option's value varies with changes in the underlying price | M
GAMMA | Gamma is the rate of change for delta with respect to the underlying asset's price | M
RHO | Rho measures the sensitivity of an option's price to a variation in the risk-free interest rate | M
THETA | Theta is the rate at which an option loses value as time passes | M
VEGA | Vega is the measurement of an option's sensitivity to changes in the volatility of the underlying asset | M
Option Premium | Premium registered on the given trading date. The amount of money that the options buyer must pay the options seller | C
Option Premium Date | Date option premium is paid | C
Trade Date | Date a transaction was originally executed, resulting in the generation of a new USI. For clearing swaps, the date when the DCO accepts the original swap | M
Event Description | Description for each position record | C
Forward Rate Agreements (Daily Position Reporting)
Previous Business Date | Previous business date | M
Position Status | Position status: active or terminated. Terminated positions should only be reported on the day of termination | M
DCO Pays Indicator | Indicates which cash flow the DCO pays | M
DCO Receives Indicator | Indicates which cash flow the DCO receives | M
Clearing Participant Pays Indicator | Indicates which cash flow the clearing member pays | M
Clearing Participant Receives Indicator | Indicates which cash flow the clearing member receives | M
Clearing Security Identifier | Code assigned by the DCO for a particular contract | M
Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to 17 CFR 45.7 | O
Security Type | Registered commodity clearing identifier | M
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
FRA Type | Type of swap stream | M
Notional Amount | Stream notional amount | M
Notional Currency | Currency of leg notional amount | M
Start Date | Date the position was established | M
Maturity Date | The date on which the principal amount becomes due | M
Payment Day Count Convention | Defines how interest is accrued/calculated | M
Payment Accrual Days | Number of accrual days between the effective date and maturity date | M
First Payment Date | Date on which the payment is made. Always report the adjusted date | C
Reset Date Bus Day Convention | Business day convention to apply to each fixing date if the fixing date falls on a holiday | M
Reset Date Fixing Date | Date on which the payment is fixed. Always report the adjusted date | M
Fixed Rate | The fixed amount in decimal terms | M
Float Index | The index for the floating portion of the Forward Rate Agreement (FRA) | M
Float First Tenor | First tenor associated with the index | M
Float Second Tenor | Second tenor associated with the index | C
Float Spread | In basis point terms | M
Float Reference Rate | The fixed floating rate in decimal terms | M
PV01 | Change in value in native currency if the relevant pricing curve is shifted up by 1 basis point | M
Dollar Value of Basis Point (DV01) | Change in value in USD if the relevant pricing curve is shifted up by 1 basis point. DV01 = "dollar" value of a basis point in currency (not percentage) terms, the change in fair value of the leg, transaction, position, or portfolio (as appropriate) commensurate with a 1 basis point (0.01 percent) instantaneous, hypothetical increase in the related zero-coupon curves. DV01 may refer to non-dollar currencies and related curves. From the DCO's point of view: positive DV01 = profit/gain resulting from 1 basis point increase, negative DV01 = loss resulting from 1 basis point increase | M
Net Present Value | Net present value (NPV) of all positions by currency | M
Settlement FX Info | Settlement price foreign exchange conversion rate | M
Net Present Value Previous | Previous day's NPV by currency | M
Price Alignment Interest | To minimize the impact of daily cash variation margin payments on the pricing of swaps, the DCO will charge interest on cumulative variation margin received and pay interest on cumulative variation margin paid | M
Universal (or Unique) Swap Identifier | Universal (or Unique) Swap Identifier (USI) namespace and USI. The USI namespace and the USI should be separated by a pipe "|" character | C
Settlement Amount | The amount paid/received on the Payment Date. Always report adjusted date. (The position pays on a negative amount.) | M
Other Payments | Includes any upfront and/or final/settlement payments made/received for the trade date. (Indicate gross pay/collect amounts.) | C
Net Cash Flow | Net cash flow recognized on report date (with actual settlements occurring according to the currency's settlement conventions). E.g., profit/loss, price alignment interest, cash payments (fees, coupons, etc.) | C
Profit/Loss | Profit/Loss resulting from changes in value due to changes in underlying curve movements or floating index rate resets. Should exclude impacts to NPVs from extraneous cash flows (price alignment interest, fees, and coupons) | C
Present Value of Other Payments | Includes the present value of any upfront and/or final/settlement payments that will be settled after the report date. Only include amounts that are affecting the NPV of current trades | C
Trade Date | Actual trade date for each position record (including specifically, the cleared date and the trade date) | M
Event Description | Description for each position record | C
Inflation Index Swaps (Daily Position Reporting)
Cleared Date | Date on which the trade was cleared at the DCO | M
Position Status | Position's status: active or terminated. Terminated positions should only be reported on the day of termination | M
DCO Pays Indicator | Indicate which cash flow the DCO pays | M
DCO Receives Indicator | Indicate which cash flow the DCO receives | M
Clearing Participant Pays Indicator | Indicate which cash flow the clearing member pays | M
Clearing Participant Receives Indicator | Indicate which cash flow the clearing member receives | M
Clearing Security Identifier | Code assigned by the DCO for a particular contract | M
Unique Product Identifier | A unique set of characters that represents a particular swap. The Commission will designate a UPI pursuant to 17 CFR 45.7 | O
Security Type | Registered commodity clearing identifier | M
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
Swap Class | The classification or type of swap | M
Swap Subclass | The sub-classification or notional schedule type of the swap | C
Security Description | Used to provide a textual description of a financial instrument | M
Leg Type | Identifies if the leg is fixed or floating | M
Leg Notional | Notional amount associated with leg | M
Leg Notional Currency | Currency of the leg's notional amount | M
Leg Start Date Adj Bus Day Conv | If start date falls on a weekend or holiday, value defines how to adjust actual start date | C
Leg Start Date | Leg's effective date | M
Leg Maturity Date Adj Bus Day Conv | If the maturity date falls on a weekend or holiday, value defines how to adjust actual maturity date | C
Leg Maturity Date | The date on which the leg's principal amount becomes due | M
Leg Maturity Date Adj Calendar | Regarding the maturity date, this specifies which dates are considered holidays | C
Leg Calc Per Adj Bus Day Conv | If a date defining the calculation period falls on a holiday, this adjusts the actual dates based on the definition of the input | C
Leg Calc Frequency | Calculation frequency, also known as the compounding frequency for compounded swaps | M
Leg Roll Conv | Describes the day of the month when the payment is made | C
Leg Calc Per Adj Calendar | Regarding the calculation period, this specifies which dates are considered holidays | C
Leg Stream Daycount | Defines how interest is accrued/calculated | M
Payment Stream Comp Method | If payments are made on one timeframe but calculations are made on a shorter timeframe, this describes how to compound interest | C
Payment Stream Business Day Conv | If cash flow pay or receive date falls on a weekend or holiday, value defines actual date payment is made | C
Payment Stream Frequency | Frequency at which payments are made | M
Payment Stream Relative To | Specifies the anchor date when the payment date is relative to that date | C
Payment Stream First Date | The unadjusted first payment date | C
Payment Stream Last Regular Date | The unadjusted last regular payment date | C
Payment Leg Calendar | Regarding dates on which cash flow payments/receipts are scheduled, this specifies which dates are considered holidays | C
Leg Reset Date Bus Day Conv | Business day convention to apply to each reset date if the reset date falls on a holiday | C
Leg Reset Date Relative To | Specifies the anchor date when reset date is relative to that date | C
Leg Reset Frequency | Frequency at which resets occur. If the Leg Reset Frequency is greater than the calculation per frequency, more than 1 reset date should be established for each calculation per frequency and some form of rate averaging is applicable | C
Leg Reset Fixing Date Offset | Specifies the fixing date relative to the reset date in terms of a business days offset | C
Leg Fixing Day Type | The type of days to use to find the fixing date (i.e., business days, calendar days, etc.) | C
Leg Reset Date Calendar | Regarding reset dates, this specifies which dates are considered holidays | C
Leg Fixing Date Bus Day Conv | Business day convention to apply to each fixing date if the fixing date falls on a holiday | C
Leg Fixing Date Calendar | Regarding the fixing date, this specifies which dates are considered holidays | C
Fixed Leg Rate or Amount | Only populate if Leg1 is Type "Fixed". This should be expressed in decimal form (e.g., 4% should be input as.04) | C
Floating Leg Inflation Index | If leg is floating rate, this gives the index applicable to the floating rate | C
Floating Leg Spread | Describes if there is a spread (typically an add-on) applied to the coupon rate | C
Floating Leg Payment Inflation Lag | Number of business days after payment due date on which the payment is actually made | C
Floating Leg Payment Inflation Interpolation Method | The method used when calculating the inflation index level from multiple points. The most common is the linear method | C
Floating Leg Inflation Index Initial Level | Initial known index level for the first calculation period | C
Floating Leg Inflation Index Fallback Bond Ind | Indicates whether a fallback bond as defined in the 2006 International Swaps and Derivatives Association (ISDA) Inflation Derivatives Definitions, sections 1.3 and 1.8, is applicable or not. If not specified, the default value is "Y" (True/Yes) | O
Leg Pmt Sched Notional | Variable notional swap notional values | C
Leg Stub Type | Stubs apply to initial or ending periods that are shorter than the usual interval between payments | C
Leg Initial Stub Fixed Rate | The interest rate applicable to the Initial Stub Period in decimal form (e.g., 4% should be input as ".04") | C
Leg Final Stub Fixed Rate | The interest rate applicable to the final stub period in decimal form (e.g., 4% should be input as ".04") | C
Leg Initial Stub Floating Rate Index 1 Tenor | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the first index | C
Leg Initial Stub Floating Rate Index 2 Tenor | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the second index | C
Leg Final Stub Floating Rate Index 1 Tenor | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the first index | C
Leg Final Stub Rate Floating Index 2 Tenor | Stub rate can be a linear interpolation between two floating rate tenors. E.g., if the stub period is 2 months, rate is linear interpolation of 1-month and 3-month reference rates. Specify the second index | C
Leg First Reg Per Start Date | If there is a beginning stub, this describes the date when the usual payment periods will begin | C
Leg Last Reg Per End Date | If there is an ending stub, this describes the date when the usual payment periods will end | C
Leg Accrued Interest (Coupon) | The net accrued coupon amount since the last payment in the leg currency. If reported by leg, indicate the associated stream (leg) description (e.g., "FIXED/FLOAT," "FLOAT1/FLOAT2") | M
Profit/Loss | Profit/Loss resulting from changes in value due to changes in underlying curve movements or floating index rate resets. This should exclude impacts to NPVs from extraneous cash flows (price alignment interest, fees, and coupons) | M
Leg Coupon Amount | Coupon amount for T + 1 in the leg currency. This should reflect the net cash flow that will actually occur on the following business day. A negative number indicates payment was made | M
Leg Current Period Coupon Rate | If leg is a floating leg, this indicates the current rate used to calculate the next floating leg coupon in decimal form (e.g., 4% should be input as ".04") | M
I01 | Change in value in native currency if the relevant pricing curve is shifted up by 1 basis point | M
Dollar Value of Basis Point (DV01) | Change in value in native currency of the swap/swaption/floor/cap if relevant pricing curve is shifted up by 1 basis point. DV01 = "dollar" value of a basis point in currency (not percentage) terms, the change in fair value of the leg, transaction, position, or portfolio (as appropriate) commensurate with a 1 basis point (0.01 percent) instantaneous, hypothetical increase in the related zero-coupon curves. DV01 may refer to non-dollar currencies and related curves. From the DCO's point of view: positive DV01 = profit/gain resulting from 1 basis point increase, negative DV01 = loss resulting from 1 basis point increase | M
Net Cash Flow | Net cash flow recognized on report date (with actual settlements occurring according to the currency's settlement conventions). E.g., profit/loss, price alignment interest, cash payments (fees, coupons, etc.) | M
Net Present Value | Net present value (NPV) of all positions by currency | M
Present Value Of Other Payments | Includes the present value of any upfront and/or final/settlement payments that will be settled after the report date. Only include amounts that are affecting the NPV of current trades | M
Net Present Value Previous | Previous day's NPV by currency | C
Price Alignment Interest | To minimize the impact of daily cash variation margin payments on the pricing of swaps, the DCO will charge interest on cumulative variation margin received and pay interest on cumulative variation margin paid | M
Universal or Unique) Swap Identifier | Universal (or Unique) Swap Identifier (USI) namespace and USI. Enter the USI Namespace and the USI separated by a pipe "|" character. | C
Stream Initial Exchange | Amount of any exchange of cash flow at initiation of trade being cleared | C
Stream Initial Exchange Date | Date that the initial exchange is set to occur | C
Stream Final Exchange | Amount of any exchange of cash flow at maturity of trade | C
Stream Final Exchange Date | Date that the final exchange is set to occur | C
Other Payments | Includes any upfront and/or final/settlement payments made/received for the trade date. (Indicate gross pay/collect amounts.) | C
Trade Date | Actual trade date for each position record (including specifically, the cleared date and the trade date) | M
Event Description | Description for each position record | C
Equity Cross Margin (Daily Position Reporting)
Exchange Security Identifier | Contract code issued by the exchange | M
Clearing Security Identifier | Code assigned by the DCO for a particular contract | M
Product Type | Indicates the type of product the security is associated with | C
Security Type | Indicates type of security | M
Maturity Month Year | Month and year of the maturity | M
Maturity Date | The date on which the principal amount becomes due. For NDFs, this represents the fixing date of the contract | C
Asset Class | The broad asset category for assessing risk exposure | M
Asset Subclass | The subcategory description of the asset class | C
Asset Type | Provides a more specific description of the asset subclass | C
Security Description | Used to provide a textual description of a financial instrument | M
Position (Long) | Long position size. If a position is quoted in a unit of measure (UOM) different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
Position (Short) | Short position size. If a position is quoted in a UOM different from the contract, specify the UOM. If a position is measured in a currency, specify the currency | M
Settlement Price/Currency | Settlement price, prior settlement price, settlement currency, and final settlement date | M
Option Strike Price | Option strike price | C
Option Put/Call Indicator | Option type | C
Underlying Exchange Commodity Code | Underlying Contract code issued by the exchange | C
Underlying Clearing Commodity Code | Registered commodity clearing identifier. The code is for the contract as if it were traded in the form it is cleared. For example, if the contract was traded as a spread but cleared as an outright, the outright symbol should be used | C
Underlying Product Type | Indicates the type of product the security is associated with | C
Underlying Security Type | Indicator which identifies the underlying derivative | C
Underlying Maturity Month Year | Month and year of the maturity | C
Underlying Maturity Date | The date on which the principal amount becomes due | C
Underlying Asset Class | The underlying broad asset category for assessing risk exposure | C
Underlying Asset Subclass | The subcategory description of the asset class | C
Underlying Asset Type | Provides a more specific description of the asset subclass | C
Underlying Settlement Price/Currency | Settlement price, prior settlement price, settlement currency, and final settlement date | C
M = mandatory C = conditional O = optional.
C. Risk Metric Ladder Reporting
Field name | Description | Use
Common Fields (Risk Metric Ladder Reporting)
Total Message Count | The total number of reports included in the file | M
FIXML Message Type | FIXML account summary report type | M
Sender ID | The CFTC-issued DCO identifier | M
To ID | Indicate "CFTC" | M
Message Transmit Datetime | The date and time the file is transmitted | M
Report ID | A unique identifier assigned by the CFTC to each clearing member report | M
Report Date | The business date of the information being reported | M
Base Currency | Base currency referenced throughout report; provide exchange rate against this currency | M
Report Time (Message Create Time) | The report "as of" or information cut-off time | M
Message Event | The event source being reported | M
Ladder Indicator | Indicator that identifies the type of risk metric ladder | M
DCO Identifier | CFTC-assigned identifier for a DCO | M
Clearing Participant Identifier | DCO-assigned identifier for a particular clearing member | M
Clearing Participant Name | The name of the clearing member | M
Fund Segregation Type | Clearing fund segregation type | M
Clearing Participant LEI | LEI for a particular clearing member | M
Clearing Participant LEI Name | The LEI name associated with the clearing member LEI | M
Customer Identifier | Proprietary identifier for a particular customer position account | C
Customer Name | The name associated with the customer position identifier | C
Customer Account Type | Type of account used for reporting | C
Customer LEI | LEI for a particular customer; provide if available | C
Customer LEI Name | The LEI name associated with the customer position LEI | C
Unique Margin Identifier | A single field that uniquely identifies the margin account. This field us used to identify associated positions | C
Delta Ladder (Daily Reporting)
Currency | ISO 4217 currency code | M
FX Rate | Rate used to convert the currency to USD | M
Curve Name | Name of the reference curve | M
Tenor | Number of days from the report date | M
Sensitivity | Theoretical profit and loss with a single upward basis point shift | M
Gamma Ladder (Daily Reporting)
Currency | ISO 4217 currency code | M
FX Rate | Rate used to convert the currency to USD | M
Curve Name | Name of the reference curve | M
Tenor | Number of days from the report date | M
Sensitivity | Theoretical profit and loss with a single upward basis point shift | M
Vega Ladder (Daily Reporting)
Currency | ISO 4217 currency code | M
FX Rate | Rate used to convert the currency to USD | M
Curve Name | Name of the reference curve | M
Tenor | Number of days from the report date | M
Sensitivity | Theoretical profit and loss with a single upward basis point shift | M
M = mandatory C = conditional O = optional.
D. Curve Reference Reporting
Field name | Description | Use
Common Fields (Curve Reference Reporting)
Total Message Count | The total number of reports included in the file | M
FIXML Message Type | FIXML account summary report type | M
Sender ID | The CFTC-issued DCO identifier | M
To ID | Indicate "CFTC" | M
Message Transmit Datetime | The date and time the file is transmitted | M
Report ID | A unique identifier assigned by the CFTC to each clearing member report | M
Report Date | The business date of the information being reported | M
Base Currency | Base currency referenced throughout report; provide exchange rate against this currency | M
Report Time (Message Create Time) | The report "as of" or information cut-off time | M
Message Event | The event source being reported | M
DCO Identifier | CFTC-assigned identifier for a DCO | M
Currency Curve (Daily Reporting)
Curve | Reference curve name | M
Currency | ISO 4217 currency code | M
Maturity Date | The date on which the principal amount becomes due | M
Par Rate | Rate such that the maturity will pay in order to sell at par today | M
Zero Rate Curve (Daily Reporting)
Currency | ISO 4217 currency code | M
Curve | Reference curve name | M
Maturity Date | The date on which the principal amount becomes due | M
Offset | The difference in days between the maturity date and reporting date | M
Accrual Factor | The difference in years between the maturity date and reporting date | M
Discount Factor | Value used to compute the present value of future cash flows values | M
Zero Rate | Averages of the one-period forward rates up to their maturity | M
M = mandatory C = conditional O = optional.
E. Backtesting Reporting
Field name | Description | Use
Common Fields (Backtesting Reporting)
Total Message Count | The total number of reports included in the file | M
FIXML Message Type | FIXML account summary report type | M
Sender ID | The CFTC-issued DCO identifier | M
To ID | Indicate "CFTC" | M
Message Transmit Datetime | The date and time the file is transmitted | M
Report ID | A unique identifier assigned by the CFTC to each clearing member report | M
Report Date | The business date of the information being reported | M
Base Currency | Base currency referenced throughout report; provide exchange rate against this currency | M
Report Time (Message Create Time) | The report "as of" or information cut-off time | M
Message Event | The event source being reported | M
Breach Indicator | Indicates the breach file | M
DCO Identifier | CFTC-assigned identifier for a DCO | M
Clearing Participant Identifier | DCO-assigned identifier for a particular clearing member | M
Clearing Participant Name | The name of the clearing member | M
Fund Segregation Type | Clearing fund segregation type | M
Clearing Participant LEI | LEI for a particular clearing member | M
Clearing Participant LEI Name | The LEI name associated with the clearing member LEI | M
Customer Identifier | Proprietary identifier for a particular customer position account | C
Customer Name | The name associated with the customer position identifier | C
Customer Account Type | Type of account used for reporting | C
Customer LEI | LEI for a particular customer; provide if available | C
Customer LEI Name | The LEI name associated with the customer position LEI | C
Unique Margin Identifier | A single field that uniquely identifies the margin account. This field us used to identify associated positions | C
Breach Details (Daily Reporting)
Initial Margin | Margin requirement calculated by the DCO's margin methodology. Unless an integral part of the margin methodology, this figure should not include any additional margin add-ons | M
Backtesting Metric | Indicates the type of profit and loss calculation used for backtesting: • VM—Variation Margin • STATIC—Static Portfolio P/L (Clean P/L) • DIRTY—Dirty P/L • MTMA—Mark to Market P/L • MTMO—Mark to Model P/L • OTHER | M
Backtesting Metric Amount | Amount on the positions for which Initial Margin is computed | M
Breach Amount | Difference between the Initial Margin and Backtesting Metric Amount | M
Margin Period of Risk | Holding period for which the Backtesting Metric is calculated in days | M
Breach Summary (Daily Reporting)
Total Instance | Total number of testing dates for the account | M
Number of Breaches | Total number of breaches in the testing period | M
Test Range Start | Beginning date of the test | M
Test Range End | End date of the test | M
M = mandatory C = conditional O = optional.
F. Manifest Reporting
Field name | Description | Use
Manifest Reporting
Total Message Count | The total number of reports included in the file | M
FIXML Message Type | FIXML account summary report type | M
Sender ID | The CFTC-issued DCO identifier | M
To ID | Indicate "CFTC" | M
Message Transmit Datetime | The date and time the file is transmitted | M
Filenames | List of files to be sent | M
M = mandatory C = conditional O = optional.
