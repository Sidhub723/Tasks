const mongoose = require('mongoose')

mongoose
    .connect('mongodb://mongodb:27017/cinema', { useNewUrlParser: true })       // changed the name of the service to which mongoose is
    .catch(e => {                                                               // connecting from localhost to mongodb(docker container)
        console.error('Connection error', e.message)
    })

const db = mongoose.connection

module.exports = db
