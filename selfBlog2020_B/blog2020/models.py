from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    is_delete = models.BooleanField(verbose_name='删除', default=False)
    created_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    def Create_Time(self):
        return str(self.created_time)[0:10]

    class Meta:
        abstract = True


class Blog(BaseModel):
    title = models.CharField(verbose_name='博客名', max_length=64)
    subTitle = models.CharField(verbose_name='副标题', max_length=64)
    passage = models.ManyToManyField(verbose_name='段落', to='Passage', blank=True)
    tag = models.ManyToManyField(verbose_name='标签', to='Tag', blank=True)
    gitHubUrl = models.CharField(verbose_name='Github网址', max_length=600, null=True, blank=True)
    blogReadPerson = models.IntegerField(verbose_name='阅读人数', default=0)

    def __str__(self):
        return self.title

    def Tag(self):
        return self.tag.values('name')

    def leaveMessageCount(self):
        return LeaveMessage.objects.filter(is_delete=False,owner=self.id).all().count()

    def Passages(self):
        return self.passage.values('title', 'content', 'code', 'imgs__url')

    class Meta:
        verbose_name = '博客表'
        verbose_name_plural = verbose_name


class Tag(BaseModel):
    name = models.CharField(verbose_name='标签', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


class Passage(BaseModel):
    title = models.CharField(verbose_name='段落标题', max_length=64)
    content = models.TextField(verbose_name='段落内容-文字', null=True, blank=True)
    code = models.CharField(verbose_name='代码', max_length=6000, null=True, blank=True)
    imgs = models.ManyToManyField(verbose_name='图片', to='Img', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '段落表'
        verbose_name_plural = verbose_name


class Img(BaseModel):
    url = models.ImageField(verbose_name='图片地址', upload_to='blogImg', null=True, blank=True)

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name = '图片表'
        verbose_name_plural = verbose_name


class Recording(BaseModel):
    name = models.CharField(verbose_name='名称', max_length=64, default='WebRecording')
    websiteReadPerson = models.IntegerField(default=0)

    def __str__(self):
        return '{}=>{}'.format(self.name, str(self.websiteReadPerson))

    class Meta:
        verbose_name = '浏览记录表'
        verbose_name_plural = verbose_name


def RandomHeadingImg():
    import random
    num = random.randint(0, 10)
    return 'headingImg/default{}.png'.format(str(num))


class LeaveMessage(BaseModel):
    owner = models.IntegerField(verbose_name='属于', default=1)
    headingImg = models.ImageField(verbose_name='留言头像', upload_to='headingImg', default=RandomHeadingImg)
    content = models.TextField(verbose_name='留言内容')
    nickName = models.CharField(verbose_name='昵称', max_length=64)
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)
    city = models.CharField(verbose_name='城市', max_length=64, null=True, blank=True)

    def __str__(self):
        return '{}=>{}'.format(self.nickName, self.content)

    class Meta:
        verbose_name = '留言表'
        verbose_name_plural = verbose_name


class ReplyMessage(BaseModel):
    owner = models.IntegerField(verbose_name='属于', default=1)
    headingImg = models.ImageField(verbose_name='留言头像', upload_to='headingImg', default=RandomHeadingImg)
    leave = models.ForeignKey(verbose_name='留言', on_delete=models.CASCADE, to='LeaveMessage')
    replyName = models.CharField(verbose_name='回复者', max_length=64)
    content = models.TextField(verbose_name='留言内容')
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)
    city = models.CharField(verbose_name='城市', max_length=64, null=True, blank=True)

    def __str__(self):
        return '{}=>{}========{}'.format(self.replyName, self.leave.nickName, self.content)

    class Meta:
        verbose_name = '留言回复表'
        verbose_name_plural = verbose_name


class Music(BaseModel):
    title = models.CharField(verbose_name='音乐名称', max_length=64)
    pic = models.ImageField(verbose_name='留言头像', upload_to='musicImg', default=RandomHeadingImg, null=True, blank=True)
    artist = models.CharField(verbose_name='作者', max_length=128)
    src = models.CharField(verbose_name='音乐链接', max_length=600)
    lrc = models.CharField(verbose_name='歌词', max_length=624, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '音乐表'
        verbose_name_plural = verbose_name


CHOICE = (('advice', '推荐'), ('like', '喜欢'))


class Cartoon(BaseModel):
    kind = models.CharField(verbose_name='属于', max_length=12, default='advice', choices=CHOICE)
    videoImg = models.ImageField(verbose_name='动漫图片', upload_to='videoImg', null=True, blank=True)
    mainName = models.CharField(verbose_name='动漫名称', max_length=64)
    simpleIntroduce = models.TextField(verbose_name='动漫简介')
    totalNum = models.IntegerField(verbose_name='集数', default=12)
    videoInfo = models.ManyToManyField(verbose_name='视频URL', to='Video')

    def __str__(self):
        return self.mainName

    class Meta:
        verbose_name = '动漫表'
        verbose_name_plural = verbose_name


class Video(BaseModel):
    subName = models.CharField(verbose_name='该集名称', max_length=64)
    url = models.CharField(verbose_name='视频链接', max_length=600)

    def __str__(self):
        return '{}=>{}'.format(self.subName, self.cartoon_set.values_list('mainName'))

    class Meta:
        verbose_name = '动漫表-单集'
        verbose_name_plural = verbose_name
