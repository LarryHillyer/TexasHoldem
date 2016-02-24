app.controller("DetailsController", function($state, $scope, $rootScope, $uibModal, $stateParams, GetPendingJobList){
    
    function findJob(sim_job) {
        for (var i = 0;i<$rootScope.pending_job_list.length;i++){
            if ($rootScope.pending_job_list[i].job_name === $stateParams.job_name) {                             
                return $rootScope.pending_job_list[i];
            }
        }      
    }
    GetPendingJobList.all().then(function(data){
        $rootScope.pending_job_list = data
        $rootScope.job = findJob($stateParams.job_name);
        $scope.job_name = $scope.job.job_name;
    
        $scope.numPlayers = {
            playersSelect: $scope.job.num_players,
                availableOptions: [
                    {id: '2', name: '2 Players'},
                    {id: '3', name: '3 Players'},
                    {id: '4', name: '4 Players'},
                    {id: '5', name: '5 Players'},
                    {id: '6', name: '6 Players'},
                    {id: '7', name: '7 Players'},
                    {id: '8', name: '8 Players'},
                        ],
        }
        
        $scope.numCPUs = {
            cpusSelect: $scope.job.num_cpus,
                availableOptions: [
                    {id: '1', name: '1 CPU'},
                    {id: '2', name: '2 CPUs'},
                    {id: '3', name: '3 CPUs'},         
                ],
        }      
    })
       
    $scope.open = function (size) {

      $uibModal.open({  
        templateUrl: '/static/components/query_job/details-modal.html',
        controller: 'ModalInstanceCtrl',
        size: size
      })
    }
       
    
     //  windowTemplateUrl: '/static/components/query_job/details.html', 
    // $uibModal.open({
    //     size: 'lg',
    //     templateUrl: '/static/components/query_job/details-modal.html',
    //     windowTemplateUrl: '/static/components/query_job/query_job.html.html',
    // })
    
})

app.controller("ModalInstanceCtrl", function($scope, $state, $uibModalInstance){
    $scope.goQuery_job = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("query_job")     
    }
})