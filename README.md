# nap-server


# Running the server

## Very first time 

% cd server  
% python db.py


## Run the server
% cd server
% python main.py   


## Running the first client at 8097

% cd peer

% python main.py 8097 hare.jpg harekrishna.jpg


## Running second client at 9090

% cd peer

% python ./main.py 9097 hare2.jpg harekrishna2.jpg


# To run protoc tool after change to a protoc file, run
protobufs % python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./server_to_client.proto


## References 

https://realpython.com/python-microservices-grpc/



https://betterprogramming.pub/grpc-file-upload-and-download-in-python-910cc645bcf0


