const express = require('express')
const app = express()
const dirpages = __dirname + '/public/'

app.get('/',function(req, res){
  res.sendFile( dirpages + 'index.html')
})

app.use(express.static(dirpages))


app.listen(3000, function(){
  
})