"""Vector store + semantic search over text embeddings (pgvector).

Embeds documents and stores the vectors in Postgres so callers can run
approximate-nearest-neighbour semantic search instead of keyword LIKE.
"""
import psycopg


class VectorIndex:
    def __init__(self, dsn):
        self._dsn = dsn

    def add(self, doc_id, embedding, text):
        with psycopg.connect(self._dsn) as c:
            c.execute(
                "INSERT INTO documents (id, embedding, body) VALUES (%s, %s, %s)"
                " ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding",
                (doc_id, embedding, text),
            )

    def search(self, query_embedding, k=5):
        with psycopg.connect(self._dsn) as c:
            cur = c.execute(
                "SELECT id, body FROM documents ORDER BY embedding <=> %s LIMIT %s",
                (query_embedding, k),
            )
            return cur.fetchall()