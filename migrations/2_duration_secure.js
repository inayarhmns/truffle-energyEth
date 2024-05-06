const DurationSecure = artifacts.require("DurationSecure")

module.exports = function (deployer) {
  deployer.deploy(DurationSecure, 'DurationSecure');
};