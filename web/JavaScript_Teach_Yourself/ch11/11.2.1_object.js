myNewObject = new Object();
myNewObject.info = 'I am a shiny new object';

function myFunc() {
    console.log(this.info);
}

myNewObject.showInfo = myFunc
myNewObject.showInfo();