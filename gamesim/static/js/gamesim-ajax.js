$(document).ready(function() {
  $("#get_status").click(function(){
  var statusid;
  statusid = $(this).attr("data-statusid");
    $.getJSON('/gamesim/get_dispatcher_status/', {dispatcher_status1_id: statusid}, function(data){
		$.each (data, function(key, value) {
		if (key == 'status')
			$("#job_dispatcher_status").html('Job Dispatcher is: ' + value);
			if (value == 'Finished') {
				$("#get_status").attr({class: "Finished"});}	
		else if (key ==	'job_name')
			if (value != '') {
				$("#job_name").attr({ visible: "true"});
				$("#job_name").html('Job: ' + value);	
				    $.getJSON('/gamesim/get_dispatcher_time/', {running_job_name: value}, function(time_data){
    					$.each (time_data, function(key, value) {
    	    				$("#dispatcher_time").html("Job has ran for: " + value);
    	    			});
    	    		});
				}
		}); 
    });	
  });

  $("#get_l_status").click(function(){
    $.getJSON('/gamesim/get_loop_status', function(table_data) {
    	$("tbody > tr > td").remove();    	
    	$("tbody > tr ").remove();

        $.each (table_data, function(i, table_data1) { 		
      	    var row = new Number(i);
 			var row_idattr = "'row" + row.toString()+ "'";       
            $("#cpu_update").append("<tr " + "id=" + row_idattr  + " >");
        	$.each(table_data1, function(key, value) {
 				var data_cell = "#row" + row.toString();
 				var cell_idattr = "'cell_" + row.toString() + key + "'";
 				var cell_idattr2 = "#cell_" + row.toString() + key;
 				if (key == "loop_num")  {
 					$(data_cell).append("<th id=" + cell_idattr + " scope='row' >");
 					$(cell_idattr2).html(value); }
 				else if	(key == "cpu1_exit_status") {
 					$(data_cell).append("<td id=" + cell_idattr + " >");
 					$(cell_idattr2).html(value); }	 				
 				else if	(key == "cpu2_exit_status") {
 					$(data_cell).append("<td id=" + cell_idattr + " >");
 					$(cell_idattr2).html(value); }		
 				else if	(key == "cpu3_exit_status") {
 					$(data_cell).append("<td id=" + cell_idattr + " >");
 					$(cell_idattr2).html(value); }						
        	});
      	});
    });
  });
  
  $("#reset_dispatch").click(function(){
    $.get('/gamesim/reset_dispatcher/', function(data) { 
    	$("#job_dispatcher_status").html('Job Dispatcher is: Reset');});  
  });
  
  $(function(){
    $("#start_date").datepicker();
  });
  
  $(function(){
    $("#end_date").datepicker();
  });
  
  $(".child-checkbox").change( function() {
    $(".checkbox-group .parent-checkbox .selectall :checkbox").prop("checked", $(".child-checkbox .selectone :checkbox").not(":checked").length==0);
 });
 $(".parent-checkbox").change(function() {
    $(".checkbox-group .child-checkbox .selectone :checkbox").prop("checked", $(".parent-checkbox .selectall :checkbox").not(":checked").length ==0);     
 });
 

 });