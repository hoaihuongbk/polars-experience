import polars as pl
from pprint import pprint

def main():
    # See https://github.com/unitycatalog/unitycatalog for the unity catalog server.
    catalog = pl.Catalog("http://127.0.0.1:8080")

    # pprint(catalog.list_catalogs())
    # [{"comment": "Main catalog", "name": "unity"}]
    # pprint(catalog.list_schemas("unity"))
    # [{"comment": "Default schema", "name": "default"}]
    # pprint(catalog.list_tables("unity", "default"))
    # pprint(catalog.get_table_info("unity", "default", "numbers"))
    print(q := catalog.scan_table("unity", "default", "numbers"))
    print(q.collect())

if __name__ == "__main__":
    main()

