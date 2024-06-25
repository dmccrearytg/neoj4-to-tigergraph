from neo4j import GraphDatabase

# Connect to Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4j123"))


def extract_schema():
    with driver.session() as session:
        result = session.run("CALL apoc.meta.schema()")
        schema = result.single()
        return schema


neo4j_schema = extract_schema()
print(neo4j_schema)
