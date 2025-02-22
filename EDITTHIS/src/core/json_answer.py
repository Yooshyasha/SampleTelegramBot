"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

import aiofiles
import json

from typing import Optional


class JsonAnswer:
    @staticmethod
    async def get(*tree: str) -> Optional[str]:
        try:
            async with aiofiles.open("data/answers.json", encoding="utf-8") as file:
                data = json.loads(await file.read())
                for name in tree:
                    data = data.get(name)
                    if data is None:
                        return None
                if isinstance(data, str):
                    return data
        except (FileNotFoundError, json.JSONDecodeError):
            return None
        return None

class SuppleJsonAnswer(JsonAnswer):
    @staticmethod
    async def get(*tree: str) -> str:
        return super().get(*tree) or str(tree)