from neomodel import config
from neomodel import db

config.DATABASE_URL = 'bolt://neo4j:password123@localhost:7687'
config.ENCRYPTED_CONNECTION = False

dbquery = "CREATE (n:Person { name: 'Frank', title: 'CEO' })"
db.cypher_query(dbquery, None)

dbquery = "CREATE (n:Person { name: 'Andy', title: 'CTO' })"
db.cypher_query(dbquery, None)

dbquery = "MATCH (a:Person),(b:Person) WHERE a.name = 'Frank' AND b.name = 'Andy' CREATE (a)-[r:KNOWS]->(b) RETURN type(r)"
db.cypher_query(dbquery, None)




