app.controller("QueryJobController", function($scope, $rootScope, $state, GetPendingJobList, StartDispatcher ) {
    
    $scope.test="QueryJob"
    GetPendingJobList.all().then(function(data){
        $scope.pending_job_list = data
        
    })
    
    $scope.start_dispatcher = function() {
        StartDispatcher.all().then(function(data){
            $rootScope.dispatcher_status1 = data
            $state.go("job_dispatcher")
        })
        
    }
})