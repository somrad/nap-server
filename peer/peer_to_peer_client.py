import grpc
# from server_to_client_pb2 import FileRequest, RegisterPeerRequest

# from server_to_client_pb2_grpc import NapsterServerStub

import peer_to_peer_pb2
import peer_to_peer_pb2_grpc
import os

from pathlib import Path


def DownloadFile(filename, peer_ip, peer_port):

    my_local_download_path = f'{Path.home()}/Downloads/{filename}'

    file_download_channel = grpc.insecure_channel(f"{peer_ip}:{peer_port}")
    file_download_client = peer_to_peer_pb2_grpc.PeerStub(file_download_channel)

    filereq =  peer_to_peer_pb2.MetaData(filename=filename, extension='')

    for response in file_download_client.DownloadFile(filereq):
        with open(my_local_download_path, mode='ab') as f:
            # print('chunk is ',response.chunk_data)
            f.write(response.chunk_data)

    print(f'\n **** {filename} downloaded to {my_local_download_path}. Enjoy your download ****** \n')
    return
    