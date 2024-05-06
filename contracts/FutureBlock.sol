pragma solidity ^0.4.11;
import "./FlexCoin.sol";

contract FutureBlock{

    // Description:
    // The product of this trading is a spesific energy amount at a spesified time interval

    // Set up a struct for the offer. The offer is from a node who needs flexibility, which most likely is the grid operator
    struct Offer {
        address owner;   // Who needs the flexibility?
        int offerAmount;   // This amount could be negative and positive. Negative implies that the oferter is using too much, and must remove his consumption
        uint[2] interval;   // Over how long time is the energy needed?
        uint offerNr;

        mapping(uint => Bid) acceptedBids; // This is a vector over the accepted bids
        uint numAcceptedBids;
        uint acceptedPrice; // This is the final market price
        bool fulfilled; // If the offer is fulfilled, it is not possible to deliver more bids to the offer
    }

    // A bid struct is made, which describes all bids
    struct Bid {
        address bidder;
        uint offerNr;  // What offer the struct is pointing at
        uint bidNr;
        int bidAmount;
        uint bidPrice;
    }

    mapping(uint => Offer) public offers;
    mapping(uint => Bid) public bids;
    uint public numOffers;
    uint public numBids;


    // Events are needed to alert the nodes in the system when the things below happen. This is useful when the grid operator needs flexibility automatically and fast.
    event NewOffer();
    event UpdateBid();
    event CorrectionOffer();

    // FUNCTIONS 

    function newOffer(int _amount, uint _startInterval, uint _endInterval) public {
        NewOffer;
        numOffers = numOffers + 1;
        Offer o = offers[numOffers];
        o.offerNr = numOffers;
        o.owner = msg.sender;
        o.offerAmount = _amount;
        o.interval[0] = _startInterval;
        o.interval[1] = _endInterval;
        o.fulfilled = false;
    }

    function getOffer(uint _offerNr) public constant returns(address, int, uint, uint, bool) {
        return(offers[_offerNr].owner, offers[_offerNr].offerAmount, offers[_offerNr].interval[0], offers[_offerNr].acceptedPrice, offers[_offerNr].fulfilled);
    }

    function setBid(uint _offerNr, int _bidAmount, uint _bidPrice) public returns(bool success)  {
        if (offers[_offerNr].fulfilled == true) {  return false;  }
        // Could have a for-loop here to ensure that the msg.sender dont have a bid in the offer. This is however not necessary, and up to market designer.
        numBids = numBids + 1;
        Bid b = bids[numBids];
        b.bidder = msg.sender;
        b.offerNr = _offerNr;
        b.bidNr = numBids;
        b.bidAmount = _bidAmount;
        b.bidPrice = _bidPrice;
        return true;
    }

    function updateBid(uint _offerNr, uint _bidNr, int _bidAmount, uint _bidPrice) public returns(bool success)  {
        // as the realizing time approaches, the batteries can update their price to more expensive prices.
        UpdateBid;
        if (offers[_offerNr].fulfilled == true) {  return false;  }
        if(bids[_bidNr].bidder == msg.sender && bids[_bidNr].offerNr == _offerNr){
            // This applies when the sender already have a bid on the applied offer
            bids[_bidNr].bidAmount = _bidAmount;
            bids[_bidNr].bidPrice = _bidPrice;
            return true;
        }
        else{
            return false;
        }
    }

    function getBid(uint _bidNr) public constant returns(address, int, uint){
        // Here we could choose wether the auction should be blind or open. Now it is open.
        return(bids[_bidNr].bidder, bids[_bidNr].bidAmount, bids[_bidNr].bidPrice);
    }


    // The two functions below is used by the grip operator, when deciding what bids should be accepted, and to what price
    function setAcceptedBids(uint _offerNr, uint _bidNr) public {
        require(offers[_offerNr].owner == msg.sender);
        offers[_offerNr].acceptedBids[offers[_offerNr].numAcceptedBids] = bids[_bidNr];
        offers[_offerNr].numAcceptedBids = offers[_offerNr].numAcceptedBids + 1;
    }

    function setAcceptedPrice(uint _offerNr, uint _acceptedPrice) {
        require(offers[_offerNr].owner == msg.sender);
        offers[_offerNr].acceptedPrice = _acceptedPrice;
    }

    function transferAndClose(uint _offerNr, address contractAddress) public returns (bool success){
        // This can only be called by the owner of the offer.
        require(offers[_offerNr].owner == msg.sender);
        uint i = 0;
        FlexCoin f = FlexCoin(contractAddress);
        // We must set the accepted bids! Everything under a certain price
        if (offers[_offerNr].offerAmount < 0) {
            // This means that the oferter must remove consumption => he buys energy from the bidders
            // Must check that the price is equal or over the bid prices.
            for (i; i < offers[_offerNr].numAcceptedBids; i++) {
                if (offers[_offerNr].acceptedBids[i].bidPrice <= offers[_offerNr].acceptedPrice) {
                    f.transferHouse(offers[_offerNr].owner, offers[_offerNr].acceptedBids[i].bidder, uint(-offers[_offerNr].acceptedBids[i].bidAmount) * offers[_offerNr].acceptedPrice);
                }
            }
        }
        if (offers[_offerNr].offerAmount > 0) {
            for (i; i < offers[_offerNr].numAcceptedBids; i++) {
                if (offers[_offerNr].acceptedBids[i].bidPrice >= offers[_offerNr].acceptedPrice) {
                    f.transferHouse(offers[_offerNr].acceptedBids[i].bidder, offers[_offerNr].owner, uint(offers[_offerNr].acceptedBids[i].bidAmount) * offers[_offerNr].acceptedPrice);
                }
            }
        }
        if (true){
            offers[_offerNr].fulfilled = true;
        }
        return(true);
    }
}
