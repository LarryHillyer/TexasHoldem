update_analyzer();
function update_analyzer() { 		
    analyze1Trigger();
    analyze2Trigger();}
	
function analyze1Trigger() {
    return setInterval(function(){ analyze_button_click() }, 2500); }
          	
function analyze2Trigger() {
	return setInterval(function(){ analyze_button2_click() }, 2500); }
	
function analyze_button_click() {		
    var status = document.getElementById("analyze_get_status").getAttribute("class");
	if (status != "Finished" ){
		document.getElementById("analyze_get_status").click(); }}
        	
function analyze_button2_click() {			
    var status = document.getElementById("analyze_get_status").getAttribute("class");	 
	if (status != "Finished" ){
		document.getElementById("analyze_get_l_status").click(); }}