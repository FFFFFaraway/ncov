import requests
import re
import json
import datetime
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

# TODO: fill your username and password of `https://app.bupt.edu.cn/uc/wap/login`
students = [{'student_name': '小明', 'username': '2021xxxxxx', 'password': 'xxxxxxxxxx'}, ]

# find info from report of last time
def extract_old_info(respond):
    oldInfolst = re.findall('oldInfo: (.*),\n', respond.text)
    return json.loads(oldInfolst[0])


def report(student):
    s = requests.Session()
    # TODO: fill your username and password of `http://10.3.8.211/index`
    r_byr_net = s.post("http://gw.bupt.edu.cn/login", data={'user': '2021xxxxxx', 'pass': 'xxxxxxxxxx'},
                       headers=headers)
    r_login = s.post('https://app.bupt.edu.cn/uc/wap/login/check', data=student, headers=headers)
    if r_login.json()['e'] != 0:
        return r_login.json()['m']
    r_main = s.get('https://app.bupt.edu.cn/ncov/wap/default/index', headers=headers)
    oldInfo = extract_old_info(r_main)
    r_done = s.post('https://app.bupt.edu.cn/ncov/wap/default/save', data=oldInfo, headers=headers)
    return r_done.json()['m']


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           f"{datetime.date.today().strftime('%Y-%m-%d')}.txt"), 'w') as log_f:
        for student in students:
            message = report(student)
            log_f.write(f"{student['student_name']}, {student['username']}: {message}\n")
