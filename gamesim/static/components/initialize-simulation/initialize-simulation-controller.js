app.controller("InitializeController", function($scope, $state, InitializeSimulation){
    
    $scope.initialSimulation = function(){
        InitializeSimulation.all().then(function(){
            $state.go("home")
        })
    }
})