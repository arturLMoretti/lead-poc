from typing import List
from database import Database
from lead import Lead


class LeadRepository:
    def __init__(self, db: Database):
        self.db = db

    def find_by_id(self, lead_id: int) -> Lead:
        return self.db.find_by_id(lead_id)

    def find_by_email(self, email: str) -> Lead:
        return self.db.find_by_email(email)

    def find_all(self) -> List[Lead]:
        return self.db.find_all()

    def save(self, lead: Lead) -> None:
        self.db.save(lead)

    def delete(self, lead: Lead) -> None:
        self.db.delete(lead)
