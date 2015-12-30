from io import BytesIO
from PIL import Image
import boto3

s3 = boto3.resource('s3')
img = Image.open(s3.Object('acessodoutorupload', 'eu.jpeg').get()['Body'])
outbuffer = BytesIO()
img.rotate(45).save(outbuffer,format="jpeg")
s3.Object('acessodoutorupload', 'eu_rotate.jpeg').put(Body=outbuffer.getvalue())
