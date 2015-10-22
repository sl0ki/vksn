var React = require('react');
var ReactDOM = require('react-dom');

var Message = require('./message');
var MessageList = require('./messageList');

require('./css/app.css');

if (module.hot) module.hot.accept()

var data = {
    user: {
        name: 'Username'
    },
    text: 'Some text here'
};
data = [data, data];

ReactDOM.render(
    <MessageList messages={data} />,
    document.getElementById('app')
);

// console.log(Message);
// React.renderComponent(<Message />, document.getElementById('app'));
