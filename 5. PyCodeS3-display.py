# S3 images to Display thru Py
import boto3
  
from botocore.client import Config

from django.http import HttpResponse
  
ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXXX'
  
ACCESS_SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  
BUCKET_NAME = 'XXXXXXXX'

def s3bucket_getfile(file_path):
  
    s3 =  boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY)
  
    obj  = s3.Object(BUCKET_NAME,file_path)
  
    try:
  
        file_stream = obj.get()['Body'].read()
  
        if "pdf" in file_path:
            response = HttpResponse(file_stream, content_type='application/pdf')
  
        if "jpg" in file_path:
            response = HttpResponse(file_stream,content_type="image/jpeg")
  
        if "jpeg" in file_path:
            response = HttpResponse(file_stream,content_type="image/jpeg")
  
        response['Content-Disposition'] = 'filename=%s' %  file_path
  
        return response
    except:
        return False
  
s3bucket_getfile(file_path)
