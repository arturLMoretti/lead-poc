import boto3

dynamodb = boto3.client('dynamodb')

for i in range(10):
    dynamodb.put_item(
          TableName='poc-leads',
          Item={
              'LeadId': {'S': f'lead{i}'},
              'NomeCompleto': {'S': f'Nome {i}'},
              'Email': {'S': f'email{i}@example.com'},
              'NumeroTelefone': {'S': f'+55 11 1234-567{i}'},
            }
        )
