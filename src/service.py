class LeadService:
    def __init__(self, lead_repository):
        self.lead_repository = lead_repository

    def create_lead(self, lead):
        return self.lead_repository.create_lead(lead)

    def get_lead(self, lead_id):
        return self.lead_repository.get_lead(lead_id)

    def get_all_leads(self):
        return self.lead_repository.get_all_leads()

    def update_lead(self, lead_id, lead):
        return self.lead_repository.update_lead(lead_id, lead)

    def delete_lead(self, lead_id):
        return self.lead_repository.delete_lead(lead_id)
