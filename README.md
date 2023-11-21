# nap-server


# Running the server

## Very first time 

% cd server  
% python db.py


## Run the server

% python main.py   


# Running the client at 8097
% cd client
% python main.py 8097 hare.jpg harekrishna.jpg


# Running another client at 9090
% cd client
% python main.py 9090 tortoise.jpg 


# To run protoc tool after change to a protoc file, run
protobufs % python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./server_to_client.proto


## References 

https://realpython.com/python-microservices-grpc/



https://betterprogramming.pub/grpc-file-upload-and-download-in-python-910cc645bcf0


