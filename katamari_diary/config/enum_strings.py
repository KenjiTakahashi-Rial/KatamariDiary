import os
from typing import Any

from katamari_diary.models.katamari_object_pb2 import (
    Category,
    CategoryString,
    LocalizedString,
    Location,
    LocationString,
    Size,
    SizeString,
)

CATEGORY_STRING_MAP: dict[Category, LocalizedString] = {}
LOCATION_STRING_MAP: dict[Location, LocalizedString] = {}
SIZE_STRING_MAP: dict[Size, LocalizedString] = {}

ENUMS_PATH = os.path.join(".", "enums")

OPEN_MODE = "rb"


def load_enum_strings() -> None:
    enums: dict[Any, tuple[Any, dict[Any, Any]]] = {
        Category: (CategoryString(), CATEGORY_STRING_MAP),
        Location: (LocationString(), LOCATION_STRING_MAP),
        Size: (SizeString(), SIZE_STRING_MAP),
    }
    for enum, (enum_str, str_map) in enums.items():
        dir_path = os.path.join(ENUMS_PATH, enum.DESCRIPTOR.name)
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            if not os.path.isfile(item_path):
                continue

            with open(item_path, OPEN_MODE) as f:
                enum_str.ParseFromString(f.read())
                str_map[enum_str.value] = enum_str.string


load_enum_strings()
