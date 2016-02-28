app.controller("QueryJobController", function($scope, $rootScope, $state, GetPendingJobList, StartDispatcher, $uibModal ) {
    
    GetPendingJobList.all().then(function(data){
        $scope.pending_job_list = data
        if ($scope.pending_job_list.length > 0) {
            $scope.open("lg")
        }
        
    })
    
    $scope.start_dispatcher = function() {
        StartDispatcher.all().then(function(data){
            $rootScope.dispatcher_status1 = data
            $state.go("job_dispatcher")
        })
        
    }
    
    $scope.open = function (size) {

      $uibModal.open({  
        templateUrl: '/static/components/query_job/query_job-modal.html',
        controller: 'ModalInstanceCtrl2',
        size: size
      })
    }
    
      
   
})

app.controller("ModalInstanceCtrl2", function($scope,$rootScope, $state, $uibModalInstance, StartDispatcher, GetPendingJobList ){
    
    GetPendingJobList.all().then(function(data){
        $scope.pending_job_list = data       
    })
    
    $scope.goQuery_job = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("query_job")     
    }
    
    $scope.start_dispatcher = function() {
        StartDispatcher.all().then(function(data){
            $rootScope.dispatcher_status1 = data
            $uibModalInstance.dismiss('cancel')
            $state.go("job_dispatcher")
        })
    }
    
    $scope.goJob = function(job) {
        $uibModalInstance.dismiss('cancel')
    }  
})