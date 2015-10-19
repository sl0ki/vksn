var React = require('react');

var Message = React.createClass({
    render: function() {
        return(
            <div className="message">
                <div className="author">
                    {this.props.user.name}
                </div>
                <div className="text">
                    {this.props.text}
                </div>
            </div>
        );
    }
});
module.exports = Message
