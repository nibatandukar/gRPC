package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"time"

	pb "github.com/nibatandukar/grpc-client-go/protos"
	"github.com/sirupsen/logrus"
	"google.golang.org/grpc"
)

func main() {

	fmt.Println("Trying to connect to the database")
	serverAddress := flag.String("address", "localhost:50051", "the server address")
	flag.Parse()
	log.Printf("Connecting to %s", *serverAddress)
	conn, err := grpc.Dial(*serverAddress, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("error while connecting: %v", err)
	}
	defer conn.Close()

	client := pb.NewUsersClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)

	defer cancel()

	// createUser(client, ctx)
	// getUserById(client, ctx)
	deleteUser(client, ctx)
	//updateUser(client, ctx)
}

func createUser(client pb.UsersClient, ctx context.Context) {
	fmt.Println("Trying to connect to the database!!!!!!")
	user := pb.User{
		Id:       "5112343444",
		Name:     "Niba Tandukar",
		Email:    "nibatandukar@gmail.com",
		Password: "1234321",
	}

	req := pb.CreateUserRequest{User: &user}
	r, err := client.CreateUser(ctx, &req)
	if err != nil {
		log.Fatal("user already exist")
	}
	logrus.Info("RESPONSE :: ", r)
}

func getUserById(client pb.UsersClient, ctx context.Context) {
	fmt.Println("The requested user is below")
	req := pb.GetUserByIdRequest{Id: "5112343444"}
	r, err := client.GetUserById(ctx, &req)
	if err != nil {
		log.Fatal("Sorry the user doesnot exist!!")
	}
	logrus.Info("RESPONSE :: ", r)
}

func deleteUser(client pb.UsersClient, ctx context.Context) {
	fmt.Println("Deleting the user..")
	req := pb.DeleteUserRequest{Id: "5112343444"}
	r, err := client.DeleteUser(ctx, &req)
	if err != nil {
		log.Fatal("The id is invalid or doesnot exist !!")
	}
	logrus.Info("REPONSE :: ", r)

}

func updateUser(client pb.UsersClient, ctx context.Context) {
	fmt.Println("Updating the user...")
	user := pb.User{
		Id:       "5112343444",
		Name:     "Hello Tan23456ytgbnjhgfghytg",
		Email:    "hellotan@gmail.com",
		Password: "1234",
	}
	req := pb.UpdateUserRequest{User: &user}
	r, err := client.UpdateUser(ctx, &req)
	if err != nil {
		log.Fatal("The user cannot update, user may not exist")
	}
	logrus.Info("RESPONSE ::", r)
}
