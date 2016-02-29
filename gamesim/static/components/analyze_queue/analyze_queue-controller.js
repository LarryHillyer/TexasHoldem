app.controller("AnalyzeQueueController", function($scope, $rootScope, $state, $uibModal, GetAnalysisJobList){
    
    GetAnalysisJobList.all().then(function(data){
        $rootScope.analysis_job_list = data
        if ($rootScope.analysis_job_list.length > 0) {
            $scope.open("lg")
        }
        
    })
    
    // $scope.start_dispatcher = function() {
    //     StartDispatcher.all().then(function(data){
    //         $rootScope.dispatcher_status1 = data
    //         $state.go("job_dispatcher")
    //     })
        
    // }
    
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/analyze_queue/analyze_queue-modal.html',
        controller: 'ModalInstanceCtrl7',
        size: size
      })
    }
     
})

app.controller("ModalInstanceCtrl7", function($scope, $state, $uibModalInstance ){
    
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("analyze_queue")     
    }
})