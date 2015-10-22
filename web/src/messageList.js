var React = require('react');
var Message = require('./message');

var MessageList = React.createClass({
    getInitialState: function() {
        return {messages: []};
    },
    addMessage: function(message) {
        this.state.messages.unshift(message);
        this.forceUpdate();
    },
    initWebSocket: function() {
        this.addMessage({
            user: {
                id: 'dscdc',
                name: "Privet"
            },
            text: "Test text"
        });
        // var ws = new WebSocket(`ws://${document.location.host}/ws`);
        // ws.onopen = (event) => console.debug('WebSocket: opened');
        // ws.onclose = (event) => console.debug('WebSocket: closed');
        // ws.onerror = (event) => console.debug('WebSocket: error');
        // ws.onmessage = (event) => this.addMessage(JSON.parse(event.data));

    },
    componentDidMount: function() {
        this.initWebSocket();
        this.initWebSocket();
        this.initWebSocket();
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
