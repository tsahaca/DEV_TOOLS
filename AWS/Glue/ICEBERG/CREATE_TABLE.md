CREATE TABLE IF NOT EXISTS iceberg.user_transactions (
  dt date,
  user_id int,
  total_cost_usd float,
  registration_date string
) 
PARTITIONED BY (dt)
LOCATION 's3://glue-sample-tsaha/iceberg/myschema/optimized-data-iceberg-parquet/' 
TBLPROPERTIES (
  'table_type'='ICEBERG',
  'format'='parquet',
  'write_target_data_file_size_bytes'='536870912',
  'optimize_rewrite_delete_file_threshold'='10'
)
;
