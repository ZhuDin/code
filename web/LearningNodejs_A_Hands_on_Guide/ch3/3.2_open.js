let fs = require('fs');

let file;
let buf = new Buffer.from(100000);
fs.open(
    'info.txt', 'r',
    function(handle) {
        file = handle;
    }
);

fs.read(
    file, buf, 0, 100000, null,
    function(){
        console.log(buf.toString());
        file.close(file, function(){/* don't care */});
    }
);