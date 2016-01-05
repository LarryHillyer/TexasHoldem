$(document).ready(function() {
  $('#get_status').click(function(){
  var statusid;
  statusid = $(this).attr("data-statusid");
    $.getJSON('/gamesim/get_dispatcher_status/', {dispatcher_status1_id: statusid}, function(data){
	$.each (data, function(key, value) {
		if (key == 'status')
			$('#job_dispatcher_status').html('Job Dispatcher is: ' + value);
		
		else if (key ==	'job_name')
			if (value != '') {
				$('#job_name').attr({ visible: "true"});
				$('#job_name').html('Job running is: ' + value);	}			
			else if (value == '') {
				$('#job_name').attr({ visible: "false"});
				$('#job_name').html(''); }
				
	});
    });
  });
                 if ((key == "p_pc_status") && ((value == "running") || (value == "finished"))) {
 					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >");
                    $(data_cell).html("Player Pie Chart Status: ");
                    $(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); } 				
                 else if	((key == "ht_bc_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >");
                    $(data_cell).html("Hand Type Bar Chart Status: ");
                    $(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); }	 				
 				else if	((key == "ht_pt_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >");
                    $(data_cell).html("Hand Type Prob Table Status: ");
                    $(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); } 		
 				else if	((key == "sp_status") && ((value == "running") || (value == "finished"))) {
 					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >");					
                    $(data_cell).html("Surface Plot Status: ");
 					$(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); }
                else if	((key == "rp_t_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >"); 					
                    $(data_cell).html("Relative Prob Table Status: ");
 					$(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); }
                else if	((key == "s_np_cp_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >"); 					
                    $(data_cell).html("Suited NonPaired Contour Plot Status: ");
 					$(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); }
                else if	((key == "ns_np_cp_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >"); 					
                    $(data_cell).html("NonSuited NonPaired Contour Plot Status: ");
                    $(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); }	
                else if	((key == "p_cp_status") && ((value == "running") || (value == "finished"))){
 					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >");					
                    $(data_cell).html("Paired Contour Plot Status: ");
 					$(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); } 
                else if	((key == "rp_sp_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >"); 					
                    $(data_cell).html("Relative Prob Scatter Plot Status: ");
 					$(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); }
                else if	((key == "pw_p_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >"); 					
                    $(data_cell).html("Percent Winning Plot Status: ");
 					$(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); }
                else if	((key == "pw_t_status") && ((value == "running") || (value == "finished"))) {
					row_idattr = "'row" + key + "'";       
                    $("#analyze_update").append("<tr " + "id=" + row_idattr  + " >");               
 				    data_cell = "#data_cell_1_" + key;
 				    data_cell_id = "'cell_1"  + key + "'";
                    data_cell_2 = "#data_cell_2_" + key;
 				    data_cell_2_id = "'cell_2"  + key + "'"; 
                    $(data_cell).append("<td id=" + data_cell_id + " scope='row' >"); 					
                    $(data_cell).html("Percent Winning Table Status: ");
 				    $(data_cell_2).append("<td id=" + data_cell_2_id + " >");
                    $(data_cell_2).html(value); } 