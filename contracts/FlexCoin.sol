
pragma solidity ^0.4.11;

// This contract must build the coin that should be used in the different trading mechanisms.
// If other things are common for the mechanisms, this is the place to include the things

contract FlexCoin {

    struct House {
        address owner;
        address smartMeter;
        uint flexCoinBalance;
    }

    mapping(address => House) houses;
    uint public numHouses;

    event Transfer(address from, address to, uint flexCoinAmount);
    event smartMeterPlan(address buyerFlex, address smartMeter, int flexAmount, uint[] interval);
    // This event is sent to the smart meters, telling them what to do, and when to do it.

    function newHouse() payable public {
        numHouses = numHouses + 1;
        House h = houses[msg.sender];
        h.smartMeter = msg.sender;
        h.flexCoinBalance = 200000000000;
    }
    // gas cost: 37 041

    function getHouse(address _address) public constant returns (address, uint) {
        return (houses[_address].smartMeter, houses[_address].flexCoinBalance);
    }

    function transferHouse(address _from, address _to, uint _amount){
        require(houses[_from].flexCoinBalance >= _amount);           // Check if the sender has enough
        require(houses[_to].flexCoinBalance + _amount >= houses[_to].flexCoinBalance); // Check for overflows
        houses[_from].flexCoinBalance -= _amount;                    // Subtract from the sender
        houses[_to].flexCoinBalance += _amount;                           // Add the same to the recipient
        Transfer(_from, _to, _amount);
    }
    // gas cost: 37 878

}
