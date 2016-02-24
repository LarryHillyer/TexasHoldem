(function(){
    
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
    })
    
    
})();