require('dotenv').config();
const axios = require('axios');

const client_id = process.env.CLIENT_ID;
const client_secret = process.env.CLIENT_SECRET;

const getToken = async () => {
    try {
        const authHeader = Buffer.from(client_id + ':' + client_secret).toString('base64');
        console.log('Base64 Auth:', authHeader); // Debugging step

        const response = await axios.post('https://accounts.spotify.com/api/token',
            new URLSearchParams({ grant_type: 'client_credentials' }),
            {
                headers: {
                    'Authorization': `Basic ${authHeader}`,
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }
        );

        console.log('Access Token:', response.data.access_token);
    } catch (error) {
        console.error('Error:', error.response ? error.response.data : error.message);
    }
};

getToken();
