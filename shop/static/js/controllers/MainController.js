angular.module('myApp').controller('MainController', function ($scope, $http, $location, ProductService) {
    ProductService.getProducts().then(function(result) {
       $scope.products = result.data.results;
   });

   $scope.deleteProduct = function(productId){
        $product_div = $('#' + productId);
        ProductService.deleteProduct(productId).success(function(){
            $product_div.remove();
        })
   }
});