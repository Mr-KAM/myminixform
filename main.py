from src.myminixform import *
#from rich import print
#print(template, file=open("Template.yaml","w",encoding="utf-8"))
form=yaml_form("Template.yaml","utf-8")
form.to_xslform("form.xlsx")