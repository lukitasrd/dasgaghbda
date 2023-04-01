const whitelisted = [938477373773, 938373] // array of guild ids

// add this listener

client.on('guildCreate', guild => {
  if (!whitelisted.includes(guild.id)) guild.leave()
})

// add check for each guild on ready

client.on('ready', () => {
  // keep all other things here that are already here
  
  // add this
  client.guilds.cache.forEach(guild => {
    if (!whitelisted.includes(guild.id)) guild.leave()
  })
})



