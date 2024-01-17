"use strict";

const http = require("http");

const server = http.createServer((req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/plain"
    });
    res.end("nodejs Docker Compose Project Rev 01");
});

server.listen(3000);
