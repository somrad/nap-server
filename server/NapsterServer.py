
import sys, os
import grpc
sys.path.append(os.path.abspath("../protobufs"))

import sqlite3 as sl




import server_to_client_pb2_grpc
import server_to_client_pb2
from server_to_client_pb2  import RegisterPeerResponse, FileResponse, FileHostingClient

class NapsterServer(server_to_client_pb2_grpc.NapsterServerServicer):
    def __init__(self) -> None:
        super().__init__()
        print('NapsterServer Initialized')


    def RegisterPeer(self, request, context):
        print(f"Client Registered  {request.ip}:{request.port_number} 'with files ' {request.file_available_with_me} ")
        # print(request)

        con = sl.connect('clients.db')
        sql = 'INSERT INTO CLIENT_FILES (ip, port, files) values (?,?,?)'
        data = [(request.ip, request.port_number, file_name) for file_name in request.file_available_with_me]
        print(data)
        with con:
            con.executemany(sql, data)
        response =  RegisterPeerResponse( ip=request.ip, port_number= request.port_number,registration_success='success')
        
        print(response)
        return response
    
    def GetPeersServingRequestedFile(self, request, context):
        print(context)
        print(f"File Requested  {request.file_name}")
        # print(request)

        con = sl.connect('clients.db')
        sql = f"SELECT * FROM CLIENT_FILES WHERE files = '{request.file_name}'"
        
        with con:
            data = con.execute(sql)

        response = FileResponse()
        
        data = list(data)
        # for row in data:
        #     print(row)
             
        clients_having_file = [FileHostingClient( ip=str(row[0]), port_number= row[1],file_name=row[2]) 
                                          for row in data]
        print('clients_having_file:',clients_having_file)
        response.availableClients.extend(clients_having_file)    
        
        print('response', response)
        return response


