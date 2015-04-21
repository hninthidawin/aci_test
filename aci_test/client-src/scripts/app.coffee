'use strict'

angular.module('app', ['ui.router', 'app.views'])
.config(['$stateProvider', '$urlRouterProvider',
  ($stateProvider, $urlRouterProvider) ->
    $stateProvider
    .state('app',
      url: '/'
      # template: 'Hi'
      templateUrl: 'app.html'
      controller: ['$scope', ($scope) ->
        $scope.APP_NAME = 'aci_test'
      ]
    )
  ])
