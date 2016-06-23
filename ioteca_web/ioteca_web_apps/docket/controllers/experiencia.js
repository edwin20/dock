app

    .controller("ExperienciaCtrl", function($scope, API, $window, $stateParams, $mdDialog, $log, toastr) {

    //Valores iniciales
    var params = {};
    params.page = $stateParams.page ? $stateParams.page : 1;
    params.page_size = 5;
    $scope.lista = [];
    $scope.menu = {};
    $scope.myDate = new Date();


    var date = new Date();
    var day = date.getDate();
    var monthIndex = date.getMonth();
    var year = date.getFullYear();
    console.log(day +"  "+ monthIndex +"  "+ year)

    $scope.list = function(params) {
        //logService.error('yeeeeeeeee');

        $log.log('log message');
        $log.debug('debug message');
        $log.info('info message');
        $log.warn('warn message');
        //$log.error('error message');
        //throw Error('gone wrong in greet');

        console.log("page_size: " + params.page_size);
        //API.Menu.list({ query: $scope.query, page: page }).$promise.then(function(r) {
        API.Experiencia.list(params).$promise.then(function(r) {

            $scope.lista = r.results;
            $scope.options = r.options;
        }, function(err) {
            console.log("Error in list:" +  JSON.stringify(err));
            toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
        });
    };

    $scope.list(params);

    $scope.buscar = function() {
        params.page = 1;
        params.fields = 'module,title,state';
        params.query = $scope.query;
        params.page_size = $scope.per;
        $scope.list(params);

    };


    $scope.listAll = function() {
        //params.page = 1;
        //params.fields = 'nombre,direccion';
        //params.query = $scope.query;
        //params.page_size= $scope.per;
        params.all = true; //así debe quedar
        $scope.list(params);

    };

    //mdDialog
    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.new = function(evt) {
        $scope.menu.id = null;
        $scope.menu = {};
        $mdDialog.show({
            scope: $scope,
            targetEvent: evt,
            templateUrl: 'ioteca_web_apps/docket/views/experiencia/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose: false,
            preserveScope: true,
        }).then(function() {
            $scope.list(params);

        }, function() {});
    };


    //end mdDialog



    $scope.sel = function(d) {
        $scope.menu = API.Experiencia.get({ id: d.id });
        $mdDialog.show({
            scope: $scope,
            templateUrl: 'ioteca_web_apps/docket/views/experiencia/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose: false,
            preserveScope: true,
        }).then(function() {
            $scope.list(params);
            $scope.menu = {};
        }, function() {});
    };


    $scope.save = function() {
        if ($scope.menu.id) {

            API.Experiencia.update({ id: $scope.menu.id }, $scope.menu).$promise.then(function(r) {
                console.log("r: " + r);
                //$scope.list();
                $mdDialog.hide();
            }, function(err) {
                console.log("Err " + err);
            });

        } else {
            API.Experiencia.save($scope.menu).$promise.then(function(r) {
                console.log("r: " + r);
                //$scope.list();
                $mdDialog.hide();
            }, function(err) {
                console.log("Err " + err);
            });
        }
    };

    $scope.delete = function(d) {
        if ($window.confirm("Seguro yolo que borras " + d.id + "?")) {
            API.Experiencia.delete({ id: d.id }).$promise.then(function(r) {
                console.log("r: " + r);
                $scope.list(params);
            }, function(err) {
                console.log("Err " + err);
            });
        }
    };


}); 
