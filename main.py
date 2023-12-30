from src.myminixform import *

print(template, file=open("Template.yaml","a",encoding="utf-8"))
form=yaml_form("Template.yaml","utf-8")
form.to_xslform("form.xlsx")