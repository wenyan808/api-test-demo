#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020/8/7
# @Author  : zhangranghan


from common.util import http_get_request, api_key_post, api_key_get
from config.conf import URL, ACCESS_KEY, SECRET_KEY


class LinearService:

    def __init__(self, url, access_key, secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key

    # 获取合约信息（全逐通用）
    def linear_contract_info(self, contract_code=None, support_margin_mode=None, business_type=None, pair=None,
                             contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if support_margin_mode:
            params['support_margin_mode'] = support_margin_mode
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        url = self.__url + '/linear-swap-api/v1/swap_contract_info'
        return http_get_request(url, params)

    # 获取合约指数信息（全逐通用）
    def linear_index(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-api/v1/swap_index'
        return http_get_request(url, params)

    # 获取合约最高限价和最低限价（全逐通用）
    def linear_price_limit(self, contract_code=None, business_type=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        url = self.__url + '/linear-swap-api/v1/swap_price_limit'
        return http_get_request(url, params)

    # 获取当前可用合约总持仓量 （全逐通用）
    def linear_open_interest(self, contract_code=None, business_type=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        url = self.__url + '/linear-swap-api/v1/swap_open_interest'
        return http_get_request(url, params)

    # 查询合约风险准备金和预估分摊比例（全逐通用）
    def linear_risk_info(self, contract_code=None, business_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        url = self.__url + '/linear-swap-api/v1/swap_risk_info'
        return http_get_request(url, params)

    # 获取风险准备金历史数据（全逐通用）
    def linear_insurance_fund(self, contract_code=None, page_size=None, page_index=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_size:
            params['page_size'] = page_size
        if page_index:
            params['page_index'] = page_index
        url = self.__url + '/linear-swap-api/v1/swap_insurance_fund'
        return http_get_request(url, params)

    # 查询平台阶梯调整系数（逐仓）
    def linear_adjustfactor(self, contract_code=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-api/v1/swap_adjustfactor'
        return http_get_request(url, params)

    # 查询平台阶梯调整系数（全仓）
    def linear_cross_adjustfactor(self, contract_code=None, business_type=None, pair=None, contract_type=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type

        url = self.__url + '/linear-swap-api/v1/swap_cross_adjustfactor'
        return http_get_request(url, params)

    # 获取平台持仓量（全逐通用）
    def linear_his_open_interest(self, contract_code=None, period=None, size=None, amount_type=None, pair=None,
                                 contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if contract_type:
            params['contract_type'] = contract_type
        if pair:
            params['pair'] = pair
        if period:
            params['period'] = period
        if size:
            params['size'] = size
        if amount_type:
            params['amount_type'] = amount_type

        url = self.__url + '/linear-swap-api/v1/swap_his_open_interest'
        return http_get_request(url, params)

    # 获取平台阶梯保证金（逐仓）
    def linear_ladder_margin(self, contract_code=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-api/v1/swap_ladder_margin'
        return http_get_request(url, params)

    # 获取平台阶梯保证金（全仓）
    def linear_cross_ladder_margin(self, contract_code=None, business_type=None, contract_type=None, pair=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if contract_type:
            params['contract_type'] = contract_type
        if pair:
            params['pair'] = pair

        url = self.__url + '/linear-swap-api/v1/swap_cross_ladder_margin'
        return http_get_request(url, params)

    # 精英账户多空持仓对比-账户数（全逐通用）
    def linear_elite_account_ratio(self, contract_code=None, period=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period

        url = self.__url + '/linear-swap-api/v1/swap_elite_account_ratio'
        return http_get_request(url, params)

    # 精英账户多空持仓对比-持仓量（全逐通用）
    def linear_elite_position_ratio(self, contract_code=None, period=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period

        url = self.__url + '/linear-swap-api/v1/swap_elite_position_ratio'
        return http_get_request(url, params)

    # 获取强平订单（全逐通用）
    def linear_liquidation_orders(self, contract_code=None, trade_type=None, create_date=None, page_index=None,
                                  page_size=None, pair=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if pair:
            params['pair'] = pair
        url = self.__url + '/linear-swap-api/v1/swap_liquidation_orders'
        return http_get_request(url, params)

    # 查询平台历史结算记录（全逐通用）
    def linear_settlement_records(self, contract_code=None, start_time=None, end_time=None, page_index=None,
                                  page_size=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        url = self.__url + '/linear-swap-api/v1/swap_settlement_records'
        return http_get_request(url, params)

    # 获取预估结算价（全逐通用）
    def linear_estimated_settlement_price(self, contract_code=None, business_type=None, pair=None, contract_type=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type

        url = self.__url + '/linear-swap-api/v1/swap_estimated_settlement_price'
        return http_get_request(url, params)

    # 查询系统状态（逐仓）
    def linear_api_state(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-api/v1/swap_api_state'
        return http_get_request(url, params)

    # 查询系统划转权限（全仓）
    def linear_cross_transfer_state(self, margin_account=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account

        url = self.__url + '/linear-swap-api/v1/swap_cross_transfer_state'
        return http_get_request(url, params)

    # 查询系统交易权限（全仓）
    def linear_cross_trade_state(self, contract_code=None, business_type=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        url = self.__url + '/linear-swap-api/v1/swap_cross_trade_state'
        return http_get_request(url, params)

    # 获取合约的资金费率（全逐通用）
    def linear_funding_rate(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-api/v1/swap_funding_rate'
        return http_get_request(url, params)

    # 批量获取合约的资金费率（全逐通用）
    def linear_batch_funding_rate(self, contract_code=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        url = self.__url + '/linear-swap-api/v1/swap_batch_funding_rate'
        return http_get_request(url, params)

    # 获取合约的历史资金费率
    def linear_historical_funding_rate(self, contract_code=None, page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        url = self.__url + '/linear-swap-api/v1/swap_historical_funding_rate'
        return http_get_request(url, params)

    # 获取行情深度数据（全逐通用）
    def linear_depth(self, contract_code=None, type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if type:
            params['type'] = type

        url = self.__url + '/linear-swap-ex/market/depth'
        return http_get_request(url, params)

    # 获取市场最优挂单（全逐通用）
    def linear_market_bbo(self, contract_code=None, business_type=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        url = self.__url + '/linear-swap-ex/market/bbo'
        return http_get_request(url, params)

    # 获取K线数据（全逐通用）
    def linear_kline(self, contract_code=None, period=None, size=None, FROM=None, to=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period
        if size:
            params['size'] = size
        if FROM:
            params['from'] = FROM
        if to:
            params['to'] = to

        url = self.__url + '/linear-swap-ex/market/history/kline'
        return http_get_request(url, params)

    # 获取聚合行情（全逐通用）
    def linear_detail_merged(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-ex/market/detail/merged'
        return http_get_request(url, params)

    # 批量获取聚合行情（全逐通用）
    def linear_detail_batch_merged(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-ex/market/detail/batch_merged'
        return http_get_request(url, params)

    # 获取基差数据（全逐通用）
    def linear_basis(self, contract_code=None, period=None, basis_price_type=None, size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period
        if size:
            params['size'] = size
        if basis_price_type:
            params['basis_price_type'] = basis_price_type

        url = self.__url + '/index/market/history/linear_swap_basis'
        return http_get_request(url, params)

    # 获取溢价指数K线数据（全逐通用）
    def linear_premium_index_kline(self, contract_code=None, period=None, size=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period
        if size:
            params['size'] = size

        url = self.__url + '/index/market/history/linear_swap_premium_index_kline'
        return http_get_request(url, params)

    # 获取预测资金费率的K线数据（全逐通用）
    def linear_estimated_rate_kline(self, contract_code=None, period=None, size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period
        if size:
            params['size'] = size

        url = self.__url + '/index/market/history/linear_swap_estimated_rate_kline'
        return http_get_request(url, params)

    # 获取标记价格的K线数据（全逐通用）
    def linear_swap_mark_price_kline(self, contract_code=None, period=None, size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period
        if size:
            params['size'] = size

        url = self.__url + '/index/market/history/linear_swap_mark_price_kline'
        return http_get_request(url, params)

    # 获取市场最近成交记录（全逐通用）
    def linear_trade(self, contract_code=None, business_type=None):
        params = {}

        if business_type:
            params['business_type'] = business_type
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/linear-swap-ex/market/trade'
        return http_get_request(url, params)

    # 批量获取最近的交易记录（全逐通用）
    def linear_history_trade(self, contract_code=None, size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if size:
            params['size'] = size

        url = self.__url + '/linear-swap-ex/market/history/trade'
        return http_get_request(url, params)

    # 获取指数的K线数据（全逐通用）
    def linear_history_index(self, contract_code=None, period=None, size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period
        if size:
            params['size'] = size

        url = self.__url + '/index/market/history/index'
        return http_get_request(url, params)

    # 获取账户总资产估值（全逐通用）
    def swap_balance_valuation(self, valuation_asset=None):
        """
        参数名称           参数类型            必填      描述
        valuation_asset   string            false    "BTC-USD",资产估值币种，不填查默认BTC
        """
        params = {}
        if valuation_asset:
            params['valuation_asset'] = valuation_asset

        request_path = '/linear-swap-api/v1/swap_balance_valuation'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


    # 获取用户的合约账户信息（逐仓）
    def linear_account_info(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/linear-swap-api/v1/swap_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约持仓信息（逐仓）
    def linear_position_info(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/linear-swap-api/v1/swap_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 批量设置子账户交易权限（全逐通用）
    def linear_sub_auth(self, sub_uid=None, sub_auth=None):

        params = {}
        if sub_uid:
            params['sub_uid'] = sub_uid
        if sub_auth:
            params['sub_auth'] = sub_auth

        request_path = '/linear-swap-api/v1/swap_sub_auth'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 批量获取子账户资产信息（逐仓）
    def linear_sub_account_info_list(self, contract_code=None, page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_sub_account_info_list'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询母账户下所有子账户资产信息（逐仓）
    def linear_sub_account_list(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/linear-swap-api/v1/swap_sub_account_list'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询母账户下的单个子账户资产信息（逐仓）
    def linear_sub_account_info(self, contract_code=None, sub_uid=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if sub_uid:
            params['sub_uid'] = sub_uid

        request_path = '/linear-swap-api/v1/swap_sub_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询母账户下的单个子账户持仓信息（逐仓）
    def linear_sub_position_info(self, contract_code=None, sub_uid=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if sub_uid:
            params['sub_uid'] = sub_uid

        request_path = '/linear-swap-api/v1/swap_sub_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户财务记录（全逐通用）
    def linear_financial_record(self, contract_code=None, margin_account=None, type=None, create_date=None,
                                page_index=None, page_size=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if type:
            params['type'] = type
        if contract_code:
            params['contract_code'] = contract_code
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_financial_record'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询用户财务记录（全逐通用）
    def linear_financial_record_exact(self, contract_code=None, margin_account=None, type=None, start_time=None,
                                      end_time=None, from_id=None, size=None, direct=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if type:
            params['type'] = type
        if contract_code:
            params['contract_code'] = contract_code
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if from_id:
            params['from_id'] = from_id
        if size:
            params['size'] = size
        if direct:
            params['direct'] = direct

        request_path = '/linear-swap-api/v1/swap_financial_record_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户结算记录（逐仓）
    def linear_user_settlement_records(self, contract_code=None, start_time=None, end_time=None, page_index=None,
                                       page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_user_settlement_records'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户结算记录（全仓）
    def linear_cross_user_settlement_records(self, margin_account=None, start_time=None, end_time=None, page_index=None,
                                             page_size=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_cross_user_settlement_records'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约下单量限制（全逐通用）
    def linear_order_limit(self, contract_code=None, order_price_type=None, business_type=None, pair=None,
                           contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_price_type:
            params['order_price_type'] = order_price_type
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_order_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约手续费费率（全逐通用）
    def linear_fee(self, contract_code=None, business_type=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_fee'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约划转限制（逐仓）
    def linear_transfer_limit(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/linear-swap-api/v1/swap_transfer_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户当前杠杆对应的持仓量限制（逐仓）
    def linear_position_limit(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/linear-swap-api/v1/swap_position_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户所有杠杆持仓量限制（逐仓）
    def linear_lever_position_limit(self, contract_code=None, lever_rate=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if lever_rate:
            params['lever_rate'] = lever_rate

        request_path = '/linear-swap-api/v1/swap_lever_position_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户资产和持仓信息（逐仓）
    def linear_account_position_info(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/linear-swap-api/v1/swap_account_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 母子账户划转（全逐通用）
    def linear_master_sub_transfer(self, sub_uid=None, asset=None, from_margin_account=None, to_margin_account=None,
                                   amount=None, type=None, client_order_id=None):
        params = {}
        if sub_uid:
            params['sub_uid'] = sub_uid
        if asset:
            params['asset'] = asset
        if from_margin_account:
            params['from_margin_account'] = from_margin_account
        if to_margin_account:
            params['to_margin_account'] = to_margin_account
        if amount:
            params['amount'] = amount
        if type:
            params['type'] = type
        if client_order_id:
            params['client_order_id'] = client_order_id

        request_path = '/linear-swap-api/v1/swap_master_sub_transfer'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取母账户下的所有母子账户划转记录（全逐通用）
    def linear_master_sub_transfer_record(self, margin_account=None, transfer_type=None, create_date=None,
                                          page_index=None, page_size=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if create_date:
            params['create_date'] = create_date
        if transfer_type:
            params['transfer_type'] = transfer_type
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_master_sub_transfer_record'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 同账号不同保证金账户的划转（全逐通用）
    def linear_transfer_inner(self, asset=None, from_margin_account=None, to_margin_account=None, amount=None,
                              client_order_id=None):

        params = {}
        if asset:
            params['asset'] = asset
        if from_margin_account:
            params['from_margin_account'] = from_margin_account
        if to_margin_account:
            params['to_margin_account'] = to_margin_account
        if amount:
            params['amount'] = amount
        if client_order_id:
            params['client_order_id'] = client_order_id

        request_path = '/linear-swap-api/v1/swap_transfer_inner'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户API指标禁用信息（全逐通用）
    def linear_api_trading_status(self):
        params = {}
        request_path = '/linear-swap-api/v1/swap_api_trading_status'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户品种实际可用杠杆倍数
    def linear_available_level_rate(self, contract_code=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/linear-swap-api/v1/swap_available_level_rate'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约下单 （逐仓）
    def linear_order(self, contract_code=None, client_order_id=None, price=None, volume=None, direction=None,
                     offset=None, lever_rate=None, order_price_type=None, tp_trigger_price=None, tp_order_price=None,
                     tp_order_price_type=None,
                     sl_trigger_price=None, sl_order_price=None, sl_order_price_type=None, channel_code=None,
                     reduce_only=None):

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
        if tp_trigger_price:
            params['tp_trigger_price'] = tp_trigger_price
        if tp_order_price:
            params['tp_order_price'] = tp_order_price
        if tp_order_price_type:
            params['tp_order_price_type'] = tp_order_price_type
        if sl_trigger_price:
            params['sl_trigger_price'] = sl_trigger_price
        if sl_order_price:
            params['sl_order_price'] = sl_order_price
        if sl_order_price_type:
            params['sl_order_price_type'] = sl_order_price_type
        if channel_code:
            params['channel_code'] = channel_code
        if reduce_only:
            params['reduce_only'] = reduce_only

        request_path = '/linear-swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约批量下单 （逐仓）
    def linear_batchorder(self, orders_data=None):

        params = orders_data

        request_path = '/linear-swap-api/v1/swap_batchorder'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 撤销合约订单（逐仓）
    def linear_cancel(self, order_id=None, client_order_id=None, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_id:
            params['order_id'] = order_id

        request_path = '/linear-swap-api/v1/swap_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 撤销全部合约单（逐仓）
    def linear_cancelall(self, contract_code=None, direction=None, offset=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset

        request_path = '/linear-swap-api/v1/swap_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 切换杠杆倍数 （逐仓）
    def linear_switch_lever_rate(self, contract_code=None, lever_rate=None):
        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if lever_rate:
            params['lever_rate'] = lever_rate

        request_path = '/linear-swap-api/v1/swap_switch_lever_rate'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约订单信息（逐仓）
    def linear_order_info(self, order_id=None, client_order_id=None, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_id:
            params['order_id'] = order_id

        request_path = '/linear-swap-api/v1/swap_order_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约订单明细信息（逐仓）
    def linear_order_detail(self, contract_code=None, order_id=None, created_at=None, order_type=None, page_index=None,
                            page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_type:
            params['order_type'] = order_type
        if order_id:
            params['order_id'] = order_id
        if created_at:
            params['created_at'] = created_at
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_order_detail'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约当前未成交委托（逐仓）
    def linear_openorders(self, contract_code=None, page_index=None, page_size=None, sort_by=None, trade_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if sort_by:
            params['sort_by'] = sort_by
        if trade_type:
            params['trade_type'] = trade_type

        request_path = '/linear-swap-api/v1/swap_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约历史委托（逐仓）
    def linear_hisorders(self, contract_code=None, trade_type=None, type=None, status=None, create_date=None,
                         sort_by=None, page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if type:
            params['type'] = type
        if status:
            params['status'] = status
        if create_date:
            params['create_date'] = create_date
        if sort_by:
            params['sort_by'] = sort_by
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询合约历史委托看接口（逐仓）
    def linear_hisorders_exact(self, contract_code=None, trade_type=None, type=None, status=None, order_price_type=None,
                               start_time=None, end_time=None, from_id=None, size=None, direct=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if type:
            params['type'] = type
        if status:
            params['status'] = status
        if order_price_type:
            params['order_price_type'] = order_price_type
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if from_id:
            params['from_id'] = from_id
        if size:
            params['size'] = size
        if direct:
            params['direct'] = direct

        request_path = '/linear-swap-api/v1/swap_hisorders_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约历史成交记录（逐仓）
    def linear_matchresults(self, contract_code=None, trade_type=None, create_date=None, page_index=None,
                            page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_matchresults'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询用户历史成交记录（逐仓）
    def linear_matchresults_exact(self, contract_code=None, trade_type=None, start_time=None, end_time=None,
                                  from_id=None, size=None, direct=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if from_id:
            params['from_id'] = from_id
        if size:
            params['size'] = size
        if direct:
            params['direct'] = direct

        request_path = '/linear-swap-api/v1/swap_matchresults_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约闪电平仓下单（逐仓）
    def linear_lightning_close_position(self, contract_code=None, volume=None, direction=None, client_order_id=None,
                                        order_price_type=None, channel_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if volume:
            params['volume'] = volume
        if direction:
            params['direction'] = direction
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_price_type:
            params['order_price_type'] = order_price_type
        if channel_code:
            params['channel_code'] = channel_code

        request_path = '/linear-swap-api/v1/swap_lightning_close_position'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约计划委托下单（逐仓）
    def linear_trigger_order(self, contract_code=None, trigger_type=None, trigger_price=None, order_price=None,
                             order_price_type=None, volume=None, direction=None, offset=None, lever_rate=None,
                             reduce_only=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if volume:
            params['volume'] = volume
        if direction:
            params['direction'] = direction
        if trigger_type:
            params['trigger_type'] = trigger_type
        if offset:
            params['offset'] = offset
        if trigger_price:
            params['trigger_price'] = trigger_price
        if order_price:
            params['order_price'] = order_price
        if order_price_type:
            params['order_price_type'] = order_price_type
        if lever_rate:
            params['lever_rate'] = lever_rate
        if reduce_only:
            params['reduce_only'] = reduce_only

        request_path = '/linear-swap-api/v1/swap_trigger_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约计划委托撤单（逐仓）
    def linear_trigger_cancel(self, contract_code=None, order_id=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id

        request_path = '/linear-swap-api/v1/swap_trigger_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约计划委托全部撤单（逐仓）
    def linear_trigger_cancelall(self, contract_code=None, direction=None, offset=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset

        request_path = '/linear-swap-api/v1/swap_trigger_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取计划委托当前委托（逐仓）
    def linear_trigger_openorders(self, contract_code=None, page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_size:
            params['page_size'] = page_size
        if page_index:
            params['page_index'] = page_index

        request_path = '/linear-swap-api/v1/swap_trigger_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取计划委托历史委托（逐仓）
    def linear_trigger_hisorders(self, contract_code=None, trade_type=None, status=None, create_date=None, sort_by=None,
                                 page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if status:
            params['status'] = status
        if create_date:
            params['create_date'] = create_date
        if sort_by:
            params['sort_by'] = sort_by
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_trigger_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 对仓位设置止盈止损订单（逐仓）
    def linear_tpsl_order(self, contract_code=None, direction=None, volume=None, tp_trigger_price=None,
                          tp_order_price=None, tp_order_price_type=None,
                          sl_trigger_price=None, sl_order_price=None, sl_order_price_type=None):
        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction
        if volume:
            params['volume'] = volume
        if tp_trigger_price:
            params['tp_trigger_price'] = tp_trigger_price
        if tp_order_price:
            params['tp_order_price'] = tp_order_price
        if tp_order_price_type:
            params['tp_order_price_type'] = tp_order_price_type
        if sl_trigger_price:
            params['sl_trigger_price'] = sl_trigger_price
        if sl_order_price:
            params['sl_order_price'] = sl_order_price
        if sl_order_price_type:
            params['sl_order_price_type'] = sl_order_price_type

        request_path = '/linear-swap-api/v1/swap_tpsl_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 止盈止损订单撤单接口（逐仓）
    def linear_tpsl_cancel(self, contract_code=None, order_id=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id

        request_path = '/linear-swap-api/v1/swap_tpsl_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 止盈止损订单全部撤单（逐仓）
    def linear_tpsl_cancelall(self, contract_code=None, direction=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction

        request_path = '/linear-swap-api/v1/swap_tpsl_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询止盈止损订单当前委托（逐仓）
    def linear_tpsl_openorders(self, contract_code=None, page_index=None, page_size=None, trade_type=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if trade_type:
            params['trade_type'] = trade_type

        request_path = '/linear-swap-api/v1/swap_tpsl_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询止盈止损订单历史委托（逐仓）
    def linear_tpsl_hisorders(self, contract_code=None, status=None, create_date=None, sort_by=None, page_index=None,
                              page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if status:
            params['status'] = status
        if create_date:
            params['create_date'] = create_date
        if sort_by:
            params['sort_by'] = sort_by
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_tpsl_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询开仓单关联的止盈止损订单详情（逐仓）
    def linear_relation_tpsl_order(self, contract_code=None, order_id=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id

        request_path = '/linear-swap-api/v1/swap_relation_tpsl_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托订单下单接口（逐仓）
    def linear_track_order(self, contract_code=None, direction=None, offset=None, lever_rate=None, volume=None,
                           callback_rate=None, active_price=None, order_price_type=None, reduce_only=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        if lever_rate:
            params['lever_rate'] = lever_rate
        if volume:
            params['volume'] = volume
        if callback_rate:
            params['callback_rate'] = callback_rate
        if active_price:
            params['active_price'] = active_price
        if order_price_type:
            params['order_price_type'] = order_price_type
        if reduce_only:
            params['reduce_only'] = reduce_only

        request_path = '/linear-swap-api/v1/swap_track_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托订单撤单接口（逐仓）
    def linear_track_cancel(self, contract_code=None, order_id=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id

        request_path = '/linear-swap-api/v1/swap_track_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托订单全部撤单接口（逐仓）
    def linear_track_cancelall(self, contract_code=None, direction=None, offset=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset

        request_path = '/linear-swap-api/v1/swap_track_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询跟踪委托订单当前委托接口（逐仓）
    def linear_track_openorders(self, contract_code=None, trade_type=None, page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/linear-swap-api/v1/swap_track_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询跟踪委托订单历史委托接口（逐仓）
    def linear_track_hisorders(self, contract_code=None, status=None, trade_type=None, create_date=None,
                               page_index=None, page_size=None, sort_by=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if status:
            params['status'] = status
        if trade_type:
            params['trade_type'] = trade_type
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if sort_by:
            params['sort_by'] = sort_by

        request_path = '/linear-swap-api/v1/swap_track_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约账户信息（全仓）
    def linear_cross_account_info(self, margin_account=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account

        request_path = '/linear-swap-api/v1/swap_cross_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约持仓信息（全仓）
    def linear_cross_position_info(self, contract_code=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_cross_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 批量获取子账户资产信息（全仓）
    def linear_cross_sub_account_info_list(self, margin_account=None, page_index=None, page_size=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        request_path = '/linear-swap-api/v1/swap_cross_sub_account_info_list'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询母账户下所有子账户资产信息 （全仓）
    def linear_cross_sub_account_list(self, margin_account=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        request_path = '/linear-swap-api/v1/swap_cross_sub_account_list'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询母账户下的单个子账户资产信息（全仓）
    def linear_cross_sub_account_info(self, margin_account=None, sub_uid=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if sub_uid:
            params['sub_uid'] = sub_uid
        request_path = '/linear-swap-api/v1/swap_cross_sub_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询母账户下的单个子账户持仓信息（全仓）
    def linear_cross_sub_position_info(self, contract_code=None, sub_uid=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if sub_uid:
            params['sub_uid'] = sub_uid
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_cross_sub_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约划转限制（全仓）
    def linear_cross_transfer_limit(self, margin_account=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        request_path = '/linear-swap-api/v1/swap_cross_transfer_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约持仓量限制（全仓）
    def linear_cross_position_limit(self, contract_code=None, business_type=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_cross_position_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户所有杠杆持仓量限制（逐仓）
    def linear_cross_lever_position_limit(self, business_type=None, contract_type=None, pair=None, contract_code=None,
                                          lever_rate=None):

        params = {}
        if business_type:
            params['business_type'] = business_type
        if contract_type:
            params['contract_type'] = contract_type
        if pair:
            params['pair'] = pair
        if contract_code:
            params['contract_code'] = contract_code
        if lever_rate:
            params['lever_rate'] = lever_rate
        request_path = '/linear-swap-api/v1/swap_cross_lever_position_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户资产和持仓信息（全仓）
    def linear_cross_account_position_info(self, margin_account=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        request_path = '/linear-swap-api/v1/swap_cross_account_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户品种实际可用杠杆倍数（全仓）
    def linear_cross_available_level_rate(self, contract_code=None, business_type=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if business_type:
            params['business_type'] = business_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_cross_available_level_rate'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约下单（全仓）
    def linear_cross_order(self, contract_code=None, pair=None, contract_type=None, client_order_id=None, price=None,
                           volume=None, direction=None, offset=None, lever_rate=None, order_price_type=None,
                           tp_trigger_price=None, tp_order_price=None, tp_order_price_type=None,
                           sl_trigger_price=None, sl_order_price=None, sl_order_price_type=None, channel_code=None,
                           reduce_only=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
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
        if tp_trigger_price:
            params['tp_trigger_price'] = tp_trigger_price
        if tp_order_price:
            params['tp_order_price'] = tp_order_price
        if tp_order_price_type:
            params['tp_order_price_type'] = tp_order_price_type
        if sl_trigger_price:
            params['sl_trigger_price'] = sl_trigger_price
        if sl_order_price:
            params['sl_order_price'] = sl_order_price
        if sl_order_price_type:
            params['sl_order_price_type'] = sl_order_price_type
        if channel_code:
            params['channel_code'] = channel_code
        if reduce_only:
            params['reduce_only'] = reduce_only

        request_path = '/linear-swap-api/v1/swap_cross_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约批量下单（全仓）
    def linear_cross_batchorder(self, orders_data=None):

        params = orders_data
        request_path = '/linear-swap-api/v1/swap_cross_batchorder'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 撤销合约订单（全仓）
    def linear_cross_cancel(self, order_id=None, client_order_id=None, contract_code=None, pair=None,
                            contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_id:
            params['order_id'] = order_id
        request_path = '/linear-swap-api/v1/swap_cross_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 撤销全部合约订单（全仓）
    def linear_cross_cancelall(self, contract_code=None, pair=None, contract_type=None, direction=None, offset=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        request_path = '/linear-swap-api/v1/swap_cross_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约订单信息（全仓）
    def linear_cross_order_info(self, order_id=None, client_order_id=None, contract_code=None, pair=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_id:
            params['order_id'] = order_id
        if pair:
            params['pair'] = pair
        request_path = '/linear-swap-api/v1/swap_cross_order_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约订单明细信息（全仓）
    def linear_cross_order_detail(self, order_id=None, created_at=None, contract_code=None, order_type=None,
                                  page_index=None, page_size=None, pair=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if created_at:
            params['created_at'] = created_at
        if order_id:
            params['order_id'] = order_id
        if order_type:
            params['order_type'] = order_type
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if pair:
            params['pair'] = pair
        request_path = '/linear-swap-api/v1/swap_cross_order_detail'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 切换杠杆倍数（全仓）
    def linear_cross_switch_lever_rate(self, contract_code=None, lever_rate=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if lever_rate:
            params['lever_rate'] = lever_rate
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type

        request_path = '/linear-swap-api/v1/swap_cross_switch_lever_rate'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约当前未成交委托（全仓）
    def linear_cross_openorders(self, contract_code=None, pair=None, page_index=None, page_size=None, trade_type=None,
                                sort_by=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if pair:
            params['pair'] = pair
        if sort_by:
            params['sort_by'] = sort_by
        if trade_type:
            params['trade_type'] = trade_type
        request_path = '/linear-swap-api/v1/swap_cross_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约历史委托（全仓）
    def linear_cross_hisorders(self, contract_code=None, pair=None, trade_type=None, type=None, status=None,
                               create_date=None, sort_by=None, page_index=None, page_size=None):

        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if trade_type:
            params['trade_type'] = trade_type
        if type:
            params['type'] = type
        if status:
            params['status'] = status
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        request_path = '/linear-swap-api/v1/swap_cross_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询合约历史委托看接口（全仓）
    def linear_cross_hisorders_exact(self, contract_code=None, pair=None, trade_type=None, type=None, status=None,
                                     order_price_type=None, start_time=None, end_time=None, from_id=None, size=None,
                                     direct=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if trade_type:
            params['trade_type'] = trade_type
        if type:
            params['type'] = type
        if status:
            params['status'] = status
        if order_price_type:
            params['order_price_type'] = order_price_type
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if from_id:
            params['from_id'] = from_id
        if size:
            params['size'] = size
        if direct:
            params['direct'] = direct
        request_path = '/linear-swap-api/v1/swap_cross_hisorders_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户的合约历史成交记录（全仓）
    def linear_cross_matchresults(self, contract_code=None, pair=None, trade_type=None, create_date=None,
                                  page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if trade_type:
            params['trade_type'] = trade_type
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        request_path = '/linear-swap-api/v1/swap_cross_matchresults'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询用户历史成交记录（全仓）
    def linear_cross_matchresults_exact(self, contract_code=None, pair=None, trade_type=None, start_time=None,
                                        end_time=None, from_id=None, size=None, direct=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if trade_type:
            params['trade_type'] = trade_type
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if from_id:
            params['from_id'] = from_id
        if size:
            params['size'] = size
        if direct:
            params['direct'] = direct
        request_path = '/linear-swap-api/v1/swap_cross_matchresults_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约闪电平仓下单（全仓）
    def linear_cross_lightning_close_position(self, contract_code=None, volume=None, direction=None,
                                              client_order_id=None, order_price_type=None, pair=None,
                                              contract_type=None, channel_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if volume:
            params['volume'] = volume
        if direction:
            params['direction'] = direction
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_price_type:
            params['order_price_type'] = order_price_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        if channel_code:
            params['channel_code'] = channel_code
        request_path = '/linear-swap-api/v1/swap_cross_lightning_close_position'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约计划委托下单（全仓）
    def linear_cross_trigger_order(self, contract_code=None, trigger_type=None, trigger_price=None, order_price=None,
                                   order_price_type=None, volume=None, direction=None, offset=None, lever_rate=None,
                                   pair=None, contract_type=None, reduce_only=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trigger_type:
            params['trigger_type'] = trigger_type
        if trigger_price:
            params['trigger_price'] = trigger_price
        if order_price:
            params['order_price'] = order_price
        if order_price_type:
            params['order_price_type'] = order_price_type
        if volume:
            params['volume'] = volume
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        if lever_rate:
            params['lever_rate'] = lever_rate
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        if reduce_only:
            params['reduce_only'] = reduce_only

        request_path = '/linear-swap-api/v1/swap_cross_trigger_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约计划委托撤单（全仓）
    def linear_cross_trigger_cancel(self, contract_code=None, order_id=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type

        request_path = '/linear-swap-api/v1/swap_cross_trigger_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约计划委托全部撤单（全仓）
    def linear_cross_trigger_cancelall(self, contract_code=None, pair=None, contract_type=None, direction=None,
                                       offset=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        request_path = '/linear-swap-api/v1/swap_cross_trigger_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取计划委托当前委托（全仓）
    def linear_cross_trigger_openorders(self, contract_code=None, pair=None, page_index=None, page_size=None,
                                        trade_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if pair:
            params['pair'] = pair
        if trade_type:
            params['trade_type'] = trade_type
        request_path = '/linear-swap-api/v1/swap_cross_trigger_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取计划委托历史委托（全仓）
    def linear_cross_trigger_hisorders(self, contract_code=None, pair=None, trade_type=None, status=None,
                                       create_date=None, sort_by=None, page_index=None, page_size=None):

        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if status:
            params['status'] = status
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if pair:
            params['pair'] = pair
        request_path = '/linear-swap-api/v1/swap_cross_trigger_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 对仓位设置止盈止损订单（全仓）
    def linear_cross_tpsl_order(self, contract_code=None, direction=None, volume=None, tp_trigger_price=None,
                                tp_order_price=None, tp_order_price_type=None,
                                sl_trigger_price=None, sl_order_price=None, sl_order_price_type=None, pair=None,
                                contract_type=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction
        if volume:
            params['volume'] = volume
        if tp_trigger_price:
            params['tp_trigger_price'] = tp_trigger_price
        if tp_order_price:
            params['tp_order_price'] = tp_order_price
        if tp_order_price_type:
            params['tp_order_price_type'] = tp_order_price_type
        if sl_trigger_price:
            params['sl_trigger_price'] = sl_trigger_price
        if sl_order_price:
            params['sl_order_price'] = sl_order_price
        if sl_order_price_type:
            params['sl_order_price_type'] = sl_order_price_type
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_cross_tpsl_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 止盈止损订单撤单接口（全仓）
    def linear_cross_tpsl_cancel(self, contract_code=None, order_id=None, pair=None, contract_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        request_path = '/linear-swap-api/v1/swap_cross_tpsl_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 止盈止损订单全部撤单（全仓）
    def linear_cross_tpsl_cancelall(self, contract_code=None, pair=None, contract_type=None, direction=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if contract_type:
            params['contract_type'] = contract_type
        if direction:
            params['direction'] = direction
        request_path = '/linear-swap-api/v1/swap_cross_tpsl_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询止盈止损订单当前委托（全仓）
    def linear_cross_tpsl_openorders(self, contract_code=None, page_index=None, page_size=None, pair=None,
                                     trade_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if pair:
            params['pair'] = pair
        if trade_type:
            params['trade_type'] = trade_type
        request_path = '/linear-swap-api/v1/swap_cross_tpsl_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询止盈止损订单历史委托（全仓）
    def linear_cross_tpsl_hisorders(self, contract_code=None, status=None, create_date=None, sort_by=None,
                                    page_index=None, page_size=None, pair=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if status:
            params['status'] = status
        if create_date:
            params['create_date'] = create_date
        if sort_by:
            params['sort_by'] = sort_by
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if pair:
            params['pair'] = pair
        request_path = '/linear-swap-api/v1/swap_cross_tpsl_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询开仓单关联的止盈止损订单详情（全仓）
    def linear_cross_relation_tpsl_order(self, contract_code=None, order_id=None, pair=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id
        if pair:
            params['pair'] = pair
        request_path = '/linear-swap-api/v1/swap_cross_relation_tpsl_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托订单下单接口（全仓）
    def linear_cross_track_order(self, contract_code=None, contract_type=None, pair=None, direction=None, offset=None,
                                 lever_rate=None, volume=None, callback_rate=None, active_price=None,
                                 order_price_type=None, reduce_only=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if contract_type:
            params['contract_type'] = contract_type
        if pair:
            params['pair'] = pair
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        if lever_rate:
            params['lever_rate'] = lever_rate
        if volume:
            params['volume'] = volume
        if callback_rate:
            params['callback_rate'] = callback_rate
        if active_price:
            params['active_price'] = active_price
        if order_price_type:
            params['order_price_type'] = order_price_type
        if reduce_only:
            params['reduce_only'] = reduce_only
        request_path = '/linear-swap-api/v1/swap_cross_track_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托订单撤单接口（全仓）
    def linear_cross_track_cancel(self, contract_code=None, contract_type=None, pair=None, order_id=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if contract_type:
            params['contract_type'] = contract_type
        if pair:
            params['pair'] = pair
        if order_id:
            params['order_id'] = order_id
        request_path = '/linear-swap-api/v1/swap_cross_track_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托订单全部撤单接口（全仓）
    def linear_cross_track_cancelall(self, contract_code=None, contract_type=None, pair=None, direction=None,
                                     offset=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if contract_type:
            params['contract_type'] = contract_type
        if pair:
            params['pair'] = pair
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        request_path = '/linear-swap-api/v1/swap_cross_track_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询跟踪委托订单当前委托接口（全仓）
    def linear_cross_track_openorders(self, contract_code=None, pair=None, trade_type=None, page_index=None,
                                      page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if trade_type:
            params['trade_type'] = trade_type
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        request_path = '/linear-swap-api/v1/swap_cross_track_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询跟踪委托订单历史委托接口（全仓）
    def linear_cross_track_hisorders(self, contract_code=None, pair=None, status=None, trade_type=None,
                                     create_date=None, page_index=None, page_size=None, sort_by=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if pair:
            params['pair'] = pair
        if status:
            params['status'] = status
        if trade_type:
            params['trade_type'] = trade_type
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if sort_by:
            params['sort_by'] = sort_by
        request_path = '/linear-swap-api/v1/swap_cross_track_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取账户总资产估值
    def linear_balance_valuation(self, valuation_asset=None):
        params = {}
        if valuation_asset:
            params['valuation_asset'] = valuation_asset
        request_path = '/linear-swap-api/v1/swap_balance_valuation'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 内部划转接口
    def linear_transfer(self, From=None, to=None, currency=None, margin_account=None, amount=None):

        params = {}
        if From:
            params['from'] = From
        if to:
            params['to'] = to
        if currency:
            params['currency'] = currency
        if margin_account:
            params['margin-account'] = margin_account
        if amount:
            params['amount'] = amount

        request_path = '/v2/account/transfer'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 新增切换持仓模式接口(逐仓)
    def linear_switch_position_mode(self, margin_account=None, position_mode=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if position_mode:
            params['position_mode'] = position_mode

        request_path = '/linear-swap-api/v1/swap_switch_position_mode'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 新增切换持仓模式接口(全仓)
    def linear_cross_switch_position_mode(self, margin_account=None, position_mode=None):

        params = {}
        if margin_account:
            params['margin_account'] = margin_account
        if position_mode:
            params['position_mode'] = position_mode

        request_path = '/linear-swap-api/v1/swap_cross_switch_position_mode'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


# 定义对象t并传入公私钥和URL,供用例直接调用
t = LinearService(URL, ACCESS_KEY, SECRET_KEY)
