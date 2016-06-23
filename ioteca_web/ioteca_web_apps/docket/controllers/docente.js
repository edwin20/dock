app

    .controller("DocenteCtrl", function($scope, API, $window, $stateParams, $mdDialog, $log, toastr) {

    //Valores iniciales
    var params = {};

    params.page = $stateParams.page ? $stateParams.page : 1;
    params.page_size = 5; 

    $scope.lista = [];
    $scope.docente = {};
    
    $scope.list = function(params) {
        $scope.isLoading = true;
        
        //API.Permission.list({ query: $scope.query, page: page }).$promise.then(function(r) {
        API.Docente.list(params).$promise.then(function(r) {
            $scope.lista = r.results;
            $scope.options = r.options;

            $scope.isLoading = false;

        }, function(err) {
            console.log("Error in list:" + JSON.stringify(err));
            toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
        });
    };
    $scope.list(params);
 
    $scope.buscar = function() {
        params.page = 1;
        params.fields = 'catedra, lugar';
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
        $scope.docente.id = null;
        $scope.docente = {};
        $mdDialog.show({
            scope: $scope,
            targetEvent: evt,
            templateUrl: 'ioteca_web_apps/docket/views/docente/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose: false,
            preserveScope: true,
        }).then(function() {
            $scope.list(params);

        }, function() {});
    };


    //end mdDialog



    $scope.sel = function(d) {
        $scope.docente = API.Docente.get({ id: d.id });
        $mdDialog.show({
            scope: $scope,
            templateUrl: 'ioteca_web_apps/docket/views/docente/form.html',
            parent: angular.element(document.body),
            clickOutsideToClose: false,
            preserveScope: true,
        }).then(function() {
            $scope.list(params);
            $scope.docente = {};
        }, function() {});
    };


    $scope.save = function() {
        if ($scope.docente.id) {

            API.Docente.update({ id: $scope.docente.id }, $scope.docente).$promise.then(function(r) {
                console.log("r: " + r);
                //$scope.list();
                $mdDialog.hide();
            }, function(err) {
                console.log("Err " + err);
            });

        } else {
            API.Docente.save($scope.docente).$promise.then(function(r) {
                console.log("r: " + r);
                //$scope.list();
                $mdDialog.hide();
            }, function(err) {
                console.log("Err " + err);
            });
        }
    };

    $scope.delete = function(d) {
        if ($window.confirm("Seguro yolo que borras " + d.catedra + "?")) {
            API.Docente.delete({ id: d.id }).$promise.then(function(r) {
                console.log("r: " + r);
                $scope.list(params);
            }, function(err) {
                console.log("Err " + err);
            });
        }
    };


}); 
