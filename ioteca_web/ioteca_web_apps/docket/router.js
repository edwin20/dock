

app
//==================================
// ui app routers
//==================================
    .config(function($stateProvider) {

    $stateProvider
    //==================================
    // ui layout base
    //==================================
        .state('dock', {
        url: '/dock',
        views: {
            '': {
                templateUrl: 'app/views/layout.html'
            },
            'aside': {
                templateUrl: 'app/views/aside.html'
            },
            'content': {
                templateUrl: 'app/views/content.html'
            }
        }
    })

    //==================================
    // test1
    //==================================
    .state("dock.docente", {
        url: "/docente",
        data: { section: 'DocketPro', page: 'Docentes' },
        templateUrl: "ioteca_web_apps/docket/views/docente/index.html",
    })
    
    .state("dock.experiencia", {
        url: "/experiencia",
        data: { section: 'DocketPro', page: 'Experiencia' },
        templateUrl: "ioteca_web_apps/docket/views/experiencia/index.html"
    })

    .state("dock.investigacion", {
        url: "/investigacion",
        data: { section: 'DocketPro', page: 'investigacion' },
        templateUrl: "ioteca_web_apps/docket/views/investigacion/index.html"
    })

   
    ;
});
