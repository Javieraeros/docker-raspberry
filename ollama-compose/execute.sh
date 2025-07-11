#!/bin/sh

start() { 
    docker exec -it ollama ollama run llama3.2
}

serve() { 
    docker exec -it ollama ollama serve llama3.2
}
stop() {
    docker exec ollama ollama stop llama3.2
}

"$@"
