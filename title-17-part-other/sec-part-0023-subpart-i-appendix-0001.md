# Part 23, Subpart I, Appendix 1—Exhibits A-D
Exhibit A—Minimum Primary Economic Terms Data—Credit Swaps and Equity Swaps
Data categories and fields for all swaps | Comment
Asset Class | Field values: Credit, equity, FX, interest rates, other commodities.
The Unique Swap Identifier for the swap | The USI is a unique identifier assigned to all swap transactions which identifies the transaction (the swap and its counterparties) uniquely throughout its duration.
The Legal Entity Identifier of the reporting counterparty | As provided in § 45.6, or substitute identifier for a natural person.
An indication of whether the reporting counterparty is a derivatives clearing organization with respect to the swap | Yes/No.
The Legal Entity Identifier of the non-reporting party | As provided in § 45.6, or substitute identifier for a natural person.
The Unique Product Identifier assigned to the swap | As provided in § 45.7.
If no Unique Product Identifier is available for the swap because the swap is not sufficiently standardized, the taxonomic description of the swap pursuant to the CFTC-approved product classification system
If no CFTC-approved UPI and product classification system is yet available, the internal product identifier or product description used by the swap data repository
An indication of the counterparty purchasing protection | Field values: LEI, or substitute identifier for a natural person.
An indication of the counterparty selling protection | Field values: LEI, or substitute identifier for a natural person.
Information identifying the reference entity | The entity that is the subject of the protection being purchased and sold in the swap. Field values: LEI, or substitute identifier for a natural person.
Contract type | E.g., swap, swaption, forward, option, basis swap, index swap, basket swap.
Execution venue | The swap execution facility or designated contract market on or pursuant to the rules of which the swap was executed. Field values: LEI of the swap execution facility or designated contract market, or "off-facility" if not so executed.
Start date | The date on which the swap starts or goes into effect.
Maturity, termination or end date | The date on which the swap expires.
The price | E.g., strike price, initial price, spread.
The notional amount, and the currency in which the notional amount is expressed
The amount and currency (or currencies) of any up-front payment
Payment frequency of the reporting counterparty | A description of the payment stream of the reporting counterparty, e.g., coupon.
Payment frequency of the non-reporting counterparty | A description of the payment stream of the non-reporting counterparty, e.g., coupon.
Clearing exception or exemption type | The type of clearing exception or exemption being claimed. Field values: End user, Inter-affiliate or Cooperative.
Indication of collateralization | Is the swap collateralized, and if so to what extent? Field values: Uncollateralized, partially collateralized, one-way collateralized, fully collateralized.
Any other term(s) of the swap matched or affirmed by the counterparties in verifying the swap | Use as many fields as required to report each such term.
Exhibit B—Minimum Primary Economic Terms Data—Foreign Exchange Transactions
[Other than cross-currency swaps]
Data fields for all swaps | Comment
Asset Class | Field values: Credit, equity, FX, interest rates, other commodities.
The Unique Swap Identifier for the swap | The USI is a unique identifier assigned to all swap transactions which identifies the transaction (the swap and its counterparties) uniquely throughout its duration.
The Legal Entity Identifier of the reporting counterparty | As provided in § 45.6, or substitute identifier for a natural person.
An indication of whether the reporting counterparty is a derivatives clearing organization with respect to the swap | Yes/No.
The Legal Entity Identifier of the non-reporting party | As provided in § 45.6, or substitute identifier for a natural person.
The Unique Product Identifier assigned to the swap | As provided in § 45.7.
If no Unique Product Identifier is available for the swap because the swap is not sufficiently standardized, the taxonomic description of the swap pursuant to the CFTC-approved product classification system
If no CFTC-approved UPI and product classification system is yet available, the internal product identifier or product description used by the swap data repository
Contract type | E.g., forward, non-deliverable forward (NDF), non-deliverable option (NDO), vanilla option, simple exotic option, complex exotic option.
Execution venue | The swap execution facility or designated contract market on or pursuant to the rules of which the swap was executed. Field values: LEI of the swap execution facility or designated contract market, or "off-facility" if not so executed.
Currency 1 | ISO code.
Currency 2 | ISO code.
Notional amount 1 | For currency 1.
Notional amount 2 | For currency 2.
Exchange rate | Contractual rate of exchange of the currencies.
Delivery type | Physical (deliverable) or cash (non-deliverable).
Settlement or expiration date | Settlement date, or for an option the contract expiration date.
Clearing exception or exemption type | The type of clearing exception or exemption being claimed. Field values: End user, Inter-affiliate or Cooperative.
Indication of collateralization | Is the trade collateralized, and if so to what extent? Field values: Uncollateralized, partially collateralized, one-way collateralized, fully collateralized.
Any other term(s) of the trade matched or affirmed by the counterparties in verifying the trade | E.g., for options, premium, premium currency, premium payment date; for non-deliverable trades, settlement currency, valuation (fixing) date; indication of the economic obligations of the counterparties. Use as many fields as required to report each such term.
Exhibit C—Minimum Primary Economic Terms Data—Interest Rate Swaps
[Including cross-currency swaps]
Data fields for all swaps | Comment
Asset Class | Field values: Credit, equity, FX, interest rates, other commodities.
The Unique Swap Identifier for the swap | The USI is a unique identifier assigned to all swap transactions which identifies the transaction (the swap and its counterparties) uniquely throughout its duration.
The Legal Entity Identifier of the reporting counterparty | As provided in § 45.6, or substitute identifier for a natural person.
An indication of whether the reporting counterparty is a derivatives clearing organization with respect to the swap | Yes/No.
The Legal Entity Identifier of the non-reporting counterparty | As provided in § 45.6, or substitute identifier for a natural person.
The Unique Product Identifier assigned to the swap | As provided in § 45.7.
If no Unique Product Identifier is available for the swap because the swap is not sufficiently standardized, the taxonomic description of the swap pursuant to the CFTC-approved product classification system
If no CFTC-approved UPI and product classification system is yet available, the internal product identifier or product description used by the swap data repository
Contract type | E.g., swap, swaption, option, basis swap, index swap.
Execution venue | The swap execution facility or designated contract market on or pursuant to the rules of which the swap was executed. Field values: LEI of the swap execution facility or designated contract market, or "off-facility" if not so executed.
Start date | The date on which the swap starts or goes into effect.
Maturity, termination or end date | The date on which the swap expires or ends.
Day count convention
Notional amount (leg 1) | The current active notional amount.
Notional currency (leg 1) | ISO code.
Notional amount (leg 2) | The current active notional amount.
Notional currency (leg 2) | ISO code.
Payer (fixed rate) | Is the reporting party a fixed rate payer? Yes/No/Not applicable.
Payer (floating rate leg 1) | If two floating legs, the payer for leg 1.
Payer (floating rate leg 2) | If two floating legs, the payer for leg 2.
Direction | For swaps: Whether the principal is paying or receiving the fixed rate. For float-to-float and fixed-to-fixed swaps: Indicate N/A. For non-swap instruments and swaptions: Indicate the instrument that was bought or sold.
Option type | E.g., put, call, straddle.
Fixed rate
Fixed rate day count fraction | E.g., actual 360.
Floating rate payment frequency
Floating rate reset frequency
Floating rate index name/rate period | E.g., USD-Libor-BBA.
Clearing exception or exemption type | The type of clearing exception or exemption being claimed. Field values: End user, Inter-affiliate or Cooperative.
Indication of collateralization | Is the swap collateralized, and if so to what extent? Field values: Uncollateralized, partially collateralized, one-way collateralized, fully collateralized.
Any other term(s) of the swap matched or affirmed by the counterparties in verifying the swap | E.g., early termination option clause. Use as many fields as required to report each such term.
Exhibit D—Minimum Primary Economic Terms Data—Other Commodity Swaps
Data field for all swaps | Comment
Asset Class | Field values: Credit, equity, FX, interest rates, other commodities.
The Unique Swap Identifier for the swap | The USI is a unique identifier assigned to all swap transactions which identifies the transaction (the swap and its counterparties) uniquely throughout its duration.
The Legal Entity Identifier of the reporting counterparty | As provided in § 45.6, or substitute identifier for a natural person.
An indication of whether the reporting counterparty is a derivatives clearing organization with respect to the swap | Yes/No.
The Legal Entity Identifier of the non-reporting party | As provided in § 45.6, or substitute identifier for a natural person.
The Unique Product Identifier assigned to the swap | As provided in § 45.7.
If no Unique Product Identifier is available for the swap because the swap is not sufficiently standardized, the taxonomic description of the swap pursuant to the CFTC-approved product classification system
If no CFTC-approved UPI and product classification system is yet available, the internal product identifier or product description used by the swap data repository
Contract type | E.g., swap, swaption, option, basis swap, index swap.
Execution venue | The swap execution facility or designated contract market on or pursuant to the rules of which the swap was executed. Field values: LEI of the swap execution facility or designated contract market, or "off-facility" if not so executed.
Start date | The date on which the swap commences or goes into effect (e.g., in physical oil, the pricing start date).
Maturity, termination, or end date | The date on which the swap expires or ends (e.g., in physical oil, the pricing end date).
Buyer | The counterparty purchasing the product: (E.g., the payer of the fixed price (for a swap), or the payer of the floating price on the underlying swap (for a put swaption), or the payer of the fixed price on the underlying swap (for a call swaption). Field values: LEI, if available, or substitute identifier, for a natural person.
Seller | The counterparty offering the product: (E.g., the payer of the floating price (for a swap), the payer of the fixed price on the underlying swap (for a put swaption), or the payer of the floating price on the underlying swap (for a call swaption). Field values: LEI, or substitute identifier, for a natural person.
Quantity unit | The unit of measure applicable for the quantity on the swap. E.g., barrels, bushels, gallons, pounds, tons.
Quantity | The amount of the commodity (the number of quantity units) quoted on the swap.
Quantity frequency | The rate at which the quantity is quoted on the swap. E.g., hourly, daily, weekly, monthly.
Total quantity | The quantity of the commodity for the entire term of the swap.
Settlement method | Physical delivery or cash.
Price | The price of the swap. For options, the strike price.
Price unit | The unit of measure applicable for the price of the swap.
Price currency | ISO code.
Buyer pay index | The published price as paid by the buyer (if applicable). For swaptions, applies to the underlying swap.
Buyer pay averaging method | The averaging method used to calculate the index of the buyer pay index. For swaptions, applies to the underlying swap.
Seller pay index | The published price as paid by the seller (if applicable). For swaptions, applies to the underlying swap.
Seller pay averaging method | The averaging method used to calculate the index of the seller pay index. For swaptions, applies to the underlying swap.
Grade | If applicable, the grade of the commodity to be delivered, e.g., the grade of oil or refined product.
Option type | Descriptor for the type of option transaction. E.g., put, call, straddle.
Option style | E.g., American, European, European Daily, European Monthly, Asian.
Option premium | The total amount paid by the option buyer.
Hours from through | For electric power, the hours of the day for which the swap is effective.
Hours from through time zone | For electric power, the time zone prevailing for the hours during which electricity is transmitted.
Days of week | For electric power, the profile applicable for the delivery of power.
Load type | For electric power, the load profile for the delivery of power.
Clearing exception or exemption type | The type of clearing exception or exemption being claimed. Field values: End user, Inter-affiliate or Cooperative.
Indication of collateralization | Is the swap collateralized, and if so to what extent? Field values: Uncollateralized, partially collateralized, one-way collateralized, fully collateralized.
Any other term(s) of the swap matched or affirmed by the counterparties in verifying the swap | Use as many fields as required to report each such term.
