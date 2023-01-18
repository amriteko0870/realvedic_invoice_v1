from apiApp.imports import *
from apiApp.auth.auth_models import *

@api_view(['POST'])
def login(request,format=None):
    data = request.data
    email = data['email']
    password = data['password']
    try:
        user_creds = UserCreds.objects.get(email = email)
    except:
        res = { 
                'status':False,
                'message':'invalid credentials'
              }
        return Response(res)
    if check_password(password,user_creds.password):
        res = {
                'status':True,
                'message':'login success',
                'user_type':user_creds.user_type,
                'token':user_creds.token
              }
        
    return Response(res)
