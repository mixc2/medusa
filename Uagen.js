const fs = require('fs');

function generatePremiumUserAgent() {
    const platforms = [
        'Windows NT 10.0; Win64; x64',
        'Macintosh; Intel Mac OS X 10_15_7',
        'X11; Linux x86_64',
        'iPhone; CPU iPhone OS 14_5 like Mac OS X',
        'iPad; CPU OS 14_5 like Mac OS X',
        'Linux armv8l'
    ];

    const browsers = [
        'Chrome/90.0.4430.212',
        'Safari/537.36',
        'Firefox/88.0',
        'Edge/91.0.864.41',
        'Opera/76.0.4017.123'
    ];

    const randomPlatform = platforms[Math.floor(Math.random() * platforms.length)];
    const randomBrowser = browsers[Math.floor(Math.random() * browsers.length)];

    return `"Mozilla/5.0 (${randomPlatform}) AppleWebKit/537.36 (KHTML, like Gecko) ${randomBrowser} Safari/537.36",`;
}

function generateAndSaveUserAgents(numUserAgents, fileName) {
    let userAgents = [];
    for (let i = 0; i < numUserAgents; i++) {
        userAgents.push(generatePremiumUserAgent());
    }
    fs.writeFile(fileName, userAgents.join('\n'), (err) => {
        if (err) {
            console.error('Error writing file:', err);
        } else {
            console.log(`Successfully generated ${numUserAgents} user agents and saved to ${fileName}`);
        }
    });
}

const numUserAgents = parseInt(process.argv[2]);
const fileName = process.argv[3];

if (isNaN(numUserAgents) || numUserAgents <= 0 || !fileName) {
    console.log(' Usage: node UAgen.js <number_of_user_agents> <output_file_name>');
} else {
    generateAndSaveUserAgents(numUserAgents, fileName);
}
