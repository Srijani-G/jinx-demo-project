"""Knowledge graph builder: maps entity relationships into Neo4j.

Reads domain entities (users, accounts, merchants) and writes typed
relationship edges (OWNS, TRANSACTED_WITH, LINKED_TO) so downstream
services can traverse the graph instead of doing N+1 joins.
"""
from neo4j import GraphDatabase


class KnowledgeGraphBuilder:
    def __init__(self, uri, auth):
        self._driver = GraphDatabase.driver(uri, auth=auth)

    def upsert_entity(self, label, key, props):
        q = f"MERGE (n:{label} {{id: $key}}) SET n += $props RETURN n"
        with self._driver.session() as s:
            s.run(q, key=key, props=props)

    def relate(self, src, rel, dst):
        q = ("MATCH (a {id: $src}), (b {id: $dst}) "
             f"MERGE (a)-[:{rel}]->(b)")
        with self._driver.session() as s:
            s.run(q, src=src, dst=dst)