/* Libs */
require("angular/angular");
require("angular-route/angular-route");
require("angular-resource/angular-resource");

/* Globals */
_ = require("lodash");
_urlPrefixes = {
  API: "api/v1/",
  TEMPLATES: "static/app/"
};

/* Components */
require("./components/home/home");

/* Loaded Configs */
var routesConfig = require("./routes");

/* App Dependencies */
angular.module("PROJECT_NAMEApp", [
  "Home",
  "ngResource",
  "ngRoute"
]);

/* App Config */
angular.module("PROJECT_NAMEApp").config(routesConfig);
