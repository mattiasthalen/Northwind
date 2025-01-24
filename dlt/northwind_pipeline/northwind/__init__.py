from typing import List

import dlt

from dlt.sources.rest_api.typing import RESTAPIConfig
from dlt.sources.rest_api import rest_api_source


@dlt.source(name="northwind", max_table_nesting=0)
def northwind_source(
    base_url: str = dlt.config.value,
) -> List[dlt.resource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "get_northwindapiv_1_categories",
                "table_name": "category_dto",
                "primary_key": "categoryId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Categories",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_categoriesid",
                "table_name": "category_dto",
                "primary_key": "categoryId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Categories/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_categories",
                            "field": "categoryId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_productsid_category",
                "table_name": "category_dto",
                "primary_key": "categoryId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Products/{id}/Category",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_products",
                            "field": "productId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_customers",
                "table_name": "customer_dto",
                "primary_key": "customerId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Customers",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_customersid",
                "table_name": "customer_dto",
                "primary_key": "customerId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Customers/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_customers",
                            "field": "customerId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_ordersid_customer",
                "table_name": "customer_dto",
                "primary_key": "customerId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Orders/{id}/Customer",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_orders",
                            "field": "orderId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_categoriesid_details",
                "table_name": "detail",
                "endpoint": {
                    "data_selector": "productNames",
                    "path": "/northwind/api/v1/Categories/{id}/Details",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_categories",
                            "field": "categoryId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_employees",
                "table_name": "employee_dto",
                "primary_key": "employeeId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Employees",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_employeesid",
                "table_name": "employee_dto",
                "primary_key": "employeeId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Employees/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_employees",
                            "field": "employeeId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # {
            #     "name": "get_northwindapiv_1_employeesid_superior",
            #     "table_name": "employee_dto",
            #     "endpoint": {
            #         "data_selector": "$",
            #         "path": "/northwind/api/v1/Employees/{id}/Superior",
            #         "params": {
            #             "id": {
            #                 "type": "resolve",
            #                 "resource": "get_northwindapiv_1_employees",
            #                 "field": "employeeId",
            #             },
            #         },
            #         "paginator": "auto",
            #     },
            # },
            {
                "name": "get_northwindapiv_1_employeesid_subordinates",
                "table_name": "employee_dto",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Employees/{id}/Subordinates",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_employees",
                            "field": "employeeId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_ordersid_employee",
                "table_name": "employee_dto",
                "primary_key": "employeeId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Orders/{id}/Employee",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_orders",
                            "field": "orderId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_territoriesid_employees",
                "table_name": "employee_dto",
                "primary_key": "employeeId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Territories/{id}/Employees",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_territories",
                            "field": "territoryId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_ordersid_order_details",
                "table_name": "order_detail_dto",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Orders/{id}/OrderDetails",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_orders",
                            "field": "orderId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_productsid_order_details",
                "table_name": "order_detail_dto",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Products/{id}/OrderDetails",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_products",
                            "field": "productId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_customersid_orders",
                "table_name": "order_dto",
                "primary_key": "orderId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Customers/{id}/Orders",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_customers",
                            "field": "customerId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_employeesid_orders",
                "table_name": "order_dto",
                "primary_key": "orderId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Employees/{id}/Orders",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_employees",
                            "field": "employeeId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_orders",
                "table_name": "order_dto",
                "primary_key": "orderId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Orders",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_ordersid",
                "table_name": "order_dto",
                "primary_key": "orderId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Orders/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_orders",
                            "field": "orderId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_shippersid_orders",
                "table_name": "order_dto",
                "primary_key": "orderId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Shippers/{id}/Orders",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_shippers",
                            "field": "shipperId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_categoriesid_products",
                "table_name": "product_dto",
                "primary_key": "productId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Categories/{id}/Products",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_categories",
                            "field": "categoryId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_ordersid_products",
                "table_name": "product_dto",
                "primary_key": "productId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Orders/{id}/Products",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_orders",
                            "field": "orderId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_products",
                "table_name": "product_dto",
                "primary_key": "productId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Products",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_productsid",
                "table_name": "product_dto",
                "primary_key": "productId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Products/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_products",
                            "field": "productId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_suppliersid_products",
                "table_name": "product_dto",
                "primary_key": "productId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Suppliers/{id}/Products",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_suppliers",
                            "field": "supplierId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_regions",
                "table_name": "region_dto",
                "primary_key": "regionId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Regions",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_regionsid",
                "table_name": "region_dto",
                "primary_key": "regionId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Regions/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_regions",
                            "field": "regionId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_territoriesid_region",
                "table_name": "region_dto",
                "primary_key": "regionId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Territories/{id}/Region",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_territories",
                            "field": "territoryId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_ordersid_shipper",
                "table_name": "shipper_dto",
                "primary_key": "shipperId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Orders/{id}/Shipper",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_orders",
                            "field": "orderId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_shippers",
                "table_name": "shipper_dto",
                "primary_key": "shipperId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Shippers",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_shippersid",
                "table_name": "shipper_dto",
                "primary_key": "shipperId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Shippers/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_shippers",
                            "field": "shipperId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_productsid_supplier",
                "table_name": "supplier_dto",
                "primary_key": "supplierId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Products/{id}/Supplier",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_products",
                            "field": "productId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_suppliers",
                "table_name": "supplier_dto",
                "primary_key": "supplierId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Suppliers",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_suppliersid",
                "table_name": "supplier_dto",
                "primary_key": "supplierId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Suppliers/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_suppliers",
                            "field": "supplierId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_employeesid_territories",
                "table_name": "territory_dto",
                "primary_key": "territoryId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Employees/{id}/Territories",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_employees",
                            "field": "employeeId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_regionsid_territories",
                "table_name": "territory_dto",
                "primary_key": "territoryId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Regions/{id}/Territories",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_regions",
                            "field": "regionId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_territories",
                "table_name": "territory_dto",
                "primary_key": "territoryId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Territories",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_northwindapiv_1_territoriesid",
                "table_name": "territory_dto",
                "primary_key": "territoryId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/northwind/api/v1/Territories/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_northwindapiv_1_territories",
                            "field": "territoryId",
                        },
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
