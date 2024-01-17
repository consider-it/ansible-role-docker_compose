"use strict";

import http from "node:http";

const server = http.createServer((req, res) => {
    res.writeHead(200, {
        "Content-Type": "application/json"
    });
    res.end(JSON.stringify({
        rev: 2,
        project: "nodejs",
        meta: "Docker Compose Project"
    }));
});

server.listen(3000);
