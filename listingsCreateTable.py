from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', aws_access_key_id='##YourKeyHere##', aws_secret_access_key='##YourKeyHere##', region_name='us-west-2')
# PRICING! https://aws.amazon.com/dynamodb/pricing/
# Tutorial: http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html

table = dynamodb.create_table(
    TableName='Listings',
    KeySchema=[ # http://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#DynamoDB.Client.create_table
    # https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/
    # http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GuidelinesForTables.html
        {
            'AttributeName': 'URL',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'query',
            'KeyType': 'RANGE'  #Sort key
        }
    ], # http://boto3.readthedocs.io/en/latest/reference/customizations/dynamodb.html not a lot of data types, one for date in Java but not python. Not even a floa
    AttributeDefinitions=[ #number of attribs has to match between key schema and attrib defs. kept these just in case schema needs adjusting
        {
            'AttributeName': 'URL',
            'AttributeType': 'S'
        },
        # {
        #     'AttributeName': 'category',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'condition',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'country',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'currency',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'endTime',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'price',
        #     'AttributeType': 'N' #might work for decimals
        # },
        {
            'AttributeName': 'query',
            'AttributeType': 'S'
        }# ,
        # {
        #     'AttributeName': 'shipsTo',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'title',
        #     'AttributeType': 'S'
        # },


    ], # http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ProvisionedThroughput.html I doubt we need 10
    # 1 read per sec for a 4kb item 1 write per sec for 1kb
    # about 25 for both for free package
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
