# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "心作乱象"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "可视化"
email = "keshihua@souletter.com"
author_homepage = "https://www.souletter.cn"
description = "视，听与文字。"
key_words = ['Maverick', '作品集', 'work', '心作乱象']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "心作乱象",
        "url": "https://www.souletter.com",
        "brief": "可视化的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Bililibili",
        "url": "https://space.bilibili.com/19404630",
        "icon": "gi gi-bili"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5994929791",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
