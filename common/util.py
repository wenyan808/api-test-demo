#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020/7/31
# @Author  : zhangranghan


import urllib.parse
import requests
import datetime
#import websocket
import json
import hmac
import base64
import hashlib
import gzip
import time
import logging
import sys
#import websockets


# timeout in 5 seconds:
TIMEOUT = 30

#各种请求,获取数据方式
def http_get_request(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept-language": "zh-CN",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }

    if add_to_headers:
        headers.update(add_to_headers)
    postdata = urllib.parse.urlencode(params)
    # while True:
    #     response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
    #     try:
    #         if response.json()['err_code'] == 403:
    #             print('continue  ',response.json())
    #             continue
    #     except:
    #         try:
    #             if response.status_code == 200:
    #                 return response.json()
    #             else:
    #                 return response.text
    #         except:
    #             return response.text
    #     break

    try:
        response = requests.get(url, postdata, headers=headers, timeout=TIMEOUT)
        # print('请求参数：', postdata)
        # print(response.url)
        # ret = ('剩余次数:',response.headers['ratelimit-remaining'],'次',
        #       '    限频间隔:',int(int(response.headers['ratelimit-interval'])/1000),'秒',
        #       '    限频次数:',response.headers['ratelimit-limit'],'次',
        #       '    解禁时间:',time.strftime("%Y-%m-%d %H:%M:%S",(time.localtime(int(response.headers['ratelimit-reset'][:-3])))),response.json())
        if response.status_code == 200:
            return response.json()
        else:
            return response.text
    except Exception as e:
        print("httpGet failed, detail is:%s" %e)
        return {"status":"fail","msg": "%s"%e}

def http_post_request(url, params, add_to_headers=None):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        "Accept-language": "zh-CN",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = json.dumps(params)

    # while True:
    #     response = requests.post(url, postdata, headers=headers, timeout=TIMEOUT)
    #     try:
    #         if response.json()['err_code'] == 403:
    #             print('continue  ',response.json())
    #             continue
    #     except:
    #         try:
    #             if response.status_code == 200:
    #                 return response.json()
    #             else:
    #                 return response.text
    #         except:
    #             return response.text
    #     break
    try:
        # print('请求参数：',postdata)
        response = requests.post(url, postdata, headers=headers, timeout=TIMEOUT)
        # print(response.url)
        # ret = ('剩余次数:',response.headers['ratelimit-remaining'],'次',
        #       '    限频间隔:',int(int(response.headers['ratelimit-interval'])/1000),'秒',
        #       '    限频次数:',response.headers['ratelimit-limit'],'次',
        #       '    解禁时间:',time.strftime("%Y-%m-%d %H:%M:%S",(time.localtime(int(response.headers['ratelimit-reset'][:-3])))),response.json())
        if response.status_code == 200:
            return response.json()
            # return ret
        else:
            return response.text
    except Exception as e:
        print("httpPost failed, detail is:%s" % e)
        return {"status":"fail","msg": "%s"%e}


def api_key_get(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'GET'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params.update({'AccessKeyId': ACCESS_KEY,
                   'SignatureMethod': 'HmacSHA256',
                   'SignatureVersion': '2',
                   'Timestamp': timestamp})

    host_url = url
    host_name = urllib.parse.urlparse(host_url).hostname.lower()
    params['Signature'] = createSign(params, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path
    return http_get_request(url, params)


def api_key_post(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'POST'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params_to_sign = {'AccessKeyId': ACCESS_KEY,
                      'SignatureMethod': 'HmacSHA256',
                      'SignatureVersion': '2',
                      'Timestamp': timestamp}

    host_url = url
    host_name = urllib.parse.urlparse(host_url).hostname.lower()
    params_to_sign['Signature'] = createSign(params_to_sign, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path + '?' + urllib.parse.urlencode(params_to_sign)
    return http_post_request(url, params)

def inter_key_get(url,request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'GET'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params.update({'AWSAccessKeyId': ACCESS_KEY,
                   'SignatureMethod': 'HmacSHA256',
                   'SignatureVersion': '2',
                   'Timestamp': timestamp})
    host_url = url
    host_name = urllib.parse.urlparse(host_url).hostname.lower()
    params['Signature'] = createSign(params, method, host_name,request_path, SECRET_KEY)
    url = host_url + request_path
    return http_get_request(url, params)


def inter_key_post(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'POST'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params_to_sign = {'AWSAccessKeyId': ACCESS_KEY,
                      'SignatureMethod': 'HmacSHA256',
                      'SignatureVersion': '2',
                      'Timestamp': timestamp}

    host_url = url
    host_name = urllib.parse.urlparse(host_url).hostname.lower()
    params_to_sign['Signature'] = createSign(params_to_sign, method, host_name, request_path, SECRET_KEY)
    url = host_url + request_path + '?' + urllib.parse.urlencode(params_to_sign)
    return http_post_request(url, params)


def createSign(pParams, method, host_url, request_path, secret_key):
    sorted_params = sorted(pParams.items(), key=lambda d: d[0], reverse=False)
    encode_params = urllib.parse.urlencode(sorted_params)
    payload = [method, host_url, request_path, encode_params]
    payload = '\n'.join(payload)
    payload = payload.encode(encoding='UTF8')
    secret_key = secret_key.encode(encoding='UTF8')
    digest = hmac.new(secret_key, payload, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    signature = signature.decode()
    return signature


def logger():
    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)
    # fh = logging.FileHandler("threading.log")  #日志文件输出
    fh = logging.StreamHandler(sys.stdout)  #日志控制台输出 #增加sys.stdout修复日志为红的bug
    # fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

logger = logger()


""" 下面的方法是ws用的 """
#鉴权订阅
def api_key_sub(url, access_key, secret_key, subs):
    host_url = urllib.parse.urlparse(url).hostname.lower()
    print(host_url)
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    data = {
        "AccessKeyId": access_key,
        "SignatureMethod": "HmacSHA256",
        "SignatureVersion": "2",
        "Accept-language": "zh-CN",
        "Timestamp": timestamp
    }
    sign = createSign(data, "GET", host_url, '/linear_swap_notification', secret_key)
    # sign = createSign(data, "GET", host_url, '/notification', secret_key)
    data["op"] = "auth"
    data["type"] = "api"
    data["Signature"] = sign
    data['cid'] = '11225747'
    try:
        ws = websocket.create_connection(url)
        msg_str = json.dumps(data)
        print("msg_str is:",msg_str)
        ws.send(msg_str)
        msg_result =json.loads(gzip.decompress(ws.recv()).decode())
        print("msg_result is:",msg_result)
        sub_str = json.dumps(subs)
        print("sub_str is:",sub_str)
        ws.send(sub_str)
        sub_result = json.loads(gzip.decompress(ws.recv()).decode())
        print("sub_result is :",sub_result)
        ws.close()
        return sub_result
    except Exception as e:
        print("Sub failed, detail is:%s" % e)
        return {"status": "fail", "msg": "%s" % e}

#普通订阅
def sub(url,sub):
    try:
        ws = websocket.create_connection(url)
        sub_str = json.dumps(sub)
        ws.send(sub_str)
        while True:
            sub_result = json.loads(gzip.decompress(ws.recv()).decode())
            if 'tick' in sub_result:
                break
        ws.close()
        return sub_result
    except Exception as e:
        print("Sub failed, detail is:%s" % e)
        return {"status": "fail", "msg": "%s" % e}


