angular.module('myApp').service('ProductService', function($http) {
    this.getProducts = function() {
       return $http.get('api/product/');
    };

    this.getProduct = function(productId){
        return $http.get('api/product/' + productId);
    };

    this.getCategories = function(){
        return $http.get('api/category/');
    };

//    this.createProduct = function(product){
//        return $http.post('api/product/', product);
//    };
//
//    this.updateProduct = function(product){
//        return $http.put('api/product/' + product.id, product);
//    };

    this.deleteProduct = function(productId){
        return $http.delete('api/product/' + productId);
    };

    this.createOrUpdateProduct = function(product) {
        if (product.id) {
            return $http.put('api/product/' + product.id, product);
        } else {
            return $http.post('api/product/', product);
        }
    }

});