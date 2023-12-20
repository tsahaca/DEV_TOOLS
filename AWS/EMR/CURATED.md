This check list can be used as the starting point for optimizing and troubleshooting bottlenecks in EMR Spark workloads. There are some prerequisites which are required before doing this task. 

Prerequisites: 
Spark Architecture and how does it integrate with Hadoop YARN. 
Deep understanding of Spark Query Plans - how spark operates under the hood.
How to read and analyze spark DAG from different perspectives. 
How to use Spark Web UI (History Server UI) to identify the bottleneck.
AWS EMR Architecture 
Check List:
The default spark.sql.shuffle.partitions=200 is wrong, if the stage input data size > 20GB. Watch this great talk https://www.youtube.com/watch?v=_ArCesElWp8&t=4512s  by Daniel Tom - how to tune this property spark.sql.shuffle.partitions. 
Based on cluster configuration how to calculate executor-memory, executor-core and num-executor: Use this article https://spoddutur.github.io/spark-notes/distribution_of_executors_cores_and_memory_for_spark_application.html
Writing the output files to s3 taking long time, then use
s3-dist-cp to copy your data back to S3. If EMR cluster is missing the s3-dist-cp command you have to include Hadoop in your create-cluster command. example: --applications Name=Hadoop Name=Spark 

Persist the Dataframe which are being used multiple times. This will reduce the read time.
