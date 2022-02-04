// run app: node 1.3_web.js
// curl 127.0.0.1:8080
// wget 127.0.0.1:8080
let http = require('http');
function process_request(req, res) {
    let body = 'Thank for calling!\n';
    let content_length = body.length;
    res.writeHead(200, {
        'Content-Length': content_length,
        'Content-Type': 'text/plain'
    });
    res.end(body)
}

let s = http.createServer(process_request);
s.listen(8080);