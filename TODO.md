# TODO

## Data Lake Format Integration Tests

### Apache Iceberg
- [ ] Wait for the PR to be merged that adds native Iceberg support
- [ ] Test reading Iceberg tables with different specs
- [ ] Test writing to Iceberg tables
- [ ] Benchmark read/write performance vs PySpark
- [ ] Document integration patterns and best practices

### Apache Hudi
- [ ] Monitor progress on Hudi integration support
- [ ] Test reading Hudi tables when available
- [ ] Test writing to Hudi tables when available
- [ ] Evaluate performance with different Hudi table types (COW vs MOR)
- [ ] Document findings and usage patterns

### DuckDB Integration
- [ ] Set up DuckDB with Polars
- [ ] Test direct query execution
- [ ] Benchmark common analytics queries
- [ ] Test data loading/unloading between Polars and DuckDB
- [ ] Compare performance with pure Polars operations
- [ ] Document integration patterns and use cases
