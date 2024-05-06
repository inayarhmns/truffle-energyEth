const FlexCoin = artifacts.require("FlexCoin")

module.exports = function (deployer) {
  deployer.deploy(FlexCoin, 'FlexCoin');
};