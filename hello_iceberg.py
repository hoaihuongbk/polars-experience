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

    # Write iceberg
    # Will continue the test faster this pr merge https://github.com/pola-rs/polars/pull/15018
    table_path = "docs/assets/data/sample-iceberg-table/"
    df.write_iceberg(
        table_path,
        mode="overwrite",
    )

if __name__ == "__main__":
    main()
