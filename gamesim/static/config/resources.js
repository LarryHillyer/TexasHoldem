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
    
    app.factory('PutSimFormData', function($http){
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
    
    app.factory('GetDispatcherStatus1', function($http){
        return{
            all: function(){
                return $http.get("/gamesim/get_dispatcher_status1/").then(function(response){
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
    
    
})();