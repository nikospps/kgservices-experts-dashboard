var svg = d3.select("svg"),
    width = +svg.node().getBoundingClientRect().width,
    height = +svg.node().getBoundingClientRect().height;

// svg objects
var link, node, linkText, nodeText;
// the data - an object with nodes and links
var triples;

// load the data
d3.json("http://dockerengine.magneto.dcom.upv.es:5545/query3", function(error, _graph) {
    if (error) throw error;
    triples = _graph;
    graph = triplesToGraph(triples);
    initializeDisplay();
    initializeSimulation();
});


//=====================Important Functions Definition for nodes and links initialization========================
function filterNodesById(nodes,id){
    return nodes.filter(function(n) { return n.id === id; });
}

function filterNodesByType(nodes,value){
    return nodes.filter(function(n) { return n.type === value; });
}

function triplesToGraph(triples){

    svg.html("");
    //Graph Initialization
    var graph={nodes:[], links:[]};

    //Initial Graph from triples (list)
    triples.forEach(function(triple){
        var subjId = triple.subject;
        var predId = triple.predicate;
        var objId = triple.object;

        var subjNode = filterNodesById(graph.nodes, subjId)[0];
        var objNode  = filterNodesById(graph.nodes, objId)[0];

        if(subjNode==null){
            subjNode = {id:subjId, label:subjId, weight:1, type:"node", l:"sub"};
            graph.nodes.push(subjNode);
        }

        if(objNode==null){
            objNode = {id:objId, label:objId, weight:1, type:"node", l:"obj"};
            graph.nodes.push(objNode);
        }

        var predNode = {id:predId, label:predId, weight:1, type:"pred", l:"pre"} ;
        graph.nodes.push(predNode);

        var blankLabel = "";

        graph.links.push({source:subjNode, target:predNode, predicate:blankLabel, weight:1});
        graph.links.push({source:predNode, target:objNode, predicate:blankLabel, weight:1});


    });

    return graph;
}
//////////////////////////////////////////
//////////// FORCE SIMULATION ////////////

// force simulator
var simulation = d3.forceSimulation();

// set up the simulation and event to update locations after each tick
function initializeSimulation() {

    simulation.nodes(graph.nodes);
    initializeForces();
    simulation.on("tick", ticked);
}

// values for all forces
forceProperties = {
    center: {
        x: 0.5,
        y: 0.3
    },
    charge: {
        enabled: true,
        strength: -50,
        distanceMin: 1,
        distanceMax: 1500
    },
    collide: {
        enabled: false,
        strength: .5,
        iterations: 1,
        radius: 4
    },
    forceX: {
        enabled: false,
        strength: .1,
        x: .5
    },
    forceY: {
        enabled: false,
        strength: .1,
        y: .5
    },
    link: {
        enabled: true,
        distance: 30,
        iterations: 1
    }
}

// add forces to the simulation
function initializeForces() {
    // add forces and associate each with a name
    simulation
        .force("link", d3.forceLink())
        .force("charge", d3.forceManyBody())
        .force("collide", d3.forceCollide())
        .force("center", d3.forceCenter())
        .force("forceX", d3.forceX())
        .force("forceY", d3.forceY());
    // apply properties to each of the forces
    updateForces();
}

// apply new force properties
function updateForces() {
    // get each force by name and update the properties
    simulation.force("center")
        .x(width * forceProperties.center.x)
        .y(height * forceProperties.center.y);
    simulation.force("charge")
        .strength(forceProperties.charge.strength * forceProperties.charge.enabled)
        .distanceMin(forceProperties.charge.distanceMin)
        .distanceMax(forceProperties.charge.distanceMax);
    simulation.force("collide")
        .strength(forceProperties.collide.strength * forceProperties.collide.enabled)
        .radius(forceProperties.collide.radius)
        .iterations(forceProperties.collide.iterations);
    simulation.force("forceX")
        .strength(forceProperties.forceX.strength * forceProperties.forceX.enabled)
        .x(width * forceProperties.forceX.x);
    simulation.force("forceY")
        .strength(forceProperties.forceY.strength * forceProperties.forceY.enabled)
        .y(height * forceProperties.forceY.y);
    simulation.force("link")
        .id(function(d) {return d.id;})
        .distance(forceProperties.link.distance)
        .iterations(forceProperties.link.iterations)
        .links(forceProperties.link.enabled ? graph.links : []);

    // updates ignored until this is run
    // restarts the simulation (important if simulation has already slowed down)
    simulation.alpha(1).restart();
}


//////////// DISPLAY ////////////

// generate the svg objects and force simulation
function initializeDisplay() {

    // ==================== Add Marker ====================
    //appending little triangles, path object, as arrowhead
    //The <defs> element is used to store graphical objects that will be used at a later time
    //The <marker> element defines the graphic that is to be used for drawing arrowheads or polymarkers on a given <path>, <line>, <polyline> or <polygon> element.
    svg.append("svg:defs").selectAll("marker")
        .data(["end"])
        .enter().append("svg:marker")
        .attr("id", 'arrowhead')//String)
        .attr("viewBox", "0 -5 10 10")
        .attr("refX", 30)
        .attr("refY", -0.5)
        .attr("markerWidth", 6)
        .attr("markerHeight", 6)
        .attr("orient", "auto")
        .append("svg:polyline")
        .attr("points", "0,-5 10,0 0,5")
        // .on("mouseout", 'url(#end-arrow-fade)');
        // .style('opacity', d => d.opacity);
    // ====================

    // set the data and properties of link lines
    link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
        .attr("marker-end", "url(#arrowhead)")
        // .attr("class", "link")
        // .attr("stroke-width",1)
        // .on("mouseover", 'url(#end-arrow-fade)');

    // ==================== Add Links Names =====================
    linkText = svg.selectAll(".link-text")
        .data(graph.links)
        .enter()
        .append("text")
        .attr("class", "link-text")
       	.text( function (d) { return d.predicate; });
// ==================== Add Nodes Names =====================
    nodeText = svg.selectAll(".node-text")
        .data(graph.nodes)
        .enter()
        .append("text")
        .attr("class", "node-text")
        .on("dblclick", function(d) {return d.l=="pre" ? d.label : "";})
        // .on("mouseover", function(d) {return d.id;})
        .text( function (d) {
          return d.l=="sub" ? d.label // collapsed package
              : d.l=="obj" ? d.label // expanded package
              : ""; // leaf node
        })//{ return d.label; });

    // set the data and properties of node circles
    node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(graph.nodes)
        .enter().append("circle")
        // .enter().append("rect")
        .attr("class", "node")
        // .attr("width", 8)
        // .attr("height", 8)
	      .style("fill", color)
        // .attr("class", "node")
        // .attr("r",8)
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));


    // node tooltip
    node.append("title")
        .text(function(d) { return d.id; });

    // visualize the graph
    updateDisplay();
}

// update the display based on the forces (but not positions)
function updateDisplay() {
    node
        .attr("r", forceProperties.collide.radius)
       // .attr("stroke", forceProperties.charge.strength > 0 ? "blue" : "purple")
        //.attr("stroke-width", forceProperties.charge.enabled==false ? 0 : Math.abs(forceProperties.charge.strength)/15)
        .on("mouseover", fade(0.1))
        .on("mouseout", fade(1));

    link
        .attr("stroke-width", forceProperties.link.enabled ? 1 : .5)
        .attr("opacity", forceProperties.link.enabled ? 1 : 0);
}

// update the display positions after each simulation tick
function ticked() {
    node
        .attr("cx", function(d){ return d.x; })
        .attr("cy", function(d){ return d.y; })
        // .attr("x", function(d) { return d.x; })
        // .attr("y", function(d) { return d.y; });
    ;

    link
        .attr("x1", 	function(d)	{ return d.source.x; })
        .attr("y1", 	function(d) { return d.source.y; })
        .attr("x2", 	function(d) { return d.target.x; })
        .attr("y2", 	function(d) { return d.target.y; })
    ;

    nodeText
        .attr("x", function(d) { return d.x + 12 ; })
        .attr("y", function(d) { return d.y + 3; })
    ;


    linkText
        .attr("x", function(d) { return 4 + (d.source.x + d.target.x)/2  ; })
        .attr("y", function(d) { return 4 + (d.source.y + d.target.y)/2 ; })
    ;
    d3.select('#alpha_value').style('flex-basis', (simulation.alpha()*100) + '%');
}
//////////// UI EVENTS ////////////
function color(d) {
  return d.l=="sub" ? "blue" // collapsed package
      : d.l=="obj" ? "orange" // expanded package
      : "green"; // leaf node
}

function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0.0001);
    d.fx = null;
    d.fy = null;
}
//Effort to insert Node Neighbor Highlight
const linkedByIndex = {};
graph.links.forEach(d => {
    linkedByIndex[`${d.source.index},${d.target.index}`] = 1;
});

function isConnected(a, b) {
    return linkedByIndex[`${a.index},${b.index}`] || linkedByIndex[`${b.index},${a.index}`] || a.index === b.index;
}

function fade(opacity) {
    return d => {
        node.style('stroke-opacity', function (o) {
            const thisOpacity = isConnected(d, o) ? 1 : opacity;
            this.setAttribute('fill-opacity', thisOpacity);
            return thisOpacity;
        });

        link.style('stroke-opacity', o => (o.source === d || o.target === d ? 1 : opacity));
        // link.attr('marker-end', o => (opacity === 1 || o.source === d || o.target === d ? 'url(#end-arrow)' : 'url(#end-arrow-fade)'));//prevents from marker opacity
    };
}
//
// update size-related forces
d3.select(window).on("resize", function(){
    width = +svg.node().getBoundingClientRect().width;
    height = +svg.node().getBoundingClientRect().height;
    updateForces();
});

// convenience function to update everything (run after UI input)
function updateAll() {
    updateForces();
    updateDisplay();
}
