import jwt
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_jwt.settings import api_settings

jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class JWTAuthentication(BaseJSONWebTokenAuthentication):
    def authenticate(self, request, token=None):
        # 从前端取出token值，放在HTTP_AUTHORIZATION中
        if token:
            jwt_token = token
        else:
            jwt_token = request.META.get('HTTP_AUTHORIZATION')

        if jwt_token is None:
            raise AuthenticationFailed('请登录')

        # 自定义校验规则：auth token jwt
        token = self.parse_jwt_token(jwt_token)

        # if token is None:
        #     raise AuthenticationFailed('请登录')

        try:
            # token => payload
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise AuthenticationFailed('token已过期，请重新登录')
        except:
            raise AuthenticationFailed('非法用户，请登录')
        # payload => user
        user = self.authenticate_credentials(payload)

        return (user, token)  # 获取到登录对象和签发的token

    # 自定义校验规则：auth token jwt，auth为前盐，jwt为后盐
    def parse_jwt_token(self, jwt_token):
        tokens = jwt_token.split()

        if len(tokens) != 2 or tokens[0].lower() != 'jwt':
            return None
        return tokens[1]