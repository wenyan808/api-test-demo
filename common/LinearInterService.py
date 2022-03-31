#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2021/3/22
# @Author  : zhangranghan



from common.util import http_get_request,inter_key_get,inter_key_post
from config.conf  import URL,ACCESS_KEY,SECRET_KEY

class LinearInterService:

    def __init__(self,url,access_key,secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key


    def linear_contract_contract_info(self,contract_code=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-inter/x/v1/linear_swap_contract_info'
        return http_get_request(url, params)


    def linear_swap_price_limit(self,contract_code=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-inter/x/v1/linear_swap_price_limit'
        return http_get_request(url, params)


    def linear_swap_sub_account_info_list(self,contract_code=None,page_index=None,page_size=None,user_id=None,interface_type=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_sub_account_info_list'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    def linear_swap_account_position_info(self,contract_code=None,user_id=None,interface_type=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_account_position_info'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    def linear_swap_position_limit(self,contract_code=None,user_id=None,interface_type=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_position_limit'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    def linear_swap_transfer_limit(self,contract_code=None,user_id=None,interface_type=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_transfer_limit'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    def linear_swap_order_limit(self,contract_code=None,order_price_type=None,user_id=None,interface_type=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if order_price_type:
            params['order_price_type'] = order_price_type
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_order_limit'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    def linear_swap_order(self,contract_code=None,client_order_id=None,price=None,volume=None,direction=None,offset=None,lever_rate=None,order_price_type=None,user_id=None,interface_type=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if client_order_id:
            params['client_order_id'] = client_order_id
        if price:
            params['price'] = price
        if volume:
            params['volume'] = volume
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        if lever_rate:
            params['lever_rate'] = lever_rate
        if order_price_type:
            params['order_price_type'] = order_price_type
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_order'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    def linear_swap_cancel(self,order_id=None,client_order_id=None,contract_code=None,user_id=None,interface_type=None):

        params = {}

        if order_id:
            params['order_id'] = order_id
        if client_order_id:
            params['client_order_id'] = client_order_id
        if contract_code:
            params['contract_code'] = contract_code
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_cancel'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    def linear_swap_order_info(self,order_id=None,client_order_id=None,contract_code=None,user_id=None,interface_type=None):

        params = {}

        if order_id:
            params['order_id'] = order_id
        if client_order_id:
            params['client_order_id'] = client_order_id
        if contract_code:
            params['contract_code'] = contract_code
        if user_id:
            params['user_id'] = user_id
        if interface_type:
            params['interface_type'] = interface_type

        request_path = '/linear-swap-inter/x/v1/linear_swap_order_info'
        return inter_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    def contract_account_total_assets(self,user_id = None):

        params = {}
        if user_id:
            params['user-id'] = user_id
        request_path =  '/contract-inter/x/v1/contract_account_total_assets'
        return inter_key_get(self.__url, request_path ,params, self.__access_key, self.__secret_key)


    def swap_account_total_assets(self,user_id = None):

        params = {}
        if user_id:
            params['user-id'] = user_id
        request_path =  '/swap-inter/x/v1/swap_account_total_assets'
        return inter_key_get(self.__url, request_path ,params, self.__access_key, self.__secret_key)


    def linear_swap_account_total_assets(self,user_id = None):

        params = {}
        if user_id:
            params['user-id'] = user_id
        request_path =  '/linear-swap-inter/x/v1/linear_swap_account_total_assets'
        return inter_key_get(self.__url, request_path ,params, self.__access_key, self.__secret_key)


    def option_account_total_assets(self,user_id = None):

        params = {}
        if user_id:
            params['user-id'] = user_id
        request_path =  '/option-inter/x/v1/option_account_total_assets'
        return inter_key_get(self.__url, request_path ,params, self.__access_key, self.__secret_key)


    def center_user_trade_turnover(self,user_id = None,interface_type='global'):
        params = {}
        if user_id:
            params['user-id'] = user_id
        if interface_type:
            params['interface-type'] = interface_type
        request_path =  '/contract-center-inter/x/v1/center_user_trade_turnover'
        return inter_key_get(self.__url, request_path ,params, self.__access_key, self.__secret_key)

#定义t并传入公私钥和URL,供用例直接调用
t = LinearInterService(URL,ACCESS_KEY,SECRET_KEY)