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
        //var ws = new WebSocket(`ws://${document.location.host}/ws`);
        var ws = new WebSocket('ws://127.0.0.1:3001/ws');
        ws.onopen = (event) => console.debug('WebSocket: opened');
        //ws.onclose = (event) => setTimeout(() => this.connect()}, 1000);
        ws.onerror = (event) => console.debug('WebSocket: error');
        ws.onmessage = (event) => this.addMessage(JSON.parse(event.data));

    },
    componentDidMount: function() {
        this.initWebSocket();
    },
    render: function() {
        var messageNodes = this.state.messages.map((message) => {
            return (
                <Message message={message} />
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
