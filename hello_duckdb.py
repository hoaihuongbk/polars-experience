import duckdb
import polars as pl

def main():
    df = pl.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "fruits": ["banana", "banana", "apple", "apple", "banana"],
            "B": [5, 4, 3, 2, 1],
            "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
        }
    )
    duckdb.sql("SELECT * FROM df").show()

    duckdb_df = duckdb.sql("""
        SELECT 1 AS id, 'banana' AS fruit
        UNION ALL
        SELECT 2, 'apple'
        UNION ALL
        SELECT 3, 'mango'"""
    ).pl()
    print(duckdb_df)

if __name__ == "__main__":
    main()