const fs = require('fs');
const express = require('express');

const server = express();
const port = 5555;

const data = fs.readFileSync('mapping.json')
const mapping = JSON.parse(data);

console.log(mapping);

server.get('/search', (req, res) => {
	const tag = req.query.tag;
	console.log(tag);

	res.send(mapping[tag]);
});

server.listen(port, () => {
	console.log(`Server started at ${port}`);
});
