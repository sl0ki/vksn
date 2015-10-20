var React = require('react');
var Message = require('./message');

var MessageList = React.createClass({
    getInitialState: function() {
        return {messages: []};
    },
    addMessage: function() {
        var i = 0;
        setInterval(() => {
            var message = {
                user: {
                    name: 'Username'
                },
                text: 'Some text here i = ' + i
            };
            i++;
            this.state.messages.unshift(message);
            this.forceUpdate();
        }, 1000);
    },
    componentDidMount: function() {
        this.addMessage();
    },
    render: function() {
        var messageNodes = this.state.messages.map((message) => {
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
