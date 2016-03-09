from settings import *

DEBUG = False
ALLOWED_HOSTS = ['ec2-52-33-184-246.us-west-2.compute.amazonaws.com', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')