from sqlwrapper import gensql,dbget

import json

def HOTEL_RES_POST_INSERT_QueryArrivalFromToReservation(request):
    d = request.json
    if request.json.get('ArrivalFrom'):
        s = {}
        ArrivalFrom = request.json['ArrivalFrom']
       
        sql_value = dbget("select * from reservation.res_reservation where  res_arrival >= '"+ArrivalFrom+"'")

        
        sql_value = json.loads(sql_value)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

    
    elif request.json.get('ArrivalFrom') and request.json.get('ArrivalTo'):
  
        ArrivalFrom = request.json['ArrivalFrom']
        ArrivalTo = request.json['ArrivalTo']
        print(type(ArrivalFrom))
        #e = { k : v for k,v in d.items() if k != '' if k in ('ArrivalFrom','ArrivalTo')}
        sql_value = dbget("select * from reservation.res_reservation where res_arrival between '"+ArrivalFrom+"' and '"+ArrivalTo+"' ")
        
        sql_value = json.loads(sql_value)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

    
    
    else:
        pass
