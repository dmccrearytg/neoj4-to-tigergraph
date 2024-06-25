# Agent Steps


## Phase 1: Extract Schema from Neo4j using APOC

1.  Connect to Neo4j: Establish a connection using the provided Neo4j credentials.

2.  Extract Schema: Use APOC procedures to extract the schema.

-   CALL apoc.meta.schema()

4.  Store Schema: Save the extracted schema in a suitable format (e.g., JSON).

## Phase 2: Convert Schema to TigerGraph GSQL

1.  Parse Neo4j Schema: Read the extracted schema.

2.  Map to GSQL Schema: Create mappings from Neo4j types and relationships to TigerGraph types and edges.

3.  Generate GSQL Schema: Write the GSQL schema based on the mappings.

4.  Store GSQL Schema: Save the generated GSQL schema for further use.

## Phase 3: Test GSQL Syntax

1.  Connect to TigerGraph: Establish a connection using the provided TigerGraph credentials.

2.  Deploy Schema: Use the GSQL interface to deploy the schema.

3.  Validate Deployment: Check for syntax errors and confirm the schema is correctly deployed.

#### Phase 4: Convert Cypher to GSQL

1.  Identify Cypher Queries: Collect Cypher queries that need to be converted.

2.  Parse Cypher Queries: Analyze the structure of the Cypher queries.

3.  Map to GSQL Queries: Create mappings from Cypher query patterns to GSQL query patterns.

4.  Generate GSQL Queries: Write the GSQL queries based on the mappings.

5.  Store GSQL Queries: Save the generated GSQL queries for further use.

#### Phase 5: Extract Data from Neo4j

1.  Connect to Neo4j: Reuse the Neo4j connection.

2.  Export Data: Extract data from Neo4j using Cypher queries or APOC procedures.

-   CALL apoc.export.csv.all()

4.  Store Data: Save the extracted data in a suitable format (e.g., CSV).

#### Phase 6: Load Data into TigerGraph

1.  Connect to TigerGraph: Reuse the TigerGraph connection.

2.  Load Data: Use the GSQL interface to load the extracted data.

-   LOAD CSV ...

4.  Validate Data Load: Confirm the data is correctly loaded into TigerGraph.

#### Phase 7: Test Queries

1.  Run GSQL Queries: Execute the converted GSQL queries on the TigerGraph database.

2.  Validate Results: Compare the results with expected outcomes or results from Neo4j.

3.  Adjust and Optimize: Make necessary adjustments and optimize the queries as needed.

**