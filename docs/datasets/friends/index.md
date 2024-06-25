# Friends

```sh
cd data/friends
```

```sh
docker cp load_friends_of_friends.cql neo4j:/load_friends_of_friends.cql
```

Successfully copied 2.05kB to neo4j:/load_friends_of_friends.cql

```sh
docker exec -it neo4j bash
```

```sh
cat /load_friends_of_friends.cql | cypher-shell -u neo4j -p neo4j123
```

or

```sh
cypher-shell -u neo4j -p neo4j123 -f load_friends_of_friends.cql
```