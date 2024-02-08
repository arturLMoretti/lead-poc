from database import Database
from botocore.exceptions import ClientError

from lead import Lead


class Dynamo(Database):
    def __init__(self, table_name, connection) -> None:
        self.table_name = table_name
        self.connection = connection
        self.table = self.connection.Table(self.table_name)

    def find_by_id(self, lead_id: int):
        try:
            response = self.table.get_item(
                Key={
                    'LeadId': lead_id
                }
            )
            item = response['Item']
            return item
        except ClientError as e:
            print(e)
            return None

    def find_by_email(self, email: str):
        try:
            response = self.table.scan(
                FilterExpression='Email = :email',
                ExpressionAttributeValues={
                    ':email': email
                }
            )
            items = response['Items']
            return items
        except ClientError as e:
            print(e)
            return None

    def find_all(self):
        try:
            response = self.table.scan()
            items = response['Items']
            return items
        except ClientError as e:
            print(e)
            return None

    def save(self, lead: Lead):
        self.table.put_item(
            Item={
                'LeadId': lead.lead_id,
                'NomeCompleto': lead.full_name,
                'Email': lead.email,
                'NumeroTelefone': lead.phone,
                'Cpf': lead.cpf
            }
        )

    def update(self, lead):
        self.table.update_item(
            Key={
                'LeadId': lead.lead_id
            },
            UpdateExpression='SET NomeCompleto = :full_name, Email = :email, NumeroTelefone = :telefone_number, Cpf = :cpf',
            ExpressionAttributeValues={
                ':full_name': lead.full_name,
                ':email': lead.email,
                ':telefone_number': lead.telefone_number,
                ':cpf': lead.cpf
            }
        )

    def delete(self, lead):
        self.table.delete_item(
            Key={
                'LeadId': lead.lead_id
            }
        )
