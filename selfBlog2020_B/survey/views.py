from itertools import chain
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, mixins, GenericViewSet
from rest_framework.response import Response
from utils import autentications

from rest_framework.filters import SearchFilter
from . import serializers, models


class TestListAPIView(ListAPIView):
    authentication_classes = [autentications.JWTAuthentication]

    def list(self, request, *args, **kwargs):
        return Response({})


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        ser_data = serializers.RegisterModelSerializer(data=data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        return Response({'status': '0', 'msg': 'register ok'})


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        ser_data = serializers.LoginSerializer(data=data)
        ser_data.is_valid(raise_exception=True)
        return Response({'status': '0', 'token': ser_data.token,
                         'results': {'id': ser_data.id, 'name': data.get('username'),
                                     'className': ser_data.classname}})


class QuestionsView(ModelViewSet):
    authentication_classes = [autentications.JWTAuthentication]
    serializer_class = serializers.QuestionsModelSerializer
    queryset = models.Questions.objects.filter(is_delete=False).all()

    def update(self, request, *args, **kwargs):
        updata_list = []
        quetions = request.data.get('quetions')
        for i in quetions:
            query_set = models.Questions.objects.filter(is_delete=False, id=i)
            instance = models.Questions.objects.filter(is_delete=False, id=i).first()
            questionnaire_list = []
            for i in range(query_set.count()):
                ll = query_set[i].questionnaire.all().values('id')
                for k in range(ll.count()):
                    pk = ll[k].get('id')
                    questionnaire_list.append(pk)
            questionnaire_list = chain(questionnaire_list + [request.data.get('quetionaire')])
            questionnaire = {'questionnaire': questionnaire_list}
            if not instance:
                return Response({
                    'status': 1,
                    'msg': '数据出现错误！'
                })
            serializer = self.get_serializer(instance, data=questionnaire, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            updata_list.append(serializer.data)
        #
        # if getattr(instance, '_prefetched_objects_cache', None):
        #     # If 'prefetch_related' has been applied to a queryset, we need to
        #     # forcibly invalidate the prefetch cache on the instance.
        #     instance._prefetched_objects_cache = {}

        return Response({
            'status': 0,
            'msg': 'ok',
            'results': updata_list
        })

    def list(self, request, *args, **kwargs):
        questionnaire_id = request.query_params.get('id')
        que = models.Questions.objects.filter(questionnaire=questionnaire_id)
        serializer = self.get_serializer(que, many=True)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': serializer.data
        })

    def create(self, request, *args, **kwargs):
        data = request.data.get('data')
        data['questionnaire'] = list(data['questionnaire'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 0, 'msg': '创建成功'})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'status': 1, 'msg': '请选择删除问题'})

        delete_obj = models.Questions.objects.filter(is_delete=False, id=pk).first()
        if not delete_obj:
            return Response({'status': 1, 'msg': '不存在该问题'})
        delete_obj.is_delete = True
        delete_obj.save()
        return Response({'status': 0, 'msg': '删除成功'})


class QuestionnaireListAPIView(ModelViewSet):
    authentication_classes = [autentications.JWTAuthentication]
    serializer_class = serializers.QuestionnaireModelSerializer
    queryset = models.Questionnaire.objects.filter(is_delete=False).all()

    def list(self, request, *args, **kwargs):
        questionnaire = models.Questionnaire.objects.filter(is_delete=False, create_user=request.user)
        serializer = self.get_serializer(questionnaire, many=True)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'status': 1, 'msg': '请选择删除问卷'})

        delete_obj = models.Questionnaire.objects.filter(is_delete=False, id=pk).first()
        if not delete_obj:
            return Response({'status': 1, 'msg': '不存在该问卷'})
        delete_obj.is_delete = True
        delete_obj.save()
        return Response({'status': 0, 'msg': '删除成功'})


class ClassListListAPIView(ListAPIView):
    authentication_classes = [autentications.JWTAuthentication]
    serializer_class = serializers.ClassListModelSerializer
    queryset = models.ClassList.objects.filter(is_delete=False).all()


class AnswerAPIView(ListAPIView, CreateAPIView):
    authentication_classes = [autentications.JWTAuthentication]
    queryset = models.Answer.objects.filter(is_delete=False).all()
    serializer_class = serializers.AnswerModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 0, 'msg': 'ok', 'results': serializer.data})

    def create(self, request, *args, **kwargs):
        data = request.data.get('data')
        results = []
        for (index, i) in enumerate(data):
            serializer = self.get_serializer(data=i)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            results.append(serializer.data)
        return Response({'status': 0, 'msg': 'ok', 'results': results})


class OptionAPIView(GenericViewSet, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    authentication_classes = [autentications.JWTAuthentication]
    queryset = models.Option.objects.filter(is_delete=False).all()
    serializer_class = serializers.OptionModelSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        opt_obj = models.Option.objects.filter(is_delete=False, name=data.get('name'))
        if opt_obj:
            return Response({'status': 1, 'msg': '已存在该答案！'})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 0, 'msg': 'ok'})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'status': 1, 'msg': '请选择删除答案'})

        delete_obj = models.Option.objects.filter(is_delete=False, id=pk).first()
        if not delete_obj:
            return Response({'status': 1, 'msg': '不存在该答案'})
        delete_obj.is_delete = True
        delete_obj.save()
        return Response({'status': 0, 'msg': '删除成功'})

    def getAnswerList(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = models.Option.objects.filter(is_delete=False, question=pk).all()

        if not queryset:
            return Response({'status': 1, 'msg': '该问题没设置答案'})
        serializer = self.get_serializer(queryset, many=True)
        if not pk:
            return Response({'status': 1, 'msg': '请选择问题'})
        return Response(
            {'status': 0, 'msg': 'ok', 'results': serializer.data})


class ScoreView(APIView):
    serializer_class = serializers.AnswerModelSerializer
    authentication_classes = [autentications.JWTAuthentication]

    def post(self, request, *args, **kwargs):
        ls = []
        questionnaire_id = request.data
        if questionnaire_id is None:
            return Response({'status': 0,
                             'msg': '你还没有参加答卷'})
        user_id = request.user.id
        for i in questionnaire_id:
            score = 0
            score_list = {}
            questionnaire = models.Questionnaire.objects.filter(is_delete=False,id=i).all()
            questionnaire_name = questionnaire[0].title
            questions = models.Questions.objects.filter(is_delete=False, questionnaire=i).all()
            for i in questions:
                one_obj = models.Answer.objects.filter(is_delete=False, student=user_id, question=i.id)
                if not one_obj:
                    continue
                score = score + one_obj[0].option.score
            score_list['title'] = questionnaire_name
            score_list['score'] = score
            ls.append(score_list)
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': ls

        })


class Check(ModelViewSet):

    def OK(self, request, *args, **kwargs):
        username = request.query_params.get('username')
        user = models.UserProfile.objects.filter(is_delete=False, username=username)
        if user:
            return Response({
                'status': 0,
                'msg': 'ok'
            })
        else:
            return Response({
                'status': 10,
                'msg': '请登录'
            })


class allQuestionnaireListAPIView(ListAPIView, CreateAPIView):
    authentication_classes = [autentications.JWTAuthentication]
    queryset = models.Questionnaire.objects.filter(is_delete=False).all()
    serializer_class = serializers.QuestionnaireModelSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status': 0, 'msg': 'ok'})

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 0, 'msg': 'ok', 'results': serializer.data})


class UserQuestionListAPIview(ListAPIView):
    serializer_class = serializers.QuestionsModelSerializer
    authentication_classes = [autentications.JWTAuthentication]

    def list(self, request, *args, **kwargs):
        questions_list = []
        lt = []
        user_id = request.user.id
        questionnaires = models.Questionnaire.objects.filter(is_delete=False, create_user=user_id).all()
        for i in questionnaires:
            questionnaire_id = i.id
            questions = models.Questions.objects.filter(is_delete=False, questionnaire=questionnaire_id)
            questions_list.append(questions)
        for i in questions_list:
            lt = chain(lt, i)
        serializer = self.get_serializer(lt, many=True)
        return Response({'status': 0, 'msg': 'ok', 'results': serializer.data})
