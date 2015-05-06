angular.module('myApp').controller('ProductController', function ($http, $scope, $location, $routeParams, ProductService) {
    var productId = $routeParams['productId'];
    if (productId){
        ProductService.getProduct(productId).then(function(result){
            var product = result.data;
            $scope.product = product;
            $scope.category = product.category;
        });
    }

    ProductService.getCategories().then(function(result){
        $scope.categories = result.data.results;
    });

    $scope.createupdateProduct = function () {
        var product = $scope.product;
        ProductService.createOrUpdateProduct(product).then(function(){
            $location.path('/');
        });
    }

});