var app = angular.module('myApp', ['ngRoute']);

app.config(function ($routeProvider, $locationProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $routeProvider
        .when('/', {
            templateUrl: 'static/pages/products.html',
            controller: 'MainController'
        })
        .when('/product/:productId', {
            templateUrl: 'static/pages/product.html',
            controller: 'ProductController'
        })
        .when('/product', {
            templateUrl: 'static/pages/product.html',
            controller: 'ProductController'
        });

        // for delete # from the url
        $locationProvider.html5Mode(true);
});






