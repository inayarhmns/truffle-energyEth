const FutureBlock = artifacts.require("FutureBlock")

module.exports = function (deployer) {
  deployer.deploy(FutureBlock, 'FutureBlock');
};