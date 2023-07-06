from concurrent import futures
from pymongo import MongoClient
import json
import pymongo

import grpc
import users_pb2
import users_pb2_grpc

def get_database():
     CONNECTION_STRING = "mongodb+srv://nibatandukar:obhjOq2Hk3kbLvrs@cluster0.yklhrlj.mongodb.net/?retryWrites=true&w=majority"
     client = MongoClient(CONNECTION_STRING)
     print("Database connected !!!")
     return client["grpc"]


class Users(users_pb2_grpc.UsersServicer):
    def CreateUser(self, request, context):
        print("There is request to creater a user",request)
        client = get_database()
        usercollection = client["user"]
        response = usercollection.find_one({
            'id': request.user.id
        })
        print("response",response)
        if response is not None:
            print("user already exist")
            raise Exception("An error occurred during gRPC function")
        
        usercollection.insert_one({
            'id':request.user.id,
            'name':request.user.name,
            'email':request.user.email,
            'password':request.user.password
        })

        return users_pb2.CreateUserResponse(user=users_pb2.User(
                  id=request.user.id, 
                  name=request.user.name,
                  email=request.user.email,
                  password=request.user.password))
    
    def DeleteUser(self, request, context):
        print("The client is requesting to delete user id", request.id, "to delete!!!!" )
        client = get_database()
        client["user"].delete_one({
            'id': request.id
            })
        return users_pb2.DeleteUserResponse(user=users_pb2.User(id=request.id))
    
    def GetUserById(self, request, context):
        print("The client is excepecting to list the user")
        client = get_database()
        dbresponse =  client["user"].find_one({
            'id': request.id     
           })
        print(dbresponse)
        #return users_pb2.GetUserByIdResponse(user=users_pb2.User(id=request.id))
        return users_pb2.GetUserByIdResponse(user=users_pb2.User(
            id = dbresponse["id"],
            name = dbresponse["name"],
            email = dbresponse["email"]
        ))
    
    def UpdateUser(self, request, context):
        client = get_database()
        print(request.user)

        find = client["user"]
        myquery = { "id": request.user.id }
        newvalues = { "$set": { "name": request.user.name, "email": request.user.email, "password": request.user.password } }

        find.update_one(myquery, newvalues)
        response = find.find_one({
            'id': request.user.id
        })

        print("response", response)
        
        return users_pb2.GetUserByIdResponse(user=users_pb2.User(
            id = response['id'],
            name = response["name"],
            email = response["email"],
            password = response["password"]
        ))
    
def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':

    serve()
