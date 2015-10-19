var React = require('react');
var Message = require('./message');

var MessageList = React.createClass({
    render: function() {
        var messageNodes = this.props.messages.map(function (message) {
            return (
                <Message user={message.user} text={message.text}/>
            );
        });
        return(
            <div className="messageList">
                {messageNodes}
            </div>
        );
    }
});

module.exports = MessageList
