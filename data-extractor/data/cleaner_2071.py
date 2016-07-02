# Extracts name and gender field from 2071 data.

filename = 'ioe_entrance_result_2071.csv'
with open(filename) as file:
    data = file.readlines()

data = data[1:]  # Skip the header

with open('starting.csv', 'w') as newfile:
    for d in data:
        fields = d.split(',')
        name = fields[2].lower()
        gender = fields[3].lower()
        output_format = "{},{}\n".format(name, gender)
        newfile.write(output_format)
