app.controller("QueryAnalyzedJobsController", function($scope, $rootScope, $uibModal, GetAnalyzedJobsList){
    $scope.test = "Analyzed Jobs Page"
    GetAnalyzedJobsList.all().then (function(data){
        $rootScope.analyzed_jobs_list = data
        if ($rootScope.analyzed_jobs_list.length > 0) {
            $scope.open("lg")
        }
    })
    
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/query_analyzed_jobs/query_analyzed_jobs-modal.html',
        controller: 'ModalInstanceCtrl10',
        size: size
      })
    }
    
})

app.controller('ModalInstanceCtrl10', function ($scope, $rootScope, $state, GetAnalyzedJobsList,  $uibModalInstance) {

    GetAnalyzedJobsList.all().then(function (data) {
         $rootScope.analyzed_jobs_list = data

    })

    $scope.checkAll = function (selectedAll) {
        if (selectedAll) {
            $scope.selectedAll = true;
        } else {
            $scope.selectedAll = false;
        }
        angular.forEach($rootScope.analyzed_jobs_list, function (job) {
            job.selected = $scope.selectedAll;
        });
    };

    $scope.goCharts = function (job) {
        $rootScope.selectedJob = job
        $uibModalInstance.dismiss('cancel')    
    }

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("query_analyzed_jobs")
    }
    
})