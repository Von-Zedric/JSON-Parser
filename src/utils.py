from pydantic import BaseModel
from .core import KeywordBase, Option, Item
from .basic_fields import *
from typing import Any, List, Tuple

md_fields = [
    Text,
    TextArea,
    CheckBox,
    Date,
    Time,
    Number
]

def populate(field: BaseModel, param_names: Tuple[str], field_args: List[Tuple[Any]]) -> List[Any]:
    out = []
    it_temp = range(len(param_names))
    for field_arg in field_args:
        inp = {}
        for idx in (it_temp):
            param = param_names[idx]
            arg = field_arg[idx]
            if arg is None:
                continue
            inp[param] = arg
        out.append(field(**inp))
    return out

def populate_options(items: Tuple[str | Tuple[str]], is_val_match: bool = True) -> List[Option]:
    if is_val_match:
        return [Option(label = option) for option in items]
    return [Option(label = option[0], name = option[1]) for option in items]

def populate_items(items: Tuple[str | Tuple[str]], is_val_match: bool = True) -> List[Item]:
    if is_val_match:
        return [Item(label = item) for item in items]
    return [Item(label = item[0], name = item[1]) for item in items]

def to_markdown(field: Any) -> MarkDown:
    if not (type(field) in md_fields):
        raise TypeError("This field is not supported for conversion to MarkDown")
    template = "{{" + field.name + "|" + field.label + "|" + field.type + "}}"
    return MarkDown(template = template)