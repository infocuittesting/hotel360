from sqlwrapper import gensql
import json

def HOTEL_RES_POST_INSERT_WaitlistReason(request):
    d = request.json

    sql_value = gensql('insert','reservation.res_waitlist',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Waitlist Reason Assigned Successfully','ReturnCode':'WRAS'}, sort_keys=True, indent=4))
   
