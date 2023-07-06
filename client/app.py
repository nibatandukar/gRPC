from __future__ import print_function
import grpc
import users_pb2
import users_pb2_grpc

##################### Create New User ########################
def createUser():
    print("Connecting the database...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        payload={
                "id":"1234543",
                "name":"Bob5",
                "email":"bb",
                "password":"dabhd"}
        try:
            response = stub.CreateUser(users_pb2.CreateUserRequest(user=payload))
        except Exception as e:
                print(f"User with {payload['id']} already exist")
                return
        print(response)

############## Delete the User by Id ####################

def deleteUser():
    print("Requested user has been deleted !!!" )
    with grpc.insecure_channel('localhost:50051') as channel:
        stub =  users_pb2_grpc.UsersStub(channel)
        response = stub.DeleteUser(users_pb2.DeleteUserRequest(id="10o"))
        print(response)

######## Get User by Id ####################

def getUserById():
    print("Requested user is listing the code")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUserById(users_pb2.GetUserByIdRequest(id="15"))
        print(response)

############ Update User by Id ##########################

def updateUser():
    print("The user is updated")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.UpdateUser(users_pb2.UpdateUserRequest(user={
            "id":"15",
            "name":"heven",
            "email":"heven@123",
            "password":"password"

        }))
        print(response)
# def updateUser():
#     print("The requested user is")
#     with grpc.insecure_channel('localhost:50051') as channel:
#          stub = users_pb2_grpc.UsersStub(channel)
#          respone = stub.GetUsers(users_pb2.GetUsersRequest)
#          print(respone)

if __name__ == '__main__':
    #   createUser()
    #   deleteUser()
      getUserById()
    #   updateUser()
