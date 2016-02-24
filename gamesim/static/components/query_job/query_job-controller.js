app.controller("QueryJobController", function($scope, $rootScope, GetPendingJobList ) {
    $scope.test="QueryJob"
    GetPendingJobList.all().then(function(data){
        $rootScope.pending_job_list = data
    })
})