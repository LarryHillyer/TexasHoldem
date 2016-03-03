app.controller("AnalyzeQueueController", function($scope, $rootScope, $state, $uibModal,  GetAnalysisJobList, StartDispatcher2 ){
    
    GetAnalysisJobList.all().then(function(data){
        $rootScope.analysis_job_list = data
        if ($rootScope.analysis_job_list.length > 0) {
            $scope.open("lg")
        }
        
    })
    
    $scope.start_dispatcher = function() {
        StartDispatcher2.all().then(function(data){
            $rootScope.dispatcher_status2 = data
            $state.go("analyze_dispatcher")
        })      
    }
       
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/analyze_queue/analyze_queue-modal.html',
        controller: 'ModalInstanceCtrl7',
        size: size
      })
    }    
})

app.controller("ModalInstanceCtrl7", function($scope, $rootScope, $state, $uibModalInstance, StartDispatcher2 ){
    
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("analyze_queue")     
    }
    
    $scope.start_dispatcher2 = function() {
        StartDispatcher2.all().then(function(data){
            $rootScope.dispatcher_status2 = data
            $uibModalInstance.dismiss('cancel')
            $state.go("analyze_dispatcher")
        })      
    }
})