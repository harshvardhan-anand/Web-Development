setTask = () => {
    let task = document.getElementById("taskinput").value;
    let node = document.createElement("h1");
    let id = () => {
            let multiplier = Math.floor(Math.random() * 10);
            let id = Math.floor(Math.random() * 10000)*multiplier;
        return id;
    }
    node.setAttribute('id', id())
    let textNode = document.createTextNode(task);
    node.appendChild(textNode);
    document.getElementById("alltask").appendChild(node);
}

comp = document.getElementById("alltask").addEventListener(
    'click',
    function(event){
        if (event.target.className!='closed'){
            document.getElementById(event.target.id).setAttribute('class','closed');
            document.getElementById(event.target.id).style.textDecorationLine = 'line-through';
        }
        else{
            document.getElementById(event.target.id).removeAttribute('style');
            document.getElementById(event.target.id).removeAttribute('class');
        }
    }
)