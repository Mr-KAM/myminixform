from src.myminixform import *
from rich import print
#print(template, file=open("Template.yaml","w",encoding="utf-8"))
form=yaml_form("Template.yaml","utf-8")
form.to_xslform("form.xlsx")
#from src.expression import *

import re

emailfaux = 'a1b2cdefg'
textes="07 87 58 04 85"



print(bool(re.match(regex("PHONE_CI")[0], textes)))

expression1="py::either(OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN, exactly(3, DIGIT)) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)"
expression2="mxf::NAME_MIN"
expression3="^[A-Z]{2}"
print("=========================================================")
print("py expression",eval_contrainte(expression1))
print("mxf expression",eval_contrainte(expression2))
print("Regex expression",eval_contrainte(expression3))
print("Liste des types de question:", list_types() )
