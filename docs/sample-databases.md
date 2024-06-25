# Sample Neo4j to TigerGraph Conversion Databases

Here are some of the most common graph database training sets used in 
beginning graph database training courses.  
We should test the agent on these simple databases first.

1.  Friends Network

-   Key Vertex Types: Person
-   Description: This dataset involves a simple social network where each person connects to others through FRIEND\_OF relationships. It's useful for teaching basic graph traversal, finding shortest paths, and community detection algorithms.

3.  Movie Recommendation

-   Key Vertex Types: Movie, Person
-   Description: This dataset includes people and the movies they like. It is used to teach recommendation algorithms, collaborative filtering, and basic graph analytics such as finding similar users or movies.

5.  Employee Hierarchy

-   Key Vertex Types: Employee, Department
-   Description: This dataset represents an organizational structure where employees belong to departments with a hierarchical reporting structure (MANAGES relationships). It is used to demonstrate hierarchical queries, pathfinding, and organizational analytics.

7.  E-commerce Transactions
-   Key Vertex Types: Customer, Product, Transaction
-   Description: This dataset captures customers and their transactions with products. It is ideal for teaching fraud detection, market basket analysis, and recommendation systems in an e-commerce context.

9.  Knowledge Graph Builder

-   Key Vertex Types: Document, Chuck, Entity, Concept
-   Description: This dataset represents a domain of knowledge in which entities are linked to concepts and other entities (RELATED\_TO, BELONGS\_TO relationships). It demonstrates semantic search, ontology management, and inference over a graph.

11.  Citation Network

-   Key Vertex Types: Paper, Author, Journal
-   Description: This dataset includes academic papers, their authors, and the journals where they are published, with CITED\_BY relationships between papers. It is used to teach bibliometric analysis, finding influential papers, and co-authorship networks.

13.  IT Infrastructure Network

-   Key Vertex Types: Device, Application, User, Change, Server, MicroService, Vulnerability, Threat
-   Description: This dataset models an IT infrastructure connecting devices, applications, and users (CONNECTED\_TO, USED\_BY relationships). It teaches network topology, security analysis, and impact assessment of outages.

15.  Supply Chain

-   Key Vertex Types: Supplier, Product, Shipment
-   Description: This dataset tracks suppliers, the products they supply, and shipments between entities. It is used to demonstrate supply chain management, tracing product origins, and optimizing logistics.

17.  Financial Network

-   Key Vertex Types: Account, Transaction, Customer
-   Description: This dataset captures financial accounts, transactions between them, and the customers who own the accounts. It is ideal for teaching money laundering detection, transaction analysis, and customer relationship management.

19.  Gene Interaction Network

-   Key Vertex Types: Gene, Protein
-   Description: This dataset includes genes and proteins with interactions (INTERACTS\_WITH relationships). It is used for teaching biological network analysis, pathway identification, and drug target discovery.

21.  Event Log

-   Key Vertex Types: Event, User, Resource
-   Description: This dataset models events in a system, with users triggering events and resources being affected. It is useful for teaching event correlation, anomaly detection, and user behavior analysis.

23.  Urban Transportation Network

-   Key Vertex Types: Station, Route, Vehicle
-   Description: This dataset represents a city's transportation system with stations, routes, and vehicles (CONNECTED\_TO, SERVED\_BY relationships). It is used to teach route optimization, traffic analysis, and public transport efficiency.

These datasets provide a wide range of real-world scenarios to help beginners understand the applications and analytical capabilities of graph databases.