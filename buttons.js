const execSh = require("exec-sh");

var pyPath = "C:/Users/Colin/AppData/Local/Programs/Python/Python311/python.exe"; // NOTE Enter your PATH to Python interpreter
var route_a = pyPath + ' ' + 'route_a.py'; // NOTE Enter PATH to route file
var route_b = pyPath + ' ' + 'route_b.py'; // NOTE Enter PATH to route file
var route_c = pyPath + ' ' + 'route_c.py'; // NOTE Enter PATH to route file
const buttonA = document.getElementById("route-a-btn"); 
const buttonB = document.getElementById("route-b-btn");
const buttonC = document.getElementById("route-c-btn");

buttonA.addEventListener("click", () => {
  execSh(route_a, { cwd: "./src" }, function(err){
    if (err) {
      console.log("Exit code: ", err.code);
    }
  });
})

buttonB.addEventListener("click", () => {
  execSh(route_b, { cwd: "./src" }, function(err){
    if (err) {
      console.log("Exit code: ", err.code);
    }
  });
})

buttonC.addEventListener("click", () => {
  execSh(route_c, { cwd: "./src" }, function(err){
    if (err) {
      console.log("Exit code: ", err.code);
    }
  });
})
