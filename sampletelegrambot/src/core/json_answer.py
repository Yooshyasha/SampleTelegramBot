import aiofiles
import json

from typing import Optional


class JsonAnswer:
    @staticmethod
    async def get(*tree: str) -> Optional[str]:
        try:
            async with aiofiles.open("data/answers.json") as file:
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
