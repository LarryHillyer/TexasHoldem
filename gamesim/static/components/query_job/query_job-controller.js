app.controller("QueryJobController", function($scope, GetPendingJobList ) {
    $scope.test="QueryJob"
    GetPendingJobList.all().then(function(data){
        $scope.pending_job_list = data
    })
    $scope.start_dispatcher = function() {
        
    }
})