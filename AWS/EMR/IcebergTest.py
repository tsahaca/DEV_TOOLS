from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

warehouse_path = "./warehouse"
iceberg_spark_jar  = 'org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0'
catalog_name = "demo"

# Setup iceberg config
conf = SparkConf().setAppName("YourAppName") \
    .set("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .set(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog") \
    .set('spark.jars.packages', iceberg_spark_jar) \
    .set(f"spark.sql.catalog.{catalog_name}.warehouse", warehouse_path) \
    .set(f"spark.sql.catalog.{catalog_name}.type", "hadoop")\
    .set("spark.sql.defaultCatalog", catalog_name) 

# Create spark session
spark = SparkSession.builder.config(conf=conf).getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Create a dataframe
schema = StructType([
    StructField('name', StringType(), True),
    StructField('age', IntegerType(), True),
    StructField('job_title', StringType(), True)
])
data = [("person1", 28, "Doctor"), ("person2", 35, "Singer"), ("person3", 42, "Teacher")]
df = spark.createDataFrame(data, schema=schema)

# Create database
spark.sql(f"CREATE DATABASE IF NOT EXISTS db")

# Write and read Iceberg table
table_name = "db.persons"
df.write.format("iceberg").mode("overwrite").saveAsTable(f"{table_name}")
iceberg_df = spark.read.format("iceberg").load(f"{table_name}")
iceberg_df.printSchema()
iceberg_df.show()
