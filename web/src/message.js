var React = require('react');

var Message = React.createClass({
    render: function() {
        return(
            <div className="message">
                <img className="photo" src={this.props.message.user.photo} />
                <a className="author" target="_blank" href={"http://vk.com/id" + this.props.message.user.id} >
                    {this.props.message.user.name}
                </a>
                <div className="text">
                    {this.props.message.text}
                </div>
            </div>
        );
    }
});
module.exports = Message
