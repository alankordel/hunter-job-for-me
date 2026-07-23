from abc import ABC, abstractmethod
from src.models.job import Job

class JobSource(ABC):
    @abstractmethod
    def get_jobs(self) -> list[Job]:
        """Retorna uma lista de vagas"""
        
        pass