var http = require('http');

http.createServer(function (req, res) {
    // Corrigir Content-Type e remover dois-pontos extras
    res.writeHead(200, { 'Content-Type': 'text/html' }); 
    res.end('Hello World!');
}).listen(8080);

console.log('Servidor rodando em http://localhost:8080/');
