# About the Neo4j to TigerGraph Agent

This is a sample project to demonstrate how intelligent agents
work with TigerGraph.  Our task is to take a running Neo4j database
and create a running TigerGraph database from that system.

Our agent will take the following steps:

1. Extract the full graph schema from Neo4j using the APOC library
1. Convert schema to TigerGraph GSQL 
1. Test GSQL syntax 
1. Convert Cypher to GSQL 
1. Extract Data from Neo4j is a series of CSV files for each vertex and edge
1. Create loading jobs to load vertices and then edges
1. Load data into TigerGraph 
1. Test queries on data
1. Execute performance test

## History

Omar  idea for this agent was 
