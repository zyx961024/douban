import requests
from json import loads

from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)
locate={
    '1':'44,44,',
    '2':'114,44,',
    '3':'185,44,',
    '4':'254,44,',
    '5':'44,124,',
    '6':'114,124,',
    '7':'185,124,',
    '8':'254,124,',
}
head={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
now_session=requests.Session()
now_session.verify=False
username,password="15558966862","96zhuyongxin"
#username,password=input("请输入账号:\n"),input("请输入密码:\n")
def Startlogin():
    print('-----------------验证码验证-----------------')
    resp1 = now_session.get(
        'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8430851651301317',
        headers=head)
    with open(r'C:\Users\asus\Desktop\code.png','wb') as f:
        f.write(resp1.content)
    print('请输入验证码代号：')
    code=input()
    write=code.split(',')
    codes=''
    for i in write:
        codes+=locate[i]
    data={
    'answer': codes,
    'login_site': 'E',
    'rand': 'sjrand'
    }
    resp=now_session.post('https://kyfw.12306.cn/passport/captcha/captcha-check',headers=head,data=data)
    print()
    html=loads(resp.content.decode('utf-8'))
    if html['result_code']=='4':
        print('验证码校验成功！')
        print('-----------------登录中-----------------')
        login_url='https://kyfw.12306.cn/passport/web/login'
        user={
            'username': username,
            'password': password,
            'appid': 'otn'
        }
        resp2=now_session.post(login_url,headers=head,data=user)
        print('登陆成功！')

    else:
        print('验证码校验失败，正在重新请求页面...')
        login()
    pass
Startlogin()
