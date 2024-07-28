# The post-trade settlement process typically involves several steps:

1. **Trade Execution**: Once a trade (buy or sell order) is executed on a stock exchange or through a broker, the details of the transaction are recorded.
*****At MYCOM OMS is order booking system. It is also integrated with third party platforms like FxConnet , Bloomberg , Trade web etc 

2. **Confirmation**: Both parties involved in the trade (buyer and seller) receive a confirmation detailing the terms of the trade, including price, quantity, and settlement date.


****MYCOM implemented confirmation application integrated with DTCC. Coverage of this app is Fixed Income and Equity trades

3. **Clearing**: This involves validating the trade details, ensuring that both parties have the necessary funds or securities to complete the transaction.

4. **Settlement**: Actual exchange of funds and securities occurs during settlement. This can involve the transfer of money from the buyer to the seller and the transfer of securities from the seller to the buyer.

****MYCOM integrated settlements with BBH for all instruments. BBH send MT messages to SWIFT networks for settlements

5. **Recording**: Once settlement is complete, the trade is recorded in the books of both parties and updated in relevant financial records and systems.

MYCOM get ack nak messages from BBH after settlements completed 

6. **Reconciliation**: This step involves verifying that all parties involved (traders, brokers, clearing houses) have accurately recorded the trade and settlement details.

MYCOM build custome recons as EOD process

7. **Reporting**: Regulatory bodies and market participants may require reporting of trades and settlement details for transparency and compliance purposes.

This high-level workflow ensures that trades are executed smoothly and all parties involved in the transaction are accounted for during the post-trade settlement process.

## Corporate actions encompass a wide range of events or decisions initiated by a company that can affect its shareholders or bondholders. Here's a comprehensive list of common corporate actions:

1. **Dividends**: Payments made by a company to its shareholders as a distribution of profits.

2. **Stock Splits**: Increasing the number of outstanding shares by splitting existing shares into multiple shares, typically to lower the share price and increase liquidity.

3. **Stock Consolidations (Reverse Splits)**: Decreasing the number of outstanding shares by consolidating existing shares into fewer shares, usually to increase the share price.

4. **Bonus Issues**: Issuing additional shares to existing shareholders based on their current holdings, often as a form of dividend.

5. **Rights Issues**: Offering existing shareholders the right to buy additional shares at a discounted price, typically to raise capital.

6. **Share Buybacks (Repurchases)**: Companies repurchasing their own shares from the open market, reducing the number of outstanding shares.

7. **Tender Offers**: Inviting shareholders to tender their shares for repurchase at a specified price and within a specific period.

8. **Mergers and Acquisitions (M&A)**: Transactions where companies combine (merger) or one company acquires another (acquisition).

9. **Spin-offs**: Creating a new independent company by divesting a portion of an existing company's assets or business.

10. **Asset Sales**: Selling significant assets or divisions of the company.

11. **Bankruptcy Proceedings**: Legal processes initiated by insolvent companies to reorganize or liquidate assets.

12. **Corporate Restructuring**: Significant changes in a company's organizational or operational structure to improve efficiency or strategic focus.

13. **Liquidation**: Complete dissolution of the company and distribution of assets to shareholders.

14. **Warrants Issuance**: Offering warrants alongside securities, allowing holders to buy company stock at a specified price within a set period.

15. **Interest Payments**: Regular payments made by issuers of bonds or other debt securities to bondholders.

16. **Principal Repayment**: Payment of the principal amount (face value) of bonds or debt securities at maturity or upon early redemption.

17. **Amortization**: Gradual repayment of the principal amount over time, particularly with mortgage-backed securities or certain types of bonds.

18. **Call and Put Options**: Callable bonds give issuers the right to redeem the bond before maturity, while putable bonds give bondholders the right to demand early repayment.

19. **Coupon Changes**: Changes in the interest rate (coupon rate) if bond terms allow for variable or adjustable rates.

These corporate actions can have significant implications for shareholders' equity positions, bondholders' returns, and the overall financial health and strategy of a company. They are closely monitored by investors, financial analysts, and regulatory authorities for their impact on market dynamics and shareholder value.
