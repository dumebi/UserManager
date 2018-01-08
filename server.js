require('dotenv').config()

let app = require('./app');
let port = process.env.PORT;

let server = app.listen(port, function() {
  console.log('Express server listening on port ' + port);
});