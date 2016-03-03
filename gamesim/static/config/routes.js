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
    
    .state ("job_dispatcher", {
        url: "/job_dispatcher",
        templateUrl:"/static/components/job_dispatcher/job_dispatcher.html",
        controller:"JobDispatcherController",
        controllerAs: "jdc"
    })
    
    .state ("analyze_jobs", {
        url: "/analyze_jobs",
        templateUrl:"/static/components/analyze_jobs/analyze_jobs.html",
        controller:"AnalyzeJobsController",
        controllerAs: "ajc"
    })
    
    .state ("query_analyze_job", {
        url: "/query_analyze_job",
        templateUrl: "/static/components/query_analyze_job/query_analyze_job.html",
        controller: "AnalyzeJobController",
        controllerAs: "qajc"
    })
    
    .state ("analyze_job", {
        url:"/query_analyze_job/:analyze_job_name",
        templateUrl:"/static/components/query_analyze_job/details.html",
        controller:"AnalyzeDetailsController",
        controllerAs: "adc"    
    })
    
    .state ("analyze_queue", {
        url: "/analyze_queue",
        templateUrl: "/static/components/analyze_queue/analyze_queue.html",
        controller: "AnalyzeQueueController",
        controllerAs: "aqc"
    })
    
    .state ("analyze_queue_job", {
        url:"/analyze_queue/:analyze_job_name",
        templateUrl:"/static/components/analyze_queue/details.html",
        controller:"AnalyzeQueueDetailsController",
        controllerAs: "aqdc"    
    })
    
    .state ("analyze_dispatcher", {
        url: "/analyzer_dispatcher",
        templateUrl:"/static/components/analyze_dispatcher/analyze_dispatcher.html",
        controller:"AnalyzeDispatcherController",
        controllerAs: "adc1"
    })
    
    .state ("initialize_simulation", {
        url:"/initialize_simulation",
        templateUrl:"/static/components/initialize-simulation/initialize-simulation.html",
        controller:"InitializeController",
        controllerAs: "ic" 
    })
    
    
    
})