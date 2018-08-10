// const express = require('express')
// const app = express()
//
// app.get('/lamp_ideo', function(req, res){
//         console.log('Turn lamp to red')
//         res.send('ack')
// })
//
// app.listen(1337, () => console.log('Port: 1337'))

var Hue = require('philips-hue');
var hue = new Hue();

var AsyncPolling = require('async-polling');


var state = cyan

const request = require('request');

var hue = new Hue;
hue.bridge = "10.5.250.16";  // from hue.getBridges
hue.username = "x0a1PUzVkjJpzUqGecgN2XW8niRa3ibKKbO3DbOl"; // from hue.auth

var red = {hue: 0, sat: 0, bri: 0};
var cyan = {hue: 8000, sat: 200, bri: 90};
var purple = {hue: 50000, sat: 200, bri:90};

  AsyncPolling(function (end) {
    request('http://as11613.itp.io:1337/return_color', { json: true }, (err, res, body) => {
      if (err) { return console.log(err); }
      console.log(body);
      if(body == 'red'){
        console.log('Turn hue red')
        // hue.light(5).on();
        hue.light(5).setState(red).then(console.log).catch(console.error);
      }
      if(body == 'purple'){
        console.log('Turn hue purple')
        // hue.light(5).on();
        hue.light(5).setState(purple).then(console.log).catch(console.error);
      }
      if(body == 'cyan'){
        console.log('Turn hue cyan')
        // hue.light(5).on();
        hue.light(5).setState(cyan).then(console.log).catch(console.error);
      }
      // Then notify the polling when your job is done:
      end();
    });
      // This will schedule the next call.
  }, 1000).run();
