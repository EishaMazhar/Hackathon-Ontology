# pip install rdflib

from rdflib import Graph

# 1. Load the ontology + data
g = Graph()
g.parse("hackathon_ecosystem_ontology.ttl", format="turtle")
print(f"Loaded {len(g)} triples")


q_teams_people_skills = """
PREFIX hack: <http://example.org/hackathon#>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?teamName ?personName ?skillLabel
WHERE {
  ?team a hack:Team ;
        dct:title ?teamName ;
        hack:hasParticipant ?p .
  ?p foaf:name ?personName ;
     hack:hasSkill ?skill .
  ?skill skos:prefLabel ?skillLabel .
}
ORDER BY ?teamName ?personName ?skillLabel
"""

q_projects_skills = """
PREFIX hack: <http://example.org/hackathon#>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?projectTitle ?skillLabel
WHERE {
  ?project a hack:Project ;
           dct:title ?projectTitle ;
           hack:requiresSkill ?skill .
  ?skill skos:prefLabel ?skillLabel .
}
ORDER BY ?projectTitle ?skillLabel
"""

q_datascience_teams = """
PREFIX hack: <http://example.org/hackathon#>
PREFIX dct:  <http://purl.org/dc/terms/>

SELECT ?teamName
WHERE {
  ?team a hack:DataScienceTeam ;
        dct:title ?teamName .
}
ORDER BY ?teamName
"""

q_wellbalanced_teams = """
PREFIX hack: <http://example.org/hackathon#>
PREFIX dct:  <http://purl.org/dc/terms/>

SELECT ?teamName
WHERE {
  ?team a hack:WellBalancedTeam ;
        dct:title ?teamName .
}
ORDER BY ?teamName
"""

# 3. Helper to run and pretty print any query


def run_query(query_str, title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)
    for row in g.query(query_str):
        # row is a tuple of rdflib.term instances, convert to Python strings
        values = [str(v) for v in row]
        print(" | ".join(values))


# 4. Run the queries
run_query(q_teams_people_skills, "Teams, members, and skills")
run_query(q_projects_skills, "Projects and required skills")
run_query(q_datascience_teams, "Data science oriented teams (SWRL inferred)")
run_query(q_wellbalanced_teams, "Well balanced teams (SWRL inferred)")
