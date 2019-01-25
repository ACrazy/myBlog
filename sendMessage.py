import yagmail

# 链接邮箱服务器

# 此处的password是授权码

def sendMail(contents, eMail, name):
    try:
        yag = yagmail.SMTP(user="2265373762@qq.com", password="pfifercqhkklecde", host='smtp.qq.com')
        # 发送邮件
        yag.send(eMail, name, contents)
        # 发送邮件带附件
        # yag.send('ccc@126.com', '发送附件', contents, ["d://1.txt", "d://1.jpg"])
        # print('success')
        return 'success'
    except:
        # print('failed')
        return 'failed'

