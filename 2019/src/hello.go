package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file_name := "inputs/hello.txt"
	file, _ := os.Open(file_name)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
	defer file.Close()
}
