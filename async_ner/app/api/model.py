# Importing libraries
from pydantic import BaseModel
from typing import Optional, List


# Model for recieveing input
class Input(BaseModel):
    text: str


class Output(BaseModel):
    entities: str
