In a fixed income order management system (OMS), various data sets are utilized to manage and streamline the process of trading fixed income securities. These data sets ensure efficient order placement, execution, and monitoring while maintaining compliance with regulatory requirements. Here are the key data sets typically involved in a fixed income OMS:

### 1. **Order Data**
   - **Order ID**: Unique identifier for each order.
   - **Order Type**: Type of order (e.g., market order, limit order).
   - **Security ID**: Identifier for the security being traded (e.g., ISIN, CUSIP).
   - **Order Date and Time**: Timestamp when the order was placed.
   - **Order Status**: Current status of the order (e.g., pending, executed, canceled).
   - **Quantity**: Number of units or face value of the securities to be traded.
   - **Price**: Price at which the order is to be executed (if applicable).
   - **Side**: Indicates whether the order is a buy or sell order.
   - **Trader ID**: Identifier for the trader who placed the order.
   - **Portfolio ID**: Identifier for the portfolio associated with the order.

### 2. **Execution Data**
   - **Execution ID**: Unique identifier for each execution.
   - **Order ID**: Identifier linking to the original order.
   - **Execution Date and Time**: Timestamp when the execution took place.
   - **Executed Quantity**: Number of units or face value of the securities executed.
   - **Executed Price**: Price at which the securities were executed.
   - **Broker ID**: Identifier for the broker or counterparty involved in the execution.
   - **Commission**: Fees associated with the execution.

### 3. **Trade Data**
   - **Trade ID**: Unique identifier for each trade.
   - **Execution IDs**: Identifiers for executions that make up the trade.
   - **Trade Date and Time**: Timestamp when the trade was completed.
   - **Settlement Date**: Date when the trade is to be settled.
   - **Trade Amount**: Total value of the trade.
   - **Accrued Interest**: Interest accrued on the securities being traded.
   - **Trade Type**: Type of trade (e.g., primary market, secondary market).

### 4. **Security Master Data**
   - **Security ID**: Unique identifier for each security.
   - **Security Type**: Type of fixed income security (e.g., bond, note, commercial paper).
   - **Issuer**: Information about the entity issuing the security.
   - **Coupon Rate**: Interest rate paid by the security.
   - **Maturity Date**: Date when the principal amount is due to be paid.
   - **Credit Rating**: Rating provided by rating agencies (e.g., Moody's, S&P).
   - **Currency**: Currency in which the security is denominated.
   - **Issue Date**: The date on which the security was issued.
   - **Face Value**: The nominal value of the security.

### 5. **Market Data**
   - **Interest Rates**: Data on interest rates (e.g., LIBOR, Treasury rates).
   - **Yield Curves**: Yield curve data for different maturities and credit qualities.
   - **Credit Spreads**: Spreads over benchmark rates for different credit ratings.
   - **Economic Indicators**: Relevant economic data (e.g., inflation rates, GDP growth).
   - **Bond Prices**: Current market prices for fixed income securities.

### 6. **Portfolio Data**
   - **Portfolio ID**: Unique identifier for each portfolio.
   - **Portfolio Name**: Name of the portfolio.
   - **Client ID**: Identifier for the client associated with the portfolio.
   - **Investment Objective**: Objectives guiding the portfolio’s investment strategy.
   - **Benchmark**: Performance benchmark for the portfolio.
   - **Risk Tolerance**: Risk tolerance level for the portfolio.

### 7. **Trader and Broker Data**
   - **Trader ID**: Unique identifier for each trader.
   - **Trader Name**: Name of the trader.
   - **Broker ID**: Unique identifier for each broker or counterparty.
   - **Broker Name**: Name of the broker.
   - **Contact Information**: Contact details for traders and brokers.
   - **Commission Rates**: Fee structures associated with brokers.

### 8. **Compliance and Regulatory Data**
   - **Investment Guidelines**: Rules and limits governing the portfolio (e.g., sector limits, credit quality constraints).
   - **Compliance Checks**: Data on compliance with investment guidelines and regulations.
   - **Reporting Requirements**: Data required for regulatory reporting (e.g., SEC filings, MiFID II).

### 9. **Risk Management Data**
   - **Risk Models**: Data from risk models used to assess portfolio risk.
   - **Stress Testing**: Results of stress tests under various market scenarios.
   - **Credit Analysis**: Data from credit analysis, including issuer financials and creditworthiness.

### 10. **Operational Data**
   - **Settlement Data**: Information related to the settlement of transactions.
   - **Custodian Data**: Data from custodians holding the securities.
   - **Corporate Actions**: Data on corporate actions affecting securities (e.g., bond calls, mergers).
   - **Reconciliation Data**: Data used to reconcile discrepancies between internal records and custodian records.

### Data Warehouse Schema Design for Fixed Income OMS

#### Fact Tables

1. **Order Fact Table**
   - order_id (Primary Key)
   - order_type
   - security_id (Foreign Key to Security Dimension)
   - order_date (Foreign Key to Date Dimension)
   - order_status
   - quantity
   - price
   - side
   - trader_id (Foreign Key to Trader Dimension)
   - portfolio_id (Foreign Key to Portfolio Dimension)

2. **Execution Fact Table**
   - execution_id (Primary Key)
   - order_id (Foreign Key to Order Fact Table)
   - execution_date (Foreign Key to Date Dimension)
   - executed_quantity
   - executed_price
   - broker_id (Foreign Key to Broker Dimension)
   - commission

3. **Trade Fact Table**
   - trade_id (Primary Key)
   - execution_ids (Foreign Key to Execution Fact Table)
   - trade_date (Foreign Key to Date Dimension)
   - settlement_date (Foreign Key to Date Dimension)
   - trade_amount
   - accrued_interest
   - trade_type

#### Dimension Tables

1. **Security Dimension Table**
   - security_id (Primary Key)
   - security_type
   - issuer
   - coupon_rate
   - maturity_date
   - credit_rating
   - currency
   - issue_date
   - face_value

2. **Portfolio Dimension Table**
   - portfolio_id (Primary Key)
   - portfolio_name
   - client_id (Foreign Key to Client Dimension)
   - investment_objective
   - benchmark
   - risk_tolerance

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

5. **Trader Dimension Table**
   - trader_id (Primary Key)
   - trader_name
   - contact_information

6. **Broker Dimension Table**
   - broker_id (Primary Key)
   - broker_name
   - contact_information
   - commission_rates

7. **Market Data Dimension Table**
   - market_data_id (Primary Key)
   - date_id (Foreign Key to Date Dimension)
   - interest_rate
   - yield_curve
   - credit_spread
   - economic_indicator
   - bond_price

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
| issue_date       |
| face_value       |
+--------+---------+
         |
+--------+---------+
| Order Fact       |
|------------------|
| order_id (PK)    |
| order_type       |
| security_id (FK) |
| order_date (FK)  |
| order_status     |
| quantity         |
| price            |
| side             |
| trader_id (FK)   |
| portfolio_id (FK)|
+--------+---------+
         |
         |
+--------+---------+
| Execution Fact   |
|------------------|
| execution_id (PK)|
| order_id (FK)    |
| execution_date(FK)|
| executed_quantity|
| executed_price   |
| broker_id (FK)   |
| commission       |
+--------+---------+

+------------------+
| Trade Fact       |
|------------------|
| trade_id (PK)    |
| execution_ids (FK)|
| trade_date (FK)  |
| settlement_date(FK)|
| trade_amount     |
| accrued_interest |
| trade_type       |
+--------+---------+

+------------------+
| Portfolio Dim    |
|------------------|
| portfolio_id (PK)|
| portfolio_name   |
| client_id (FK)   |
| investment_obj   |
| benchmark        |
| risk_tolerance   |
+--------+---------+

+------------------+
| Client Dim       |
|------------------|
| client_id (PK)   |
| client_name      |
| contact_info     |
| address          |
| account_manager  |
| regulatory
