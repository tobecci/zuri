const http = require("http");
const fs = require('fs')
const apiUrl = "http://jsonplaceholder.typicode.com/posts";
const fileUrl = `result/posts.json`;

const storePosts = (data) => {
    console.log("storing posts");

    fs.appendFile(fileUrl, data, { encoding: 'utf8' },
        (err) => {
            if (err) {
                console.log(err);
                return;
            }
            console.log("wrote successfully");
        })
}

http.get(apiUrl, function (res) {
    res.on("data", (chunk) => {
        let data = chunk.toString('utf8')
        storePosts(data);
    })
})