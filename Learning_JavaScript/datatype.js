// Undefined is a datatype used when we have decleared the variable but do not initialise it.
// Undefined is automatically given to a variable if it is not initialised.
// null is the object and it is same as None in python. We need to assign this value.
// var have global scope
// let have local scope
// const is constant

var number = 3;
number = 'string';
console.log(number);

let num = 10;
num = 'str';
console.log(num);

const PI = 3.14;

num, number = 3, 5;

var c;
console.log(c) // undefined

// Incrementing the variable
c++
console.log(c)  // this is NaN because we have did, c = undefined + 1

// Decrementing the number 
d = 1;
d--;
console.log(d);

d += 3
console.log(d)

d -= 5
console.log(d)

// finding the length of the string
var string = 'this is a string'
console.log("Length of string is: " + string.length)

// grabbing the last character of the string
var lastCharacter = string[string.length-1]
console.log(lastCharacter)

// Array
var array = [1,2,3,'5'];
console.log(array);

// Grabbing element from the array
var element = array[0]
console.log(element)
element = array[array.length-1]
console.log(element)
array[array.length-1] = 10
element = array[array.length-1]
console.log(element)

// removing the first element
var array = [1,2,3, 4]
console.log('removed element is: '+array.shift())

// pushing element as the first element
array.unshift("one")
console.log(array)

// Funcitons
function functionName(){
    console.log('Hey I am called from a function');
}
functionName();


function f(){
    // var variable = 30
    console.log(variable);
}
function af(){
    console.log(variable);
}
f();
console.log(variable)
// af();
var variable = 10;
console.log('---------------')
function f(){
    var x = 100;
    function a(){
        console.log(x);
    }
    a()
}
f()

// using return keyword
function add(a, b){
    return a+b;
}
console.log(add(10, 15))

// boolean
console.log(true)
console.log(false)

// conditions
console.log('---------')
isItTrue();
function isItTrue() {
    condition = true;
    if (condition) {
        console.log(condition);
    }
    console.log(false);
}

alpha = 40
console.log(alpha)
// var alpha

isItTrue();

if (2 && null){
    console.log(2);
}
else if(2 || null){
    console.log('This is true')
}
else{
    console.log(null)
}

// switch uses strict version of js

option = 1

switch(option){
    case 'a' :console.log(option)
                break
    case 'b': console.log('b')
        break;
    default: console.log('Default Value')
        break
    case 1: console.log(1)
        break
    case 1: console.log(2)
        break    
}

console.log('--------')
var opt = 4
switch(opt){
    case 1:
    case 2:
    case 3:
        console.log(('Top level'))
        break
    case 4:
    case 5:
    case 6:
        console.log(('Low level'))
        break;
}

// Objects
var myobj={
    [[12]]:2,
    'property': 5
}
console.log(myobj[12])
prop = 12
console.log(myobj[prop])

// deleting property
delete myobj.property
console.log(myobj)

// checking whether property exist or not
console.log(myobj.hasOwnProperty(12));

// loop
var i = 0
while (i<5){
    console.log(i)
    i++
}

for(let i=0; i<5; i++){
    console.log(i)
}

var array = [21,22,23,42]

for(var i=0; i<array.length; i++){
    console.log(array[i])
}

// do while loop
var i = 10
do{
    console.log(i);
    i++
}while(i<3)


// generating random function
for(let i=0; i<3; i++){
    console.log(Math.random())
}

// generating random whole number using Math.floor()
for(let i=0; i<3; i++){
    console.log(Math.floor(Math.random()*20))
}

// if a number cannot be converted to intiger then it will return NaN
// parsing character into  integer

console.log(parseInt('4'))
2==2?console.log('yes'):console.log('No')

// we cannot redeclear the variable if we have decleared a variable using let keyword

// variable decleared using var in function have local scope to the function

// variable defined using let keyword in have block scope


const S = [1,2,3]

S[0] = [3,4,5]
console.log(S)

Object.freeze(S)  // now data is freezed

// anonymous function
var variable = () => console.log(4)

// taking variable argument
var variable = (...args) => console.log(...args)
variable(234,234,234)

// spread operator is deep copy
var array = [1,2,3]
console.log([...array])

var [x, y, , z] = [1,2,3,4]

// print formatting
console.log(`Hello this is ${x}`)

// in class, 'this' represents 'self' of python
// 'new' is used to instantiate the class

function a(){
    console.log('a')
}
// export {a};

function a(){
    console.log('b')
}