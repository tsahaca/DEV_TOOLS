
# Spark Session
```python
from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .appName("Dynamic Allocation")
    .master("spark://197e20b418a6:7077")
    .config("spark.executor.cores", 2)
    .config("spark.executor.memory", "512M")
    .config("spark.dynamicAllocation.enabled", True)
    .config("spark.dynamicAllocation.minExecutors", 0)
    .config("spark.dynamicAllocation.maxExecutors", 5)
    .config("spark.dynamicAllocation.initialExecutors", 1)
    .config("spark.dynamicAllocation.shuffleTracking.enabled", True)
    .config("spark.dynamicAllocation.executorIdleTimeout", "60s")
    .config("spark.dynamicAllocation.cachedExecutorIdleTimeout", "60s")
    .getOrCreate()
)
```
. config(“spark.dynamicAllocation.initialExecutors”, 1) — As soon the SparkSession will be generated, 1 executor (with 2 core and 512MB memory) will initially be assigned to the Application.

. config(“spark.dynamicAllocation.shuffleTracking.enabled”, True) — Enables Shuffle Tracking service for the Application, which will allows newly created Executors to access the existing shuffle data.

. config(“spark.dynamicAllocation.executorIdleTimeout”, “60s”) — Kills Executors if they are idle for more than 60s (required for Scaling down and releasing resources)

. config(“spark.dynamicAllocation.cachedExecutorIdleTimeout”, “60s”) — Kills Executors having cached data if they are idle for more than 60s (required for Scaling down and releasing resources gracefully)
