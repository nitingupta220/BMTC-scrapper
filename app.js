var app = angular.module('bmtc', []);
app.controller('bmtcController', function ($scope, $http) {
    'use strict';
    $http.get("scrapper/final.json")
        .then(function (response) {
            console.log(response.data);
            $scope.stops = response.data.stops;
            $scope.fares = response.data.fare;
            $scope.route_timings = response.data.route_timings;
        });
});
