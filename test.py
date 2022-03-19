from pprint import pprint
from common.LinearService import t as lt


pprint(lt.linear_switch_position_mode(margin_account='BTC-USDT',position_mode='single_side'))#dual_side
# pprint(lt.linear_cross_switch_position_mode(margin_account='USDT',position_mode='dual_side'))#


# pprint(lt.linear_account_info(contract_code='btc-usdt'))B
# pprint(lt.linear_cross_account_info(margin_account='usdt'))


# pprint(lt.linear_sub_account_info(contract_code='btc-usdt',sub_uid='114337044'))
# pprint(lt.linear_cross_sub_account_info(margin_account='usdt',sub_uid='114337044'))


# pprint(lt.linear_account_position_info(contract_code='btc-usdt'))
# pprint(lt.linear_cross_account_position_info(margin_account='usdt'))


# pprint(lt.linear_position_info(contract_code='eth-usdt'))
# pprint(lt.linear_cross_position_info(contract_code='ltc-usdt-220325'))


# pprint(lt.linear_sub_position_info(contract_code='btc-usdt',sub_uid='114337044'))
# pprint(lt.linear_cross_sub_position_info(contract_code='btc-usdt',sub_uid='114337044'))


# pprint(lt.linear_order(contract_code='eth-usdt',price='3000',volume='1',direction='buy',offset='open',lever_rate='5',order_price_type='limit',reduce_only='1',tp_trigger_price='4000',tp_order_price='4000',tp_order_price_type='limit'))
# pprint(lt.linear_cross_order(contract_code='eth-usdt',price='3000',volume='1',direction='buy',offset='open',lever_rate='5',order_price_type='limit',reduce_only='1',tp_trigger_price='4000',tp_order_price='4000',tp_order_price_type='limit'))


# pprint(lt.linear_batchorder({"orders_data": [{"contract_code": 'eth-usdt', "client_order_id": '',"price": '3000',"volume": '1',"direction": 'buy',"offset": 'open',"lever_rate": '5',"order_price_type": 'limit',"reduce_only" : '1'}]}))
# pprint(lt.linear_cross_batchorder({"orders_data": [{"contract_code": 'eth-usdt', "client_order_id": '',"price": '3000',"volume": '1',"direction": 'buy',"offset": 'open',"lever_rate": '5',"order_price_type": 'limit',"reduce_only" : '1'}]}))


# pprint(lt.linear_trigger_order(contract_code='eth-usdt',trigger_type='le',trigger_price='2999',order_price='3000',order_price_type='limit',volume='1',direction='buy',offset='open',lever_rate='5',reduce_only = '1'))
# pprint(lt.linear_cross_trigger_order(contract_code='eth-usdt',trigger_type='le',trigger_price='2999',order_price='3000',order_price_type='limit',volume='1',direction='buy',offset='open',lever_rate='5',reduce_only = '1'))


# pprint(lt.linear_track_order(contract_code='eth-usdt',direction='buy',offset='open',lever_rate='5',volume='1',callback_rate='0.01',active_price='900',order_price_type='optimal_5',reduce_only='1'))
# pprint(lt.linear_cross_track_order(contract_code='eth-usdt',direction='buy',offset='open',lever_rate='5',volume='1',callback_rate='0.01',active_price='900',order_price_type='optimal_5',reduce_only='1'))


# pprint(lt.linear_order_info(order_id='941666271915905024',contract_code='eth-usdt'))
# pprint(lt.linear_cross_order_info(order_id='941666527449681920',contract_code='eth-usdt'))


# pprint(lt.linear_order_detail(contract_code='eth-usdt',order_id='941667293879046144',created_at='7',order_type='1'))
# pprint(lt.linear_cross_order_detail(contract_code='eth-usdt',order_id='941689851051479040',created_at='7',order_type='1'))


# pprint(lt.linear_openorders(contract_code='eth-usdt',trade_type='18'))
# pprint(lt.linear_cross_openorders(contract_code='eth-usdt',trade_type='18'))


# pprint(lt.linear_hisorders(contract_code='eth-usdt',trade_type='0',type='1',status='0',create_date='90'))
# pprint(lt.linear_cross_hisorders(contract_code='eth-usdt',trade_type='0',type='1',status='0',create_date='90'))


# pprint(lt.linear_hisorders_exact(contract_code='eth-usdt',trade_type='0',type='1',status='0'))
# pprint(lt.linear_cross_hisorders_exact(contract_code='eth-usdt',trade_type='0',type='1',status='0'))


# pprint(lt.linear_matchresults(contract_code='eth-usdt',trade_type='0',create_date='90'))
# pprint(lt.linear_cross_matchresults(contract_code='eth-usdt',trade_type='0',create_date='90'))


# pprint(lt.linear_matchresults_exact(contract_code='eth-usdt',trade_type='0'))
# pprint(lt.linear_cross_matchresults_exact(contract_code='eth-usdt',trade_type='0'))


# pprint(lt.linear_trigger_openorders(contract_code='eth-usdt'))
# pprint(lt.linear_cross_trigger_openorders(contract_code='eth-usdt'))



# pprint(lt.linear_trigger_hisorders(contract_code='eth-usdt',status='0',trade_type='0',create_date='90'))
# pprint(lt.linear_cross_trigger_hisorders(contract_code='eth-usdt',status='0',trade_type='0',create_date='90'))


# pprint(lt.linear_relation_tpsl_order(contract_code='eth-usdt',order_id='941695578226790400'))
# pprint(lt.linear_cross_relation_tpsl_order(contract_code='eth-usdt',order_id='941695579715768320'))


# pprint(lt.linear_track_openorders(contract_code='eth-usdt',trade_type='0'))
# pprint(lt.linear_cross_track_openorders(contract_code='eth-usdt',trade_type='0'))


# pprint(lt.linear_track_hisorders(contract_code='ltc-usdt',status='0',trade_type='0',create_date='7'))
# pprint(lt.linear_cross_track_hisorders(contract_code='ltc-usdt-220325',status='0',trade_type='0',create_date='7'))