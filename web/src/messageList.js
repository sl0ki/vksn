var React = require('react');
var Message = require('./message');

var MessageList = React.createClass({
    getInitialState: function() {
        return { messages: [] };
    },
    addMessage: function(message) {
        this.state.messages.unshift(message);
        this.forceUpdate();
    },
    initWebSocket: function() {
        var ws = new WebSocket(`ws://${document.location.host}/ws`);
        ws.onmessage = (event) => this.addMessage(JSON.parse(event.data));

    },
    componentDidMount: function() {
        this.initWebSocket();
    },
    render: function() {
        var messageNodes = this.state.messages.map((message) => {
            return ( <Message key={message.id} message={message} /> );
        });
        return(
            <div className="messageList">
                {messageNodes}
            </div>
        );
    }
});

module.exports = MessageList
