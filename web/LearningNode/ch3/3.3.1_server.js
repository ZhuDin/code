let net = require('net');
let server = net.createServer(function(conn) {
    console.log('connected');
    conn.on('data', function (data) {
        console.log(data + ' from ' + conn.remoteAddress + ' ' 
            + conn.remotePort);
    });
    conn.on('colse', function() {
        console.log('client closed connetion');
    });
}).listen(8080);
console.log('listening on port 8080');