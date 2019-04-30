# -*- coding: utf-8 -*-
import emails
import codecs
import time


message = emails.Message(html=codecs.open('mailcontent.html',encoding='utf8'),
                         subject=time.strftime("%Y%m%d") +'_测试报告2',
                         mail_from=('测试部', ''))

message.attach(filename='th.jpeg', data=open('th.jpeg', 'rb'))
message.attachments['th.jpeg'].is_inline = True
message.transformer.synchronize_inline_images()
message.transformer.save()
message.html
u'<html><body><img src="cid:th.jpeg"></body></html>'
r = message.send(to=('', ''),
                 smtp={'host': 'smtp.126.com', 'port': 465, 'ssl': True, 'user': '',
                       'password': 'shouquanma126'})
print(r.status_code)
