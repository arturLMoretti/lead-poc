import uuid


class Lead:

    def __init__(
        self,
        full_name: str,
        email: str,
        cpf: str,
        phone: str
      ):
        self._lead_id = str(uuid.uuid4())
        self._full_name = full_name
        self._email = email
        self._cpf = cpf
        self._phone = phone

    @property
    def lead_id(self):
        return self._lead_id

    @property
    def full_name(self):
        return self._full_name

    @property
    def email(self):
        return self._email

    @property
    def cpf(self):
        return self._cpf

    @property
    def phone(self):
        return self._phone
