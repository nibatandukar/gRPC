package main

import (
	"fmt"
	"flag"
	"time"
	"log"
	// "golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "/home/niba/grpc-py-backup/server/protos"
)
const (
	defaultName = "CRUD"
)

var (
addr = flag.String("addr", "localhost:50051", "the address to connect to")
name = flag.String("name", defaultName, "Name to greet")

)
func main() {
	flag.Parse()
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	fmt.Println("Hello")
	now := time.Now()
    fmt.Println(now)
	// fmt.Println(var.addr)
}




