import grpc
from server_to_client_pb2 import FileRequest, RegisterPeerRequest
from server_to_client_pb2_grpc import NapsterServerStub
import os


def queryServerForFile(filename, server_ip='localhost', server_port=50051):
    file_query_channel = grpc.insecure_channel(f"{server_ip}:{server_port}")
    file_query_client = NapsterServerStub(file_query_channel)

    filereq = FileRequest(file_name=filename)

    response = file_query_client.GetPeersServingRequestedFile(filereq)
    print('response', response)
    return response.availableClients
    


def registerWithServer(ip,port, files_with_this_client, server_ip='localhost', server_port=50051):
    register_channel = grpc.insecure_channel(f"{server_ip}:{server_port}")
    register_client = NapsterServerStub(register_channel)
    
    registerRequest = RegisterPeerRequest(ip=ip, port_number=int(port))
    registerRequest.file_available_with_me.extend(files_with_this_client)
    response = register_client.RegisterPeer(registerRequest)

    print(response)