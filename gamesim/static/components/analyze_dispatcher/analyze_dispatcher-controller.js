app.controller('AnalyzeDispatcherController', function($scope, $rootScope,  $uibModal ){
    
    $scope.open = function (size) {

      $uibModal.open({  
        templateUrl: '/static/components/analyze_dispatcher/analyze_dispatcher-modal.html',
        controller: 'ModalInstanceCtrl3',
        size: size
      })
    }
       
    $scope.open("lg")
      
})

app.controller("ModalInstanceCtrl9", function($scope, $rootScope, $state,  $uibModalInstance, StartDispatcher, ResetDispatcher, GetPendingJobList,GetDispatcherStatus1, GetDispatcherTime1, GetLoopStatus1  ){
    
function update_dispatcher() {		
	   sim1Trigger();
	   sim2Trigger();
    }
		
    function sim1Trigger() {
       var int1 = setInterval(function(){ 
           GetDispatcherStatus1.all().then(function(data) {
                $rootScope.dispatcher_status1 = data
                if ($rootScope.dispatcher_status1.status === "Finished" || $rootScope.dispatcher_status1.status === "Stopped"){
                    clearInterval(int1)    
                } else {

                    if ($rootScope.dispatcher_status1.job_name) {
                        var job_name = {"running_job_name": $rootScope.dispatcher_status1.job_name}
                        GetDispatcherTime1.all(job_name).then(function(data){
                            $rootScope.time = data.time_delta
                        })
                    }
                }
           })
       }, 2500) 
    }
    	
    function sim2Trigger() {
       var int2 = setInterval(function(){      
           GetDispatcherStatus1.all().then(function(data) {
                $rootScope.dispatcher_status1 = data
                if ($rootScope.dispatcher_status1.status === "Finished" || $rootScope.dispatcher_status1.status === "Stopped"){
                    clearInterval(int2)    
                } else {
                    GetLoopStatus1.all().then(function(table_data){
                        $rootScope.renderTable = true ;
                        $rootScope.table_data = table_data
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
        $state.go("analyzer_dispatcher")     
    }    
    
    update_dispatcher();
    
})