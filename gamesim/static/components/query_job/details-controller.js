app.controller("DetailsController", function($state, $scope, $rootScope, $uibModal, $stateParams, GetPendingJobList, GetSimJob){
    
    
    function findJob(sim_job) {
        for (var i = 0;i<$rootScope.pending_job_list.length;i++){
            if ($rootScope.pending_job_list[i].job_name === $stateParams.job_name) {                             
                return $rootScope.pending_job_list[i];
            }
        }      
    }
    
   GetPendingJobList.all().then(function (data) {
            $rootScope.pending_job_list = data
            $rootScope.simFormData = findJob($stateParams.job_name);
            $rootScope.job_name = $rootScope.simFormData.job_name;

            $rootScope.numPlayers = {
                playersSelect: $rootScope.simFormData.num_players,
                availableOptions: [
                    { id: '2', name: '2 Players' },
                    { id: '3', name: '3 Players' },
                    { id: '4', name: '4 Players' },
                    { id: '5', name: '5 Players' },
                    { id: '6', name: '6 Players' },
                    { id: '7', name: '7 Players' },
                    { id: '8', name: '8 Players' },
                ],
            }

            $rootScope.numCPUs = {
                cpusSelect: $rootScope.simFormData.num_cpus,
                availableOptions: [
                    { id: '1', name: '1 CPU' },
                    { id: '2', name: '2 CPUs' },
                    { id: '3', name: '3 CPUs' },
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
       
})

app.controller("ModalInstanceCtrl", function($scope,$rootScope, $state, $uibModalInstance, DeleteSimJob, PutSimFormData, putPlayers1, putCPUs1 ){
    $scope.goQuery_job = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("query_job")     
    }
    
    $scope.deleteSimJob = function() {
    //    var deleteSimJobJSON = JSON.stringify($rootScope.job.job_name)
       DeleteSimJob.all({'delete_sim_job': $rootScope.simFormData.job_name})
       $uibModalInstance.dismiss('cancel')
       $state.go("query_job")
   }
   
   $rootScope.putPlayers = function(num_players) {
       putPlayers1.all($rootScope, num_players);
       
    }
    
    $rootScope.putCPUs = function(num_cpus) {
       putCPUs1.all($rootScope, num_cpus);
       
    }
   
   $scope.updateSimJob = function () {
       DeleteSimJob.all({'delete_sim_job': $rootScope.simFormData.job_name}).then(function (){
           var simFormDataJSON = JSON.stringify($rootScope.simFormData)
           PutSimFormData.all({'sim_form_data':simFormDataJSON})
           $uibModalInstance.dismiss('cancel')
           $state.go("query_job")
       })      
   }
    
})