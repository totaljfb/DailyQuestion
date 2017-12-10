# -*- coding: utf-8 -*-

from mongoengine import connect
from mongoengine import Document
from mongoengine import IntField
from mongoengine import StringField
from mongoengine import DateTimeField
from mongoengine import URLField

__author__ = "liuzhijun"

# 连接 mongodb
connect('weixin', host='localhost', port=27017)


class Post(Document):
    """
    文章信息
    """
    title = StringField()  # 文章标题
    content_url = StringField()  # 文章链接
    content = StringField()  # 文章内容
    source_url = StringField()  # 原文链接
    digest = StringField()  # 文章摘要
    cover = URLField()  # 封面图
    c_date = DateTimeField()  # 推送时间
    read_num = IntField(default=0)  # 阅读数
    like_num = IntField(default=0)  # 点赞数
    comment_num = IntField(default=0)  # 评论数
    reward_num = IntField(default=0)  # 赞赏数
    author = StringField()  # 作者


class Account(Document):
    """
    公众号账号信息
    """
    # TODO
    pass


