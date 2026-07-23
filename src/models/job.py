from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Job:
    title: str
    url: str
    company: Optional[str] = None
    location: Optional[str] = None
    work_model: Optional[str] = None
    technologies: list[str] = field(default_factory=list)
    source: Optional[str] = None
    published_at: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self) -> None:
        self.title = self.title.strip() if self.title else ""
        self.url = self.url.strip() if self.url else ""

        if not self.title or not self.url:
            raise ValueError("A vaga precisa ter título e URL")
