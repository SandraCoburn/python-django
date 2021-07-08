var num = 1;

while (num < 10) {
  if (num % 2 === 0) {
    console.log("It's even number" + num);
  }
  num = num + 1;
}

//default parameter
function formal(name = 'Sam', title = 'Sir') {
  console.log(title + '' + name);
  return title + '' + name;
}

//scope
function timesFive(numInput) {
  //local scope to the function
  var result = numInput * 5;
  return result;
}
//Global scope
var v = 'Global V';

function sleepIn(weekday, vacation) {
  return !weekday || vacation;
}
function monkeyTrouble(aSmile, bSmile) {
  return (aSmile && bSmile) || (!aSmile && !bSmile);
}

// Given a tring and a non-negative int n, return a larger string that is n copies of the original string
//ex. stringTimes("Hi",2) -> "HiHi"
function stringTimes(str, n) {
  var returnStr = '';
  var i = 0;
  while (i < n) {
    returnStr += str;
    i++;
  }
  return returnStr;
}

/**Given 3 numerical values, a b c, return their sum. However, if one of the value
 * is 13 then it does not count towars the sum and values to its right do not count.
 * So for ex. if b is 13, then both b anc do not count
 * ex. luckySum(1,2,3) -> 6
 * luckySum(1,13,3) -> 1
 */

function luckySum(a, b, c) {
  if (a == 13) return 0;
  if (b == 13) return a;
  if (c == 13) return a + b;
  return a + b + c;
}

/** 0=no ticket, 1=small ticket, 2=big ticket, if speed is 60 or less, the result is 0. If spped
 *  is between 61 and 80 inclusive, the result is 1. If spped is 81 or more, the result is 2.
 * Unless is is your birthday - on that day, your speed can be 5 higher in all cases.
 * caught_speeding(65, true) -> 0
 */

function caught_speeding(speed, is_birthday) {
  if (is_birthday) {
    speed -= 5;
  }
  if (speed <= 60) return 0;
  if (60 < speed <= 80) return 1;
  return 2;
}

//We want to make a row of bricks that is goal inches long. We have a number of small bricks(1in)
// and big bricks(5in). Return true if is is possible to make the goal by choosing from the given bricks

function makeBricks(small, big, goal) {
  return goal % 5 >= 0 && (goal % 5) - small <= 0 && small + 5 * big >= goal;
}

//Array Iteration
const arr = ['a', 'b', 'c'];
for (letter of arr) {
  console.log(letter);
}

// for (letter of arr) {
//   alert(letter);
// }
//Built in array does the same as above
// arr.forEach(alert);

function addAwesome(name) {
  console.log(name + 'is awesome!');
}
var topics = ['python', 'django', 'science'];
topics.forEach(addAwesome);

var roster = [];
function addNew() {
  var newName = prompt('What name would you like to add?');
}
function remove() {
  var remName = prompt('What name would you like to remove?');
  var index = roster.indexOf(remName);
  roster.splice(index, 1);
}
function display() {
  console.log(roster);
}
var start = prompt('Would you like to start the roster web app? y/n');
var request = 'empty';

if (start === 'y') {
  while (request !== 'quit') {
    request = prompt('Please select an action: add, remove, display, or quit.');
    if (request === 'add') {
      addNew();
    } else if (request === 'display') {
      display();
    } else if (request === 'remove') {
      remove();
    } else {
      alert('Not recognized');
    }
  }
}
alert('Thanks for using the web app. Please refresh to start over.');

// objects
var carInfo = {
  make: 'Toyota',
  year: '1990',
  model: 'camry',
  carAlert: function () {
    alert("We've got a car here!");
  },
};
carInfo['make']; //will display "Toyota"
console.dir(carInfo);

var myNewObj = {
  a: 'hello',
  b: [1, 2, 4],
  c: { inside: ['a', 'b', 'c'] },
};
console.log(myNewObj['a']);
console.log(myNewObj['b'][1]); //2
console.log(myNewObj['c']['inside'][2]); //c

for (key in carInfo) {
  console.log(key); //all keys
  console.log(carInfo[key]); //all keys and values
}

var myObj = {
  prop: 37,
  reportProp: function () {
    return this.prop;
  },
};
console.log(myObj.reportProp()); //logs 37

var simple = {
  prop: 'Hello',
  myMethod: function () {
    console.log('The myMethod was called');
  },
};
console.dir(simple);
simple.myMethod();

var myObj = {
  name: 'Sandra',
  greet: function () {
    console.log('Hello' + this.name);
  },
};
console.log(myObj['name']);
console.log(myObj.greet());

//get the last name of employee
var employee = {
  name: 'John Smith',
  job: 'programmer',
  age: 31,
  lastName: function () {
    console.log(this.name.split(' ')[1]);
  },
};
