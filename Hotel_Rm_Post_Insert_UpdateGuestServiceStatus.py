from sqlwrapper import gensql,dbget
import json

def hotel_rm_post_insert_updateguestservicestatus(request):
    d = request.json
    print(gensql('insert','room_management.guest_service_status',d))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
def hotel_rm_post_select_queryguestservicestatus(request):
    sql = json.loads(dbget("select * from room_management.rm_room_list join room_management.guest_service_status \
                           on  room_management.rm_room_list.rm_room = \
                           room_management.guest_service_status.rm_room"))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'ReturnCode':'RRTS'},indent=4))



