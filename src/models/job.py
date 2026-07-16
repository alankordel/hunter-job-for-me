from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Job:

    title: str

    company: Optional[str] = None

    location: Optional[str] = None

    work_model: Optional[str] = None

    url: Optional[str] = None

    technologies: Optional[List[str]] = None
    
    def __post_init__(self):

        if not self.title:
            raise ValueError(
                "Job precisa ter um título"
            )