#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020/7/31
# @Author  : zhangranghan


from common.util import http_get_request, api_key_post, api_key_get, http_post_request
from config.conf import URL, ACCESS_KEY, SECRET_KEY


class SwapService:

    def __init__(self, url, access_key, secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key

    # =============================================================#
    #                                                              #
    #                        Market Date API                       #
    #                                                              #
    # =============================================================#

    # 获取合约信息
    def swap_contract_info(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_contract_info'
        return http_get_request(url, params)

    # 获取合约指数信息
    def swap_index(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_index'
        return http_get_request(url, params)

    # 获取合约最高限价和最低限价
    def swap_price_limit(self, contract_code=None):
        """
        参数名称         参数类型            必填     描述
        contract_code   string            false    BTC-USD.....
        """
        # params = {'contract_code': contract_code}
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_price_limit'
        return http_get_request(url, params)

    # 获取当前可用合约总持仓量
    def swap_open_interest(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """
        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_open_interest'
        return http_get_request(url, params)

    # 获取行情深度数据   ##tag
    def swap_depth(self, contract_code=None, type=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        type            string            true     step0, step1, step2, step3, step4, step5....
        """

        params = {'contract_code': contract_code,
                  'type': type}

        url = self.__url + '/swap-ex/market/depth'
        return http_get_request(url, params)

    # 获取K线数据    ##tag
    def swap_kline(self, contract_code=None, period=None, size=None, From=None, to=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        period          string            true     K线类型    1min, 5min, 15min, 30min, 60min,4hour,1day, 1mon  |
        size            integer           true     获取数量   |  150  |  [1,2000]  |
        """

        params = {'contract_code': contract_code,
                  'period': period,
                  'size': size,
                  'from': From,
                  'to': to}

        url = self.__url + '/swap-ex/market/history/kline'
        return http_get_request(url, params)

    # 获取K线数据    ##tag
    def swap_history_index(self, symbol=None, period=None, size=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        period          string            true     K线类型    1min, 5min, 15min, 30min, 60min,4hour,1day, 1mon  |
        size            integer           true     获取数量   |  150  |  [1,2000]  |
        """

        params = {}
        if symbol:
            params['symbol'] = symbol
        if period:
            params['period'] = period
        if size:
            params['size'] = size

        url = self.__url + '/index/market/history/index'
        return http_get_request(url, params)

    # 获取聚合行情   ##tag
    def swap_detail_merged(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        """

        params = {'contract_code': contract_code}

        url = self.__url + '/swap-ex/market/detail/merged'
        return http_get_request(url, params)

    # 获取市场最近成交记录  ##tag
    def swap_trade(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        """
        params = {'contract_code': contract_code}

        url = self.__url + '/swap-ex/market/trade'
        return http_get_request(url, params)

    # 批量获取最近的交易记录   ##tag
    def swap_history_trade(self, contract_code=None, size=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        size            number            true     1-2000 ，默认1
        """

        params = {'contract_code': contract_code,
                  'size': size}

        url = self.__url + '/swap-ex/market/history/trade'
        return http_get_request(url, params)

    # 查询合约风险准备金余额和预估分摊比例
    def swap_risk_info(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_risk_info'
        return http_get_request(url, params)

    # 查询合约风险准备金余额历史数据
    def swap_insurance_fund(self, contract_code=None, page_index=None, page_size=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        url = self.__url + '/swap-api/v1/swap_insurance_fund'
        return http_get_request(url, params)

    # 查询平台阶梯调整系数
    def swap_adjustfactor(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_adjustfactor'
        return http_get_request(url, params)

    # 平台持仓量的查询
    def swap_his_open_interest(self, contract_code=None, period=None, size=None, amount_type=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        period          string            true     时间周期类型 | 1小时:"60min"，4小时:"4hour"，12小时:"12hour"，1天:"1day"
        size            int               false    获取数量 | 默认为：48，取值范围 [1,200]
        amount_type     int               true     计价单位 | 1:张，2:币
        """

        params = {'contract_code': contract_code,
                  'period': period,
                  'amount_type': amount_type}
        if size:
            params['size'] = size

        url = self.__url + '/swap-api/v1/swap_his_open_interest'
        return http_get_request(url, params)

    # 平台持仓量的查询
    def swap_ladder_margin(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        period          string            true     时间周期类型 | 1小时:"60min"，4小时:"4hour"，12小时:"12hour"，1天:"1day"
        size            int               false    获取数量 | 默认为：48，取值范围 [1,200]
        amount_type     int               true     计价单位 | 1:张，2:币
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_ladder_margin'
        return http_get_request(url, params)

    # 精英账户多空持仓对比-账户数
    def swap_elite_account_ratio(self, contract_code=None, period=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        period          string            true     周期  | 5min, 15min, 30min, 60min,4hour,1day
        """

        params = {'contract_code': contract_code,
                  'period': period}

        url = self.__url + '/swap-api/v1/swap_elite_account_ratio'
        return http_get_request(url, params)

    # 精英账户多空持仓对比-持仓量
    def swap_elite_position_ratio(self, contract_code=None, period=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     BTC-USD.....
        period          string            true     周期  | 5min, 15min, 30min, 60min,4hour,1day
        """

        params = {'contract_code': contract_code,
                  'period': period}

        url = self.__url + '/swap-api/v1/swap_elite_position_ratio'
        return http_get_request(url, params)

    # 获取强平订单
    def swap_liquidation_orders(self, contract_code=None, trade_type=None, create_date=None, page_index=None,
                                page_size=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        trade_type          int               true       交易类型  |     0:全部,5: 卖出强平,6: 买入强平
        create_date         int               true       日期    7，90（7天或者90天）
        page_index          int               false      页码，不填默认第1页  |  1
        page_size           int               false      每页条数，不填默认20  |  20  | 不得多于50
        """

        params = {'contract_code': contract_code,
                  'trade_type': trade_type,
                  'create_date': create_date}
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        url = self.__url + '/swap-api/v1/swap_liquidation_orders'
        return http_get_request(url, params)

    # 查询系统状态
    def swap_api_state(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_api_state'
        return http_get_request(url, params)

    # 获取合约的资金费率
    def swap_funding_rate(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            true     "BTC-USD",不填查询所有合约
        """

        params = {'contract_code': contract_code}

        url = self.__url + '/swap-api/v1/swap_funding_rate'
        return http_get_request(url, params)

    # 获取合约的历史资金费率
    def swap_historical_funding_rate(self, contract_code=None, page_index=None, page_size=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        page_index          int               false      页码，不填默认第1页  |  1
        page_size           int               false      每页条数，不填默认20  |  20  | 不得多于50
        """

        params = {'contract_code': contract_code}
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        url = self.__url + '/swap-api/v1/swap_historical_funding_rate'
        return http_get_request(url, params)

        # =============================================================#
        #                                                             #
        #                          Trade API                          #
        #                                                             #
        # =============================================================#
    # 获取账户总资产估值
    def swap_balance_valuation(self, valuation_asset=None):
        """
        参数名称           参数类型            必填      描述
        valuation_asset   string            false    "BTC-USD",资产估值币种，不填查默认BTC
        """
        params = {}
        if valuation_asset:
            params['valuation_asset'] = valuation_asset

        request_path = '/swap-api/v1/swap_balance_valuation'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户账户信息
    def swap_account_info(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户持仓信息
    def swap_position_info(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询母账户下所有子账户资产信息
    def swap_sub_account_list(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_sub_account_list'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询单个子账户资产信息
    def swap_sub_account_info(self, contract_code=None, sub_uid=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        sub_uid         long              true     子账户UID
        """

        params = {'sub_uid': sub_uid}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_sub_account_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询单个子账户持仓信息
    def swap_sub_position_info(self, contract_code=None, sub_uid=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        sub_uid         long              true     子账户UID
        """

        params = {'sub_uid': sub_uid}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_sub_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户财务记录
    def swap_financial_record(self, contract_code=None, type=None, create_date=None, page_index=None, page_size=None):
        """
        参数名称         参数类型            必填       描述
        contract_code   string            true      BTC-USD.....
        type            string            false     不填查询全部类型,【查询多类型中间用，隔开】 | 平多：3，平空：4，开仓手续费-吃单：5，开仓手续费-挂单：6，平仓手续费-吃单：7，平仓手续费-挂单：8，交割平多：9，交割平空：10，交割手续费：11，强制平多：12，强制平空：13，从币币转入：14，转出至币币：15，结算未实现盈亏-多仓：16，结算未实现盈亏-空仓：17，穿仓分摊：19，系统：26，活动奖励：28，返利：29，资金费：30
        create_date     int               false     可随意输入正整数，如果参数超过90则默认查询90天的数据
        page_index      int               false     第几页,不填默认第一页
        page_size       int               false     不填默认20，不得多于50
        """

        params = {'contract_code': contract_code}
        if type:
            params['type'] = type
        if create_date:
            params['create_date'] = create_date
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_financial_record'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户当前的下单量限制
    def swap_order_limit(self, contract_code=None, order_price_type=None):
        """
        参数名称              参数类型       必填      描述
        contract_code        string       false    "BTC-USD",不填查询所有合约
        order_price_type     string       true     订单报价类型 | "limit":限价，"opponent":对手价，"lightning":闪电平仓，"optimal_5":最优5档，"optimal_10":最优10档，"optimal_20":最优20档，"fok":FOK订单，"ioc":IOC订单
        """

        params = {'order_price_type': order_price_type}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_order_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户当前的手续费费率
    def swap_fee(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_fee'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户当前的划转限制
    def swap_transfer_limit(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_transfer_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 用户持仓量限制的查询
    def swap_position_limit(self, contract_code=None):
        """
        参数名称         参数类型            必填      描述
        contract_code   string            false    "BTC-USD",不填查询所有合约
        """

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_position_limit'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约下单
    def swap_order(self, contract_code=None, client_order_id=None, price=None, volume=None, direction=None, offset=None,
                   lever_rate=None, order_price_type=None, tp_trigger_price=None, tp_order_price=None,
                   tp_order_price_type=None,
                   sl_trigger_price=None, sl_order_price=None, sl_order_price_type=None, channel_code=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        client_order_id     long              false      客户自己填写和维护，必须为数字
        price               decimal           false      价格
        volume              long              true       委托数量(张)
        direction           string            true       "buy":买 "sell":卖
        offset              string            true       "open":开 "close":平
        lever_rate          int               true       杠杆倍数[“开仓”若有10倍多单，就不能再下20倍多单]
        order_price_type    string            true       订单报价类型 "limit":限价 "opponent":对手价 "post_only":只做maker单,post only下单只受用户持仓数量限制,optimal_5：最优5档、optimal_10：最优10档、optimal_20：最优20档，"fok":FOK订单，"ioc":IOC订单
        """

        params = {'contract_code': contract_code,
                  'volume': volume,
                  'direction': direction,
                  'offset': offset,
                  'lever_rate': lever_rate,
                  'order_price_type': order_price_type}
        if client_order_id:
            params['client_order_id'] = client_order_id
        if price:
            params['price'] = price
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

        request_path = '/swap-api/v1/swap_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 合约批量下单
    def swap_batchorder(self, orders_data=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        client_order_id     long              false      客户自己填写和维护，必须为数字
        price               decimal           false      价格
        volume              long              true       委托数量(张)
        direction           string            true       "buy":买 "sell":卖
        offset              string            true       "open":开 "close":平
        lever_rate          int               true       杠杆倍数[“开仓”若有10倍多单，就不能再下20倍多单]
        order_price_type    string            true       订单报价类型 "limit":限价 "opponent":对手价 "post_only":只做maker单,post only下单只受用户持仓数量限制,optimal_5：最优5档、optimal_10：最优10档、optimal_20：最优20档，"fok":FOK订单，"ioc":IOC订单
        """

        params = orders_data

        request_path = '/swap-api/v1/swap_batchorder'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 撤销订单
    def swap_cancel(self, order_id=None, client_order_id=None, contract_code=None):
        """
        参数名称             参数类型            必填        描述
        order_id            string            false      订单ID(多个订单ID中间以","分隔,一次最多允许撤消20个订单)
        client_order_id     string            false      客户订单ID(多个订单ID中间以","分隔,一次最多允许撤消20个订单)
        contract_code       string            true       BTC-USD.....
        """

        params = {'contract_code': contract_code}
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_id:
            params['order_id'] = order_id

        request_path = '/swap-api/v1/swap_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 全部撤单
    def swap_cancelall(self, contract_code=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        """

        params = {'contract_code': contract_code}

        request_path = '/swap-api/v1/swap_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取合约订单信息
    def swap_order_info(self, order_id=None, client_order_id=None, contract_code=None):
        """
        参数名称             参数类型            必填        描述
        order_id            string            false      订单ID(多个订单ID中间以","分隔,一次最多允许撤消20个订单)
        client_order_id     string            false      客户订单ID(多个订单ID中间以","分隔,一次最多允许撤消20个订单)
        contract_code       string            true       BTC-USD.....
        """

        params = {'contract_code': contract_code}
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_id:
            params['order_id'] = order_id

        request_path = '/swap-api/v1/swap_order_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取订单明细信息
    def swap_order_detail(self, contract_code=None, order_id=None, created_at=None, order_type=None, page_index=None,
                          page_size=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        order_id            long              true       订单ID
        created_at          long              false      下单时间戳
        order_type          int               true       订单类型，1:报单 、 2:撤单 、 3:强平、4:交割
        page_index          int               false      第几页,不填第一页
        page_size           int               false      不填默认20，不得多于50
        """

        params = {'contract_code': contract_code,
                  'order_id': order_id,
                  'order_type': order_type}
        if created_at:
            params['created_at'] = created_at
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_order_detail'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取合约当前未成交委托
    def swap_openorders(self, contract_code=None, page_index=None, page_size=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        page_index          int               false      第几页,不填第一页
        page_size           int               false      不填默认20，不得多于50
        """

        params = {'contract_code': contract_code}
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取合约历史委托
    def swap_hisorders(self, contract_code=None, trade_type=None, type=None, status=None, create_date=None,
                       sort_by=None, page_index=None, page_size=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        trade_type          int               true       交易类型  |    0:全部,1:买入开多,2: 卖出开空,3: 买入平空,4: 卖出平多,5: 卖出强平,6: 买入强平,7:交割平多,8: 交割平空
        type                int               true       类型  |  1:所有订单,2:结束状态的订单
        status              string            true       订单状态  |  可查询多个状态，"3,4,5" , 0:全部,3:未成交, 4: 部分成交,5: 部分成交已撤单,6: 全部成交,7:已撤单
        create_date         int               true       日期  |   可随意输入正整数，如果参数超过90则默认查询90天的数据
        page_index          int               false      页码，不填默认第1页  |  1
        page_size           int               false      每页条数，不填默认20  |  20  | 不得多于50
        """

        params = {'contract_code': contract_code,
                  'trade_type': trade_type,
                  'type': type,
                  'status': status,
                  'create_date': create_date}
        if sort_by:
            params['sort_by'] = sort_by
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取历史成交记录
    def swap_matchresults(self, contract_code=None, trade_type=None, create_date=None, page_index=None, page_size=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        trade_type          int               true       交易类型  |     0:全部,1:买入开多,2: 卖出开空,3: 买入平空,4: 卖出平多,5: 卖出强平,6: 买入强平
        create_date         int               true       日期  |   可随意输入正整数，如果参数超过90则默认查询90天的数据
        page_index          int               false      页码，不填默认第1页  |  1
        page_size           int               false      每页条数，不填默认20  |  20  | 不得多于50
        """

        params = {'contract_code': contract_code,
                  'trade_type': trade_type,
                  'create_date': create_date}
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_matchresults'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 闪电平仓下单
    def swap_lightning_close_position(self, contract_code=None, volume=None, direction=None, client_order_id=None,
                                      order_price_type=None, channel_code=None):
        """
        参数名称             参数类型            必填        描述
        contract_code       string            true       BTC-USD.....
        volume              number            true       委托数量（张）
        direction           string            true       “buy”:买，“sell”:卖
        client_order_id     number            false      客户自己填写和维护，必须保持唯一
        """

        params = {'contract_code': contract_code,
                  'volume': volume,
                  'direction': direction}
        if client_order_id:
            params['client_order_id'] = client_order_id
        if order_price_type:
            params['order_price_type'] = order_price_type
        if channel_code:
            params['channel_code'] = channel_code

        request_path = '/swap-api/v1/swap_lightning_close_position'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询系统是否可用
    def swap_heartbeat(self):

        params = {}
        # colo没有配置
        url = 'http://swap.btcquant.pro' + '/swap/heartbeat'
        return http_get_request(url, params)

    # 获取用户API指标禁用信息
    def swap_api_trading_status(self):
        params = {}

        request_path = '/swap-api/v1/swap_api_trading_status'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 母子划转
    def swap_master_sub_transfer(self, sub_uid=None, contract_code=None, amount=None, type=None, client_order_id=None):

        params = {}
        if sub_uid:
            params['sub_uid'] = sub_uid
        if contract_code:
            params['contract_code'] = contract_code
        if amount:
            params['amount'] = amount
        if type:
            params['type'] = type
        if client_order_id:
            params['client_order_id'] = client_order_id
        request_path = '/swap-api/v1/swap_master_sub_transfer'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 母子划转记录
    def swap_master_sub_transfer_record(self, contract_code=None, transfer_type=None, create_date=None, page_index=None,
                                        page_size=None):
        params = {'contract_code': contract_code,
                  'create_date': create_date}
        if transfer_type:
            params['transfer_type'] = transfer_type
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        request_path = '/swap-api/v1/swap_master_sub_transfer_record'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取基差数据
    def swap_basis(self, contract_code=None, period=None, basis_price_type=None, size=None):

        params = {'contract_code': contract_code,
                  'period': period,
                  'size': size}

        if basis_price_type:
            params['basis_price_type'] = basis_price_type

        url = self.__url + '/index/market/history/swap_basis'
        return http_get_request(url, params)

    # 获取溢价指数k线
    def swap_premium_index_kline(self, contract_code=None, period=None, size=None):

        params = {'contract_code': contract_code,
                  'period': period,
                  'size': size}

        url = self.__url + '/index/market/history/swap_premium_index_kline'
        return http_get_request(url, params)

    # 获取预测资金费率的k线
    def swap_estimated_rate_kline(self, contract_code=None, period=None, size=None):

        params = {'contract_code': contract_code,
                  'period': period,
                  'size': size}

        url = self.__url + '/index/market/history/swap_estimated_rate_kline'
        return http_get_request(url, params)

    # 计划委托下单接口
    def swap_trigger_order(self, contract_code=None, trigger_type=None, trigger_price=None, order_price=None,
                           order_price_type=None, volume=None, direction=None, offset=None, lever_rate=None):

        params = {'contract_code': contract_code,
                  'trigger_type': trigger_type,
                  'trigger_price': trigger_price,
                  'volume': volume,
                  'direction': direction,
                  'offset': offset,
                  'lever_rate': lever_rate}
        if order_price:
            params['order_price'] = order_price
        if order_price_type:
            params['order_price_type'] = order_price_type

        request_path = '/swap-api/v1/swap_trigger_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 计划委托撤单接口
    def swap_trigger_cancel(self, contract_code=None, order_id=None):

        params = {'contract_code': contract_code,
                  'order_id': order_id}

        request_path = '/swap-api/v1/swap_trigger_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 计划委托全部撤单接口
    def swap_trigger_cancelall(self, contract_code=None):

        params = {'contract_code': contract_code}

        request_path = '/swap-api/v1/swap_trigger_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取计划委托当前委托接口
    def swap_trigger_openorders(self, contract_code=None, page_index=None, page_size=None):

        params = {'contract_code': contract_code}

        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_trigger_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取计划委托历史委托接口
    def swap_trigger_hisorders(self, contract_code=None, trade_type=None, status=None, create_date=None, sort_by=None,
                               page_index=None, page_size=None):

        params = {'contract_code': contract_code,
                  'trade_type': trade_type,
                  'status': status,
                  'create_date': create_date}

        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size
        if sort_by:
            params['sort_by'] = sort_by

        request_path = '/swap-api/v1/swap_trigger_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取用户资产和持仓信息
    def swap_account_position_info(self, contract_code=None):
        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        request_path = '/swap-api/v1/swap_account_position_info'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询合约历史委托
    def swap_hisorders_exact(self, contract_code=None, trade_type=None, type=None, status=None, start_time=None,
                             end_time=None, from_id=None, size=None, direct=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if type:
            params['type'] = type
        if status:
            params['status'] = status
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
        request_path = '/swap-api/v1/swap_hisorders_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询用户财务记录
    def swap_financial_record_exact(self, contract_code=None, type=None, start_time=None, end_time=None, from_id=None,
                                    size=None, direct=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if type:
            params['type'] = type
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
        request_path = '/swap-api/v1/swap_financial_record_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 组合查询用户历史成交记录
    def swap_matchresults_exact(self, contract_code=None, trade_type=None, start_time=None, end_time=None, from_id=None,
                                size=None, direct=None):

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
        request_path = '/swap-api/v1/swap_matchresults_exact'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户结算记录
    def swap_user_settlement_records(self, contract_code=None, start_time=None, end_time=None, page_index=None,
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
        request_path = '/swap-api/v1/swap_user_settlement_records'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询用户品种实际可用杠杆倍数
    def swap_available_level_rate(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        request_path = '/swap-api/v1/swap_available_level_rate'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 切换杠杆倍数
    def swap_switch_lever_rate(self, contract_code=None, lever_rate=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if lever_rate:
            params['lever_rate'] = lever_rate
        request_path = '/swap-api/v1/swap_switch_lever_rate'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 平台结算记录
    def swap_settlement_records(self, contract_code=None, start_time=None, end_time=None, page_index=None,
                                page_size=None):

        params = {'contract_code': contract_code}

        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        url = self.__url + '/swap-api/v1/swap_settlement_records'
        return http_get_request(url, params)

    # 获取预估结算价
    def swap_estimated_settlement_price(self, contract_code=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_estimated_settlement_price'
        return http_get_request(url, params)

    # 获取市场最优挂单
    def swap_bbo(self, contract_code=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-ex/market/bbo'
        return http_get_request(url, params)

    # 批量获取聚合行情
    def swap_batch_merged(self, contract_code=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-ex/market/detail/batch_merged'
        return http_get_request(url, params)

    # 获取标记价格的K线数据
    def swap_mark_price_kline(self, contract_code=None, period=None, size=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if period:
            params['period'] = period
        if size:
            params['size'] = size

        url = self.__url + '/index/market/history/swap_mark_price_kline'
        return http_get_request(url, params)

    # 批量获取合约的资金费率
    def swap_batch_funding_rate(self, contract_code=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code

        url = self.__url + '/swap-api/v1/swap_batch_funding_rate'
        return http_get_request(url, params)

    # 对仓位设置止盈止损订单接口
    def swap_tpsl_order(self, contract_code=None, volume=None, direction=None, tp_trigger_price=None,
                        tp_order_price=None, tp_order_price_type=None,
                        sl_trigger_price=None, sl_order_price=None, sl_order_price_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if volume:
            params['volume'] = volume
        if direction:
            params['direction'] = direction
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

        request_path = '/swap-api/v1/swap_tpsl_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 止盈止损订单撤单接口
    def swap_tpsl_cancel(self, contract_code=None, order_id=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id

        request_path = '/swap-api/v1/swap_tpsl_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 止盈止损订单全部撤单接口
    def swap_tpsl_cancelall(self, contract_code=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code

        request_path = '/swap-api/v1/swap_tpsl_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询止盈止损订单当前委托接口
    def swap_tpsl_openorders(self, contract_code=None, page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_tpsl_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询止盈止损订单历史委托接口
    def swap_tpsl_hisorders(self, contract_code=None, status=None, create_date=None, sort_by=None, page_index=None,
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

        request_path = '/swap-api/v1/swap_tpsl_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 查询开仓单关联的止盈止损订单详情接口
    def swap_relation_tpsl_order(self, contract_code=None, order_id=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id

        request_path = '/swap-api/v1/swap_relation_tpsl_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 批量设置子账户交易权限
    def swap_sub_auth(self, sub_uid=None, sub_auth=None):

        params = {}

        if sub_uid:
            params['sub_uid'] = sub_uid
        if sub_auth:
            params['sub_auth'] = sub_auth

        request_path = '/swap-api/v1/swap_sub_auth'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 批量获取子账户资产信息
    def swap_sub_account_info_list(self, contract_code=None, page_index=None, page_size=None):

        params = {}

        if contract_code:
            params['contract_code'] = contract_code
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_sub_account_info_list'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托下单
    def swap_track_order(self, contract_code=None, volume=None, direction=None, offset=None, lever_rate=None,
                         callback_rate=None, active_price=None, order_price_type=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if volume:
            params['volume'] = volume
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset
        if lever_rate:
            params['lever_rate'] = lever_rate
        if callback_rate:
            params['callback_rate'] = callback_rate
        if active_price:
            params['active_price'] = active_price
        if order_price_type:
            params['order_price_type'] = order_price_type

        request_path = '/swap-api/v1/swap_track_order'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托撤单
    def swap_track_cancel(self, contract_code=None, order_id=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if order_id:
            params['order_id'] = order_id

        request_path = '/swap-api/v1/swap_track_cancel'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 跟踪委托全部撤单
    def swap_track_cancelall(self, contract_code=None, direction=None, offset=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if direction:
            params['direction'] = direction
        if offset:
            params['offset'] = offset

        request_path = '/swap-api/v1/swap_track_cancelall'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取跟踪委托当前委托
    def swap_track_openorders(self, contract_code=None, trade_type=None, page_index=None, page_size=None):

        params = {}
        if contract_code:
            params['contract_code'] = contract_code
        if trade_type:
            params['trade_type'] = trade_type
        if page_index:
            params['page_index'] = page_index
        if page_size:
            params['page_size'] = page_size

        request_path = '/swap-api/v1/swap_track_openorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取跟踪委托当前委托
    def swap_track_hisorders(self, contract_code=None, status=None, trade_type=None, create_date=None, page_index=None,
                             page_size=None, sort_by=None):

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

        request_path = '/swap-api/v1/swap_track_hisorders'
        return api_key_post(self.__url, request_path, params, self.__access_key, self.__secret_key)


# 定义t并传入公私钥和URL,供用例直接调用
t = SwapService(URL, ACCESS_KEY, SECRET_KEY)
