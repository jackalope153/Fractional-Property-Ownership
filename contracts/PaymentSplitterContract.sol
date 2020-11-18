pragma solidity 0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/math/SafeMath.sol";


contract PaymentSplitter {
    using SafeMath for uint256;

    event PayeeAdded(address account, uint256 shares);
    event PaymentReleased(address to, uint256 amount);
    event PaymentReceived(address from, uint256 amount);

    uint256 private _totalTokens;
    uint256 private _totalReleased;

    mapping(address => uint256) private TokensMapped;
    mapping(address => uint256) private paidAmount;
    address[] private _payees;

    constructor (address[] memory payees, uint256[] memory ownedTokens) public payable {
        require(payees.length == ownedTokens.length, "PaymentSplitter: payees and shares length mismatch");
        require(payees.length > 0, "PaymentSplitter: no payees");

        for (uint256 i = 0; i < payees.length; i++) {
            _addPayee(payees[i], ownedTokens[i]);
        }
    }

    function totalTokens() public view returns (uint256) {
        return _totalTokens;
    }


    function totalReleased() public view returns (uint256) {
        return _totalReleased;
    }


    function tokens(address account) public view returns (uint256) {
        return TokensMapped[account];
    }


    function released(address account) public view returns (uint256) {
        return paidAmount[account];
    }

    function payee(uint256 index) public view returns (address) {
        return _payees[index];
    }


    function release(address payable account) public {
        require(TokensMapped [account] > 0, "PaymentSplitter: account has no shares");
        uint256 totalReceived = address(this).balance.add(_totalReleased);
        uint256 payment = totalReceived.mul(TokensMapped [account]).div(_totalTokens).sub(paidAmount[account]);
        require(payment != 0, "PaymentSplitter: account is not due payment");
        paidAmount[account] = paidAmount[account].add(payment);
        _totalReleased = _totalReleased.add(payment);
        account.transfer(payment);
        emit PaymentReleased(account, payment);
    }


    function _addPayee(address account, uint256 ownedTokens) private {
        require(account != address(0), "PaymentSplitter: account is the zero address");
        require(ownedTokens > 0, "PaymentSplitter: Tokens are 0");
        require(TokensMapped[account] == 0, "PaymentSplitter: account already has Tokens");

        _payees.push(account);
        TokensMapped[account] = ownedTokens;
        _totalTokens = _totalTokens.add(ownedTokens);
        emit PayeeAdded(account, ownedTokens);
    }
}
