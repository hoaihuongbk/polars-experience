import duckdb

def main():
    # create a connection to a file called 'sample_duckdb_database.db'
    # this database is created using duckdb cli and integrated with unity catalog
    # to setup a delta catalog, please follow the instructions here:
    # https://docs.unitycatalog.io/quickstart/ to run UC in local mode
    # and this docs https://docs.unitycatalog.io/integrations/unity-catalog-duckdb/
    # to setup a delta catalog in duckdb

    conn = duckdb.connect()
    conn.sql("""
        install uc_catalog from core_nightly;
        load uc_catalog;
        load delta;
    """)

    conn.sql("""
        CREATE SECRET (
            TYPE UC,
            TOKEN 'not-used',
            ENDPOINT 'http://127.0.0.1:8080',
            AWS_REGION 'us-east-2'
       );
    """)

    conn.sql("""
        ATTACH 'unity' AS unity (TYPE UC_CATALOG);
    """)

    conn.sql("""
        SHOW ALL TABLES;
    """).show()

    conn.sql("SELECT * from unity.default.numbers").show()

    # work with polars
    df = conn.sql("SELECT * from unity.default.numbers").pl()
    print(df)

if __name__ == "__main__":
    main()