from sqlwrapper import gensql, dbput, dbget
import json
import requests
from flask import Flask,request,jsonify
def HOTEL_RES_GET_SELECT_RoomUnassign(request):
    Res_id = request.json['Res_id']
    print(Res_id)
    Res_id  = Res_id.split(',')

    Res_id = str(Res_id)[1:-1]

    sqlvalue = json.loads(dbget("select res_room from reservation.res_reservation where res_id in ("+Res_id+")"))
    print("sqlval",sqlvalue)
    rooms = ''
    for  i in sqlvalue:
        if len(rooms) == 0:
            rooms += "'"+i['res_room']+"'"
        else:
            rooms += ","+"'"+i['res_room']+"'"
    print(rooms)        
    
    fo_status = "vaccant"
    res_status = "not reserved"
    psql = dbput("update room_management.rm_room_list set rm_fo_status = '"+fo_status+"',rm_reservation_status = '"+res_status+"',rm_fo_person = '0' where rm_room in ("+rooms+")")
    print(psql)
    data = '0'
    sql = dbput("update reservation.res_reservation set res_room = "+data+" where res_id in ("+Res_id+") ")

    print(sql)

    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':'Room UnAssigned Successfully'  ,'ReturnCode':'RUAS'},indent=4))
