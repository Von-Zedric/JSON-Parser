from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import List, Optional, Any, Dict, Tuple
from uuid import uuid4

def getID():
    rid = uuid4().hex
    return rid[:9] + "-" + rid[9:13] + "-" + rid[13:17] + "-" + rid[17:21] + "-" + rid[21:]

class Section(BaseModel):
    id: str = Field(default_factory = getID)
    title: str
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    fields: List[Any] = []


class FieldModel(BaseModel):
    id: str = Field(default_factory = getID)
    name: Optional[str] = None
    type: str
    required: Optional[bool] = None
    columnSpan: Optional[int] = None
    tags: Optional[List[str]] = None
    model_config = ConfigDict(extra = "allow")

class KeywordBase(BaseModel):
    key: str
    value: Optional[str | int] = None
    model_config = ConfigDict(extra = "allow")

    @model_validator(mode = "after")
    def check_field_values(self):
        if self.value is None:
            self.value = self.key.strip().lower().replace(" ", "-")
        return self

class Option(KeywordBase):
    key: str = Field(alias = "label")

class Item(KeywordBase):
    key: str = Field(alias = "label")
    value: Optional[str | int] = Field(alias = "name")