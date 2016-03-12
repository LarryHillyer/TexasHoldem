app.controller("ChartsController", function($scope, $rootScope, $uibModal, $stateParams){
    
    
    $rootScope.job_name = $stateParams.analyzed_job_name;
       
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/query_analyzed_jobs/charts-modal.html',
        controller: 'ModalInstanceCtrl11',
        size: size
      })
    }
    
    $scope.open("lg")   
})

app.controller("ModalInstanceCtrl11", function($scope, $rootScope, $state, $uibModalInstance ){
    
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("query_analyzed_jobs")     
    }
    $rootScope.charts_list = []
    angular.forEach($rootScope.analyzed_jobs_list, function (job) {
          if (job.job_name === $rootScope.job_name || job.job_name === $rootScope.selectedJob.job_name) {
               
               angular.forEach(job.analyzed_job_data, function(chart) {
                   for (var chart_name in chart) {
                       $rootScope.charts_list.push(chart_name)
                   } 
               })          
          }  
    });
    
    $rootScope.goChart = function(chart) {
        $rootScope.selectedChart = chart
        var foundChart = false
        for (var i=0;i<$rootScope.selectedJob.analyzed_job_data.length; i++) {
            for (var chartType in $rootScope.selectedJob.analyzed_job_data[i]) {
                if (chartType === chart) {
                    $rootScope.analyzed_jobs_data = $rootScope.selectedJob.analyzed_job_data[i]
                    foundChart = true
                    break
                }
            }
            if (foundChart) {
                break
            }
        }       
        $uibModalInstance.dismiss('cancel')
    }
    
})