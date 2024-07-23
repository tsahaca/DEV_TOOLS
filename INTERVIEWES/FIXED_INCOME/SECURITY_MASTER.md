A fixed income security master table typically includes comprehensive information about various fixed income instruments, such as bonds, treasury notes, and other debt securities. The fields in this table are designed to capture all relevant attributes of these securities to facilitate trading, risk management, reporting, and other financial operations. Here are the common fields you might find in a fixed income security master table:

1. **Security Identifier Information:**
   - **CUSIP:** A unique identifier for securities issued in the United States.
   - **ISIN:** International Securities Identification Number for global identification.
   - **SEDOL:** Stock Exchange Daily Official List number, primarily used in the UK.
   - **Ticker Symbol:** The abbreviation used to uniquely identify publicly traded shares of a particular stock on a particular stock market.
   - **Security ID:** A unique identifier assigned internally by the organization.

2. **Basic Security Information:**
   - **Security Name:** The name of the security.
   - **Issuer Name:** The name of the entity that issued the security.
   - **Issue Date:** The date on which the security was issued.
   - **Maturity Date:** The date on which the principal amount of the security is due to be paid.
   - **Coupon Rate:** The interest rate that the issuer of the bond will pay to the bondholder.
   - **Coupon Frequency:** How often the coupon payments are made (e.g., annually, semi-annually, quarterly).

3. **Security Type and Classification:**
   - **Security Type:** The type of security (e.g., bond, note, bill).
   - **Sub-Type:** Further classification within the security type (e.g., municipal bond, corporate bond).
   - **Sector:** The sector in which the issuer operates (e.g., government, corporate, municipal).
   - **Rating:** Credit rating assigned by rating agencies (e.g., Moody’s, S&P).

4. **Trading Information:**
   - **Par Value:** The face value of the bond.
   - **Currency:** The currency in which the security is denominated.
   - **Trading Market:** The market or exchange where the security is traded.
   - **Lot Size:** The minimum quantity that can be traded.
   - **Accrued Interest:** Interest that has been earned but not yet paid since the last coupon payment.

5. **Yield Information:**
   - **Yield to Maturity (YTM):** The total return anticipated on a bond if held until it matures.
   - **Current Yield:** The annual income (interest or dividends) divided by the current price of the security.
   - **Yield Spread:** The difference in yield between different securities, often compared to a benchmark (e.g., Treasury bonds).

6. **Redemption Information:**
   - **Call Date:** The date on which a bond can be redeemed early by the issuer.
   - **Call Price:** The price at which a bond can be redeemed early.
   - **Put Date:** The date on which a bondholder can sell the bond back to the issuer.
   - **Put Price:** The price at which a bondholder can sell the bond back to the issuer.

7. **Coupon Details:**
   - **Coupon Dates:** The dates on which coupon payments are made.
   - **Day Count Convention:** The convention used to calculate the amount of accrued interest (e.g., 30/360, Actual/Actual).

8. **Legal and Regulatory Information:**
   - **Prospectus:** The document that provides details about the security's terms, issuer, and risk factors.
   - **Regulatory Filings:** References to regulatory documents filed with agencies such as the SEC.
   - **Legal Entity Identifier (LEI):** A unique identifier for the legal entity that issues the bond.

9. **Additional Attributes:**
   - **Callable/Non-Callable:** Indicates whether the bond can be called before maturity.
   - **Convertible/Non-Convertible:** Indicates whether the bond can be converted into a specified number of shares of the issuing company's stock.
   - **Zero Coupon:** Indicates whether the bond does not pay periodic interest but is issued at a discount.

### Example of a Fixed Income Security Master Table Entry

| Field Name          | Value                     |
|---------------------|---------------------------|
| CUSIP               | 123456AB7                 |
| ISIN                | US123456AB78              |
| SEDOL               | B12HJK4                   |
| Ticker Symbol       | ABCD                      |
| Security ID         | 00123456                  |
| Security Name       | ABC Corp 5% 2028 Bond     |
| Issuer Name         | ABC Corporation           |
| Issue Date          | 2023-01-15                |
| Maturity Date       | 2028-01-15                |
| Coupon Rate         | 5.00%                     |
| Coupon Frequency    | Semi-Annual               |
| Security Type       | Bond                      |
| Sub-Type            | Corporate Bond            |
| Sector              | Corporate                 |
| Rating              | A                         |
| Par Value           | $1,000                    |
| Currency            | USD                       |
| Trading Market      | NYSE                      |
| Lot Size            | 1                         |
| Accrued Interest    | $25                       |
| Yield to Maturity   | 4.85%                     |
| Current Yield       | 4.90%                     |
| Yield Spread        | 150 bps                   |
| Call Date           | 2026-01-15                |
| Call Price          | $1,050                    |
| Put Date            | N/A                       |
| Put Price           | N/A                       |
| Coupon Dates        | 2023-07-15, 2024-01-15    |
| Day Count Convention| 30/360                    |
| Prospectus          | Link to Document          |
| Regulatory Filings  | Link to SEC Filing        |
| Legal Entity Identifier (LEI) | 5493001KJTIIGC8Y1R12 |
| Callable            | Yes                       |
| Convertible         | No                        |
| Zero Coupon         | No                        |

### Summary

The fixed income security master table serves as a comprehensive repository of detailed information about fixed income securities, enabling efficient management, trading, and reporting of these instruments. The fields listed above cover various aspects such as identification, classification, trading details, yield information, and legal attributes.
