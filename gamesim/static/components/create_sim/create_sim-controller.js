app.controller("CreateSimController", function($scope, $rootScope, GetSimFormData, PutSimFormData){
    $scope.test = "Create Simulation"
    $scope.simFormData = {};
    
    GetSimFormData.all().then(function(data){
        $scope.simFormData = data
        $scope.simFormData['save_game_data'] = false
    })
    $scope.numPlayers = {
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
   $scope.numCPUs = {
        cpusSelect: '3',
        availableOptions: [
            {id: '1', name: '1 CPU'},
            {id: '2', name: '2 CPUs'},
            {id: '3', name: '3 CPUs'},         
        ],
   }
   
   $scope.putPlayers = function(num_players) {
       $scope.simFormData['num_players'] = num_players
   }
   $scope.putCPUs = function(num_cpus) {
       $scope.simFormData['num_cpus'] = num_cpus
   }
   $scope.putSimJob = function() {
       var simFormDataJSON = JSON.stringify($scope.simFormData)
       PutSimFormData.all({'sim_form_data':simFormDataJSON})
   }
})