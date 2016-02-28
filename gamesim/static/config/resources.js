(function(){
    
    app.factory('GetSimJob', function(){
        return {
            all:function(job_name) {
                return $.post("/gamesim/get_sim_job/", job_name).then(function(response){
                    return JSON.parse(response.data);
                })
            }
        }
    })
    
    app.factory('GetSimFormData', function($http){
        return {
            all: function (){
                return $http.get("/gamesim/get_sim_form_data/").then(function(response) {
                    return JSON.parse(response.data);
                })
            }
        }       
    });
    
    app.factory('PutSimFormData', function(){
        return {
            all: function(sim_form_data) {
                return $.post("/gamesim/put_sim_form_data/", sim_form_data)
            }
        }
    });
    
    app.factory('GetPendingJobList', function($http){
        return{
            all: function(){
                return $http.get("/gamesim/get_pending_job_list/").then(function(response){
                    return response.data;
                })
            }
        }
    });
    
    app.factory('DeleteSimJob', function(){
        return{
            all: function(job_name){
                return $.post("/gamesim/delete_sim_job/", job_name )
            }
        }
    });
    
    app.factory('StartDispatcher', function($http){
        return {
            all: function() {
                return $http.get("/gamesim/start_dispatcher/").then(function(response){
                    return response.data
                })
            }
        }
    })
    
    app.factory('ResetDispatcher', function($http){
        return {
            all: function() {
                return $http.get("/gamesim/reset_dispatcher/").then(function(response){
                    return response.data
                })
            }
        }
    })
    
    app.factory('GetDispatcherStatus1', function($http){
        return{
            all: function(){
                return $http.get("/gamesim/get_dispatcher_status1/").then(function(response){
                    return response.data;
                })
            }
        }
    });
    
    app.factory('GetDispatcherTime1', function(){
        return{
            all: function(job_name){
                return $.post("/gamesim/get_dispatcher_time1/", job_name).then(function(response){
                    return response;
                })
            } 
        }
    });
    
    app.factory('GetLoopStatus1', function($http){
        return {
            all: function (){
                return $http.get("/gamesim/get_loop_status1/").then(function(response) {
                    return response.data;
                })
            }
        }       
    }); 
    
    app.service('putPlayers1', function(){       
        this.all = function($rootScope, num_players) {
            $rootScope.simFormData['num_players'] = num_players    
        }    
    })
    
    app.service('putCPUs1', function(){       
        this.all = function($rootScope, num_cpus) {
            $rootScope.simFormData['num_cpus'] = num_cpus    
        }    
    })
    
    app.service('putStartDate2', function(){       
        this.all = function($rootScope, start_date) {
            $rootScope.analyzeFormData['start_date'] = start_date.toString()    
        }    
    })
    
   app.service('putEndDate2', function(){       
        this.all = function($rootScope, end_date) {
            $rootScope.analyzeFormData['end_date'] = end_date.toString()  
        }    
    }) 
    
     
    
   app.service('putPlayers2', function(){       
        this.all = function($rootScope, num_players) {
            $rootScope.analyzeFormData['num_players'] = num_players    
        }    
    }) 
     
   app.factory('PutAnalyzeFormData', function(){
        return {
            all: function(analyze_form_data) {
                return $.post("/gamesim/put_analyze_form_data/", analyze_form_data)
            }
        }
    });    
    
    
})();