app.controller("AnalyzeJobsController", function($scope, $rootScope, $uibModal){
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/analyze_jobs/analyze_jobs-modal.html',
        controller: 'ModalInstanceCtrl4',
        size: size
      })
    }
    
    $scope.open();
     
})

app.controller("ModalInstanceCtrl4", function($scope, $rootScope, $uibModalInstance, putPlayers2, putStartDate2, putEndDate2, PutAnalyzeFormData) {
    
    $rootScope.analyzeFormData = {}
    var analyzeFormData1 = {}
    
    $rootScope.num_players = {
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
    
    $scope.today = function () {
        $scope.analyzeFormData.start_date = new Date();
        $scope.analyzeFormData.end_date = new Date();
    };
    $scope.today();

    $scope.clear = function () {
        $scope.analyzeFormData.start_date = null;
        $scope.analyzeFormData.end_date = null;
    };

    $scope.inlineOptions = {
        customClass: getDayClass,
        minDate: new Date(),
        showWeeks: true
    };

    $scope.dateOptions = {
        dateDisabled: disabled,
        formatYear: 'yy',
        maxDate: new Date(2020, 5, 22),
        minDate: new Date(),
        startingDay: 1
    };

    // Disable weekend selection
    function disabled(data) {
        var date = data.date,
            mode = data.mode;
        return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
    }

    $scope.toggleMin = function () {
        $scope.inlineOptions.minDate = $scope.inlineOptions.minDate ? null : new Date();
        $scope.dateOptions.minDate = $scope.inlineOptions.minDate;
    };

    $scope.toggleMin();

    $scope.openStartDate = function () {
        $scope.startDate.opened = true;
    };
    
    $scope.openEndDate = function () {
        $scope.endDate.opened = true;
    };

    $scope.setDate = function (year, month, day) {
        $scope.analyzeFormData.start_date = new Date(year, month, day);
        $scope.analyzeFormData.end_date = new Date(year, month, day);
    };

    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    $scope.format = $scope.formats[0];
    $scope.altInputFormats = ['M!/d!/yyyy'];

    $scope.startDate = {
        opened: false
    };
    
    $scope.endDate = {
        opened: false
    };

    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    var afterTomorrow = new Date();
    afterTomorrow.setDate(tomorrow.getDate() + 1);
    $scope.events = [
        {
            date: tomorrow,
            status: 'full'
        },
        {
            date: afterTomorrow,
            status: 'partially'
        }
    ];

    function getDayClass(data) {
        var date = data.date,
            mode = data.mode;
        if (mode === 'day') {
            var dayToCheck = new Date(date).setHours(0, 0, 0, 0);

            for (var i = 0; i < $scope.events.length; i++) {
                var currentDay = new Date($scope.events[i].date).setHours(0, 0, 0, 0);

                if (dayToCheck === currentDay) {
                    return $scope.events[i].status;
                }
            }
        }
        return '';
    }
    
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')           
    }
    
    $scope.putPlayers = function($rootScope, num_players) {
       putPlayers2.all($rootScope, num_players);
    }
    
    $scope.putStartDate = function($rootScope, start_date) {
        putStartDate2.all($rootScope, start_date)
    }
    
    $scope.putEndDate = function($rootScope, end_date) {
        putEndDate2.all($rootScope, end_date)
    }
    
    $scope.putPlayers($rootScope, $rootScope.num_players.playersSelect)
    
    $scope.putAnalyzeQueue = function() {
        
        analyzeFormData1['num_players'] = $rootScope.analyzeFormData.num_players
        analyzeFormData1['start_date'] = $rootScope.analyzeFormData.start_date.toISOString()
        analyzeFormData1['end_date'] = $rootScope.analyzeFormData.end_date.toISOString()
        var analyzeFormDataJSON1 = JSON.stringify(analyzeFormData1)
        PutAnalyzeFormData.all({'analyze_form_data':analyzeFormDataJSON1})
    }
    
})
