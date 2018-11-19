const fs = require('fs');
const express = require('express');

const server = express();
const port = 5555;

const data = fs.readFileSync('mapping.json')
const mapping = JSON.parse(data);

console.log(mapping);

server.get('/search', (req, res) => {
	const tag = req.query.tag;
	candidate = []

	for (let i = 0 ; i < tag.length; i ++){
		candidate = candidate.concat(mapping[tag[i]]);
	}

	// Word Count
	tmp = {}
	for (let i = 0 ; i < candidate.length; i ++) {
		if (candidate[i] in tmp) {
			tmp[candidate[i]] += 1;
		} else {
			tmp[candidate[i]] = 1;
		}
	} 
	
	// Counting Sort
	buffer = [];
	const max_len = 50;
	for (let i = 0 ; i < max_len ; i ++ ) {
		buffer[i] = [];	
	}
	for (let key in tmp){
		buffer[tmp[key]].push(key);
	}
	
	// Make sorted result
	ret = []
	for (let i = max_len - 1; i > 0 ; i --) {
		ret = ret.concat(buffer[i]);
	}

	res.send(ret);
});

server.listen(port, () => {
	console.log(`Server started at ${port}`);
});
