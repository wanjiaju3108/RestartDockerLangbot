#!/bin/bash
port=8000
while true; do
    { printf 'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'; sleep 1; } | nc -l -p "$port"
    docker restart langbot
done