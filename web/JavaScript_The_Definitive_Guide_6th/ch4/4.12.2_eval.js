var geval = eval;
var x = 'global';
var y = 'global';
function f() {
    var x = 'local';
    eval("x += 'Changed';");
    return x;
}
function g() {
    var y = 'local';
    geval("y += 'Changed';");
    return y;
}

console.log(f(), x);
console.log(g(), y);