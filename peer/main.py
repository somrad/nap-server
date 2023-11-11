import argparse
import socket
import client_to_server
import peer_to_peer_server
import threading
import signal
import sys
import peer_to_peer_client

parser = argparse.ArgumentParser()
parser.add_argument("port", help='Port number where peers can reach this client for files')
parser.add_argument("files_with_me",nargs='+' ,help='List of files available with this client')

args = parser.parse_args()
print(args.port, args.files_with_me)


''''''
def act_as_peer():

        # *** Am starting my peer to peer server at port {args.port}....and start sharing files if I have any 
        act_as_server = peer_to_peer_server.PeerServer()
        print(f'*** client starting at port {args.port}....')
        print(f'*** *** Files that this client can share {args.files_with_me}')
        peer_to_peer_server.serve(args.port)

        


def act_as_client():
        file_name = input("Press Ctrl+c to exit or Enter the name of the file you want to search: ")
        
        response_from_server = client_to_server.queryServerForFile(file_name)
        print('call returned with ', len(response_from_server), ' items.')
        
        # check if the file exits
        if len(response_from_server) > 0:
                print(response_from_server[0])

                # make a connection to another peer
                peer_to_peer_client.DownloadFile(filename=file_name, peer_ip='[::]', peer_port=response_from_server[0].port_number)
        else:
                print('---- I am sorry, looks like no one has this file--- \n')

        act_as_client()


def signal_handler(sig, frame):
        client_to_server.deregisterWithServer("localhost",args.port)
        print('\n ********* Exiting.....You pressed Ctrl+c **********')
        sys.exit()


if __name__ == "__main__":
        
        peer_server_thread =threading.Thread(target=act_as_peer, daemon=True)
        peer_server_thread.start()

        # Now that I can serve, I register myself with the server
        print('\n *** Regitering with Server... \n')
        client_to_server.registerWithServer("localhost",args.port, args.files_with_me)
        print('Registration successful, waiting for calls from peer ')
        

        signal.signal(signal.SIGINT, signal_handler)
        act_as_client()

        
        

        # 



        
        
