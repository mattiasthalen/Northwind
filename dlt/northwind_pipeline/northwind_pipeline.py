import dlt

from northwind import northwind_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="northwind",
        destination=dlt.destinations.duckdb("../../data/warehouse/northwind.duckdb"),
        #destination='motherduck',
        dataset_name="northwind",
        progress="enlighten",
        export_schema_path="schemas/export"
    )
    source = northwind_source("https://demodata.grapecity.com/")
    info = pipeline.run(source)
    print(info)
