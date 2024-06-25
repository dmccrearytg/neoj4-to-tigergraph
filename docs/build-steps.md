# Build Steps

These steps assume you are running Neo4j locally on a Docker image.  You should have at least

## Create a conda virtual environment for Python 3

```sh
conda create -n 'neo4j-to-tigergraph' python=3
conda activate 
```

This process should take under 1 minute.

## Install the required libraries within this Conda environment

```sh
pip install -r requirements.txt
```

## Install Neo4j on a local Docker Image

```sh
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/neo4j123 neo4j:latest
```

Here's what each part of the command does:

-   `docker run -d`: Runs the container in detached mode (in the background).
-   `--name neo4j`: Names the container "neo4j".
-   `-p 7474:7474`: Maps port 7474 on your host to port 7474 on the container (used for the Neo4j Browser).
-   `-p 7687:7687`: Maps port 7687 on your host to port 7687 on the container (used for the Bolt protocol).
-   `-e NEO4J_AUTH=neo4j/neo4j123`: Sets the Neo4j authentication credentials (`neo4j` as the username and `password` as the password). You should replace `password` with a more secure password.  Note that the password must be 8 or more characters.
-   `neo4j:latest`: Specifies the Neo4j image to use (the `latest` tag pulls the most recent version).

If you want to use a specific version of Neo4j, replace `latest` with the desired version number, for example, `neo4j:4.4.9`.

The log file in the Docker log should look like the following:

```
2024-06-25 11:06:21 Changed password for user 'neo4j'. IMPORTANT: this change will only take effect if performed before the database is started for the first time.
2024-06-25 11:06:22 2024-06-25 16:06:22.997+0000 INFO  Logging config in use: File '/var/lib/neo4j/conf/user-logs.xml'
2024-06-25 11:06:23 2024-06-25 16:06:23.005+0000 INFO  Starting...
2024-06-25 11:06:23 2024-06-25 16:06:23.485+0000 INFO  This instance is ServerId{5e89297d} (5e89297d-0a9f-4d5a-91ea-76f1f081524f)
2024-06-25 11:06:23 2024-06-25 16:06:23.979+0000 INFO  ======== Neo4j 5.20.0 ========
2024-06-25 11:06:25 2024-06-25 16:06:25.046+0000 INFO  Anonymous Usage Data is being sent to Neo4j, see https://neo4j.com/docs/usage_data/
2024-06-25 11:06:25 2024-06-25 16:06:25.289+0000 INFO  Bolt enabled on 0.0.0.0:7687.
2024-06-25 11:06:25 2024-06-25 16:06:25.630+0000 INFO  HTTP enabled on 0.0.0.0:7474.
2024-06-25 11:06:25 2024-06-25 16:06:25.631+0000 INFO  Remote interface available at http://localhost:7474/
2024-06-25 11:06:25 2024-06-25 16:06:25.632+0000 INFO  id: 10096F7F7FE1A4729427034A450EBD24ACFF1586035FB1EA54F55F0878E2C303
2024-06-25 11:06:25 2024-06-25 16:06:25.632+0000 INFO  name: system
2024-06-25 11:06:25 2024-06-25 16:06:25.632+0000 INFO  creationDate: 2024-06-25T16:06:24.463Z
2024-06-25 11:06:25 2024-06-25 16:06:25.632+0000 INFO  Started.
```

## Verify that Neo4j is running on port 7474

```sh
http://localhost:7474/browser/
```

