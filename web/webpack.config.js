var webpack = require('webpack');

var config = {
    entry: {
        javascript: "./src/app.js",
        html: "./index.html",
    },
    resolve: { alias: {} },
    output: {
        path: './dist',
        filename: 'app.js',
    },
    module: {
        noParse: [],
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'react-hot!babel',
            },
            {
                test: /\.html$/,
                loader: 'file?name=[name].[ext]',
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            }
        ],
        plugins: [
          new webpack.HotModuleReplacementPlugin()
        ]
    }
}
module.exports = config
