// index.js
exports.hello = function hello(req, res) {
    res.status(200)
       .send('Hello, Functions\n');
};