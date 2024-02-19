package main

import (
	"encoding/json"
	"io"
	"net/http"
)

type ResponsePayload struct {
	Method  string              `json:"method"`
	Path    string              `json:"path"`
	Query   string              `json:"query"`
	Headers map[string][]string `json:"headers"`
	Payload string              `json:"payload"`
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, "Error reading request body", http.StatusInternalServerError)
			return
		}

		responsePayload := ResponsePayload{
			Method:  r.Method,
			Path:    r.URL.Path,
			Query:   r.URL.RawQuery,
			Headers: r.Header,
			Payload: string(body),
		}

		jsonResponse, err := json.Marshal(responsePayload)
		if err != nil {
			http.Error(w, "Error creating JSON response", http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		w.Write(jsonResponse)

		println(string(jsonResponse))
	})

	println("Server is listening on port 8080...")
	http.ListenAndServe(":8080", nil)
}
