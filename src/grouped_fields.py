from .core import FieldModel
from pydantic import Field
from typing import Optional, List, Any

class FieldGroup(FieldModel):
    type: str = Field(default = "field-group")
    title: Optional[str] = None
    fields: List[Any]
    columns: Optional[int] = None

class FieldGrid(FieldModel):
    type: str = Field(default = "field-grid")
    title: Optional[str] = None
    columns: List[Any]

class WoundPlotter(FieldModel):
    type: str = Field(default = "wound-plotter")
    title: Optional[str] = None
    columns: List[FieldModel]