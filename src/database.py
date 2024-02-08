from typing import List
from lead import Lead


class Database:
    def save(self, lead: Lead) -> None:
        pass

    def find_by_id(self, lead_id: int) -> Lead:
        pass

    def find_by_email(self, email: str) -> Lead:
        pass

    def find_all(self) -> List[Lead]:
        pass

    def update(self, lead: Lead) -> None:
        pass

    def delete(self, lead: Lead) -> None:
        pass
