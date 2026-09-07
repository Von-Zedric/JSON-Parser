from src import Section
from ref import title, description, fields, tags

forms = Section(title = title, tags = tags, description = description)
forms.fields = fields
form_json = forms.model_dump_json(indent = 4, exclude_none = True, by_alias = True)

try: 
    with open("./out.json", "w") as f:
        s = f.write(form_json)
        print("Write success:", s)
except Exception as e:
    print("Error:", e)