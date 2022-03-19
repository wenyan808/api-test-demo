#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022/3/15
# @Author  : tanwenyan 116

from pprint import pprint
from common.ContractService import t as ct

# 交割合约
# 私有接口
pprint(ct.contract_account_info())
pprint(ct.contract_account_info(symbol='BTC'))
pprint(ct.contract_account_info(symbol='ETH'))
pprint(ct.contract_account_info(symbol='EOS'))
pprint(ct.contract_position_info(symbol='ETH'))
pprint(ct.contract_sub_auth(sub_uid='112283122,112283148', sub_auth=1))
pprint(ct.contract_sub_auth(sub_uid='112283148', sub_auth=1))
pprint(ct.contract_sub_account_info_list(symbol='ETH'))
pprint(ct.contract_sub_account_list())
pprint(ct.contract_sub_account_list(symbol='ETH'))
pprint(ct.contract_sub_account_list(symbol='BTC'))
pprint(ct.contract_sub_account_info(sub_uid='112283148'))
pprint(ct.contract_sub_position_info(sub_uid='112283148'))
pprint(ct.contract_financial_record(symbol='BTC'))
pprint(ct.contract_financial_record_exact(symbol='BTC'))
pprint(ct.contract_user_settlement_records(symbol='BTC'))
pprint(ct.contract_order_limit(symbol='BTC', order_price_type='FOK'))
pprint(ct.contract_fee(symbol='BTC'))
pprint(ct.contract_fee())
pprint(ct.contract_transfer_limit())
pprint(ct.contract_position_limit())
pprint(ct.contract_account_position_info())
pprint(ct.contract_transfer_limit(symbol='BTC'))
pprint(ct.contract_position_limit(symbol='BTC'))
pprint(ct.contract_account_position_info(symbol='BTC'))

pprint(ct.contract_master_sub_transfer(sub_uid='296145790', symbol='BTC', amount='1008', type='macter_to_sub'))
pprint(ct.contract_master_sub_transfer_record(symbol='BTC', create_date='90'))
pprint(ct.contract_api_trading_status())
pprint(ct.contract_available_level_rate())
pprint(ct.contract_available_level_rate(symbol='BTC'))

pprint(ct.contract_order(symbol='BTC', contract_type='this_week', volume='1', direction='buy', offset='both',
                         lever_rate='10',
                         order_price_type='limit', price='1200'))
pprint(ct.contract_batchorder({
    "orders_data": [{
        "symbol": 'BTC',
        "contract_type": 'this_week',
        "price": '1300',
        "volume": '1',
        "direction": 'buy',
        "offset": 'both',
        "lever_rate": '5',
        "order_price_type": 'limit'
    }]
}))
pprint(ct.contract_cancel(symbol='BTC', order_id='953329103506190336'))
pprint(ct.contract_cancelall(symbol='BTC'))
pprint(ct.contract_switch_lever_rate(symbol='BTC', lever_rate='1'))
pprint(ct.contract_order_info(symbol='BTC', order_id='953329103506190336'))
pprint(ct.contract_order_detail(symbol='BTC', order_id='953329103506190336'))
pprint(ct.contract_openorders(symbol='BTC'))
pprint(ct.contract_hisorders(symbol='BTC', trade_type='0', type='1', status='3,4,5', create_date='90'))
pprint(ct.contract_hisorders_exact(symbol='BTC', trade_type='0', type='1', status='3,4,5'))
pprint(ct.contract_matchresults(symbol='BTC', trade_type='0', create_date='90'))
pprint(ct.contract_matchresults_exact(symbol='BTC', trade_type='0'))
pprint(ct.contract_lightning_close_position(symbol='BTC', volume='1', direction='6'))
pprint(ct.contract_trigger_order(symbol='BTC', trigger_type='ge', trigger_price='1', order_price='1001',
                             volume='1', direction='buy', offset='both'))
pprint(ct.contract_trigger_cancel(symbol='BTC', order_id='953329103506190336'))
pprint(ct.contract_trigger_cancelall(symbol='BTC'))
pprint(ct.contract_trigger_openorders(symbol='BTC'))
pprint(ct.contract_trigger_hisorders(symbol='BTC', trade_type='0', create_date='90', status='0'))

pprint(ct.contract_tpsl_order(symbol='BTC', volume='1', direction='6'))
pprint(ct.contract_tpsl_cancel(symbol='BTC', order_id='953329103506190336'))
pprint(ct.contract_tpsl_cancelall(symbol='BTC'))
pprint(ct.contract_tpsl_openorders(symbol='BTC'))
pprint(ct.contract_tpsl_hisorders(symbol='BTC', create_date='90', status='0'))
pprint(ct.contract_relation_tpsl_order(symbol='BTC', order_id='953329103506190336'))
pprint(ct.contract_track_order(symbol='BTC', callback_rate='0.01', active_price='1',
                           order_price_type='optimal_5',
                           volume='1', direction='buy', offset='both', lever_rate='5'))
pprint(ct.contract_track_cancel(symbol='BTC', order_id='953375774726262786'))
pprint(ct.contract_track_cancelall(symbol='BTC'))
pprint(ct.contract_track_openorders(symbol='BTC'))
pprint(ct.contract_track_hisorders(symbol='BTC', create_date='90', status='0', trade_type='0'))
pprint(ct.transfer())

# '''公共接口'''
pprint(ct.contract_contract_info(symbol='BTC', contract_type='quarter'))
pprint(ct.contract_contract_info(symbol='BTC', contract_type='this_week'))
pprint(ct.contract_contract_info(symbol='ETH', contract_type='next_week'))
pprint(ct.contract_contract_info(symbol='ETH', contract_type='next_quarter'))
pprint(ct.contract_index())
pprint(ct.contract_index(symbol='BTC'))
pprint(ct.contract_price_limit(symbol='BTC', contract_type='quarter'))
pprint(ct.contract_price_limit(symbol='BTC', contract_type='this_week'))
pprint(ct.contract_price_limit(symbol='ETH', contract_type='next_week'))
pprint(ct.contract_price_limit(symbol='ETH', contract_type='next_quarter'))
pprint(ct.contract_open_interest(symbol='BTC', contract_type='quarter'))
pprint(ct.contract_open_interest(symbol='BTC', contract_type='this_week'))
pprint(ct.contract_open_interest(symbol='ETH', contract_type='next_week'))
pprint(ct.contract_open_interest(symbol='ETH', contract_type='next_quarter'))
pprint(ct.contract_delivery_price(symbol='ETH'))
pprint(ct.contract_risk_info(symbol='ETH'))
pprint(ct.contract_risk_info())
pprint(ct.contract_insurance_fund(symbol='BTC'))
pprint(ct.contract_adjustfactor(symbol='BTC'))
pprint(ct.contract_adjustfactor())
pprint(ct.contract_his_open_interest(symbol='BTC', period='60min', contract_type='quarter', amount_type=1, size=48))
pprint(ct.contract_ladder_margin(symbol='BTC'))
pprint(ct.contract_ladder_margin())
pprint(ct.contract_elite_account_ratio(symbol='BTC', period='60min'))
pprint(ct.contract_elite_position_ratio(symbol='BTC', period='60min'))
pprint(ct.contract_liquidation_orders(symbol='BTC', trade_type='0', create_date=90))
pprint(ct.contract_settlement_records(symbol='BTC'))
pprint(ct.contract_estimated_settlement_price())
pprint(ct.contract_estimated_settlement_price(symbol='BTC'))
pprint(ct.contract_api_state(symbol='BTC'))
pprint(ct.contract_depth(symbol='BTC_CW', type='step1'))
pprint(ct.contract_market_bbo(symbol='BTC_CW'))
pprint(ct.contract_market_bbo(symbol='BTC_NW'))
pprint(ct.contract_market_bbo(symbol='BTC_CQ'))
pprint(ct.contract_market_bbo(symbol='BTC_NQ'))
pprint(ct.contract_kline(symbol='BTC', period='1day', size='5'))
pprint(ct.contract_detail_merged(symbol='BTC_CW'))
pprint(ct.contract_detail_merged(symbol='BTC_NW'))
pprint(ct.contract_detail_merged(symbol='BTC_CQ'))
pprint(ct.contract_detail_merged(symbol='BTC_NQ'))
pprint(ct.contract_detail_batch_merged(symbol='BTC_CW'))
pprint(ct.contract_detail_batch_merged(symbol='BTC_NW'))
pprint(ct.contract_detail_batch_merged(symbol='BTC_CQ'))
pprint(ct.contract_detail_batch_merged(symbol='BTC_NQ'))
pprint(ct.contract_trade(symbol='BTC_CW'))
pprint(ct.contract_trade(symbol='BTC_NW'))
pprint(ct.contract_trade(symbol='BTC_CQ'))
pprint(ct.contract_trade(symbol='BTC_NQ'))
pprint(ct.contract_history_trade(symbol='BTC_CW', size='10'))
pprint(ct.contract_history_trade(symbol='BTC_NW', size='10'))
pprint(ct.contract_history_trade(symbol='BTC_CQ', size='10'))
pprint(ct.contract_history_trade(symbol='BTC_NQ', size='10'))
pprint(ct.contract_history_index(symbol='BTC', period='1day', size=20))
pprint(ct.contract_mark_price_kline(symbol='BTC', period='30min', size=20))
pprint(ct.contract_basis(symbol='BTC', period='1day', size='10'))
