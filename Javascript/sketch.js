/*
let max = 100;
let min = 5;
let range = max - min;


let radius = 5;

function setup() {

	createCanvas(500,500, WEBGL);
	//rotateY(PI/2);
	//rotateZ(PI/2);

	fill('red');
	ellipse(5,5,5);
	data.forEach(function(item){

		ellipse(item.x, item.y, radius);

	});

	data.sort(function(a, b){
	    let x1 = a.x;
	    let x2 = b.x;

	    if(x1 < x2) return -1;
	    if(x1 > x2) return 1;

	    return 0;
	});

	console.log(data);

	let pointOnFront = data[0];

	data.forEach(function(item){

		console.log('Front: ' + JSON.stringify(pointOnFront) + 'Next: ' + JSON.stringify(item));

		if(item.y >= pointOnFront.y){
			fill('blue');
			ellipse(pointOnFront.x, pointOnFront.y, radius);
			pointOnFront = item;
		}

	});
}

function draw() {



}*/

var container = document.getElementById('visualization');
let data = [
	{x : 72 , y : 20 , group: 0},
	{x : 24 , y : 90 , group: 0},
	{x : 49 , y : 94 , group: 0},
	{x : 66 , y : 14 , group: 0},
	{x : 72 , y : 27 , group: 0},
	{x : 32 , y : 23 , group: 0},
	{x : 62 , y : 6  , group: 0},
	{x : 87 , y : 72 , group: 0},
	{x : 31 , y : 31 , group: 0},
	{x : 76 , y : 97 , group: 0},
	{x : 63 , y : 56 , group: 0},
	{x : 28 , y : 60 , group: 0},
	{x : 92 , y : 11 , group: 0},
	{x : 50 , y : 94 , group: 0},
	{x : 44 , y : 51 , group: 0},
	{x : 70 , y : 30 , group: 0},
	{x : 42 , y : 60 , group: 0},
	{x : 73 , y : 45 , group: 0},
	{x : 36 , y : 12 , group: 0},
	{x : 67 , y : 72 , group: 0}
];

let groups = new vis.DataSet();

groups.add({
	id: 0,
	content: '<div class="regular"></div>'
});

groups.add({
	id: 1,
	content: 'Front',
	className: 'front'
});

var dataset = new vis.DataSet(data);
var options = {
	style: 'points'
};
var graph2d = new vis.Graph2d(container, dataset, options);