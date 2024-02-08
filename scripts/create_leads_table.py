import os
import boto3


region_name = os.environ.get('AWS_REGION')
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
    )

TABLE_NAME = 'poc-leads'

# Criação da tabela
table = dynamodb.create_table(
    TableName=TABLE_NAME,
    KeySchema=[
        {
            'AttributeName': 'LeadId',  # Chave primária
            'KeyType': 'HASH'  # Partição
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'LeadId',  # Chave primária
            'AttributeType': 'S'  # Tipo de atributo: String
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Espera até que a tabela seja criada
table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)

# Insere os dados na tabela
with table.batch_writer() as batch:
    for i in range(1, 101):
        batch.put_item(
            Item={
                'LeadId': f'lead{i}',
                'NomeCompleto': f'Nome {i}',
                'Email': f'email{i}@example.com',
                'NumeroTelefone': f'+55 11 1234-567{i}',
            }
        )

print("Dados inseridos com sucesso!")
