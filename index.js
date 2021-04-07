const http = require("http");
const fs = require('fs');

const port = process.env.PORT || 3000;

fs.readFile('./index.html', 'utf8', (err,data) => {

    const server = http.createServer((req,res) => {
        res.writeHead(200, {
            'Content-Type':'text/html',
        });
        
        res.write(data);
        res.end();
    });
    server.listen(port, (arg) => {
        console.log(`server started on http://localhost:${port}`);
    });
    
});

