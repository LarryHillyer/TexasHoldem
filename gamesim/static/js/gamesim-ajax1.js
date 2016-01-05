$(document).ready(function() {
  $("#analyze_get_status").click(function(){
    var statusid;
    statusid = $(this).attr("data-analyzeid");
    $.getJSON('/gamesim/get_dispatcher_status2/', {dispatcher_status1_id: statusid}, function(data){
		$.each (data, function(key, value) {
		if (key == 'status') {
            $("#analyze_dispatcher_status").html('Job Dispatcher is: ' + value);
			if (value == 'Finished') {
				$("#analyze_get_status").attr({class: "Finished"});}}	
		else if (key ==	'job_name'){
			if (value != '') {
				$("#analyze_job").attr({ visible: "true"});
				$("#analyze_job").html('Job: ' + value);	
				    $.getJSON('/gamesim/get_dispatcher_time2/', {running_job_name: value}, function(time_data){
    					$.each (time_data, function(key, value) {
    	    				$("#analyze_dispatcher_time").html("Job has ran for: " + value);
    	    			});
    	    		});
			}}
		}); 
    });	
  });
  
  $("#analyze_get_l_status").click(function(){
    $.getJSON('/gamesim/get_analyze_job_status/', function(table_data) {
    	$("tbody > tr > td").remove();    	
    	$("tbody > tr ").remove();
        $.each (table_data, function(i, table_data1) { 		
        	$.each(table_data1, function(key, value) {
 				var row_idattr = "'row-" + key + "'";                  
 				var data_cell = "#row-" + key;
 				var data_cell_id = "'cell_1"  + key + "'";
                var data_cell_idattr = "#cell_1"  + key;
 				var data_cell_2_id = "'cell_2"  + key + "'";
                var data_cell_2_idattr = "#cell_2"  + key;                      
                if ((key == "p_pc_status") && ((value == "running") || (value == "finished"))) {
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                      
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Player Pie Chart Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}                                    				
                else if ((key == "ht_bc_status") && ((value == "running") || (value == "finished"))) {     
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                     
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Hand Type Bar Chart Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}                
                else if ((key == "ht_pt_status") && ((value == "running") || (value == "finished"))) {      
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                    
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Hand Type Prob Table Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}                
                else if ((key == "sp_status") && ((value == "running") || (value == "finished"))) {       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                     
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Surface Plot Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}        
                else if ((key == "rp_t_status") && ((value == "running") || (value == "finished"))) {      
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                     
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Relative Prob Table Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}
                else if ((key == "s_np_cp_status") && ((value == "running") || (value == "finished"))) {       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                     
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Suited NonPaired Contour Plot Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}                    
                else if ((key == "ns_np_cp_status") && ((value == "running") || (value == "finished"))) {      
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                     
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("NonSuited NonPaired Contour Plot Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}
                else if ((key == "p_cp_status") && ((value == "running") || (value == "finished"))) {       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                    
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Paired Contour Plot Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}
                else if ((key == "rp_bc_status") && ((value == "running") || (value == "finished"))) {       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                     
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Relative Prob Bar Chart Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}                    
                else if ((key == "rp_sp_status") && ((value == "running") || (value == "finished"))) {       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                     
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Relative Prob Scatter Plot Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}
                else if ((key == "pw_p_status") && ((value == "running") || (value == "finished"))) {       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                    
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Percent Winning Plot Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}
                else if ((key == "pw_t_status") && ((value == "running") || (value == "finished"))) {       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");                                    
                    $(data_cell).append("<th id=" + data_cell_id + " scope='row' >");
                    $(data_cell_idattr).html("Percent Winning Table Status: ")
                    $(data_cell).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2_idattr).html(value);}
                                                                                                                                                 					
        	});
      	});
    });
  });
  
   $("#analyze_reset_dispatch").click(function(){
    $.get('/gamesim/reset_dispatcher2/', function(data) { 
    	$("#analyze_dispatcher_status").html('Job Dispatcher is: Reset');});  
  });
});
   