const Duration = artifacts.require("Duration")

module.exports = function (deployer) {
  deployer.deploy(Duration, 'Duration');
};