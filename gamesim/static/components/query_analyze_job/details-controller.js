app.controller("AnalyzeDetailsController", function($scope, $rootScope, $uibModal, GetSimJob, $stateParams){
    
    
    $rootScope.job_name = $stateParams.analyze_job_name;
    
    GetSimJob.all({'get_sim_job':$stateParams.analyze_job_name}).then(function(data){
        $rootScope.analyzeQueueJob = data
        $scope.open("lg")
    })
    
    
       
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/query_analyze_job/details-modal.html',
        controller: 'ModalInstanceCtrl6',
        size: size
      })
    }
       
})

app.controller("ModalInstanceCtrl6", function($scope, $state, $uibModalInstance ){
    
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("query_analyze_job")     
    }
    
    
    
})