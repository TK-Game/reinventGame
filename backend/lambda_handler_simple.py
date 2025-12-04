import json
import boto3
import os
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE', 'Events')
table = dynamodb.Table(table_name)

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def handler(event, context):
    try:
        http_method = event.get('httpMethod', event.get('requestContext', {}).get('http', {}).get('method', 'GET'))
        path = event.get('path', event.get('rawPath', '/'))
        body = event.get('body')
        
        # CORS headers
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*'
        }
        
        # Handle OPTIONS for CORS
        if http_method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'OK'})
            }
        
        # Root endpoint
        if path == '/' and http_method == 'GET':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Event Management API'})
            }
        
        # Health endpoint
        if path == '/health' and http_method == 'GET':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'status': 'healthy'})
            }
        
        # List events
        if path == '/events' and http_method == 'GET':
            response = table.scan()
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'events': response.get('Items', [])}, cls=DecimalEncoder)
            }
        
        # Create event
        if path == '/events' and http_method == 'POST':
            if not body:
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({'error': 'Request body is required'})
                }
            
            event_data = json.loads(body) if isinstance(body, str) else body
            event_id = str(uuid.uuid4())
            event_data['eventId'] = event_id
            
            # Validate required fields
            required_fields = ['title', 'descriptions', 'date', 'location', 'capacity', 'organizer', 'status']
            for field in required_fields:
                if field not in event_data:
                    return {
                        'statusCode': 400,
                        'headers': headers,
                        'body': json.dumps({'error': f'Missing required field: {field}'})
                    }
            
            table.put_item(Item=event_data)
            return {
                'statusCode': 201,
                'headers': headers,
                'body': json.dumps(event_data, cls=DecimalEncoder)
            }
        
        # Get single event
        if path.startswith('/events/') and http_method == 'GET':
            event_id = path.split('/')[-1]
            response = table.get_item(Key={'eventId': event_id})
            if 'Item' not in response:
                return {
                    'statusCode': 404,
                    'headers': headers,
                    'body': json.dumps({'error': 'Event not found'})
                }
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(response['Item'], cls=DecimalEncoder)
            }
        
        # Update event
        if path.startswith('/events/') and http_method == 'PUT':
            event_id = path.split('/')[-1]
            if not body:
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({'error': 'Request body is required'})
                }
            
            # Check if event exists
            response = table.get_item(Key={'eventId': event_id})
            if 'Item' not in response:
                return {
                    'statusCode': 404,
                    'headers': headers,
                    'body': json.dumps({'error': 'Event not found'})
                }
            
            update_data = json.loads(body) if isinstance(body, str) else body
            update_data = {k: v for k, v in update_data.items() if v is not None and k != 'eventId'}
            
            if not update_data:
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({'error': 'No fields to update'})
                }
            
            update_expression = "SET " + ", ".join([f"#{k} = :{k}" for k in update_data.keys()])
            expression_attribute_names = {f"#{k}": k for k in update_data.keys()}
            expression_attribute_values = {f":{k}": v for k, v in update_data.items()}
            
            response = table.update_item(
                Key={'eventId': event_id},
                UpdateExpression=update_expression,
                ExpressionAttributeNames=expression_attribute_names,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="ALL_NEW"
            )
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(response['Attributes'], cls=DecimalEncoder)
            }
        
        # Delete event
        if path.startswith('/events/') and http_method == 'DELETE':
            event_id = path.split('/')[-1]
            # Check if event exists
            response = table.get_item(Key={'eventId': event_id})
            if 'Item' not in response:
                return {
                    'statusCode': 404,
                    'headers': headers,
                    'body': json.dumps({'error': 'Event not found'})
                }
            
            table.delete_item(Key={'eventId': event_id})
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Event deleted successfully'})
            }
        
        # Not found
        return {
            'statusCode': 404,
            'headers': headers,
            'body': json.dumps({'error': 'Not found'})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
