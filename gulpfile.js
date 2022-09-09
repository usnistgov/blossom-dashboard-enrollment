const uswds = require("@uswds/compile");

uswds.settings.version = 3;

uswds.paths.dist.css = './assets';
uswds.paths.dist.sass = './node_modules/@uswds/uswds/packages';

exports.init = uswds.init;
exports.compile = uswds.compile;