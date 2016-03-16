app.controller("ChartController", function($scope, $rootScope, $uibModal, $stateParams){
    
    
    $rootScope.job_name = $stateParams.analyzed_job_name;
       
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/query_analyzed_jobs/chart-modal.html',
        controller: 'ModalInstanceCtrl12',
        size: size
      })
    }
    
    $scope.open("lg")   
})

app.controller("ModalInstanceCtrl12", function($scope, $rootScope, $state, $uibModalInstance, $timeout){
    
    $scope.showChart = false
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $showChart = false
        $state.go("charts")     
    }
    
    var fileSS = $rootScope.analyzed_jobs_data[$state.params.chart_name]
    $scope.fileS ="/static/img/" + fileSS
    $scope.showChart = true
    
    // $timeout(function(){
    //     if (!($state.params.chart_name === 'rel_probs_s')) {
    //         var data = $rootScope.analyzed_jobs_data[$state.params.chart_name];
    //         window.data = data
    //         var fig = mpld3.draw_figure('testC', data);
    //         window.fig = fig
    //         fig.enable_zoom()
    //     } else {
            
    //         var fileSS = $rootScope.analyzed_jobs_data[$state.params.chart_name][$state.params.chart_name]
    //         $scope.fileS ="/static/img/" + fileSS
    //         $scope.showChart = true
    // }
                    
    // },300)
    
    
})