# Hackathon-Ontology

This project contains an ontology for the hackathon ecosystem, relevant files, and sample SPARQL queries to run on that ontology.

## Contents

- ontology/
  - The RDF/Turtle/OWL files that define the hackathon ontology.
- samples/
  - Example RDF instances and SPARQL query files.
- scripts/
  - Helper scripts (Python) to load the ontology, run queries, and convert formats.
- examples/
  - Example usages and demonstrations.

(If any of the above directories are named differently in the repository, update the paths accordingly.)

## Features

- A domain ontology modeling hackathons, participants, projects, mentors, sponsors, prizes, and events.
- Sample instance data to illustrate how to populate the ontology.
- A set of SPARQL queries demonstrating common queries over the hackathon data.
- Python scripts to load the ontology and execute queries locally using RDF libraries.

## Getting started

Prerequisites

- Python 3.8+
- pip
- (Optional) Apache Jena Fuseki if you want a SPARQL server

Install basic Python requirements (example):

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install rdflib rdflib-jsonld
```

If you prefer to use a SPARQL server, download and run Apache Jena Fuseki: https://jena.apache.org/download/index.cgi

## Loading the ontology locally (rdflib)

Example Python snippet to load a Turtle file and run a SPARQL query using rdflib:

```python
from rdflib import Graph

g = Graph()
# replace with the path to your ontology/instance file
g.parse("ontology/hackathon.ttl", format="turtle")

q = '''
PREFIX ex: <http://example.org/hackathon#>
SELECT ?hackathon ?name
WHERE {
  ?hackathon a ex:Hackathon ;
             ex:name ?name .
}
'''

for row in g.query(q):
    print(row)
```

## Running SPARQL queries with Fuseki

1. Start Fuseki server and create a dataset (e.g., "hackathon").
2. Upload the ontology and data (Turtle/TTL files) to the dataset.
3. Use the Fuseki web console or a curl request to run queries.

Example curl request to run a SELECT query:

```bash
curl -X POST --data-urlencode "query@samples/queries/list-hackathons.sparql" \
  http://localhost:3030/hackathon/sparql
```

## Example SPARQL queries

Below are a few example queries you can adapt. Put these in samples/queries/*.sparql for convenience.

- List all Teams, members, and skills

```sparql
PREFIX hack: <http://example.org/hackathon#>
PREFIX dct: <http://purl.org/dc/terms/>
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
```

- Teams and Projects per hackathon

```sparql
PREFIX hack: <http://example.org/hackathon#>
PREFIX dct: <http://purl.org/dc/terms/>
SELECT ?hackathonTitle ?teamTitle ?projectTitle
WHERE {
?hack a hack:Hackathon ;
dct:title ?hackathonTitle ;
hack:hasTeam ?team .
?team dct:title ?teamTitle ;
hack:worksOn ?project .
?project dct:title ?projectTitle .
}
ORDER BY ?hackathonTitle ?teamTitle
```

- Required Skills per Project

```sparql
PREFIX hack: <http://example.org/hackathon#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?projectTitle ?skillLabel
WHERE {
?project a hack:Project ;
dct:title ?projectTitle ;
hack:requiresSkill ?skill .
?skill skos:prefLabel ?skillLabel .
}
ORDER BY ?projectTitle ?skillLabel
```

## Repository layout and conventions

- Use meaningful URIs and a consistent namespace (change example.org to your chosen base URI).
- Use Turtle (.ttl) for human-friendly serializations and OWL (.owl) where appropriate.
- Keep SPARQL queries in a samples/queries directory and name them clearly.

## Contributing

Contributions are welcome. Please:

1. Open an issue describing the change or feature.
2. Create a branch for your change.
3. Submit a pull request with tests or example usage where appropriate.

## License

Specify a license for your project (e.g., MIT, Apache-2.0). If you don't have one yet, add a LICENSE file.

## Contact

If you have questions or suggestions, open an issue or contact the repository owner.


----

This README provides a starting point for using and extending the Hackathon ontology. Update the file paths and example URIs to reflect the actual files and namespaces in this repository.
