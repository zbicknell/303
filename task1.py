
import json

data = {}
data['students'] = []
data['students'].append({
    'name': 'Zac Bicknell',
    'GitHubID': 'zbicknell',
    'NetID': '819000583'
})

with open('identity.txt', 'w') as outfile:
    json.dump(data, outfile)
