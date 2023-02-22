import requests
import os
import datetime as dt

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_MAIN = 'https://pixe.la/v1/users/'
PIXELA_USERNAME = 'phucnb'
PIXELA_GRAPH = '/graphs/reading'
# user_creation = {
#     'token' : '*',
#     'username' : 'phucnb',
#     'agreeTermsOfService' : 'yes',
#     'notMinor' : 'yes'
# }

# pixela_graph_creation = {
#     'id' : 'reading',
#     'name' : 'Daily Reading',
#     'unit' : 'Page(s)',
#     'type' : 'int',
#     'color' : 'sora'
# }
pixel_graph_post = {
    'date' : dt.datetime.now().strftime('%Y%m%d'),
    'quantity' : '10',
}
pixela_update_graph = {
    'unit' : 'Page'
}
pixela_header = {
    'X-USER-TOKEN' : PIXELA_TOKEN
}

graph_response = requests.put(url=PIXELA_MAIN+PIXELA_USERNAME+PIXELA_GRAPH, json=pixela_update_graph, headers=pixela_header)
print(graph_response.text)
graph_response.raise_for_status()