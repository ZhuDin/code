let dgram = require('dgram');
let client = dgram.createSocket('udp4');
process.stdin.resume();
process.stdin.on('data', function(data){
    console.log(data.toString('utf8'));
    client.send(data, 0, data.length, 8124, 'www.example.com',
        function(err, bytes) {
            if (err) {
                console.log('error: ' + err);
            } else {
                console.log('successful');
            }
        });
});