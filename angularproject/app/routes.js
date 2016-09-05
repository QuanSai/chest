function routesConfig($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/home/home.html",
      label: "Home",
      reloadOnSearch: false
    })
    .otherwise({
      templateUrl: "static/app/404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig;
