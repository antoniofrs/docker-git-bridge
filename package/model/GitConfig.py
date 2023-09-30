from dataclasses import dataclass

@dataclass
class GitConfig:
    url: str
    username: str
    password: str
    branch: str

