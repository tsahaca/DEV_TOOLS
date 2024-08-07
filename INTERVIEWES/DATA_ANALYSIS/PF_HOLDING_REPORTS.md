Designing a data warehouse for Portfolio Holdings Reports involves creating a schema that captures detailed information about portfolio holdings, including assets, their classifications, performance metrics, and other relevant attributes. The schema typically includes fact and dimension tables to organize and simplify the retrieval of data for reporting and analysis.

### Fact Tables
1. **Holdings Fact Table**
2. **Transaction Fact Table**
3. **Performance Fact Table**

### Dimension Tables
1. **Time Dimension**
2. **Portfolio Dimension**
3. **Instrument Dimension**
4. **Sector Dimension**
5. **Issuer Dimension**
6. **Geography Dimension**
7. **Currency Dimension**

### Detailed Schema Design

#### 1. Holdings Fact Table
This table captures the details of portfolio holdings.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| holding_id         | INT        | Primary Key                          |
| time_id            | INT        | Foreign Key to Time Dimension        |
| portfolio_id       | INT        | Foreign Key to Portfolio Dimension   |
| instrument_id      | INT        | Foreign Key to Instrument Dimension  |
| sector_id          | INT        | Foreign Key to Sector Dimension      |
| issuer_id          | INT        | Foreign Key to Issuer Dimension      |
| geography_id       | INT        | Foreign Key to Geography Dimension   |
| currency_id        | INT        | Foreign Key to Currency Dimension    |
| quantity           | DECIMAL    | Quantity of the Instrument Held      |
| market_value       | DECIMAL    | Market Value of the Holding          |
| cost_basis         | DECIMAL    | Cost Basis of the Holding            |
| unrealized_gain    | DECIMAL    | Unrealized Gain/Loss of the Holding  |

#### 2. Transaction Fact Table
This table captures all transactions related to the portfolio holdings.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| transaction_id     | INT        | Primary Key                          |
| time_id            | INT        | Foreign Key to Time Dimension        |
| portfolio_id       | INT        | Foreign Key to Portfolio Dimension   |
| instrument_id      | INT        | Foreign Key to Instrument Dimension  |
| transaction_type   | VARCHAR    | Type of Transaction (Buy/Sell)       |
| quantity           | DECIMAL    | Quantity of the Instrument Transacted|
| transaction_amount | DECIMAL    | Total Amount of the Transaction      |
| transaction_price  | DECIMAL    | Price per Unit of the Instrument     |

#### 3. Performance Fact Table
This table captures the performance metrics of holdings over time.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| performance_id     | INT        | Primary Key                          |
| time_id            | INT        | Foreign Key to Time Dimension        |
| portfolio_id       | INT        | Foreign Key to Portfolio Dimension   |
| instrument_id      | INT        | Foreign Key to Instrument Dimension  |
| market_value       | DECIMAL    | Market Value of the Instrument       |
| total_return       | DECIMAL    | Total Return of the Instrument       |
| income             | DECIMAL    | Income Generated by the Instrument   |
| capital_gain       | DECIMAL    | Capital Gain/Loss                    |

#### Dimension Tables

#### 1. Time Dimension
Captures different time granularity levels.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| time_id            | INT        | Primary Key                          |
| date               | DATE       | Date                                 |
| day                | INT        | Day                                  |
| month              | INT        | Month                                |
| quarter            | INT        | Quarter                              |
| year               | INT        | Year                                 |
| day_of_week        | VARCHAR    | Day of the Week                      |

#### 2. Portfolio Dimension
Details about the portfolios.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| portfolio_id       | INT        | Primary Key                          |
| portfolio_name     | VARCHAR    | Name of the Portfolio                |
| manager            | VARCHAR    | Portfolio Manager                    |
| strategy           | VARCHAR    | Investment Strategy                  |
| inception_date     | DATE       | Portfolio Inception Date             |

#### 3. Instrument Dimension
Details about financial instruments.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| instrument_id      | INT        | Primary Key                          |
| instrument_name    | VARCHAR    | Name of the Instrument               |
| instrument_type    | VARCHAR    | Type of the Instrument (e.g., bond, stock) |
| ticker             | VARCHAR    | Ticker Symbol                        |
| cusip              | VARCHAR    | CUSIP Identifier                     |

#### 4. Sector Dimension
Details about the sector classification.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| sector_id          | INT        | Primary Key                          |
| sector_name        | VARCHAR    | Name of the Sector                   |

#### 5. Issuer Dimension
Details about the issuers of the instruments.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| issuer_id          | INT        | Primary Key                          |
| issuer_name        | VARCHAR    | Name of the Issuer                   |
| issuer_type        | VARCHAR    | Type of Issuer (e.g., corporate, government) |

#### 6. Geography Dimension
Details about geographical locations.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| geography_id       | INT        | Primary Key                          |
| country            | VARCHAR    | Country                              |
| region             | VARCHAR    | Region                               |
| city               | VARCHAR    | City                                 |

#### 7. Currency Dimension
Details about currencies.

| Column Name        | Data Type  | Description                          |
|--------------------|------------|--------------------------------------|
| currency_id        | INT        | Primary Key                          |
| currency_code      | VARCHAR    | Currency Code (e.g., USD, EUR)       |
| currency_name      | VARCHAR    | Name of the Currency                 |

### ER Diagram

Here's a conceptual ER diagram representing the above schema:

```
+-------------------+         +-------------------+         +-------------------+
|   Time Dimension  |<--------| Holdings Fact Table|------>|Portfolio Dimension|
+-------------------+         +-------------------+         +-------------------+
           |                              |                              |
           |                              |                              |
           |                              |                              |
           V                              V                              V
+-------------------+         +-------------------+         +-------------------+
| Instrument Dimension |<----|Transaction Fact Table|--->|Sector Dimension|
+-------------------+         +-------------------+         +-------------------+
           |                              |                              |
           |                              |                              |
           |                              |                              |
           V                              V                              V
+-------------------+         +-------------------+         +-------------------+
|Issuer Dimension  |<--------|Performance Fact Table|--->|Geography Dimension|
+-------------------+         +-------------------+         +-------------------+
                                                         |
                                                         |
                                                         V
                                                 +-------------------+
                                                 |Currency Dimension|
                                                 +-------------------+
```

### Explanation

1. **Holdings Fact Table**: Stores detailed information about portfolio holdings, including quantity, market value, cost basis, and unrealized gain/loss. It links to time, portfolio, instrument, sector, issuer, geography, and currency dimensions.

2. **Transaction Fact Table**: Captures details of buy/sell transactions, including transaction type, quantity, amount, and price. This table links to time, portfolio, and instrument dimensions.

3. **Performance Fact Table**: Contains performance metrics such as market value, total return, income, and capital gains for holdings over time. It links to time, portfolio, and instrument dimensions.

4. **Dimension Tables**: Provide contextual information about time periods, portfolios, financial instruments, sectors, issuers, geographical locations, and currencies.

### Use Cases for the Data Warehouse

1. **Portfolio Holdings Reports**:
   - Generate detailed reports of portfolio holdings, including market value, cost basis, and unrealized gains/losses.
   - Analyze holdings by various dimensions such as sector, issuer, geography, and currency.

2. **Transaction Analysis**:
   - Track and analyze buy/sell transactions over time.
   - Monitor transaction volumes and amounts for different instruments and portfolios.

3. **Performance Analysis**:
   - Evaluate the performance of portfolio holdings, including returns, income, and capital gains.
   - Compare performance across different time periods and against benchmarks.

4. **Sector and Issuer Exposure**:
   - Assess portfolio exposure to different sectors and issuers.
   - Monitor concentration risks and diversification strategies.

5. **Geographical and Currency Analysis**:
   - Analyze the geographical distribution of portfolio holdings.
   - Assess currency exposure and the impact of currency fluctuations on portfolio value.

This data warehouse design supports comprehensive portfolio holdings reporting and analysis, providing a robust structure for detailed insights into portfolio composition, transactions, and performance metrics.
