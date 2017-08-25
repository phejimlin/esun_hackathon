pragma solidity ^0.4.11;
contract Feedback {
    
    struct User {
        int score;
    }
    
    struct Deal {
        //uint dealtime;
        //uint itemID;
        address buyer;
        address seller;
        bool buyer_sent;
        bool seller_sent;
        //uint buyer_sent_time;
        //uint seller_sent_time;
        //int8 buyer_score;
        //int8 sender_score;
        //string buyer_message;
        //string seller_message;
    }
    
    mapping(address=>User) users;
    Deal[] public deals;
    uint numDeals;
    
    address public master;
    
    function Feedback() {
        master = msg.sender;
        numDeals = 0;
    }
    
    event deal_created(uint _dealID, string _timestamp, string _itemName, address indexed _buyer, address indexed _seller);
    event feedback_sent(uint indexed _dealID, string _timestamp, address indexed sender, address indexed receiver,
            bool _sender_is_seller, int _score, string _message);
    event user_score_changed(address indexed addr, uint indexed timestamp, int old_score, int new_score);
    
    function create_deal(string timestamp, string itemName, address buyer, address seller) {
        require(msg.sender == master);
        deals.push(Deal(buyer, seller, false, false));
        deal_created(numDeals, timestamp, itemName, buyer, seller);
        numDeals++;
    }
    
    function send_feedback(uint dealID, string timestamp, int score, string message) {
        require(dealID <= numDeals);
        require((msg.sender == deals[dealID].buyer && !deals[dealID].buyer_sent)||
                (msg.sender == deals[dealID].seller && !deals[dealID].seller_sent));
        if(msg.sender == deals[dealID].buyer) {
            deals[dealID].buyer_sent = true;
            feedback_sent(dealID, timestamp, deals[dealID].buyer, deals[dealID].seller, false, score, message);
        }
        else {
            deals[dealID].seller_sent = true;
            feedback_sent(dealID, timestamp, deals[dealID].seller, deals[dealID].buyer, true, score, message);
        }
    }
    
    function set_user_score(uint timestamp, address addr, int score) {
        require(msg.sender == master);
        int old_score = users[addr].score;
        users[addr].score = score;
        user_score_changed(addr, timestamp, old_score, score);
    }
}