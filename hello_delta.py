# Follow this docs: https://delta-io.github.io/delta-rs/integrations/delta-lake-polars/#reading-a-delta-lake-table-with-polars

import polars as pl

def main():
    df = pl.DataFrame(
        {
            "foo": [1, 2, 3, 4, 5],
            "bar": [6, 7, 8, 9, 10],
            "ham": ["a", "b", "c", "d", "e"],
        }
    )

    import os
    os.makedirs("docs/assets/data", exist_ok=True)

    # Write delta
    table_path = "docs/assets/data/sample-delta-table/"
    df.write_delta(
        table_path,
        mode="overwrite",
        delta_write_options={"schema_mode": "overwrite"},
    )

    # Read delta
    delta_df = pl.read_delta(table_path)
    print(delta_df)

    # Register delta table as SQL table
    ctx = pl.SQLContext()
    ctx.register("delta_df", delta_df)
    result = ctx.execute("SELECT * FROM delta_df", eager=True)
    print(result)

    # Read from specific version
    print(pl.read_delta(table_path, version=0))

if __name__ == "__main__":
    main()
