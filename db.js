let mongoose = require('mongoose');
let options = { promiseLibrary: require('bluebird'), useMongoClient: true, keepAlive: true };
mongoose.Promise = require('bluebird');
mongoose.connect(process.env.DB_URL, options);