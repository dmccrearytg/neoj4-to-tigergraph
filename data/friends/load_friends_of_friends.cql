:use system
CREATE DATABASE friends;

// Create nodes
CREATE (Alice:Person {name: 'Alice'});
CREATE (Bob:Person {name: 'Bob'});
CREATE (Carol:Person {name: 'Carol'});
CREATE (Dave:Person {name: 'Dave'});

// Create relationships
CREATE (Alice)-[:FRIEND]->(Bob);
CREATE (Bob)-[:FRIEND]->(Carol);
CREATE (Carol)-[:FRIEND]->(Dave);
CREATE (Dave)-[:FRIEND]->(Alice);
