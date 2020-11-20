// contracts/GameItem.sol
//SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;


import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";




      
contract Registration is ERC721Full{
    using Counters for Counters.Counter;
    
    struct Property {
        uint propertyID;
        uint userID;
        string URI;
        
    }
    
    struct User {
        uint userID;
        address Address;
        
    }
    struct PropertyManagement {
        uint PropertyManagementID;
        address _address;
        
    }
    
    Counters.Counter private propertyIDS;
    Counters.Counter private UserIDS;
    Counters.Counter private PropertyManagementIDS;
    
    
    //mapping token id to the property
    //Users (userID => userinfo)
    //Property (propertyID => propertyinfo)
    //PropertyManagement (pmuserID => pmuserinfo)
    //Tokens (propertyID => current token balance)
        
    mapping(uint => Property) Properties;
    mapping(uint => User) Users;
    mapping(uint => PropertyManagement) PropertyManagers;
    //mapping(uint => mapping(uint => tokenID)) public Properties;
    
    // Transfer of Property Ownership (amount of tokens, userID, propertyID) 
   event TransferTokens (uint tokens , uint userID, uint propertyID);
   
    // TOken Balance available to purchase (propertyID) 
    event TokenBalance (uint);
    
    
    constructor() public {   }
    
    
    //taking in a userID of owner, property uri, market value of property and total supply of tokens (100) (ether conversion in python), validation id
    //return propertyID
    //mint tokens
    // error message for validation id not beinf correct, or 
   function registerProperty(address propertyAddress, string memory propertyURI) public returns(uint) {
        propertyIDS.increment();
        uint propertyID = propertyIDS.current();
        // fix this part
        Properties[propertyID] = Property(1, 2, "");
        
        return propertyID;
   }
   
   
    //input wallet address, IPFS to personal info
    //return userid
    function registerUser(address userAddress, string memory userURI) public returns(uint) {
        //userIDS.increment();
        //uint userID = userIDS.current();
        //users[userID] = User(userURI, userAddress);
        
        //return userID;
        return 0;
    }  
    
    //input wallet address, IPFS to personal info
    //output propertymanagementID
    function registerPropertyManagement(address PropertyManagementAddress) public returns(uint) {
        //propertymanagementIDS.increment();
        //uint propertymanagementID = propertymanagementIDS.current();
        //propertymanagement[propertymanagementID] = PropertyManagement(PropertyManagementAddress);
        
        //return propertymanagementID;   
        return 0;
        
    //only for property management, pull token per user token amount/100 * revenue transfer ether to user minus admin fee and maintenance
    function profit splitter
    
    ///validation id check done in python
    
    
    ///new contract with crowdasle function
         //create token, give owner address, 
        ///available tokens
        
        
    //propety investment report 
        //how many properties does user own, what revenue generated?
        
    // add minting to registeryproperty function
    
    
    
    }*/
    
    
}