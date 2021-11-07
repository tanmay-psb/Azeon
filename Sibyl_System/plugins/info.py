from Sibyl_System import System, system_cmd

from Sibyl_System.plugins.Mongo_DB.gbans import get_gban

@System.on(system_cmd(pattern=r"info ", allow_enforcer=True))
async def info(event):
	if event.reply_to_msg_id:
		replied = await event.get_reply_message()
		if replied:
		      	id = replied.sender.id
	else:
		id = str(event.pattern_match.group(1)).strip()
	if id:
		try:
			msg = await event.reply("Finding Information of the user in Azeon Database..")
			info = await System.get_entity(id)
			text = f"Id: {info.id}"
			text += f"\nFirst Name: {info.first_name}\n"
			if info.last_name:
				text += f"Last name: {info.last_name}\n"
			if info.username:
				text += f"Username: @{info.username}\n"
			text += f"Restricted: {info.restricted}\n"
			
		except Exception as e:
			print(e)
			await msg.edit("Given User id or Username is invalid!")
			
__plugin_name__ = "info"
	
help_plus = """
Get info of the specific user:
	by .info <username or reply to an user>
"""
# stormshadow2op testing this rn
