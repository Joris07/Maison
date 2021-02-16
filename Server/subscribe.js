var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://172.20.78.137')
 
client.on('connect', function () {
  client.subscribe('sensor/temperature', function (err) {
    if (!err) {
      console.log("Pas d'erreur")
    }
  })
})
 
client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  client.end()
})
