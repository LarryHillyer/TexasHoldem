app.controller("InitializeController", function($scope, InitializeSimulation){
    
    $scope.initialSimulation = function(){
        InitializeSimulation.all()
    }
})