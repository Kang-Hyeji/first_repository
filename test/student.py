import json
student_data={
  "students": [
    {
     "name":"강혜지",
     "age":"24",
     "job":"student",
     "id":"hj",
     "pw":"1234"
    },
    {
    "name":"전지현",
    "age":"26",
    "job":"teacher",
    "id":"jh",
    "pw":"3456"
    }
    
  ]
}
with open("student_file.json","w",encoding="utf-8") as f:
    json.dump(student_data, f,ensure_ascii=False,indent="\t")

with open("student_file.json","r",encoding="utf-8") as f :
    json_data = json.load(f)
print(json.dumps(json_data,ensure_ascii=False,indent="\t"))