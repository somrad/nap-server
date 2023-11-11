import grpc
# from server_to_client_pb2 import FileRequest, RegisterPeerRequest

# from server_to_client_pb2_grpc import NapsterServerStub

import server_to_client_pb2
import server_to_client_pb2_grpc
import os


def queryServerForFile(filename, server_ip='localhost', server_port=50051):
    file_query_channel = grpc.insecure_channel(f"{server_ip}:{server_port}")
    file_query_client = server_to_client_pb2_grpc.NapsterServerStub(file_query_channel)

    filereq =  server_to_client_pb2.PeersServingFile_Request(file_name=filename)

    response = file_query_client.GetPeersServingRequestedFile(filereq)
    # print('response', response)
    return response.availableClients
    


def registerWithServer(ip,port, files_with_this_client, server_ip='localhost', server_port=50051):
    register_channel = grpc.insecure_channel(f"{server_ip}:{server_port}")
    register_client = server_to_client_pb2_grpc.NapsterServerStub(register_channel)
    
    registerRequest = server_to_client_pb2.RegisterPeerRequest(ip=ip, port_number=int(port))
    registerRequest.file_available_with_me.extend(files_with_this_client)
    response = register_client.RegisterPeer(registerRequest)

    print(response)

def deregisterWithServer(ip,port, server_ip='localhost', server_port=50051):
    deregister_channel = grpc.insecure_channel(f"{server_ip}:{server_port}")
    deregister_client = server_to_client_pb2_grpc.NapsterServerStub(deregister_channel)
    
    deregisterRequest = server_to_client_pb2.UnRegisterPeerRequest(ip=ip, port_number=int(port))
    
    response = deregister_client.UnregisterPeer(deregisterRequest)

    print(response)

