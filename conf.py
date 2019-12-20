# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "https://work.souletter.com/"
source_dir = "../src/"
build_dir = "../dist/"
template = "Galileo"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "souletter/souletter@gh-pages"
}

# 站点设置
site_name = "心作乱象"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-07-13T09:04+08:00"
author = "可视化"
email = "keshihua@souletter.com"
author_homepage = "https://www.souletter.cn"
description = "视，听与文字。"
key_words = ['Maverick', '作品集', 'work', '心作乱象']
language = 'zh-CN'
background_img = '${static_prefix}58103072_p0.jpg'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "maverick."
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
        "name": "Bilibili",
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
<link rel="shortcut icon" href="${static_prefix}logo.ico?v=yyLyaqbyRG" />
'''






footer_addon = ''

body_addon = ''
