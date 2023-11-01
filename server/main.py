import sys
import os

import grpc
from concurrent import futures

import NapsterServer


import server_to_client_pb2
import server_to_client_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_to_client_pb2_grpc.add_NapsterServerServicer_to_server(NapsterServer.NapsterServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print('Server starting....')
    serve()

