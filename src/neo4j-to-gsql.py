"""
Generate a GSQL schema from a neo4j database.
"""

def convert_to_gsql(neo4j_schema):
    gsql_schema = ""
    for label, properties in neo4j_schema.items():
        gsql_schema += f"CREATE VERTEX {label} (PRIMARY_ID id STRING, "
        for prop, prop_type in properties.items():
            gsql_schema += f"{prop} {prop_type}, "
        gsql_schema = gsql_schema.rstrip(", ") + ");\n"
    return gsql_schema


gsql_schema = convert_to_gsql(neo4j_schema)
print(gsql_schema)
