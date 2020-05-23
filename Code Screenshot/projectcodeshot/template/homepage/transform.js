// function get_loc(event){
//     var char = event.which || event.keyCode;
//     if (char == 32){
//         // ASCII value of space is 32
//         console.log(char)
//     }
// }

function pretty(){
    var x = document.getElementById("textarea").value;
    console.log(x.length);
}
var keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']