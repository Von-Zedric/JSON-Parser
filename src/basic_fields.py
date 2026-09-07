from .core import FieldModel
from pydantic import Field
from typing import Optional

class MarkDown(FieldModel):
    type: str = Field(default = "markdown")
    template: str

class Text(FieldModel):
    type: str = Field(default = "text")
    label: str

class TextArea(FieldModel):
    type: str = Field(default = "textarea")
    label: str

class CheckBox(FieldModel):
    type: str = Field(default = "checkbox")
    label: str

class Date(FieldModel):
    type: str = Field(default = "date")
    label: str

class Time(FieldModel):
    type: str = Field(default = "time")
    label: str

class Number(FieldModel):
    type: str = Field(default = "number")
    label: str
    min: Optional[int] = None

class Signature(FieldModel):
    type: str = Field(default = "signature")
    message: str

class Template(FieldModel):
    type: str = Field(default = "template")
    multiple: bool
    allowDuplicates: bool

class LookUp(FieldModel):
    type: str = Field(default = "lookup")
    label: str
    provider: str
    #provider can be any of the ff
    #rvs-codes, diagnosis-codes, physicians, icd/diag

class Action(FieldModel):
    type: str = Field(default = "action")
    label: str
    action: str
    #action can be any of the ff
    #preview:phic/hemodialysis

class Integration(FieldModel):
    type: str = Field(default = "integration")
    provider: str
    #provider can be any of the ff
    #dosespot/prescription, philhealth-check, philhealth-check-mca, philhealth-ymca
    #phic/konsulta/diagnostics, phic/konsulta/prescriptions