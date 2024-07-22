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
