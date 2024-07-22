### DynamoDB Interview Questions and Answers

#### Basic Questions

**Q1: What is DynamoDB?**

**A:** DynamoDB is a fully managed NoSQL database service provided by Amazon Web Services (AWS) that offers fast and predictable performance with seamless scalability. It is designed to handle large amounts of data and high request rates.

**Q2: What are the main features of DynamoDB?**

**A:** Some main features of DynamoDB include:
- **Automatic scaling:** DynamoDB automatically scales throughput capacity to meet your application's requirements.
- **Flexible data model:** Supports both document and key-value store models.
- **Event-driven programming:** Integrates with AWS Lambda for serverless architecture.
- **Global tables:** Provides multi-region, fully replicated tables for low-latency data access.

**Q3: What are the primary components of DynamoDB?**

**A:** The primary components are:
- **Tables:** A collection of items.
- **Items:** A group of attributes, similar to a row in a relational database.
- **Attributes:** A fundamental data element, similar to a column in a relational database.
- **Primary Key:** A unique identifier for each item in a table, can be a simple primary key or a composite primary key.

#### Advanced Questions

**Q4: How does DynamoDB ensure data consistency?**

**A:** DynamoDB offers two types of read consistency:
- **Eventually Consistent Reads:** Provides the lowest latency. Consistency is usually reached within a second.
- **Strongly Consistent Reads:** Guarantees that the most recent write is returned. It has higher latency than eventually consistent reads.

**Q5: What is the difference between a partition key and a sort key in DynamoDB?**

**A:** 
- **Partition Key (Primary Key):** A single attribute used to uniquely identify an item in a table. DynamoDB uses the partition key's value as input to an internal hash function, which determines the partition (physical location) where the data is stored.
- **Sort Key (Optional):** Used in conjunction with the partition key to create a composite primary key. The sort key allows multiple items to have the same partition key but different sort keys, enabling the storage of related items together and sorted by the sort key.

**Q6: How does DynamoDB handle high availability and fault tolerance?**

**A:** DynamoDB is designed to be highly available and fault-tolerant through:
- **Replication:** Data is automatically replicated across multiple Availability Zones within an AWS Region.
- **Automatic Failover:** If an Availability Zone becomes unavailable, DynamoDB automatically routes traffic to healthy replicas in other zones.

#### Practical Questions

**Q7: How can you optimize the performance of a DynamoDB table?**

**A:** 
- **Use the right partition key:** Choose a partition key that distributes requests evenly across partitions.
- **Indexing:** Use Global Secondary Indexes (GSI) and Local Secondary Indexes (LSI) to support query patterns.
- **Provisioned Throughput:** Appropriately provision read and write capacity units based on your application's needs.
- **DAX (DynamoDB Accelerator):** Use DAX for in-memory caching to reduce read latency.

**Q8: What are Global Secondary Indexes (GSI) and Local Secondary Indexes (LSI) in DynamoDB?**

**A:** 
- **GSI:** An index with a partition key and an optional sort key that can be different from those on the base table. It provides a way to query data using non-primary key attributes.
- **LSI:** An index that shares the same partition key as the base table but uses a different sort key. It allows for a more efficient way to query data with multiple attributes.

**Q9: Explain the concept of DynamoDB Streams.**

**A:** DynamoDB Streams is a feature that captures a time-ordered sequence of item-level changes in a DynamoDB table and stores this information for up to 24 hours. This can be used for:
- **Replicating data across regions**
- **Triggering AWS Lambda functions**
- **Maintaining materialized views**

#### Scenario-Based Questions

**Q10: How would you handle a scenario where you need to store and retrieve large binary files in DynamoDB?**

**A:** Storing large binary files directly in DynamoDB is not recommended due to size limitations and cost. Instead, you can:
- **Store binary files in Amazon S3.**
- **Store metadata and S3 object keys in DynamoDB.**

This allows for efficient data retrieval and management, leveraging S3's capabilities for handling large objects.

**Q11: How can you implement a time-to-live (TTL) feature in DynamoDB?**

**A:** DynamoDB has a built-in TTL feature that automatically deletes items after a specified expiration time. To use TTL:
- **Enable TTL on the table and specify the attribute that will store the expiration time (in Unix epoch time format).**
- **DynamoDB will automatically remove expired items from the table, reducing storage costs.**

**Q12: How would you perform a migration from a relational database to DynamoDB?**

**A:** The migration process involves:
- **Schema Design:** Map relational schema to a DynamoDB schema, considering differences in data models.
- **Data Transformation:** Use AWS Database Migration Service (DMS) to transform and migrate data from the relational database to DynamoDB.
- **Application Changes:** Modify your application to interact with DynamoDB, considering differences in query capabilities and optimization strategies.

These questions and answers cover a broad range of topics, from basic concepts to more advanced and practical scenarios, providing a comprehensive understanding of DynamoDB for interview preparation.

### Use Cases of DynamoDB Global Secondary Indexes (GSI) and Local Secondary Indexes (LSI)

#### Global Secondary Indexes (GSI)

**Use Case 1: Querying on Non-Primary Key Attributes**
- **Scenario:** You have an e-commerce application where the primary key is `OrderID`, but you frequently need to query orders by `CustomerID`.
- **Solution:** Create a GSI with `CustomerID` as the partition key and `OrderDate` as the sort key. This allows you to efficiently query orders by customer.

**Use Case 2: Supporting Multiple Query Patterns**
- **Scenario:** In a content management system, articles are primarily identified by `ArticleID`, but you also need to query articles by `AuthorID` and `PublishDate`.
- **Solution:** Create a GSI with `AuthorID` as the partition key and `PublishDate` as the sort key. This allows for efficient queries to retrieve articles written by a specific author within a certain date range.

**Use Case 3: Maintaining Materialized Views**
- **Scenario:** In a social media application, you store posts with `UserID` as the partition key and `PostID` as the sort key, but you also want to provide a global feed sorted by `CreationTime`.
- **Solution:** Create a GSI with `CreationTime` as the partition key and `PostID` as the sort key. This enables you to quickly retrieve the latest posts across all users.

**Use Case 4: Handling Sparse Indexes**
- **Scenario:** You have a table storing various types of transactions, but only a subset of these transactions includes a `RefundDate`.
- **Solution:** Create a GSI with `RefundDate` as the partition key. Only the items with a `RefundDate` attribute will appear in the GSI, making it easy to query all refunded transactions.

#### Local Secondary Indexes (LSI)

**Use Case 1: Enabling Efficient Range Queries**
- **Scenario:** In an order management system, orders are stored with `CustomerID` as the partition key and `OrderID` as the sort key. You need to query orders by `OrderDate` within a specific `CustomerID`.
- **Solution:** Create an LSI with `OrderDate` as the sort key. This allows you to efficiently query and retrieve orders within a date range for a particular customer.

**Use Case 2: Supporting Multiple Sort Keys for the Same Partition Key**
- **Scenario:** In a logging system, log entries are stored with `ApplicationID` as the partition key and `LogID` as the sort key. You need to query logs by `LogLevel` within the same application.
- **Solution:** Create an LSI with `LogLevel` as the sort key. This enables you to query logs based on their level (e.g., ERROR, WARN, INFO) within a specific application.

**Use Case 3: Optimizing Read Performance for Specific Queries**
- **Scenario:** You have a table of user activities with `UserID` as the partition key and `ActivityID` as the sort key. You need to frequently retrieve activities by `ActivityType` within a user.
- **Solution:** Create an LSI with `ActivityType` as the sort key. This improves the performance of queries that retrieve user activities filtered by activity type.

**Use Case 4: Reducing Data Duplication and Query Costs**
- **Scenario:** In a task management system, tasks are stored with `ProjectID` as the partition key and `TaskID` as the sort key. You also need to query tasks by `DueDate` within the same project.
- **Solution:** Create an LSI with `DueDate` as the sort key. This avoids the need to duplicate task data in a separate table for due date queries, reducing storage costs and maintaining data consistency.

### Conclusion

Global Secondary Indexes (GSI) and Local Secondary Indexes (LSI) are powerful features in DynamoDB that allow you to create additional access patterns without duplicating data. GSIs are ideal for enabling queries on non-primary key attributes and supporting multiple query patterns across the entire table, while LSIs are best for adding additional sort keys to enable efficient range queries and filtering within a specific partition key. By strategically using GSIs and LSIs, you can significantly enhance the performance and flexibility of your DynamoDB-based applications.
