class LeadController:
    def __init__(self, lead_service):
        self.lead_service = lead_service

    def create_lead(self, lead):
        return self.lead_service.create_lead(lead)

    def get_lead(self, lead_id):
        return self.lead_service.get_lead(lead_id)

    def update_lead(self, lead_id, lead):
        return self.lead_service.update_lead(lead_id, lead)

    def delete_lead(self, lead_id):
        return self.lead_service.delete_lead(lead_id)

    def get_leads(self):
        return self.lead_service.get_leads()
