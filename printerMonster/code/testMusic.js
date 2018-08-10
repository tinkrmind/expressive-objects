const { createAudio } = require('node-mp3-player')
const Audio = createAudio();

(async () => {
  const myFile = await Audio(`${__dirname}/musicMaster.mp3`)
  await myFile.volume(0.5)
  const currentVolume = await myFile.volume() // 0.5
  await myFile.loop()
  await myFile.stop()
})()

async function play(){
  const myFile = await Audio('./musciMaster.mp3')
  await myFile.play() // plays the file
}

play();
//await myFile.stop() // stops the file
