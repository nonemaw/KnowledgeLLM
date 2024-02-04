const path = require("path");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const ReactRefreshPlugin = require("@pmmmwh/react-refresh-webpack-plugin");

const configForWeb = {
  name: "web",
  entry: {
    index: __dirname + "/UI/index.ts",
  },
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
  },
  plugins: [new CopyWebpackPlugin({ patterns: [__dirname + "/UI/static"] }), new ReactRefreshPlugin()],
  devServer: {
    port: 5012,
    devMiddleware: {
      writeToDisk: true,
    },
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: {
          plugins: [require.resolve("react-refresh/babel")],
          configFile: __dirname + "/UI/.babelrc",
        },
      },
      {
        test: /\.tsx?$/,
        exclude: /node_modules/,
        loader: "ts-loader",
      },
      {
        test: /\.(png|jpg|gif|ttf|eot|woff|woff2)$/i,
        use: [
          {
            loader: "url-loader",
            options: { limit: 8192 },
          },
        ],
      },
    ],
  },
  resolve: {
    extensions: [".js", ".jsx", ".ts", ".tsx"],
  },
};

const configForServer = {
  name: "server",
  entry: path.resolve(__dirname, "server", "main"),
  output: {
    filename: "server.js",
    path: path.resolve(__dirname, "dist"),
  },
  node: {
    __dirname: false,
  },
  resolve: {
    extensions: [".ts", ".js"],
  },
  devServer: {
    devMiddleware: {
      writeToDisk: true,
    },
  },
};

module.exports = [configForWeb, configForServer];