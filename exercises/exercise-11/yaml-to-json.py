def convert_file(file):
    json = open("exercises/exercise-11/json/json_file.json", "x")
    indentation = 1
    json.write("{\n")
    for line in file:
        pass
    json.write("}")

with open("exercises/exercise-11/yaml/example.yaml") as file:
    convert_file(file)