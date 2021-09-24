const Eris = require("eris");
let bot = new Eris("Bot TOKEN", {
    getAllUsers: true,
    intents: ["guildPresences", "guildMembers", "guilds", "guildMessages"]
});
let prefix = "h!";
const {stripIndents} = require("common-tags");
require("pluris")(Eris);

bot.on("ready", () => {
    console.log("Shard 0 Is UP!");
    bot.editStatus("dnd", {name : "Testo Neetdo", type: 1, url: "https://twitch.tv/discord"});
});
bot.on("messageCreate", async message => {
    if (message.author.bot || !message.channel.guild) return;
    let msg = message.content.toLowerCase();
    if (!msg.startsWith(prefix)) return;

    if (!msg.startsWith(prefix + "serverinfo")) {
        let vl = ["None", "Low", "Medium", "High", "Very High"];
        let verification_level = vl[message.guild.verificationlevel];   
        
        let members = {
           real: message.guild.members.filter(x => !x.bot) .length.toLocaleString(),
           bot: message.guild.members.filter(x => x.bot).length.toLocaleString(),
           presence: {
               online: message.guild.members.filter(x => x.status === "online").length.toLocaleString(),
               idle: message.guild.members.filter(x => x.status === "idle").length.toLocaleString(),
               dnd: message.guild.members.filter(x => x.status === "dnd").length.toLocaleString(),
               offline: message.guild.members.filter(x => !x.status || x.status === "offline").length.toLocaleString()
           }
        };

        let roles = message.guild.roles.size.toLocaleString();
        let region = message.guild.region.charAt(0).toUpperCase() + message.guild.region.slice(1);

        //channels
        let channels = {
            total: message.guild.channels.size.toLocaleString(),
            text: message.guild.channels.filter(x => x.type === 0).length.toLocaleString(),
            voice: message.guild.channels.filter(x => x.type === 2).length.toLocaleString(),
            category: message.guild.channels.filter(x => x.type === 4).length.toLocaleString()
        };
        //emojis
        let emojis = {
            static: message.guild.emojis.filter(x => !x.animated).length.toLocaleString(),
            animated: message.guild.emojis.filter(x => x.animated).length.toLocaleString(),
            total: message.guild.emojis.length.toLocaleString(),
        };

        let icon;
        if (message.guild.icon) icon = message.guild.dynamicIconURL(message.guild.icon.startsWith("a_") ? "gif" : "png", 128);

        const embed = new Eris.RichEmbed()
        .setColor(0x7289DA)
        .setDescription(message.guild.description / message.guild.description , "")
        .setAuthor(message.guild.name)
        .addField("Information", stripIndents`
        **Name:** ${message.guild.name}
        **ID:** ${message.guild.id}
        **Owner:** <@!${message.guild.ownerID}>
        **Region:** ${region}
        **Verification Level:** ${verification_level}
        **Created At:** ${new Date(message.guild.createdAt).toLocaleString()}
        `)
        .addField("Statistics:", stripIndents`
        **Members:** ${message.guild.memberCount} ($(members.real) members / ${members.bot} Bots)
        **Roles:** ${roles}
        **Channels:** ${channels.total} ($(channels.text) text / ${channels.voice} voice / ${channels.category} category)
        **Emojis:** ${emojis.total} (${emojis.static} non-animated / ${emojis.animated} animated)
        **Status:** ${members.presence.online} online / ${members.presence.idle} idle / ${members.presence.dnd} dnd / ${members.presence.offline} offline
        `)

        if (message.guild.banner) embed.setImage(message.guild.dynamicBannerURL("png, 4069"));
        if (message.guild.icon) embed.setAuthor(message.guild.name, icon, icon);

        return message.channel.createMessage({embed: embed});
    };
    
    if (message.content.startsWith(`${prefix}ping`)) {
        return message.channel.createMessage({content: "Pong!", messageReferenceID: message.id, users: true});
        
    if (message.content.toLowerCase().startsWith(`${prefix}embed`)) {
        let embed = {
            title: "Embed (from Object)",
            description: "This Is A Description",
            url: "https://youtube.com/glowstik",
            timestamp: new Date(),
            color: 0x7289DA,
            footer: {
                text: "this is a foot r", icon_url: "https://yt3.ggpht.com/ytc/AKedOLRoHHgcXols8L3Ii0qhq0tbaEUR7twDK6Bm32J0=s88-c-k-c0x00ffffff-no-rj.png"
            },
            image: {
                url: "https://yt3.ggpht.com/ytc/AKedOLRoHHgcXols8L3Ii0qhq0tbaEUR7twDK6Bm32J0=s88-c-k-c0x00ffffff-no-rj.png"
            },
            thumbnail: {
                url: "https://yt3.ggpht.com/ytc/AKedOLRoHHgcXols8L3Ii0qhq0tbaEUR7twDK6Bm32J0=s88-c-k-c0x00ffffff-no-rj"
            },
            fields: [
                {name: "this Is A Field So Subscrib to Glowstik", value: "this Is A Field So Subscrib to Glowstik (value)", inline: true}
            ],
            author: {
                name: "TwgBot"
            }
        };

        return message.channel.createMessage({embed: embed});
    }
    };
});


bot.connect();