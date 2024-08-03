In fixed income asset management, a variety of data sets are used to manage, analyze, and report on fixed income investments. These data sets provide comprehensive information on securities, transactions, market conditions, risk factors, and portfolio performance. Here are the key data sets typically involved:

### 1. **Security Master Data**
   - **Security ID**: Unique identifier for each security (e.g., ISIN, CUSIP).
   - **Security Type**: Type of fixed income security (e.g., bond, note, commercial paper).
   - **Issuer**: Information about the entity issuing the security.
   - **Coupon Rate**: Interest rate paid by the security.
   - **Maturity Date**: Date when the principal amount is due to be paid.
   - **Credit Rating**: Rating provided by rating agencies (e.g., Moody's, S&P).
   - **Currency**: Currency in which the security is denominated.
   - **Call and Put Features**: Terms related to callable or puttable bonds.
   - **Issue Date**: The date on which the security was issued.
   - **Face Value**: The nominal value of the security.
   - **Yield to Maturity**: The total return anticipated if the security is held until it matures.

### 2. **Portfolio Holdings Data**
   - **Portfolio ID**: Unique identifier for each portfolio.
   - **Security ID**: Unique identifier for each security held in the portfolio.
   - **Quantity**: Number of units or face value of the securities held.
   - **Market Value**: Current market value of the holdings.
   - **Book Value**: Original purchase value of the holdings.
   - **Accrued Interest**: Interest accumulated but not yet paid.
   - **Yield**: Yield of the security or the portfolio.
   - **Duration**: Measure of the sensitivity of the price of a bond to a change in interest rates.
   - **Convexity**: Measure of the curvature in the relationship between bond prices and bond yields.
   - **Cost Basis**: The original value of an asset for tax purposes.

### 3. **Transaction Data**
   - **Transaction ID**: Unique identifier for each transaction.
   - **Trade Date**: Date the trade was executed.
   - **Settlement Date**: Date the trade is settled.
   - **Transaction Type**: Type of transaction (e.g., buy, sell, maturity, coupon payment).
   - **Security ID**: Identifier for the security involved in the transaction.
   - **Quantity**: Amount of the security bought or sold.
   - **Price**: Price at which the transaction was executed.
   - **Broker**: Information about the broker or counterparty.
   - **Commission**: Fees associated with the transaction.

### 4. **Market Data**
   - **Interest Rates**: Data on interest rates (e.g., LIBOR, Treasury rates).
   - **Yield Curves**: Yield curve data for different maturities and credit qualities.
   - **Credit Spreads**: Spreads over benchmark rates for different credit ratings.
   - **Economic Indicators**: Relevant economic data (e.g., inflation rates, GDP growth).
   - **Exchange Rates**: Foreign exchange rates for currency conversion.
   - **Bond Indices**: Performance of bond indices for benchmarking purposes.

### 5. **Performance Data**
   - **Returns**: Historical and current returns for the portfolio and individual securities.
   - **Benchmarks**: Performance of relevant benchmarks or indices.
   - **Risk Metrics**: Measures such as duration, convexity, and value-at-risk (VaR).
   - **Attribution Analysis**: Analysis of factors contributing to performance (e.g., sector allocation, security selection).
   - **Sharpe Ratio**: Measure of risk-adjusted return.
   - **Alpha**: Measure of excess return relative to the benchmark.
   - **Beta**: Measure of the portfolio's volatility relative to the market.

### 6. **Compliance and Regulatory Data**
   - **Investment Guidelines**: Rules and limits governing the portfolio (e.g., sector limits, credit quality constraints).
   - **Compliance Checks**: Data on compliance with investment guidelines and regulations.
   - **Reporting Requirements**: Data required for regulatory reporting (e.g., SEC filings, MiFID II).
   - **KYC Data**: Know Your Customer information required for regulatory compliance.
   - **AML Data**: Anti-Money Laundering checks and flags.

### 7. **Client and Account Data**
   - **Client Information**: Details about the clients whose assets are being managed.
   - **Account Information**: Information about individual accounts, including mandates and investment objectives.
   - **Fee Structures**: Details of fees and expenses associated with the account.
   - **Account Performance**: Performance metrics specific to client accounts.

### 8. **Risk Management Data**
   - **Risk Models**: Data from risk models used to assess portfolio risk.
   - **Stress Testing**: Results of stress tests under various market scenarios.
   - **Credit Analysis**: Data from credit analysis, including issuer financials and creditworthiness.
   - **Scenario Analysis**: Analysis of portfolio performance under different hypothetical scenarios.

### 9. **Operational Data**
   - **Settlement Data**: Information related to the settlement of transactions.
   - **Custodian Data**: Data from custodians holding the securities.
   - **Corporate Actions**: Data on corporate actions affecting securities (e.g., bond calls, mergers, tender offers).
   - **Reconciliation Data**: Data used to reconcile discrepancies between internal records and custodian records.

### Data Warehouse Schema Design for Fixed Income Asset Management

#### Fact Tables

1. **Transaction Fact Table**
   - transaction_id (Primary Key)
   - trade_date (Foreign Key to Date Dimension)
   - settlement_date (Foreign Key to Date Dimension)
   - security_id (Foreign Key to Security Dimension)
   - portfolio_id (Foreign Key to Portfolio Dimension)
   - transaction_type
   - quantity
   - price
   - broker
   - commission

2. **Holdings Fact Table**
   - holding_id (Primary Key)
   - date_id (Foreign Key to Date Dimension)
   - security_id (Foreign Key to Security Dimension)
   - portfolio_id (Foreign Key to Portfolio Dimension)
   - quantity
   - market_value
   - book_value
   - accrued_interest
   - yield
   - duration
   - convexity

3. **Performance Fact Table**
   - performance_id (Primary Key)
   - date_id (Foreign Key to Date Dimension)
   - portfolio_id (Foreign Key to Portfolio Dimension)
   - return
   - benchmark_return
   - sharpe_ratio
   - alpha
   - beta

#### Dimension Tables

1. **Security Dimension Table**
   - security_id (Primary Key)
   - security_type
   - issuer
   - coupon_rate
   - maturity_date
   - credit_rating
   - currency
   - call_feature
   - put_feature
   - issue_date
   - face_value
   - yield_to_maturity

2. **Portfolio Dimension Table**
   - portfolio_id (Primary Key)
   - portfolio_name
   - client_id (Foreign Key to Client Dimension)
   - investment_objective
   - benchmark
   - risk_tolerance
   - fee_structure

3. **Client Dimension Table**
   - client_id (Primary Key)
   - client_name
   - contact_information
   - address
   - account_manager
   - regulatory_requirements

4. **Date Dimension Table**
   - date_id (Primary Key)
   - date
   - day
   - month
   - year
   - quarter
   - day_of_week
   - is_weekend
   - is_holiday

5. **Market Data Dimension Table**
   - market_data_id (Primary Key)
   - date_id (Foreign Key to Date Dimension)
   - interest_rate
   - yield_curve
   - credit_spread
   - economic_indicator
   - exchange_rate

### Data Warehouse Schema Diagram

```plaintext
+------------------+
| Security Dim     |
|------------------|
| security_id (PK) |
| security_type    |
| issuer           |
| coupon_rate      |
| maturity_date    |
| credit_rating    |
| currency         |
| call_feature     |
| put_feature      |
| issue_date       |
| face_value       |
| yield_to_maturity|
+--------+---------+
         |
+--------+---------+
| Holdings Fact    |
|------------------|
| holding_id (PK)  |
| date_id (FK)     |
| security_id (FK) |
| portfolio_id (FK)|
| quantity         |
| market_value     |
| book_value       |
| accrued_interest |
| yield            |
| duration         |
| convexity        |
+--------+---------+
         |
         |
+--------+---------+
| Portfolio Dim    |
|------------------|
| portfolio_id (PK)|
| portfolio_name   |
| client_id (FK)   |
| investment_obj   |
| benchmark        |
| risk_tolerance   |
| fee_structure    |
+--------+---------+

+------------------+
| Client Dim       |
|------------------|
| client_id (PK)   |
| client_name      |
| contact_info     |
| address          |
| account_manager  |
| regulatory_reqs  |
+--------+---------+

+------------------+
| Date Dim         |
|------------------|
| date_id (PK)     |
| date             |
| day              |
| month            |
| year             |
| quarter          |
| day_of_week      |
| is_weekend       |
| is_holiday       |
+--------+---------+

+------------------+
| Transaction Fact |
|------------------|
| transaction
