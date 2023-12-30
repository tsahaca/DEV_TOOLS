# Check List
This check list can be used as the starting point for optimizing and troubleshooting bottlenecks in EMR Spark workloads. There are some prerequisites which are required before doing this task. 

## Prerequisites: 
1. Spark Architecture and how does it integrate with Hadoop YARN.
2. Deep understanding of Spark Query Plans - how spark operates under the hood.
3. How to read and analyze spark DAG from different perspectives.
4. How to use Spark Web UI (History Server UI) to identify the bottleneck.
5. AWS EMR Architecture 

##Check List:
1. The default spark.sql.shuffle.partitions=200 is wrong, if the stage input data size > 20GB. Watch this great talk https://www.youtube.com/watch?v=_ArCesElWp8&t=4512s  by Daniel Tom - how to tune this property spark.sql.shuffle.partitions. 
Based on cluster configuration
2. how to calculate executor-memory, executor-core and num-executor: Use this article https://spoddutur.github.io/spark-notes/distribution_of_executors_cores_and_memory_for_spark_application.html
3. Writing the output files to s3 taking long time, then use
s3-dist-cp to copy your data back to S3. If EMR cluster is missing the s3-dist-cp command you have to include Hadoop in your create-cluster command. example: --applications Name=Hadoop Name=Spark
4. Persist the Dataframe which are being used multiple times. This will reduce the read time.
5. [Shuffle Partitions Calculator](https://github.com/justinbreese/databricks-gems/blob/master/shufflePartitionCalculator/sparkShufflePartitionCalculator.py)
6. [AQE Auto Optimizer](https://community.databricks.com/t5/data-engineering/ideal-number-and-size-of-partitions/td-p/25502)
7. [AQE in Databricks](https://www.databricks.com/blog/2020/10/21/faster-sql-adaptive-query-execution-in-databricks.html)
8. [AQE User Guide](https://docs.databricks.com/en/optimizations/aqe.html)
9. [AQE Optimization](https://docs.databricks.com/en/optimizations/aqe.html#spark-ui)
10. [Spark SQL Query Engine Deep Dive](https://dataninjago.com/2022/02/21/spark-sql-query-engine-deep-dive-20-adaptive-query-execution-part-2/)
11. [AQE Part 2](https://blog.madhukaraphatak.com/spark-aqe-part-2)
   
   
   
