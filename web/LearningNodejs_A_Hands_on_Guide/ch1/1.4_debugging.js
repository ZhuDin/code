// node debug debugging.js
let http = require('http');
function process_request(req, res) {
    let body = 'Thank for calling!\n';
    let content_length = body.lenggth;
    res.writeHead(200, {
        'Content-Length': content_length,
        'Content-Type': 'text/plain'
    });
    res.end(body);
}

var s = http.createServer(process_request);
s.listen(8080);