from neomodel import config
from neomodel import db

config.DATABASE_URL = 'bolt://neo4j:password123@localhost:7687'
config.ENCRYPTED_CONNECTION = False

dbquery = "CREATE (n:Person { name: 'Alex', title: 'intern' })"
db.cypher_query(dbquery, None)


