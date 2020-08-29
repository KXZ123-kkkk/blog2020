from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    '''基类表'''
    is_delete = models.BooleanField(verbose_name="是否删除", default=False)
    created_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now)

    class Meta:
        abstract = True


CHOICE_CHARACTER = (
    (1, '学生'),
    (2, '工作人员')
)


class UserProfile(AbstractUser, BaseModel):
    '''用户表'''
    character = models.IntegerField(verbose_name='角色', choices=CHOICE_CHARACTER, default=1)
    username = models.CharField(max_length=32, verbose_name="学生账号", unique=True)
    password = models.CharField(max_length=628, verbose_name="学生密码")
    cls = models.OneToOneField(to="ClassList", verbose_name="所属班级", on_delete=models.CASCADE, db_constraint=False,
                               null=True, blank=True)

    @property
    def notClassName(self):
        return '没有班级'

    @property
    def className(self):
        return self.cls.className

    def __str__(self):
        return "{}--{}".format(self.username, self.get_character_display())

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


class ClassList(BaseModel):
    '''班级表'''
    className = models.CharField(max_length=32, verbose_name="班级名")

    def __str__(self):
        return self.className

    class Meta:
        verbose_name = "班级表"
        verbose_name_plural = verbose_name


class Questionnaire(BaseModel):
    '''问卷表'''
    title = models.CharField(max_length=32, verbose_name="问卷名")
    cls = models.ForeignKey(to="ClassList", verbose_name="问卷班级", on_delete=models.CASCADE, db_constraint=False,
                            null=True, blank=True)
    create_user = models.ForeignKey(to="UserProfile", verbose_name="创建问卷的用户", on_delete=models.CASCADE,
                                    db_constraint=False)

    @property
    def className(self):
        return self.cls.className

    @property
    def Create_user(self):
        return self.create_user.username

    @property
    def Written_person(self):
        id_list = []
        stu_list = []
        stu_id_list = []
        for i in Questions.objects.filter(questionnaire=self.id).values('id'):
            id = i.get('id')
            id_list.append(id)
        for i in id_list:
            ls = Answer.objects.filter(question=i).values('student_id')
            stu_list.append(ls)
        for i in stu_list:
            for k in i:
                id = k.get('student_id')
                stu_id_list.append(id)
        return list(set(stu_id_list))

    @property
    def Question(self):
        return Questions.objects.filter(is_delete=False, questionnaire=self.id).values('question')

    @property
    def Options(self):
        all_que = Questions.objects.filter(is_delete=False, questionnaire=self.id)
        all_que_list = []
        for i in all_que:
            one_que = Option.objects.filter(is_delete=False, question=i.id)
            if one_que is None:
                continue
            all_que_list.append(one_que.values('name'))
        return all_que_list

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "问卷表"
        verbose_name_plural = verbose_name


class Questions(BaseModel):
    '''问卷问题表'''
    question = models.CharField(max_length=32, verbose_name="问题题目")
    type_choices = (
        (1, "打分"),
        (2, "单选"),
        (3, "评价")
    )
    question_type = models.IntegerField(choices=type_choices, verbose_name="问题类型", default=2)
    questionnaire = models.ManyToManyField(to="Questionnaire", verbose_name="所属问卷", blank=True)

    def __str__(self):
        return self.question

    @property
    def questionType(self):
        return self.get_question_type_display()

    @property
    def Questionnaire(self):
        return self.questionnaire.values('title')

    class Meta:
        verbose_name = "问卷问题表"
        verbose_name_plural = verbose_name


class Answer(BaseModel):
    '''问卷回答表'''  # 谁什么时候对那个问题作答了
    student = models.ForeignKey(to="UserProfile", verbose_name="所属学生", on_delete=models.CASCADE, db_constraint=False)
    question = models.ForeignKey(to="Questions", verbose_name="所属问题", on_delete=models.CASCADE, db_constraint=False)
    option = models.ForeignKey(verbose_name="单选选项", to="Option", null=True, blank=True, on_delete=models.CASCADE,
                               db_constraint=False)
    val = models.IntegerField(null=True, blank=True, verbose_name="数字答案")
    content = models.CharField(max_length=255, null=True, blank=True, verbose_name="文本答案")

    def __str__(self):
        return str(self.student.username) + "--{}".format(self.question)

    @property
    def Student(self):
        return self.student.username

    @property
    def Question(self):
        return self.question.question

    @property
    def Option(self):
        return {'name': self.option.name, 'score': self.option.score}

    class Meta:
        verbose_name = "问卷回答表"
        verbose_name_plural = verbose_name


class Option(BaseModel):
    '''问卷单选题的选项表'''
    name = models.CharField(max_length=32, verbose_name="选项名")
    score = models.IntegerField(verbose_name="选项对应的分值")
    question = models.ForeignKey(to="Questions", verbose_name="所属问题", on_delete=models.CASCADE, db_constraint=False)

    @property
    def Question(self):
        return self.question.question

    def __str__(self):
        return "单选--" + str(self.score) + "分--{}".format(self.question) + '选择的答案：{}'.format(self.name)

    class Meta:
        verbose_name = "问卷单选题的选项表"
        verbose_name_plural = verbose_name


class Image(models.Model):
    img = models.ImageField(verbose_name='图片', upload_to='img/%Y/%m/%d/', default='img/default.jpg')
