app.controller("ChartController", function($scope, $rootScope, $uibModal, $stateParams){
    
    
    $rootScope.job_name = $stateParams.analyzed_job_name;
       
    $scope.open = function (size) {
      $uibModal.open({  
        templateUrl: '/static/components/query_analyzed_jobs/chart-modal.html',
        controller: 'ModalInstanceCtrl12',
        size: size
      })
    }
    
    $scope.open("lg")   
})

app.controller("ModalInstanceCtrl12", function($scope, $rootScope, $state, $uibModalInstance, $timeout){
    
    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel')
        $state.go("charts")     
    }
    $timeout(function(){
        if (!($state.params.chart_name === 'rel_probs_s')) {
            var data = $rootScope.analyzed_jobs_data[$state.params.chart_name];
            window.data = data
            var fig = mpld3.draw_figure('testC', data);
            window.fig = fig
            fig.enable_zoom()
        } else {
            var dataS = $rootScope.analyzed_jobs_data[$state.params.chart_name][$state.params.chart_name];
            var surfacePlot = [{name:$state.params.chart_name,
                                data: dataS   
            }]
            var yaw=0.5,pitch=0.5, width=600, height=350, drag=false;
            // var selected=surfacePlot[0];

            var ul=d3.select("body")
                .append('ul');
            var svg=d3.select("body")
                .append('svg')
                .attr('height',height)
                .attr('width',width);

            var group = svg.append("g");
            
            var md=group.data([surfacePlot[0].data])
                        .surface3D(width,height)
                        .surfaceHeight(function(d){ 
                            return d;
                        }).surfaceColor(function(d){
                            var c=d3.hsl((d+100), 0.6, 0.5).rgb();
                            return "rgb("+parseInt(c.r)+","+parseInt(c.g)+","+parseInt(c.b)+")";
                        });

            ul.selectAll('li')
                .data(surfacePlot)
                .enter().append('li')
                    .html(function(d){
                    return d.name
                    }).on('mousedown',function(){
                    md.data([d3.select(this).datum().data]).surface3D()
                        .transition().duration(500)
                        .surfaceHeight(function(d){
                        return 10*d;
                        }).surfaceColor(function(d){
                        var c=d3.hsl((d+100), 0.6, 0.5).rgb();
                        return "rgb("+parseInt(c.r)+","+parseInt(c.g)+","+parseInt(c.b)+")";
                        });
                    });

            svg.on("mousedown",function(){
                drag=[d3.mouse(this),yaw,pitch];
            }).on("mouseup",function(){
                drag=false;
            }).on("mousemove",function(){
                if(drag){            
                var mouse=d3.mouse(this);
                yaw=drag[1]-(mouse[0]-drag[0][0])/50;
                pitch=drag[2]+(mouse[1]-drag[0][1])/50;
                pitch=Math.max(-Math.PI/2,Math.min(Math.PI/2,pitch));
                md.turntable(yaw,pitch);
                }
            });
        }
        
                
    },10000)

})