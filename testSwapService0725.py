#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022/3/15
# @Author  : tanwenyan  110

import inspect
from pprint import pprint
from common.SwapService import t as st

# 反向永续
# 私有接口
'''
725 test case
'''
# 1
# pprint(st.swap_sub_account_list())
# pprint(st.swap_sub_account_list(contract_code='ETH-USD'))
# pprint(st.swap_sub_account_list(contract_code='BTC-USD'))
# pprint(st.swap_sub_account_list(contract_code='LTC-USD'))

# 2
# pprint(st.swap_sub_account_info(sub_uid='112287539'))
# pprint(st.swap_sub_account_info(sub_uid='112287539',contract_code='BTC-USD'))
# pprint(st.swap_sub_account_info(sub_uid='112287539',contract_code='ETH-USD'))
# pprint(st.swap_sub_account_info(sub_uid='112287539',contract_code='LTC-USD'))

# 3
# pprint(st.swap_balance_valuation())
# pprint(st.swap_balance_valuation(valuation_asset='BTC'))
# pprint(st.swap_balance_valuation(valuation_asset='USD'))
# pprint(st.swap_balance_valuation(valuation_asset='CNY'))
# pprint(st.swap_balance_valuation(valuation_asset='EUR'))
# pprint(st.swap_balance_valuation(valuation_asset='GBP'))
# pprint(st.swap_balance_valuation(valuation_asset='VND'))
# pprint(st.swap_balance_valuation(valuation_asset='HKD'))
# pprint(st.swap_balance_valuation(valuation_asset='TWD'))
# pprint(st.swap_balance_valuation(valuation_asset='MYR'))
# pprint(st.swap_balance_valuation(valuation_asset='SGD'))
# pprint(st.swap_balance_valuation(valuation_asset='KRW'))
# pprint(st.swap_balance_valuation(valuation_asset='RUB'))
# pprint(st.swap_balance_valuation(valuation_asset='TRY'))
'''
"BTC","USDT","USD","CNY","EUR","GBP","VND","HKD","TWD","MYR","SGD","KRW","RUB","TRY"
'''
# 4.1
# pprint(st.swap_account_info())
# pprint(st.swap_account_info(contract_code='BTC-USD'))
# pprint(st.swap_account_info(contract_code='LTC-USD'))
# pprint(st.swap_account_info(contract_code='ETH-USD'))
# pprint(st.swap_account_info(contract_code='EOS-USD'))
# 4.2
# pprint(st.swap_account_position_info(contract_code='BTC-USD'))
# pprint(st.swap_account_position_info(contract_code='LTC-USD'))
# pprint(st.swap_account_position_info(contract_code='ETH-USD'))
# pprint(st.swap_account_position_info(contract_code='EOS-USD'))
# 4.3
# pprint(st.swap_position_info())
# pprint(st.swap_position_info(contract_code='BTC-USD'))
# pprint(st.swap_position_info(contract_code='LTC-USD'))
# pprint(st.swap_position_info(contract_code='ETH-USD'))
4.4
pprint(st.swap_sub_position_info(sub_uid='112287497'))#112287497，112287825，112287839
pprint(st.swap_sub_position_info(sub_uid='112287539', contract_code='BTC-USD'))
pprint(st.swap_sub_position_info(sub_uid='112287539', contract_code='ETH-USD'))

# 5
#guadan
# pprint(st.swap_order(contract_code='BTC-USD', volume='5', direction='buy', offset='open', lever_rate='5',
#                      # order_price_type='limit', price='40001.6'))
#
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='limit', price='32000'))  # 957047923417862144
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='opponent'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='optimal_5', tp_order_price_type='limit', tp_trigger_price='50000',
#                      tp_order_price='50001', sl_trigger_price='40000', sl_order_price_type='limit',
#                      sl_order_price='40002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='optimal_10', tp_order_price_type='limit', tp_trigger_price='9999',
#                      tp_order_price='9999', sl_trigger_price='50000', sl_order_price_type='limit',
#                      sl_order_price='50002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='optimal_20', tp_order_price_type='limit', tp_trigger_price='50000',
#                      tp_order_price='50002', sl_trigger_price='20000', sl_order_price_type='limit',
#                      sl_order_price='20002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='post_only', price='42000', tp_order_price_type='limit', tp_trigger_price='30000',
#                      tp_order_price='30001', sl_trigger_price='50000', sl_order_price_type='limit',
#                      sl_order_price='50002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='ioc', price='42000', tp_order_price_type='limit', tp_trigger_price='50000',
#                      tp_order_price='50001', sl_trigger_price='40000', sl_order_price_type='limit',
#                      sl_order_price='40002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='opponent_ioc', tp_order_price_type='limit', tp_trigger_price='30000',
#                      tp_order_price='30001', sl_trigger_price='50000', sl_order_price_type='limit',
#                      sl_order_price='50002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='optimal_5_ioc', tp_order_price_type='limit', tp_trigger_price='50000',
#                      tp_order_price='50001', sl_trigger_price='40000', sl_order_price_type='limit',
#                      sl_order_price='40002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='optimal_10_ioc', tp_order_price_type='limit', tp_trigger_price='9999',
#                      tp_order_price='9999', sl_trigger_price='50000', sl_order_price_type='limit',
#                      sl_order_price='5002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='optimal_20_ioc', tp_order_price_type='limit', tp_trigger_price='50000',
#                      tp_order_price='50001', sl_trigger_price='40000', sl_order_price_type='limit',
#                      sl_order_price='40002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='fok', price='42000', tp_order_price_type='limit', tp_trigger_price='33000',
#                      tp_order_price='33001', sl_trigger_price='50000', sl_order_price_type='limit',
#                      sl_order_price='50002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='opponent_fok', tp_order_price_type='limit', tp_trigger_price='50000',
#                      tp_order_price='50001', sl_trigger_price='40000', sl_order_price_type='limit',
#                      sl_order_price='40002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='optimal_5_fok', tp_order_price_type='limit', tp_trigger_price='39903',
#                      tp_order_price='39901', sl_trigger_price='50000', sl_order_price_type='limit',
#                      sl_order_price='50002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='open', lever_rate='5',
#                      order_price_type='optimal_10_fok', tp_order_price_type='limit', tp_trigger_price='50000',
#                      tp_order_price='50001', sl_trigger_price='40000', sl_order_price_type='limit',
#                      sl_order_price='40002'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='sell', offset='open', lever_rate='5',
#                      order_price_type='optimal_20_fok', tp_order_price_type='limit', tp_trigger_price='1199',
#                      tp_order_price='1199', sl_trigger_price='50000', sl_order_price_type='limit',
#                      sl_order_price='50002'))
# pprint(st.swap_batchorder({"orders_data": [{"contract_code": 'BTC-USD', "client_order_id": '', "price": '1300',
#                                             "volume": '1', "direction": 'buy', "offset": 'open', "lever_rate": '5',
#                                             "order_price_type": 'limit'}]}))
# pprint(st.swap_batchorder(
#     {
#         "orders_data": [{
#             "contract_code": 'BTC-USD',
#             "client_order_id": '',
#             "price": '33000',
#             "volume": '1',
#             "direction": 'buy',
#             "offset": 'open',
#             "lever_rate": '5',
#             "order_price_type": 'limit'
#         },
#             {
#                 "contract_code": 'BTC-USD',
#                 "client_order_id": '',
#                 "price": '34000',
#                 "volume": '1',
#                 "direction": 'sell',
#                 "offset": 'open',
#                 "lever_rate": '5',
#                 "order_price_type": 'post_only',
#                 'tp_order_price_type': 'limit',
#                 'tp_trigger_price': '33000',
#                 'tp_order_price': '33001',
#                 'sl_trigger_price': '50000',
#                 'sl_order_price_type': 'limit',
#                 'sl_order_price': '50002'
#             }]
#     }))
#
# pprint(st.swap_lightning_close_position(contract_code='BTC-USD', volume='1', direction='buy', order_price_type='lightning'))
# pprint(st.swap_lightning_close_position(contract_code='BTC-USD', volume='2', direction='sell', order_price_type='lightning_ioc'))
# pprint(st.swap_lightning_close_position(contract_code='BTC-USD', volume='3', direction='buy', order_price_type='lightning_fok'))

## originaloriginaloriginaloriginal

# pprint(st.swap_balance_valuation())
# pprint(st.swap_balance_valuation(valuation_asset='BTC'))
# pprint(st.swap_balance_valuation(valuation_asset='USDT'))
# pprint(st.swap_balance_valuation(valuation_asset='USD'))
# pprint(st.swap_account_info())
# pprint(st.swap_account_info(contract_code='BTC-USD'))
# pprint(st.swap_account_info(contract_code='BTC-USD'))
# pprint(st.swap_account_info(contract_code='ETH-USD'))
#
# pprint(st.swap_position_info(contract_code='ETH-USD'))
# pprint(st.swap_sub_auth(sub_uid='296145790,112283148', sub_auth=1))
# pprint(st.swap_sub_auth(sub_uid='296145790', sub_auth=1))
# pprint(st.swap_sub_account_info_list(contract_code='ETH-USD'))
# pprint(st.swap_sub_account_list())
# pprint(st.swap_sub_account_list(contract_code='ETH-USD'))
# pprint(st.swap_sub_account_list(contract_code='BTC-USD'))
#
# # pprint(st.swap_sub_account_info(sub_uid='296145790'))
# pprint(st.swap_sub_position_info(sub_uid='296145790'))
# pprint(st.swap_financial_record(contract_code='BTC-USD', create_date='90'))
# pprint(st.swap_financial_record_exact(contract_code='BTC-USD', size=10, direct='next'))
# pprint(st.swap_user_settlement_records(contract_code='BTC-USD'))
# pprint(st.swap_order_limit(order_price_type='limit'))
# pprint(st.swap_order_limit(order_price_type='lightning'))
# pprint(st.swap_order_limit(order_price_type='optimal_5'))
# pprint(st.swap_fee())
# pprint(st.swap_fee(contract_code='BTC-USD'))
# pprint(st.swap_transfer_limit())
# pprint(st.swap_transfer_limit(contract_code='BTC-USD'))
# pprint(st.swap_position_limit())
# pprint(st.swap_position_limit(contract_code='BTC-USD'))
# pprint(st.swap_account_position_info(contract_code='BTC-USD'))
#
# pprint(st.swap_master_sub_transfer(sub_uid='296145790', contract_code='BTC-USD', amount='1008', type='master_to_sub'))
# pprint(st.swap_master_sub_transfer_record(contract_code='BTC-USD', create_date='90'))
# pprint(st.swap_api_trading_status())
# # pprint(st.swap_api_trading_status(contract_code='BTC-USD'))
# pprint(st.swap_available_level_rate())
# pprint(st.swap_available_level_rate(contract_code='BTC-USD'))
# pprint(st.swap_order(contract_code='BTC-USD', volume='1', direction='buy', offset='both', lever_rate='10',
#                      order_price_type='limit', price='1200'))
# pprint(st.swap_batchorder({"orders_data": [{"contract_code": 'BTC-USD', "client_order_id": '', "price": '1300',
#                                             "volume": '1', "direction": 'buy', "offset": 'both', "lever_rate": '5',
#                                             "order_price_type": 'limit'}]}))
# pprint(st.swap_cancel(contract_code='BTC-USD', order_id='953329103506190336'))
# pprint(st.swap_cancelall(contract_code='BTC-USD'))
# pprint(st.swap_switch_lever_rate(contract_code='BTC-USD', lever_rate='1'))
# pprint(st.swap_order_info(contract_code='BTC-USD', order_id='953329103506190336'))
# pprint(st.swap_order_detail(contract_code='BTC-USD', order_id='953329103506190336'))
# pprint(st.swap_openorders(contract_code='BTC-USD'))
# pprint(st.swap_hisorders(contract_code='BTC-USD', trade_type='0', type='1', status='3,4,5', create_date='90'))
# pprint(st.swap_hisorders_exact(contract_code='BTC-USD', trade_type='0', type='1', status='3,4,5'))
# pprint(st.swap_matchresults(contract_code='BTC-USD', trade_type='0', create_date='90'))
# pprint(st.swap_matchresults_exact(contract_code='BTC-USD', trade_type='0'))
#
# pprint(st.swap_lightning_close_position(contract_code='BTC-USD', volume='1', direction='6'))
# pprint(st.swap_trigger_order(contract_code='BTC-USD', trigger_type='ge', trigger_price='1', order_price='1001',
#                              volume='1', direction='buy', offset='both'))
# pprint(st.swap_trigger_cancel(contract_code='BTC-USD', order_id='953329103506190336'))
# pprint(st.swap_trigger_cancelall(contract_code='BTC-USD'))
# pprint(st.swap_trigger_openorders(contract_code='BTC-USD'))
# pprint(st.swap_trigger_hisorders(contract_code='BTC-USD', trade_type='0', create_date='90', status='0'))
# pprint(st.swap_tpsl_order(contract_code='BTC-USD', volume='1', direction='6'))
# pprint(st.swap_tpsl_cancel(contract_code='BTC-USD', order_id='953329103506190336'))
# pprint(st.swap_tpsl_cancelall(contract_code='BTC-USD'))
# pprint(st.swap_tpsl_openorders(contract_code='BTC-USD'))
# pprint(st.swap_tpsl_hisorders(contract_code='BTC-USD', create_date='90', status='0'))
# pprint(st.swap_relation_tpsl_order(contract_code='BTC-USD', order_id='953329103506190336'))
# pprint(st.swap_track_order(contract_code='BTC-USD', callback_rate='0.01', active_price='1',
#                            order_price_type='optimal_5',
#                            volume='1', direction='buy', offset='both', lever_rate='5'))
# pprint(st.swap_track_cancel(contract_code='BTC-USD', order_id='953375774726262786'))
# pprint(st.swap_track_cancelall(contract_code='BTC-USD'))
# pprint(st.swap_track_openorders(contract_code='BTC-USD'))
# pprint(st.swap_track_hisorders(contract_code='BTC-USD', create_date='90', status='0', trade_type='0'))
#
# # # 公共接口
# pprint(st.swap_contract_info())
# pprint(st.swap_contract_info(contract_code='BTC-USD'))
# pprint(st.swap_index())
# pprint(st.swap_index(contract_code='BTC-USD'))
# pprint(st.swap_price_limit())
# pprint(st.swap_price_limit(contract_code='BTC-USD'))
# pprint(st.swap_open_interest())
# pprint(st.swap_open_interest(contract_code='BTC-USD'))
# pprint(st.swap_risk_info())
# pprint(st.swap_risk_info(contract_code='BTC-USD'))
# pprint(st.swap_insurance_fund(contract_code='BTC-USD'))
# pprint(st.swap_adjustfactor())
# pprint(st.swap_adjustfactor(contract_code='BTC-USD'))
# pprint(st.swap_his_open_interest(contract_code='BTC-USD', period='60min', amount_type=1))
# pprint(st.swap_ladder_margin())
# pprint(st.swap_ladder_margin(contract_code='BTC-USD', ))
# pprint(st.swap_elite_account_ratio(period='60min', contract_code='BTC-USD'))
# pprint(st.swap_elite_position_ratio(period='60min', contract_code='BTC-USD'))
# pprint(st.swap_liquidation_orders(contract_code='BTC-USD', trade_type='0', create_date=90))
# pprint(st.swap_settlement_records(contract_code='ETH-USD'))
# pprint(st.swap_estimated_settlement_price())
# pprint(st.swap_estimated_settlement_price(contract_code='ETH-USD'))
# pprint(st.swap_api_state())
# pprint(st.swap_api_state(contract_code='BTC-USD'))
# pprint(st.swap_funding_rate(contract_code='BTC-USD'))
# pprint(st.swap_batch_funding_rate())
# pprint(st.swap_batch_funding_rate(contract_code='BTC-USD'))
# pprint(st.swap_historical_funding_rate(contract_code='BTC-USD'))
# pprint(st.swap_depth(contract_code='BTC-USD', type='step1'))
# pprint(st.swap_depth(contract_code='BTC-USD', type='step0'))
# pprint(st.swap_bbo())
# pprint(st.swap_bbo(contract_code='BTC-USD'))
#
# pprint(st.swap_kline(contract_code='BTC-USD', period='1day', size='5'))
# pprint(st.swap_detail_merged(contract_code='ETH-USD'))
# pprint(st.swap_detail_merged(contract_code='BTC-USD'))
# pprint(st.swap_detail_batch_merged())
# pprint(st.swap_detail_batch_merged(contract_code='ETH-USD'))
# pprint(st.swap_detail_batch_merged(contract_code='BTC-USD'))
# pprint(st.swap_basis(contract_code='BTC-USD', period='1day', basis_price_type='open', size='5'))
# pprint(st.swap_premium_index_kline(contract_code='BTC-USD', period='1day', size='10'))
# pprint(st.swap_premium_index_kline(contract_code='BTC-USD', period='1min', size='10'))
# pprint(st.swap_estimated_rate_kline(contract_code='BTC-USD', period='1day', size='10'))
# pprint(st.swap_estimated_rate_kline(contract_code='BTC-USD', period='1min', size='10'))
# pprint(st.swap_mark_price_kline(contract_code='BTC-USD', period='1day', size='10'))
# pprint(st.swap_mark_price_kline(contract_code='BTC-USD', period='1min', size='10'))
# pprint(st.swap_trade(contract_code='BTC-USD'))
# pprint(st.swap_trade(contract_code='ETH-USD'))
# pprint(st.swap_history_trade(contract_code='BTC-USD', size='10'))
# pprint(st.swap_history_index(symbol='BTC-USD', period='1min', size='10'))
# pprint(st.swap_history_index(symbol='BTC-USD', period='1day', size='10'))
