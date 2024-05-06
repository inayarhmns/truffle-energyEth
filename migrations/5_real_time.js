const RealTime = artifacts.require("RealTime")

module.exports = function (deployer) {
  deployer.deploy(RealTime, 'RealTime');
};