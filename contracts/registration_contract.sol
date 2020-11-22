pragma solidity ^0.5.0;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
//contract PropertyCrowdSale is ERC721Full, Crowdsale, MintedCrowdsale, CappedCrowdsale, TimedCrowdsale, RefundablePostDeliveryCrowdsale { }
contract Registration {
    
    struct Property {
        uint UserID;
        string URI;
    }
    
    struct User {
        address Address;
        string URI;
    }
    
    struct PropertyManagement {
        address Address;
        string URI;
    }
    
    using Counters for Counters.Counter;
    
    Counters.Counter private PropertyIDS;
    Counters.Counter private UserIDS;
    Counters.Counter private PropertyManagementIDS;
    
    //Tokens (propertyID => current token balance)
    mapping(uint => uint[]) tokens;
    mapping(uint => Property) Properties;
    mapping(uint => User) Users;
    mapping(uint => PropertyManagement) PropertyManagers;
    //mapping(uint => mapping(uint => tokenID)) public Properties;
    
    // Transfer of Property Ownership (amount of tokens, userID, propertyID)
    event TransferTokens(uint tokens, uint userID, uint propertyID);
    
    // Token Balance available to purchase (propertyID)
    event TokenBalance(uint propertyID);
    
    event RegisterProperty(uint propertyID, uint userID);
    
    event RegisterUser(uint userID);
    
    constructor() public { }
    
    function registerProperty(address user_address, string memory propertyURI) public returns(uint) {
        PropertyIDS.increment();
        uint propertyID = PropertyIDS.current();
        Properties[propertyID] = Property(userID, propertyURI);
        
        //
        
        emit RegisterProperty(propertyID, userID);
        
        return propertyID;
    }
    
    function registerUser(address userAddress, string memory userURI) public returns(uint) {
        UserIDS.increment();
        uint userID = UserIDS.current();
        Users[userID] = User(userAddress, userURI);
        
        emit RegisterUser(userID);
        
        return userID;
    }
    
    function registerPropertyManagement(address propertyManagementAddress, string memory propertyManagemenURI) public returns(uint) {
        PropertyManagementIDS.increment();
        uint propertymanagementID = PropertyManagementIDS.current();
        PropertyManagers[propertymanagementID] = PropertyManagement(propertyManagementAddress, propertyManagemenURI);
        return propertymanagementID;
    }
}
