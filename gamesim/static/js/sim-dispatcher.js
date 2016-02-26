

function update_dispatcher() {		
	sim1Trigger();
	sim2Trigger();}
		
function sim1Trigger() {
	return setInterval(function(){ sim_button_click() }, 2500); }	
function sim2Trigger() {
	return setInterval(function(){ sim_button2_click() }, 2500); }
	
function sim_button_click() {		
	var status = document.getElementById("get_status").getAttribute("class");
	if (status != "Finished" ){
		document.getElementById("get_status").click(); }}	
function sim_button2_click() {			
	var status = document.getElementById("get_status").getAttribute("class");	 
	if (status != "Finished" ){
		document.getElementById("get_l_status").click(); }}
        
update_dispatcher();       