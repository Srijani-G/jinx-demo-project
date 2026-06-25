// Knowledge graph schema: entity relationship constraints
CREATE CONSTRAINT entity_id IF NOT EXISTS FOR (n:Entity) REQUIRE n.id IS UNIQUE;
CREATE INDEX rel_type IF NOT EXISTS FOR ()-[r:LINKED_TO]-() ON (r.weight);