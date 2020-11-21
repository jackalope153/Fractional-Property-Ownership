pragma solidity ^0.5.5;
import "./PropertyCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";


contract PropertyCrowdsale is Crowdsale, MintedCrowdsale, CappedCrowdsale, TimedCrowdsale, RefundablePostDeliveryCrowdsale {
    constructor(
        uint rate,
        address payable wallet,
        PropertyCoin token,
        uint goal,
        uint open,
        uint close
    )
        Crowdsale(rate, wallet, token)
        CappedCrowdsale(goal)
        RefundableCrowdsale(goal)
        TimedCrowdsale(open, close)
        public
    {
    }
    
    
}


contract PropertySaleDeployer {
    address public token_sale_address;
    address public token_address;
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet,
        uint goal
    )
        public
    {
        PropertyCoin token = new PropertyCoin(name, symbol, 0);
        token_address = address(token);
        PropertyCrowdsale property_sale = new PropertyCrowdsale(1, wallet, token, goal, now, now + 1 weeks);
        token_sale_address = address(property_sale);
        token.addMinter(token_sale_address);
        token.renounceMinter();
    }
    
}