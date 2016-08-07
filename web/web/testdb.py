# -*- coding: utf-8 -*-

from django.http import HttpResponse

from ArticleModel.models import Article

# 数据库操作
def insertdb(request):
	article = Article(title='title',author='author')
	article.save()
	return HttpResponse("<p>数据添加成功！</p>")


def querydb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Article.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Article.objects.filter(id=1)

    # 获取单个对象
    response3 = Article.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Article.objects.order_by('title')[0:2]

    # 数据排序
    Article.objects.order_by("title")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")