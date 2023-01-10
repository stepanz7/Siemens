import json
import sys
# Get the file name from the command line
jsonFile = sys.argv[1]

# Open the file and read the data
with open(jsonFile, 'r') as file:
  data = json.load(file)




# Generate the code to insert
items_to_insert = ""
colNames_to_insert = ""
for coll_name in data.keys():
    for item in data[coll_name]:
        name, tag, type, size = item['name'], item['tag'], item['type'], item['size']
        items_to_insert += (f"initDataItem(\"{name}\", {tag}, \"{type}\", {size});\n    ")
        colNames_to_insert += (f"Colection.{coll_name}->push(\"{name}\");\n    ")

# Open the template file
with open('template.cpp', 'r') as template_file:
    template = template_file.read()

#Inserting items
index_items = template.index("//items") # Get the index where we want to insert items
template = template[:index_items] + items_to_insert + template[index_items+7:]

#Inserting collections
index_colls = template.index("//collections") # Get the index where we want to insert collections names
template = template[:index_colls] + colNames_to_insert + template[index_colls+13:]


# Open the output file
output_file = open('output.cpp', 'w')

# Write the template to the output file
output_file.write(template)
# Close the output file
output_file.close()


