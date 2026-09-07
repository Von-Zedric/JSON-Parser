from .core import FieldModel, Option, Item
from pydantic import Field, model_validator, ConfigDict
from typing import List, Optional

class OptionModel(FieldModel):
    options: List[Option] | List[str]
    non_opt: Optional[Option] = None
    model_config = ConfigDict(extra = "allow")

    @model_validator(mode = "after")
    def check_option_vals(self):
        is_str = type("") == type(self.options[0])
        if is_str:
            new_opts = [
                Option(label = label)
                for label in self.options
            ]
            self.options = new_opts
        return self

class Radio(OptionModel):
    type: str = Field(default = "radio")
    label: str

class DropDown(OptionModel):
    type: str = Field(default = "dropdown")
    label: str

class CheckboxList(OptionModel):
    type: str = Field(default = "checkbox-list")
    label: str

class RadioGrid(OptionModel):
    type: str = Field(default = "radio-grid")
    items: List[Item] | List[str]

    @model_validator(mode = "after")
    def check_item_valss(self):
        is_str = type("") == type(self.items[0])
        if is_str:
            new_its = [
                Item(label = label)
                for label in self.items
            ]
            self.items = new_its
        return self