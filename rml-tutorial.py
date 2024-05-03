import morph_kgc

# config1 = """
#             [DataSource1]
#             mappings: rml/example.rml
#             file_path: rml/example.json
#         """
# graph1 = morph_kgc.materialize(config1)
# graph1.serialize(destination="rml/example_output.ttl")

config2 = """
            [DataSource1]
            mappings: rml/OCED.rml.ttl
            file_path: rml/OCED_19April.json
        """
graph2 = morph_kgc.materialize(config2)
graph2.serialize(destination="rml/oced_output.ttl")