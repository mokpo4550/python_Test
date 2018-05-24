#django, json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
#문자열 파싱, 시간 등등
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
from datetime import datetime, timedelta
import re

week = ( '월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일' );

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)', '저녁 학식 메뉴(내일)',
                    '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    t = datetime.now()

    if datacontent == '아침 학식 메뉴(오늘)':
        date = t.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday) % len(week)] + ") - 아침\r\n" +
                        "======================\r\n" +
                        GetInfo(time.localtime().tm_wday, 1)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '점심 학식 메뉴(오늘)':
        date = t.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday) % len(week)] + ") - 점심\r\n" +
                        "======================\r\n" +
                        GetInfo(time.localtime().tm_wday, 2)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '저녁 학식 메뉴(오늘)':
        date = t.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday) % len(week)] + ") - 저녁\r\n" +
                        "======================\r\n" +
                        GetInfo(time.localtime().tm_wday, 3)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '아침 학식 메뉴(내일)':
        tommorrow = t + timedelta(days=1)
        date = tommorrow.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday + 1) % len(week)] + ") - 아침\r\n" +
                        "======================\r\n" +
                                        GetInfo(time.localtime().tm_wday + 1, 1)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '점심 학식 메뉴(내일)':
        tommorrow = t + timedelta(days=1)
        date = tommorrow.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday + 1) % len(week)] + ") - 점심\r\n" +
                        "======================\r\n" +
                                        GetInfo(time.localtime().tm_wday + 1, 2)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '저녁 학식 메뉴(내일)':
        tommorrow = t + timedelta(days=1)
        date = tommorrow.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday + 1) % len(week)] + ") - 저녁\r\n" +
                        "======================\r\n" +
                        GetInfo(time.localtime().tm_wday + 1, 3)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '아침 학식 메뉴(모래)':
        tommorrow = t + timedelta(days=2)
        date = tommorrow.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday + 2) % len(week)] + ") - 아침\r\n" +
                        "======================\r\n" +
                        GetInfo(time.localtime().tm_wday + 2, 1)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '점심 학식 메뉴(모래)':
        tommorrow = t + timedelta(days=2)
        date = tommorrow.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday + 2) % len(week)] + ") - 점심\r\n" +
                        "======================\r\n" +
                        GetInfo(time.localtime().tm_wday + 2, 2)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

    elif datacontent == '저녁 학식 메뉴(모래)':
        tommorrow = t + timedelta(days=2)
        date = tommorrow.strftime("%Y. %m. %d. ")
        return JsonResponse({
            'message': {
                'text': "======================\r\n" +
                        date + "(" + week[(time.localtime().tm_wday + 2) % len(week)] + ") - 저녁\r\n" +
                        "======================\r\n" +
                        GetInfo(time.localtime().tm_wday + 2, 3)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침 학식 메뉴(오늘)', '점심 학식 메뉴(오늘)', '저녁 학식 메뉴(오늘)', '아침 학식 메뉴(내일)', '점심 학식 메뉴(내일)',
                            '저녁 학식 메뉴(내일)', '아침 학식 메뉴(모래)', '점심 학식 메뉴(모래)', '저녁 학식 메뉴(모래)']
            }

        })

def GetInfo(weekDay, set):
    html = urlopen('http://www.kopo.ac.kr/jungsu/content.do?menu=247')
    source = html.read()
    html.close()

    soup = BeautifulSoup(source, "lxml")
    table_div = soup.find(id="contents")
    tables = table_div.find_all("table")

    dietInformation = tables[1]
    trs = dietInformation.find_all('tr')
    today_tr = trs[weekDay + 1]
    today_td = today_tr.find_all('td')
    if set==1:
        soup = BeautifulSoup(str(today_td[1]), "lxml")
        return "학식이 없거나 미정입니다." if soup.getText().strip() == "" else "\n".join(soup.getText().strip().split(", "))
    elif set==2:
        soup = BeautifulSoup(str(today_td[2]), "lxml")
        return "학식이 없거나 미정입니다."if soup.getText().strip() == "" else "\n".join(soup.getText().strip().split(", "))
    elif set==3:
        soup = BeautifulSoup(str(today_td[3]), "lxml")
        return "학식이 없거나 미정입니다." if soup.getText().strip() == "" else "\n".join(soup.getText().strip().split(", "))
    else:
        return ""
