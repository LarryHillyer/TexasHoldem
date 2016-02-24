app.config(function($stateProvider, $urlRouterProvider){
   $urlRouterProvider.otherwise("home")
   
   $stateProvider
    .state ("home", {
        url: "/home",
        templateUrl: "/static/components/home/home.html",
        controller: "HomeController",
        controllerAs: "hc"
    })
    .state ("create_sim", {
        url: "/create_sim",
        templateUrl: "/static/components/create_sim/create_sim.html",
        controller: "CreateSimController",
        controllerAs: "csc"
    })
    .state ("query_job", {
        url: "/query_job",
        templateUrl: "/static/components/query_job/query_job.html",
        controller: "QueryJobController",
        controllerAs: "qjc"
    })
    
    .state ("job", {
        url:"/query_job/:job_name",
        templateUrl:"/static/components/query_job/details.html",
        controller:"DetailsController",
        controllerAs: "dc"
        
    })
    
})