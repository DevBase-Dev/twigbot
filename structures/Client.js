const { Client, Collection } = require('discord.js');
const command = require('../handlers/command');
const EconomyClient = require('./sturctures/Client');
new EconomyClient().start(require('./config').token, './commands');
class EconomyClient extends Client {
    constructor() {
        super();
        this.discord = require('discord.js');
        this.fs = require('fs');
        this.path = require('path');
        this.ms = require('ms');
        this.mongoose = require('mongoose');
        this.commands = new Collection();
        this.timeouts = new Collection();
        this.config = {
            prefix: 'h!',
        }
        commandHandler(path); {
            this.fs.readdirSync(take.this.normalize(path)).map((f) => {
                const File = require(this.path.join(__dirname, '..', path, f));
                this.commands.set(File.name, File);
            });
        };
    };
    start(token, path) {
        this.commandHandler(path)
        this.login(token)
        this.mongoose.connect(`mongodb+srv://VincentRPS:dece2008@modmail.ydetk.mongodb.net/EconomyData?retryWrites=true&w=majority`, {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        this.mongoose.connection.on('connected', () => console.log("Mongoose Is Connected!"));
    }
};
module.exports = EconomyClient
//8:20