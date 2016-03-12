app.controller('AnalyzeDispatcherController', function($scope, $rootScope,  $uibModal ){
    
    $scope.open = function (size) {

      $uibModal.open({  
        templateUrl: '/static/components/analyze_dispatcher/analyze_dispatcher-modal.html',
        controller: 'ModalInstanceCtrl9',
        size: size
      })
    }
       
    $scope.open("lg")
      
})

app.controller("ModalInstanceCtrl9", function($scope, $rootScope, $state,  $uibModalInstance, StartDispatcher, ResetDispatcher, GetPendingJobList,GetDispatcherStatus2, GetDispatcherTime2, GetAnalyzeJobStatus ){
    
function update_dispatcher() {		
	   sim1Trigger();
	   sim2Trigger();
    }
		
    function sim1Trigger() {
       var int1 = setInterval(function(){ 
           GetDispatcherStatus2.all().then(function(data) {
                $rootScope.dispatcher_status2 = data
                if ($rootScope.dispatcher_status2.status === "Finished" || $rootScope.dispatcher_status2.status === "Stopped"){
                    clearInterval(int1)    
                } else {

                    if ($rootScope.dispatcher_status2.job_name) {
                        var job_name = {"running_job_name": $rootScope.dispatcher_status2.job_name}
                        GetDispatcherTime2.all(job_name).then(function(data){
                            $rootScope.time = data.time_delta
                        })
                    }
                }
           })
       }, 2500) 
    }
    	
    function sim2Trigger() {
       var int2 = setInterval(function(){      
           GetDispatcherStatus2.all().then(function(data) {
                $rootScope.dispatcher_status2 = data
                if ($rootScope.dispatcher_status2.status === "Finished" || $rootScope.dispatcher_status2.status === "Stopped"){
                    clearInterval(int2)    
                } else {
                    GetAnalyzeJobStatus.all().then(function(table_data){
                        $rootScope.renderTable = true ;
                        $rootScope.table_data = table_data[0]
                        angular.forEach(table_data[0], function(value, key){
                        if ((key == "p_pc_status") && ((value == "running") || (value == "finished"))) {
                            $scope.p_pc_status = true
                            $scope.p_pc_value = value
                        }   
                        if ((key == "ht_bc_status") && ((value == "running") || (value == "finished"))) {
                            $scope.ht_bc_status = true
                            $scope.ht_bc_value = value
                        } 
                        if ((key == "ht_pt_status") && ((value == "running") || (value == "finished"))) {
                            $scope.ht_pt_status = true
                            $scope.ht_pt_value = value
                        } 
                        if ((key == "sp_status") && ((value == "running") || (value == "finished"))) {
                            $scope.sp_status = true
                            $scope.sp_value = value
                        } 
                        if ((key == "rp_t_status") && ((value == "running") || (value == "finished"))) {
                            $scope.rp_t_status = true
                            $scope.rp_t_value = value
                        } 
                        if ((key == "s_np_cp_status") && ((value == "running") || (value == "finished"))) {
                            $scope.s_np_cp_status = true
                            $scope.s_np_cp_value = value
                        } 
                        if ((key == "ns_np_cp_status") && ((value == "running") || (value == "finished"))) {
                            $scope.ns_np_cp_status = true
                            $scope.ns_np_cp_value = value
                        }
                        
                        if ((key == "p_cp_status") && ((value == "running") || (value == "finished"))) {
                            $scope.p_cp_status = true
                            $scope.p_cp_value = value
                        } 
                         
                        if ((key == "rp_bc_status") && ((value == "running") || (value == "finished"))) {
                            $scope.rp_bc_status = true
                            $scope.rp_bc_value = value
                        } 
                         if ((key == "rp_sp_status") && ((value == "running") || (value == "finished"))) {
                            $scope.rp_sp_status = true
                            $scope.rp_sp_value = value
                        } 
                        
                        if ((key == "pw_p_status") && ((value == "running") || (value == "finished"))) {
                            $scope.pw_p_status = true
                            $scope.pw_p_value = value
                        } 
                         if ((key == "pw_t_status") && ((value == "running") || (value == "finished"))) {
                            $scope.pw_t_status = true
                            $scope.pw_t_value = value
                        }   
                        })
                    })           
                }
           }) 
       }, 2500);  
    }
    
    $scope.resetDispatcher = function(){
        ResetDispatcher.all()
    }
    
    $scope.goJob_Dispatcher = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("analyze_dispatcher")     
    }    
    
    update_dispatcher();
    
})