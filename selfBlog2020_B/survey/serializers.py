from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler
from django.contrib.auth.hashers import make_password, check_password
from . import models


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = models.UserProfile
        fields = ['id', 'username', 'password', 'notClassName']

        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'id': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        password_obj = models.UserProfile.objects.filter(username=self.initial_data.get('username')).first()
        if password_obj is None:
            raise ValidationError('账号或密码错误')
        else:
            payload = jwt_payload_handler(password_obj)
            token = jwt_encode_handler(payload)
            password = self.initial_data.get('password')
            self.token = token
            self.classname = password_obj.notClassName
            self.id = password_obj.id
            if check_password(password, password_obj.password):
                return attrs
            else:
                raise ValidationError('未知错误！！')


class RegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['username', 'password']

        extra_kwargs = {
            'username': {
                'min_length': 5,
                'validators': [UniqueValidator(
                    queryset=models.UserProfile.objects.all(),
                    message='用户已存在')],
                'error_messages': {
                    'min_length': '至少5个文字'
                }
            },
            'password': {
                'write_only': True,
            }
        }

    def validate(self, attrs):
        password_origin = attrs.get('password')
        password = make_password(password_origin)
        attrs['password'] = password
        return attrs


class QuestionsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = ['id', 'question', 'questionType', 'Questionnaire', 'question_type', 'questionnaire']

        extra_kwargs = {
            'question': {
                'validators': [UniqueValidator(
                    queryset=models.Questions.objects.all(),
                    message='问题已存在')],
            },
            'question_type': {
                'write_only': True
            },
            'questionnaire': {
                'write_only': True
            }
        }


class QuestionnaireModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questionnaire

        fields = ['id', 'title', 'className', 'Create_user', 'create_user', 'Written_person', 'Question', 'Options']

        extra_kwargs = {
            'title': {
                'validators': [UniqueValidator(
                    queryset=models.Questionnaire.objects.all(),
                    message='问卷已存在')],
            },
            'create_user': {
                'write_only': True
            }
        }


class ClassListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassList
        fields = ['id', 'className']


class AnswerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ['id', 'Student', 'Question', 'Option', 'val', 'content', 'student', 'question', 'option']
        # depth = 1

        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'student': {
                'write_only': True
                # 'source':'student'
            },
            'question': {
                # 'write_only': True
            },

        }


class OptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = ['id', 'name', 'score', 'question', 'Question']

        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'Question': {
                'read_only': True
            },
            'question': {
                'write_only': True
            },

        }


class OptionSelectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = ['id', 'name', 'score', 'question']

        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'name': {
                'read_only': True
            },
            'score': {
                'read_only': True
            },
            'question': {
                'write_only': True
            },

        }


class Image(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
