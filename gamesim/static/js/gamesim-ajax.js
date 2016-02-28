$(document).ready(function() {
  
  
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