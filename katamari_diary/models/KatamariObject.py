import dataclasses
from dataclasses import dataclass

from katamari_diary.models.Size import Size


@dataclass
class KatamariObject:
    name: str
    size: Size
    category: str
    location: str
    size_to_roll: str
    description: str

    def as_dict(self) -> dict[str, str]:
        d = dataclasses.asdict(self)
        d["size"] = d["size"].name
        return d
