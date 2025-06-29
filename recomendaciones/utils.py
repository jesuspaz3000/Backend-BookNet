from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "test123"))
def obtener_recomendaciones(user_id):
    query="""
    MATCH (u:Usuario {id: $user_id})-[:COMPRO]->(l:Libro)<-[:COMPRO]-(o:Usuario)
    WITH o, COUNT(l) as comunes
    ORDER BY comunes DESC LIMIT 5
    MATCH (o)-[:COMPRO]->(recomendado:Libro)
    WHERE NOT (u)-[:COMPRO]->(recomendado)
    RETURN DISTINCT recomendado
    """
    
    with driver.session() as session:
        result = session.run(query, user_id=user_id)
        return [record["recomendado"] for record in result]