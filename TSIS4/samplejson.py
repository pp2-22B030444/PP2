import json

with open('sampledata.json') as file:
    data = json.load(file)

header = "Interface Status\n" + "=" * 80 + "\n"
header += "{:<50}{:<25}{:<8}{}\n".format("DN", "Description", "Speed", "MTU")
header += "-" * 80 + "\n"

body = ""
for interface in data["data"]:
    body += "{:<50}{:<25}{:<8}{}\n".format(interface["DN"], interface["Description"], interface["Speed"],interface["MTU"])

print(header + body)