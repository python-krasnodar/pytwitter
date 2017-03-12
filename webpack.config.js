const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    entry: {
        vendors: './static/src/vendors.js'
    },
    output: {
        filename: '[name].js',
        path: __dirname + '/static/dist'
    },
    module: {
        rules: [
            { test: /\.js$/, use: 'babel-loader', exclude: /(node_modules|bower_components)/ },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: ["css-loader", "sass-loader"]
                })
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin('[name].css')
    ]
};