import json
import os 

# get current directory 
dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path += '/data.json'
# creating some fake data
data = {}
data['people'] = {
    'name': 'EC',
    'course': 'Comp160',
    'student_id' : '123456'
}

# write to a json file
with open(dir_path, 'w') as outfile:
    json.dump(data, outfile)


# oepn a local json file
f = open(dir_path)
data = json.load(f)
f.close()
print(data['people'])

# add filed
data["people2"] = {
    'name': 'somebody',
    'course': 'Comp170',
    'student_id' : '111111'
}

# write back
with open(dir_path, 'w') as outfile:
    json.dump(data, outfile)

