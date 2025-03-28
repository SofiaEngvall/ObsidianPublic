// go install github.com/gorilla/mux@latest

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
)

var port int = 50000

type Article struct {
	Title   string `json:"Title"`
	Desc    string `json:"desc"`
	Content string `json:"content"`
}

// Simulate a database
var Articles []Article

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: homePage")
	fmt.Fprintf(w, "Welcome to the HomePage!")
}

func returnAllArticles(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Endpoint Hit: returnAllArticles")
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(Articles)
}

func handleRequests() {
	//myRouter := mux.NewRouter().StrictSlash(true)
	//myRouter.HandleFunc("/", homePage)
	//myRouter.HandleFunc("/articles", returnAllArticles)
	//log.Fatal(http.ListenAndServe(":"+strconv.Itoa(port), myRouter))
	http.HandleFunc("/", homePage)
	http.HandleFunc("/articles", returnAllArticles)
	log.Fatal(http.ListenAndServe(":"+strconv.Itoa(port), nil))
}

func main() {
	// Dummy data
	Articles = []Article{
		Article{Title: "Hello", Desc: "Article Description", Content: "Article Content"},
		Article{Title: "Hello 2", Desc: "Article Description", Content: "Article Content"},
	}
	fmt.Printf("Starting the web server on port %d\n", port)
	handleRequests()
}
