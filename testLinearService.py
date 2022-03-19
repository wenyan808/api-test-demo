#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022/3/15
# @Author  : tanwenyan 146

from pprint import pprint
from common.LinearService import t as lt

# 正向永续
# 私有接口
# pprint(lt.linear_account_info())
# pprint(lt.linear_account_info(contract_code='BTC-USDT'))
# pprint(lt.linear_account_info(contract_code='ETH-USDT'))
# pprint(lt.linear_position_info(contract_code='ETH-USDT'))
# pprint(lt.linear_sub_auth(sub_uid='296145790', sub_auth=1))
# pprint(lt.linear_sub_account_info_list(contract_code='ETH-USDT'))

# pprint(lt.linear_sub_account_list())
# pprint(lt.linear_sub_account_list(contract_code='ETH-USDT'))
# pprint(lt.linear_sub_account_list(contract_code='BTC-USDT'))
# pprint(lt.linear_sub_account_info(contract_code='BTC-USDT', sub_uid='296145790'))
# pprint(lt.linear_sub_account_info(contract_code='ETH-USDT', sub_uid='296145790'))
# pprint(lt.linear_sub_position_info(sub_uid='296145790'))
# pprint(lt.linear_financial_record(margin_account='BTC-USDT'))
# pprint(lt.linear_financial_record_exact(margin_account='BTC-USDT', size=10, direct='next'))
# pprint(lt.linear_user_settlement_records(contract_code='ETH-USDT'))
# pprint(lt.linear_cross_user_settlement_records(margin_account='USDT'))
# pprint(lt.linear_order_limit(contract_code='ETH-USDT', order_price_type='limit'))
# pprint(lt.linear_order_limit(contract_code='BTC-USDT', order_price_type='optimal_10'))
# pprint(lt.linear_fee(contract_type='swap', contract_code='BTC-USDT', pair='BTC-USDT'))
# pprint(lt.linear_transfer_limit())
# pprint(lt.linear_transfer_limit(contract_code='BTC-USDT'))
# pprint(lt.linear_position_limit())
# pprint(lt.linear_position_limit(contract_code='BTC-USDT'))
# pprint(lt.linear_account_position_info(contract_code='BTC-USDT'))
# pprint(lt.linear_master_sub_transfer(sub_uid='296145790', asset='USDT', from_margin_account='USDT',
#                                      to_margin_account='BTC-USDT',amount='1008', type='master_to_sub'))

# pprint(lt.linear_master_sub_transfer_record(margin_account='BTC-USDT', create_date='90'))
# pprint(lt.linear_transfer_inner(asset='USDT', from_margin_account='USDT',
#                                 to_margin_account='BTC-USDT', amount='1008'))
# pprint(lt.linear_api_trading_status())
# pprint(lt.linear_available_level_rate(contract_code='BTC-USDT'))

# pprint(lt.linear_order(contract_code='BTC-USDT', volume='1', direction='buy', offset='both', lever_rate='10',
#                        order_price_type='limit', price='1200'))
# pprint(lt.linear_batchorder({"orders_data": [{"contract_code":'BTC-USDT', "volume":'1', "direction":'buy', """offset“:'both',  ”lever_rate“:'10',
#                             ”order_price_type“:'limit', ”price“ :'1300'}]}))
# pprint(lt.linear_batchorder({"orders_data": [{"contract_code": 'BTC-USDT', "client_order_id": '', "price": '1300',
#                                               "volume": '1', "direction": 'buy', "offset": 'both', "lever_rate": '5', "order_price_type": 'limit'}]}))
# pprint(lt.linear_cancel(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_cancelall(contract_code='BTC-USDT'))

# pprint(lt.linear_switch_lever_rate(contract_code='BTC-USDT', lever_rate='1'))
# pprint(lt.linear_order_info(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_order_detail(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_openorders(contract_code='BTC-USDT'))
# pprint(lt.linear_hisorders(contract_code='BTC-USDT', trade_type='0', type='1', status='3,4,5',create_date='90'))
# pprint(lt.linear_hisorders_exact(contract_code='BTC-USDT', trade_type='0', type='1', status='3,4,5'))

# pprint(lt.linear_matchresults(contract_code='BTC-USDT', trade_type='0', create_date='90'))
# pprint(lt.linear_matchresults_exact(contract_code='BTC-USDT', trade_type='0'))

# pprint(lt.linear_lightning_close_position(contract_code='BTC-USDT', volume='1', direction='6'))
# pprint(lt.linear_trigger_order(contract_code='BTC-USDT', trigger_type='ge', trigger_price='1', order_price='1001',
#                                volume='1', direction='buy', offset='both'))
# pprint(lt.linear_trigger_cancel(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_trigger_cancelall(contract_code='BTC-USDT'))
# pprint(lt.linear_trigger_openorders(contract_code='BTC-USDT'))
# pprint(lt.linear_trigger_hisorders(contract_code='BTC-USDT', trade_type='0', create_date='90',status ='0'))

# pprint(lt.linear_tpsl_order(contract_code='BTC-USDT', volume='1', direction='6'))
# pprint(lt.linear_tpsl_cancel(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_tpsl_cancelall(contract_code='BTC-USDT'))
# pprint(lt.linear_tpsl_openorders(contract_code='BTC-USDT'))
# pprint(lt.linear_tpsl_hisorders(contract_code='BTC-USDT', create_date='90', status ='0'))
# pprint(lt.linear_relation_tpsl_order(contract_code='BTC-USDT', order_id='953329103506190336'))

# pprint(lt.linear_track_order(contract_code='BTC-USDT', callback_rate='0.01', active_price='1',
#                              order_price_type='optimal_5',
#                              volume='1', direction='buy', offset='both', lever_rate='5'))
# pprint(lt.linear_track_cancel(contract_code='BTC-USDT', order_id='953375774726262786'))
# pprint(lt.linear_track_cancelall(contract_code='BTC-USDT'))
# pprint(lt.linear_track_openorders(contract_code='BTC-USDT'))
# pprint(lt.linear_track_hisorders(contract_code='BTC-USDT', create_date='90', status ='0', trade_type='0'))

# pprint(lt.linear_cross_account_info())
# pprint(lt.linear_cross_position_info())
# pprint(lt.linear_cross_sub_account_info_list())
# pprint(lt.linear_cross_sub_account_list())
# pprint(lt.linear_cross_sub_account_info(sub_uid='296145790'))
# pprint(lt.linear_cross_sub_position_info(sub_uid='296145790'))
# pprint(lt.linear_cross_transfer_limit())
# pprint(lt.linear_cross_position_limit())
# pprint(lt.linear_cross_account_position_info(margin_account='USDT'))
# pprint(lt.linear_cross_available_level_rate())

# pprint(lt.linear_cross_order(contract_code='BTC-USDT', volume='1', direction='buy', offset='both', lever_rate='10',
#                              order_price_type='limit', price='1200'))
# pprint(lt.linear_cross_batchorder({"orders_data": [{"contract_code": 'BTC-USDT', "client_order_id": '', "price": '1300',
#                                                     "volume": '1', "direction": 'buy', "offset": 'both',
#                                                     "lever_rate": '5', "order_price_type": 'limit'}]}))
# pprint(lt.linear_cross_cancel(contract_code='BTC-USDT', order_id='953352277211643904'))
# pprint(lt.linear_cross_cancelall())
# pprint(lt.linear_cross_switch_lever_rate(lever_rate= '1'))
# pprint(lt.linear_cross_order_info())
# pprint(lt.linear_cross_order_detail())
# pprint(lt.linear_cross_openorders())
# pprint(lt.linear_cross_hisorders(contract_code='BTC-USDT', create_date='90', type= '1', status ='0', trade_type='0'))
# pprint(lt.linear_cross_hisorders_exact(type= '1', status ='0', trade_type='0'))

# pprint(lt.linear_cross_matchresults(contract_code='BTC-USDT', trade_type='0', create_date='90'))
# pprint(lt.linear_cross_matchresults_exact(contract_code='BTC-USDT', trade_type='0'))
# pprint(lt.linear_cross_lightning_close_position(contract_code='BTC-USDT', volume='1', direction='6'))
#
# pprint(lt.linear_cross_trigger_order(contract_code='BTC-USDT', trigger_type='ge', trigger_price='1', order_price='1001',
#                                      volume='1', direction='buy', offset='both'))
# pprint(lt.linear_cross_trigger_cancel(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_cross_trigger_cancelall(contract_code='BTC-USDT'))
# pprint(lt.linear_cross_trigger_openorders(contract_code='BTC-USDT'))
# pprint(lt.linear_cross_trigger_hisorders(contract_code='BTC-USDT', trade_type='0', create_date='90', status='0'))
#
# pprint(lt.linear_cross_tpsl_order(contract_code='BTC-USDT', volume='1', direction='6'))
# pprint(lt.linear_cross_tpsl_cancel(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_cross_tpsl_cancelall(contract_code='BTC-USDT'))
# pprint(lt.linear_cross_tpsl_openorders(contract_code='BTC-USDT'))
# pprint(lt.linear_cross_tpsl_hisorders(contract_code='BTC-USDT', create_date='90', status='0'))
# pprint(lt.linear_cross_relation_tpsl_order(contract_code='BTC-USDT', order_id='953329103506190336'))

# pprint(lt.linear_cross_track_order(contract_code='BTC-USDT', callback_rate='0.01', active_price='1',
#                              order_price_type='optimal_5',
#                              volume='1', direction='buy', offset='both'))
# pprint(lt.linear_cross_track_cancel(contract_code='BTC-USDT', order_id='953329103506190336'))
# pprint(lt.linear_cross_track_cancelall(contract_code='BTC-USDT'))
# pprint(lt.linear_cross_track_openorders(contract_code='BTC-USDT'))
# pprint(lt.linear_cross_track_hisorders(contract_code='BTC-USDT', create_date='90', status ='0', trade_type='0'))

# pprint(lt.linear_balance_valuation())
# pprint(lt.linear_transfer(From='spot', to='linear-swap', currency='USDT', margin_account='BTC-USDT',amount='0.0001'))

#  公共接口
# pprint(lt.linear_contract_info(contract_code='BTC-USDT'))
# pprint(lt.linear_index(contract_code='BTC-USDT'))
# pprint(lt.linear_price_limit(contract_code='BTC-USDT'))
# pprint(lt.linear_open_interest(contract_code='BTC-USDT', contract_type='swap'))

# pprint(lt.linear_risk_info(business_type='swap', contract_code='BTC-USDT'))
# pprint(lt.linear_insurance_fund(contract_code='BTC-USDT'))
# pprint(lt.linear_adjustfactor(contract_code='BTC-USDT'))
# pprint(lt.linear_cross_adjustfactor(business_type='swap', contract_code='BTC-USDT'))
# pprint(lt.linear_his_open_interest(contract_type='swap', period='60min', contract_code='BTC-USDT', pair='BTC-USDT',
#                                    amount_type=1))
# pprint(lt.linear_ladder_margin(contract_code='ETH-USDT'))
# pprint(lt.linear_cross_ladder_margin(contract_type='swap', contract_code='BTC-USDT', pair='BTC-USDT'))

# pprint(lt.linear_elite_account_ratio(period='60min', contract_code='BTC-USDT'))
# pprint(lt.linear_elite_position_ratio(period='60min', contract_code='BTC-USDT'))

# pprint(lt.linear_liquidation_orders(contract_code='BTC-USDT', pair='BTC-USDT', trade_type='0', create_date=90))
# pprint(lt.linear_settlement_records(contract_code='ETH-USDT'))
# pprint(lt.linear_estimated_settlement_price(business_type='swap', contract_type='swap', contract_code='BTC-USDT', pair='BTC-USDT'))

# pprint(lt.linear_api_state(contract_code='BTC-USDT'))
# pprint(lt.linear_api_state(contract_code='ETH-USDT'))
# pprint(lt.linear_cross_transfer_state(margin_account='USDT'))
# pprint(lt.linear_cross_trade_state(business_type='swap', contract_type='swap', contract_code='BTC-USDT', pair='BTC-USDT'))
# pprint(lt.linear_funding_rate(contract_code='BTC-USDT'))
# pprint(lt.linear_funding_rate(contract_code='ETH-USDT'))
# pprint(lt.linear_batch_funding_rate(contract_code='BTC-USDT'))
# pprint(lt.linear_batch_funding_rate(contract_code='BTC-USDT'))

# pprint(lt.linear_historical_funding_rate(contract_code='BTC-USDT'))
# pprint(lt.linear_historical_funding_rate(contract_code='ETH-USDT'))

# pprint(lt.linear_depth(contract_code='BTC-USDT', type='step1'))
# pprint(lt.linear_depth(contract_code='ETH-USDT', type='step1'))
# pprint(lt.linear_market_bbo(business_type='swap', contract_code='BTC-USDT'))
# pprint(lt.linear_market_bbo(business_type='swap', contract_code='ETH-USDT'))
# pprint(lt.linear_kline(contract_code='BTC-USDT', period='1day', size=5))
# pprint(lt.linear_detail_merged(contract_code='BTC-USDT'))
# pprint(lt.linear_detail_merged(contract_code='ETH-USDT'))
# pprint(lt.linear_detail_batch_merged(contract_code='BTC-USDT'))
# pprint(lt.linear_detail_batch_merged(contract_code='ETH-USDT'))
# lt.linear_basis(contract_code='BTC-USDT', period='1day', basis_price_type='open')
# pprint(lt.linear_basis(contract_code='BTC-USDT', period='1day', basis_price_type='open'))
# pprint(lt.linear_premium_index_kline(contract_code='BTC-USDT', period='1day', size='10'))
# pprint(lt.linear_premium_index_kline(contract_code='BTC-USDT', period='1min', size='10'))
# pprint(lt.linear_estimated_rate_kline(contract_code='BTC-USDT', period='1min', size='10'))
# pprint(lt.linear_swap_mark_price_kline(contract_code='BTC-USDT', period='1min', size='10'))
# pprint(lt.linear_trade(business_type='swap', contract_code='BTC-USDT'))
# pprint(lt.linear_history_trade(size=20, contract_code='BTC-USDT'))
# pprint(lt.linear_history_index(size=20, contract_code='BTC-USDT'))
