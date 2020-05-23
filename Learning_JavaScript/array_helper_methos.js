var foods = [
    {name:'cauliflower', type:'vegetable'},
    {name1:'banana', type:'fruit'},
    {name:'apple', type:'fruit'},
    {name:'cabbage', type:'vagetable'}
];

var filtered = 
foods.filter(function(food){
    return food.type == 'fruit';
});

console.log(filtered)