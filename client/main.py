import argparse
import socket
import client_to_server

parser = argparse.ArgumentParser()
parser.add_argument("port", help='Port number where peers can reach this client for files')
parser.add_argument("files_with_me",nargs='+' ,help='List of files available with this client')

args = parser.parse_args()
print(args.port, args.files_with_me)


if __name__ == "__main__":
        
        print(f'*** client starting at port {args.port}....')
        print(f'*** *** Files that this client can share {args.files_with_me}')
        
        print('\n *** Regitering with Server... \n')
        client_to_server.registerWithServer("localhost",args.port, args.files_with_me)
        print('Registration successful, waiting for calls from peer ')
        
        response_from_server = client_to_server.queryServerForFile('hare.jpg')
        print('call returned')
        print(response_from_server)
        
