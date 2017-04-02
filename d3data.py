import requests
import json
r = requests.get('https://api.github.com/repos/d3/d3')
if(r.ok):
    repoItem = json.loads(r.text or r.content)
    print "Django repository created: " + repoItem['created_at']