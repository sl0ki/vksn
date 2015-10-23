var React = require('react');

var Message = React.createClass({

    render: function() {
        return(
            <div className="message show">
                <img className="photo" src={this.props.message.user.photo} />
                <span className="type">
                    { this.props.message.type == 'INBOX' ? "↑" : "↓"}
                </span>
                <div className="content">
                    <a className="author" target="_blank" href={"http://vk.com/id" + this.props.message.user.id} >
                        {this.props.message.user.name}
                    </a>
                    <div className="text">
                        {this.props.message.text}
                    </div>
                </div>
            </div>
        );
    }
});
module.exports = Message
