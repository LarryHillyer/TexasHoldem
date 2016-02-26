app.controller("CreateSimController", function($scope, $rootScope, GetSimFormData, PutSimFormData,  $uibModal){
    $scope.test = "Create Simulation"
    $rootScope.simFormData = {};
    
    GetSimFormData.all().then(function(data){
        $rootScope.simFormData = data
        $rootScope.simFormData['save_game_data'] = false
    })
    $rootScope.numPlayers = {
        playersSelect: '2',
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
   $rootScope.numCPUs = {
        cpusSelect: '3',
        availableOptions: [
            {id: '1', name: '1 CPU'},
            {id: '2', name: '2 CPUs'},
            {id: '3', name: '3 CPUs'},         
        ],
   }
   
   $scope.open = function (size) {

      $uibModal.open({  
        templateUrl: '/static/components/create_sim/create_sim-modal.html',
        controller: 'ModalInstanceCtrl1',
        size: size
      })
    }
    
   

})

app.controller("ModalInstanceCtrl1", function($scope, $rootScope, $state, $uibModalInstance, PutSimFormData, putPlayers1, putCPUs1 ){
    
    $rootScope.putPlayers = function(num_players) {
       putPlayers1.all($rootScope, num_players);
    }
    
    $rootScope.putCPUs = function(num_cpus) {
       putCPUs1.all($rootScope, num_cpus)
    }
    
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')           
    }
    
    $scope.putSimJob = function() {
       var simFormDataJSON = JSON.stringify($rootScope.simFormData)
       PutSimFormData.all({'sim_form_data':simFormDataJSON})
   }   
})