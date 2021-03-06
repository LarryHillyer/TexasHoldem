app.controller("AnalyzeJobController", function($scope, $rootScope, $uibModal, GetFinishedJobList){
    $scope.test = "Analyze Job Page"
    GetFinishedJobList.all().then (function(data){
        $rootScope.finished_job_list = data
        if ($rootScope.finished_job_list.length > 0) {
            $scope.open("lg")
        }
    })
    
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/query_analyze_job/query_analyze_job-modal.html',
        controller: 'ModalInstanceCtrl5',
        size: size
      })
    }
    
})

app.controller('ModalInstanceCtrl5', function ($scope, $rootScope, $state, GetFinishedJobList, GetAnalysisJobList, PutAnalyzeJob, $uibModalInstance, StartDispatcher2) {

    GetFinishedJobList.all().then(function (data) {
         $rootScope.finished_job_list = data
         GetAnalysisJobList.all().then(function(data1){
             $rootScope.analysisJobList = data1
         })
    })

    $scope.checkAll = function (selectedAll) {
        if (selectedAll) {
            $scope.selectedAll = true;
        } else {
            $scope.selectedAll = false;
        }
        angular.forEach($rootScope.finished_job_list, function (job) {
            job.selected = $scope.selectedAll;
        });
    };
    
    $scope.goCreateAnalysisJob = function() {
        $rootScope.analyze_job_list = [];
        $scope.error = ""
        angular.forEach($rootScope.finished_job_list, function (job, i) {
            if (job.selected) {
                $rootScope.analyze_job_list.push(job.job_name)
            }
        })
           
        if ($rootScope.analyze_job_list.length > 0) {
            var analyze_job_listJSON = JSON.stringify($rootScope.analyze_job_list)
            PutAnalyzeJob.all({ 'analyze_job_list': analyze_job_listJSON }).then(function(){
                GetAnalysisJobList.all().then(function(data1){
                $rootScope.analysisJobList = data1
        })
            })
        } else {
            $scope.error = "No Jobs Seleted!"
        }
        
        
    }

    $scope.goAnalysisQueue = function () {

        $uibModalInstance.dismiss('cancel')
        $state.go("analyze_queue")
        
    }

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("query_analyze_job")
    }
    
    $scope.goAnalysisDispatcher = function () {
        StartDispatcher2.all().then(function(data){
            $rootScope.dispatcher_status2 = data
            $uibModalInstance.dismiss('cancel')
            $state.go("analyze_dispatcher")
        })      
    }
})