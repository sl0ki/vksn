var config = {
    entry: {
        javascript: "./src/app.js",
        html: "./index.html",
    },
    resolve: { alias: {} },
    output: {
        path: './dist',
        filename: 'app.js'
    },
    module: {
        noParse: [],
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel'
            },
            {
                test: /\.html$/,
                loader: "file?name=[name].[ext]",
            }
        ]
    }
}
module.exports = config
