import grpc

from peer_to_peer_pb2 import FileResponse, MetaData
import peer_to_peer_pb2_grpc

import sys
import os

import grpc
from concurrent import futures
from pathlib import Path


class PeerServer(peer_to_peer_pb2_grpc.PeerServicer):
    def __init__(self) -> None:
        super().__init__()
        
        print('PeerServer Initialized')

    # rpc DownloadFile(MetaData) returns (stream FileResponse ) {}
    def DownloadFile(self, request: MetaData, context):
        file_to_serve = f'{Path.cwd()}/my_files/{request.filename}'
        print('\n Hmmmm...Someone needs a file peer_to_peer_server::Download File: ', file_to_serve , ' and I found it', {os.path.exists(file_to_serve)} )
        print(context)
        chunk_size = 1024
        
        if os.path.exists(file_to_serve):
            with open(file_to_serve, mode='rb') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if chunk:
                        entry_response = FileResponse(chunk_data=chunk)
                        yield entry_response
                    else:
                        return
                    
def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    peer_to_peer_pb2_grpc.add_PeerServicer_to_server(PeerServer(), 
                                                                    server)
    peer_server_port = f"[::]:{port}"
    server.add_insecure_port(peer_server_port)
    
    print(f"Peer server running in [::]:{port}")
    
    server.start()
    
    server.wait_for_termination()


    
