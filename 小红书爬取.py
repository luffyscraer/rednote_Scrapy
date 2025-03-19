import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii
import base64
from urllib.parse import quote
import time
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
from urllib.parse import quote,quote_plus,unquote
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
from hashlib import md5
import time
import os
import json
import subprocess
import hashlib
import base64
import json
import time
from lxml import etree
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import execjs
from functools import partial
import random
import pymysql
import subprocess
import hashlib
import base64
import json
import tkinter as tk
import time
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import math
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'rednote',
    'charset': 'utf8'
}
conn = pymysql.connect(**db_config)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Database1 (id VARCHAR(255) PRIMARY KEY)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Database2 (id VARCHAR(255) PRIMARY KEY, xsec_token TEXT)''')
conn.commit()
def searichid(u=int(time.time()*1000)):
    n = 2147483646
    l=math.ceil(random.random() * n)
    def to_base36(n):
        if n == 0:
            return '0'
        chars = '0123456789abcdefghijklmnopqrstuvwxyz'
        result = ''
        while n:
            result = chars[n % 36] + result
            n //= 36
        return result
    return to_base36(u*2**64+l)
def store_to_database2(id, token):
    cursor.execute("INSERT IGNORE INTO Database2 (id, xsec_token) VALUES (%s, %s)", (id, token))
    conn.commit()
def get_data_from_database2():
    cursor.execute("Select IGNORE From Database2 (id, xsec_token) VALUES (%s, %s)", (id, token))
    conn.commit()
def is_in_database1(id):
    cursor.execute("SELECT 1 FROM database_shenzhen_used_id WHERE id = %s", (id,))
    return cursor.fetchone() is not None
def move_data_from_db2_to_db1():
    cursor.execute("INSERT IGNORE INTO database_shenzhen_used_id (id) SELECT id FROM Database2")
    cursor.execute(f"DELETE FROM Database2")
    conn.commit()
from functools import partial
def get_x_s_DATA(x_t,data):
    url = "/api/sns/web/v1/search/notes"
    a1 = '19328cba987t9dncoahgckcwthtxdjnklnyvm3jom50000202209'
    # 计算MD5哈希
    x1 = hashlib.md5(('url=' + url + json.dumps(data, ensure_ascii=False, separators=(",", ":"))).encode()).hexdigest()
    x2 = '0|0|0|1|0|0|1|0|0|0|1|0|0|0|0|1|0|0|0'
    x4=x_t
    def aes_encrypt(data, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
        return binascii.hexlify(encrypted_data).decode()
    key = 'glt6h61ta7kisow7'.encode()
    iv = '4hrivgw5s342f9b2'.encode()
    payload_str = f"x1={x1};x2={x2};x3={a1};x4={x4};"
    payload_str = base64.b64encode(payload_str.encode()).decode()
    payload = aes_encrypt(payload_str, key, iv)
    final_data = {
        "signSvn": "55",
        "signType": "x2",
        "appId": "xhs-pc-web",
        "signVersion": "1",
        "payload": payload
    }
    final_json = base64.b64encode(json.dumps(final_data, ensure_ascii=False,
                                separators=(",", ":")).encode()).decode()
    xs = 'XYW_' + final_json
    return xs
def get_x_s(x_t,url):
    a1 = '19328cba987t9dncoahgckcwthtxdjnklnyvm3jom50000202209'
    x1 = hashlib.md5(('url=' + url).encode()).hexdigest()
    x2 = '0|0|0|1|0|0|1|0|0|0|1|0|0|0|0|1|0|0|0'
    x4 = x_t
    def aes_encrypt(data, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
        return binascii.hexlify(encrypted_data).decode()
    key = 'glt6h61ta7kisow7'.encode()
    iv = '4hrivgw5s342f9b2'.encode()
    payload_str = f"x1={x1};x2={x2};x3={a1};x4={x4};"
    payload_str = base64.b64encode(payload_str.encode()).decode()
    payload = aes_encrypt(payload_str, key, iv)
    final_data = {
        "signSvn": "55",
        "signType": "x2",
        "appId": "xhs-pc-web",
        "signVersion": "1",
        "payload": payload
    }
    final_json = base64.b64encode(json.dumps(final_data, ensure_ascii=False, separators=(",", ":")).encode()).decode()
    xs = 'XYW_' + final_json
    return xs
def get_enc(xs):
    f = execjs.compile(open('./xcomman.js', 'r', encoding='utf-8').read())
    fa=f.call('encrypt_mcr',xs)
    return fa
def get_result(xt,xs,ex9):
    f2 = execjs.compile(open('./xsconmmmon.js', 'r', encoding='utf-8').read())
    f222 = f2.call('getresult', xt,xs,get_enc(ex9))
    return f222
def requestt(X_s,X_scommon,data):
    headers = {'accept':'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
                     'x-s-common':X_scommon ,
              'x-s':X_s,
               'cookie':'a1=19328cba987t9dncoahgckcwthtxdjnklnyvm3jom50000202209;web_session=0400698e35b26257983c9765ef354ba75728ac;webId=0c423d2491393bba08fe89f2a2afb2de'         ,
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    }
    url='https://edith.xiaohongshu.com/api/sns/web/v1/search/notes'
    response=requests.post(url=url,headers=headers,data=json.dumps(data,ensure_ascii=False,separators=(",", ":")))
    time.sleep(1)
    print(response.text)
    print(json.loads(response.text)['data'])
    return json.loads(response.text)['data']
def store_data(keyword='深圳政府手机消费券补贴'):
    xt = int(time.time() * 1000)
    search_id = searichid(xt)
    for i in range(1, 5):
        has_more=True
        xt2 = int(time.time() * 1000)
        search_id2 = searichid(xt2)
        search_iq=search_id+'@'+search_id2
        # data = {"keyword":keyword, "page": i, "page_size": 20, "search_id": search_iq,
        #         "sort": "time_descending",
        #         "note_type": 0, "ext_flags": [], "image_formats": ["jpg", "webp", "avif"]}

        data = {"keyword": keyword, "page": i, "page_size": 20, "search_id": search_iq, "sort": "popularity_descending",
                "note_type": 0, "ext_flags": [], "image_formats": ["jpg", "webp", "avif"]}
        # data = {"keyword": keyword, "page": i, "page_size": 20, "search_id": search_id, "sort": "general",
        #         "note_type": 0, "ext_flags": [], "image_formats": ["jpg", "webp", "avif"]}
        xs = get_x_s_DATA(xt, data)
        ex9 = str(xt) + str(
            xs) + "I38rHdgsjopgIvesdVwgIC+oIELmBZ5e3VwXLgFTIxS3bqwErFeexd0ekncAzMFYnqthIhJeSBMDKutRI3KsYorWHPtGrbV0P9WfIi/eWc6eYqtyQApPI37ekmR1QL+5Ii6sdnoeSfqYHqwl2qt5B0DoIx+PGDi/sVtkIxdsxuwr4qtiIkrwIi/skcc3I3VvIC7sYuwXq9qtpFveDSJsSPwXIEvsiVtJOPw8BuwfPpdeTDWOIx4VIiu1ZPwbPutXIvlaLb/s3qtxIxes1VwHIkumIkIyejgsY/WTge7eSqte/D7sDcpipedeYrDtIC6eDVw2IENsSqtlnlSuNjVtIvoekqwMgbOe1B8sIEDGIERn+7uUI3Eq8IYgIEhIoPwSIChV8gJsWm5s1uwRICOe0jKejeE+IiKe3WcI2utAIkKexfve6l/e3Pt4BageYqwVIvpsc0vedPwvpnesSuwsI3lpI3QTruwGLPw+LjIaKS6sdoNe6PwJIh7sWd7e6IY3IENeSWvs6dZdIEAe1VtYIir5tutKKVw1IvosxutFIiAsiqtSIENsDqtSHuwPoVwxICzAIxiK4ncA+b3sVPwAIiuaICos1PwQpSuGmjee0AQUIk8w4Pt+ruwAICde6VtuQc7eTY5siF8LIEJsVfOe3qtpLPwqIvvefVtzIC3ekoZ="
        x_scommen = get_result(xt, xs, ex9)
        aa = requestt(xs, x_scommen, data)
        time.sleep(1)
        if 'has_more' in aa:
            has_more=aa['has_more']
        if has_more:
            for item in aa['items']:
                item_id = item['id']
                item_token = item['xsec_token']
                print(is_in_database1(item_id),'zheli')
                if not is_in_database1(item_id):
                    store_to_database2(item_id, item_token)
                    print('store')
        else:
            break
        time.sleep(1)
def get_data(keyword='港科广'):
    def get_data_from_database2(cursor):
        # 注意：这里我们假设有一个特定的 id 值用于检索数据
        # 如果您的目的是检索所有行，则不需要 WHERE 子句
        query = "SELECT id, xsec_token FROM Database2"
        cursor.execute(query)
        # 获取所有结果行
        results = cursor.fetchall()
        # 返回结果（或者您可以在函数内部处理结果）
        return results
    data_id_token = get_data_from_database2(cursor)
    return data_id_token
def get(url,headers):
    resp=requests.get(url,headers=headers)
    print(resp.text)
    data_comment=json.loads(resp.text)
    time.sleep(1)
    has_more=data_comment["data"]['has_more']#return true flase
    print(has_more)
    return  data_comment
def get_subcomment(url):
    #前面去除https://edith.xiaohongshu.com
    xt=int(time.time()*1000)
    xs = get_x_s(xt, url)
    ex9 = str(xt) + str(xs) + "I38rHdgsjopgIvesdVwgIC+oIELmBZ5e3VwXLgFTIxS3bqwErFeexd0ekncAzMFYnqthIhJeSBMDKutRI3KsYorWHPtGrbV0P9WfIi/eWc6eYqtyQApPI37ekmR1QL+5Ii6sdnoeSfqYHqwl2qt5B0DoIx+PGDi/sVtkIxdsxuwr4qtiIkrwIi/skcc3I3VvIC7sYuwXq9qtpFveDSJsSPwXIEvsiVtJOPw8BuwfPpdeTDWOIx4VIiu1ZPwbPutXIvlaLb/s3qtxIxes1VwHIkumIkIyejgsY/WTge7eSqte/D7sDcpipedeYrDtIC6eDVw2IENsSqtlnlSuNjVtIvoekqwMgbOe1B8sIEDGIERn+7uUI3Eq8IYgIEhIoPwSIChV8gJsWm5s1uwRICOe0jKejeE+IiKe3WcI2utAIkKexfve6l/e3Pt4BageYqwVIvpsc0vedPwvpnesSuwsI3lpI3QTruwGLPw+LjIaKS6sdoNe6PwJIh7sWd7e6IY3IENeSWvs6dZdIEAe1VtYIir5tutKKVw1IvosxutFIiAsiqtSIENsDqtSHuwPoVwxICzAIxiK4ncA+b3sVPwAIiuaICos1PwQpSuGmjee0AQUIk8w4Pt+ruwAICde6VtuQc7eTY5siF8LIEJsVfOe3qtpLPwqIvvefVtzIC3ekoZ="
    x_scommen = get_result(xt, xs, ex9)
    print(url)
    headers = {'accept': 'application/json, text/plain, */*',
               'Content-Type': 'application/json;charset=UTF-8',
               'x-s-common': x_scommen,
               'x-s': xs,
               'cookie':'a1=19328cba987t9dncoahgckcwthtxdjnklnyvm3jom50000202209;web_session=0400698e35b26257983c9765ef354ba75728ac;webId=0c423d2491393bba08fe89f2a2afb2de'
              , 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
               }
    print(headers)
    url_ = f"https://edith.xiaohongshu.com{url}"
    print(url_,'我是comment 的yrl')
    resonsetext = get(url_, headers)
    print()

    return resonsetext
def get_all_one_note(id,token):
    title,content=write_doc(id,token)
    title = title.replace("|", '').replace('/', '').replace('、','').replace('"','').replace("'",'').replace('?','').replace('!','')
    if content !='kong2':

        ff = open(f'./{title}.txt', 'a+', encoding='utf-8')
        print('文件打开')
        ff.write(title)
        ff.write(content)
        ff.close()
    if title=='kong2':
        title='广州消费券综合'
    if title!='kong' and token!='kong':
        ff = open(f'./{title}.txt', 'a+', encoding='utf-8')
        print('文件打开')
        # ff.write(content)
        url = f'/api/sns/web/v2/comment/page?note_id={id}&cursor=&top_comment_id=&image_formats=jpg,webp,avif&xsec_token={quote(token)}'
        aa = get_subcomment(url)
        print(aa)
        if  'cursor' in aa['data']:
            cursor = aa['data']['cursor']
        else:
            cursor=''
        has_more = aa['data']['has_more']
        for i in aa['data']['comments']:
            str1 = ''
            # 每一次循环是一条评论
            sub_comment_has_more = i['sub_comment_has_more']
            cursor_subcomment = i['sub_comment_cursor']
            root_comment_id = i['id']
            content_main = i['content']
            str1 += content_main + '---'
            for j in i['sub_comments']:
                str1 += j['content'] + '。'
            print(str1, '我是str')
            # 判断一下有无子评论
            while sub_comment_has_more:
                url_next = f"/api/sns/web/v2/comment/sub/page?note_id={id}&root_comment_id={root_comment_id}&num=10&cursor={cursor_subcomment}&image_formats=jpg,webp,avif&top_comment_id=&xsec_token={quote(token)}"
                aa_sub = get_subcomment(url_next)
                sub_comment_has_more = aa_sub['data']['has_more']
                cursor_subcomment = aa_sub['data']['cursor']
                content_next = aa_sub['data']['comments']
                for q in content_next:
                    str1 += q['content'] + '。'
                print(str1)
                time.sleep(1)
            # 写入每条评论及其子评论内容
            ff.write(str1 + '\n')
            print('评论写入')
        while has_more:
            for i in aa['data']['comments']:
                str1 = ''
                # 每一次循环是一条评论
                sub_comment_has_more = i['sub_comment_has_more']
                cursor_subcomment = i['sub_comment_cursor']
                root_comment_id = i['id']
                content_main = i['content']
                str1 += content_main + '---'
                for j in i['sub_comments']:
                    str1 += j['content'] + '。'
                print(str1,'我是str')
                # 判断一下有无子评论
                while sub_comment_has_more:
                    url_next = f"/api/sns/web/v2/comment/sub/page?note_id={id}&root_comment_id={root_comment_id}&num=10&cursor={cursor_subcomment}&image_formats=jpg,webp,avif&top_comment_id=&xsec_token={quote(token)}"
                    aa_sub = get_subcomment(url_next)
                    sub_comment_has_more = aa_sub['data']['has_more']
                    cursor_subcomment = aa_sub['data']['cursor']
                    content_next = aa_sub['data']['comments']
                    for q in content_next:
                        str1 += q['content'] + '。'
                    print(str1)
                    time.sleep(1)
                # 写入每条评论及其子评论内容
                ff.write(str1 + '\n')
                print('评论写入')
            # 获取下一页评论
            url = f'/api/sns/web/v2/comment/page?note_id={id}&cursor={cursor}&top_comment_id=&image_formats=jpg,webp,avif&xsec_token={quote(token)}'
            aa = get_subcomment(url)
            has_more = aa['data']['has_more']
            if 'cursor' in aa['data']:
                cursor = aa['data']['cursor']
            else:
                cursor=''
        ff.close()
        print('文件关闭')
        time.sleep(1)
    else:
        print('空下一条了')
def show_alert():
    import winsound
    winsound.Beep(1000,1000)
    root=tk.Tk()
    root.title='该打开小红书扫码了'
    root.geometry('300x150')
    root.attributes('-topmost',True)
    label=tk.Label(root,text='这是一个弹出来的置顶框')
    label.pack(pady=30)
    close_button=tk.Button(root,text='关闭',command=root.quit)
    close_button.pack()
    root.mainloop()
def write_doc(id,token):
    token=quote(f'{token}')
    url = f'https://www.xiaohongshu.com/explore/{id}?xsec_token={token}&xsec_source=pc_search&source=web_note_detail_r10'
    # url = 'https://www.xiaohongshu.com/explore/66f7ba78000000002a03527e?xsec_token=ABxEfESLPq5aV3vFuerGZ3IhPwbrmC5yOw6bnlbwVYTHs&xsec_source=pc_search&source=web_note_detail_r10'
    headers={'accept': 'application/json, text/plain, */*',
               'Content-Type': 'application/json;charset=UTF-8',
             'pragma':'no-cache',
             'priority':'u=0, i',
             'sec-ch-ua':'"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
             'sec-ch-ua-mobile':'?0',
             'sec-ch-ua-platform':"Windows",
             'sec-fetch-dest':'document',
             'sec-fetch-mode':'navigate',
             'sec-fetch-site':'same-origin',
             'sec-fetch-user':'?1',
             'upgrade-insecure-requests':'1',
             'cookie':'a1=19328cba987t9dncoahgckcwthtxdjnklnyvm3jom50000202209;web_session=0400698e35b26257983c9765ef354ba75728ac;webId=0c423d2491393bba08fe89f2a2afb2de',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
               }
    print(url)
    resp=requests.get(url,headers=headers,verify=False)
    import time
    time.sleep(1)
    resp.encoding='utf-8'
    print(resp.text)
    print('ssssssssssssssssssssssssssssssssss===============================================ssssssssssssssssssssssssssssssssss=================')
    tree = etree.HTML(resp.text)
    if tree.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[1]')!=[]:
        content = tree.xpath('.//meta[@name="description"]')[0].get('content')
        title=tree.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[1]')[0].text
    elif tree.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[1]')!=[] and tree.xpath('.//meta[@name="description"]')!=[]:
        title='empty'
    else:
        print('s')
        title='kong2'
        content='kong2'
    print(content)
    print(title)
    if title==None:
        title='kong2'
    if content==None:
        content='kong2'
    title=title.replace(' ','_').replace('//','').replace('/',  '')
    # print(file)
    import os
    import time
    title = title + str(int(time.time() * 1000))[9:14]
    found_title = False  # 标记是否找到相同的标题
    # for i in os.listdir():
    #     if f'{title}' in i:
    #         print(i)
    #         found_title = True  # 标记找到相同标题的文件
    #         with open(f'{i}', 'r', encoding='utf-8') as fww:
    #             content_have = fww.readline()[:40]
    #
    #         print(content_have)
    #
    #         # 如果内容相同则退出，标记为 'kong'
    #         if content_have in content:
    #             title = 'kong'
    #             content = 'kong'
    #             break
    #         else:
    #             print('文件内容不同，继续查找下一个文件')
    #     else:
    #         print('查找下一个文件')
    #
    # # 仅当找到相同标题且内容不同才加时间戳
    # if found_title and title != 'kong':
    #     title = title + str(int(time.time() * 1000))[9:14]

        # title=title+str(int(time.time()*1000))[9:14]
        # with open(f'{title}.txt', 'r', encoding='utf-8') as fww:
        #     content_have = fww.readlines()[0][:40]
        #     fww.close()
        # if content_have in content:
        #     title='kong'
        #     content='kong'
        # else:c
        #     title=title+str(int(time.time()*1000))[9:14]

    print(content)
    print(title)
    return title,content
if __name__ == '__main__':
    i=0
    while i<18:
        try:
            i+=1
            store_data(keyword='香港科技大学广州')
            abb=get_data(keyword='香港科技大学广州')
            print('kk')
            for kkk in abb:
                xt = int(time.time() * 1000)
                id = kkk[0]
                if '#17' in id:
                    continue
                token = kkk[1]
                print(id,token,'我是不能走的id')
                get_all_one_note(id, token)
                # print(kkk, '现在是id')
                print('完成')

            move_data_from_db2_to_db1()
            print('remove successfully')
            time.sleep(2)
        except Exception as e:
            print('卡了',e)
            import webbrowser
            path = r'C:\Users\legion\AppData\Local\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('chrome').open('https://www.xiaohongshu.com/')
            #show_alert()
            time.sleep(180)