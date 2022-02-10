function Dog() {
    this.breed = '';
    this.setBreed = function(newBreed) {
        this.setBreed = newBreed;
    }
}

Dog.prototype = new Pet();

let myDog  = new Pet();
myDog.setName('Alan');
myDog.setBreed("Greyhound");
console.log(myDog.name + " is a " + myDog.breed);