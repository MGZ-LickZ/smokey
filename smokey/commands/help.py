
# Translation:
# You can put any poetry, no need to translate specifically these
poetry = {"fr": [
            "Jour meilleur n'existe qu'avec douleur.",
            "La seule personne que vous êtes destiné à devenir est la personne que vous décidez d'être.",
            "L'avenir appartient à ceux qui croient en la beauté de leurs rêves.",
            "L'échec est le fondement de la réussite.",
            "Ne rêvez pas votre vie, vivez vos rêves.",
            "Crois en toi, et les autres suivront.",
            "Sois le changement que tu veux voir dans le monde.",
            "Poursuis tes rêves, ils connaissent le chemin.",
            "La vie récompense l'action.",
            "Tu es plus fort que tu ne le crois.",
            "Le succès commence par l'action.",
            "La persévérance bat le talent.",
            "Ne remettez pas à demain.",
            "Chaque effort compte.",
            "Les montagnes les plus hautes ont les pentes les plus raides.",
            "Les éclats de lumière percent l'obscurité la plus profonde.",
            ],
            "en": [
            "Your attitude determines your direction.",
            "Progress, not perfection.",
            "Embrace the challenges, for they are the stepping stones to success.",
            "Embrace failure as a stepping stone, not a stumbling block.",
            "The only limits that exist are the ones you place on yourself.",
            "Courage is not the absence of fear but the triumph over it.",
            "Dreams don't work unless you do",
            "Opportunities don't happen. You create them.",
            "Don't wait for the perfect moment; take the moment and make it perfect.",
            "The only way to do great work is to love what you do.",
            "Believe you can, and you're halfway there.",
            "Don't watch the clock; do what it does. Keep going.",
            ],
            "es": [
            "Tu actitud determina tu dirección.",
            "Progreso, no perfección.",
            "Abraza los desafíos, porque son los peldaños hacia el éxito.",
            "Abraza el fracaso como un peldaño, no como un obstáculo.",
            "Los únicos límites que existen son los que te impones a ti mismo.",
            "El coraje no es la ausencia de miedo, sino el triunfo sobre él.",
            "Los sueños no funcionan a menos que tú lo hagas.",
            "Las oportunidades no suceden. Tú las creas.",
            "No esperes el momento perfecto; toma el momento y hazlo perfecto.",
            "La única manera de hacer un gran trabajo es amar lo que haces.",
            "Cree que puedes, y ya estás a mitad de camino.",
            "No mires el reloj; haz lo que hace. Sigue adelante.",
            "Un mejor día solo existe con dolor.",
            "La única persona que estás destinado a convertirte es la persona que decides ser.",
            "El futuro pertenece a aquellos que creen en la belleza de sus sueños.",
            "El fracaso es la base del éxito.",
            "No sueñes tu vida, vive tus sueños.",
            "Cree en ti mismo, y los demás te seguirán.",
            "Sé el cambio que quieres ver en el mundo.",
            "Persigue tus sueños, ellos conocen el camino.",
            "La vida recompensa la acción.",
            "Eres más fuerte de lo que crees.",
            "El éxito comienza con la acción.",
            "La perseverancia supera al talento.",
            "No dejes para mañana.",
            "Cada esfuerzo cuenta.",
            "Las montañas más altas tienen las pendientes más empinadas.",
            "Los destellos de luz atraviesan la oscuridad más profunda.",
            ],
            "jp": [
            "あなたの態度があなたの方向を決めます。",
            "完璧さではなく、進歩。",
            "挑戦を受け入れ、それが成功への踏み石であることを認識してください。",
            "失敗を障害ではなく、踏み石として受け入れましょう。",
            "存在する限界は、自分が設ける限界だけです。",
            "勇気は恐怖の不在ではなく、それを克服することです。",
            "夢は、あなたが働かなければ実現しません。",
            "機会は起こるものではありません。あなたが作り出します。",
            "完璧な瞬間を待たず、その瞬間を完璧にしましょう。",
            "素晴らしい仕事をする唯一の方法は、あなたがしていることを愛することです。",
            "自分ができると信じれば、半分は達成したも同然です。",
            "時計を見てはいけません; 時計のように行動し続けましょう。",
            "より良い日々は痛みと共にしか存在しません。",
            "あなたがなるべき唯一の人は、あなたが決めた人です。",
            "未来は、自分の夢の美しさを信じる人々のものです。",
            "失敗は成功の基盤です。",
            "人生を夢見るのではなく、夢を生きましょう。",
            "自分を信じれば、他の人もついてきます。",
            "世界で見たい変化になりましょう。",
            "夢を追いかけてください、それらは道を知っています。",
            "人生は行動を報います。",
            "あなたは自分が思うよりも強いです。",
            "成功は行動から始まります。",
            "忍耐は才能に勝ります。",
            "明日まで延ばさないでください。",
            "すべての努力が大切です。",
            "最も高い山は最も急な斜面を持っています。",
            "光の閃光は最も深い暗闇を貫きます。",
            ],
}

from discord.ext import commands
import random

import config_selfbot
from utils import lang


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name}:**__ ☄
  ☄ "{random.choice(poetry[config_selfbot.lang])}" ☄

  📂| __**{lang.text('help_utils')}:**__ `{config_selfbot.prefix}utils`
  🎤| __**{lang.text('help_voice')}:**__ `{config_selfbot.prefix}voice`
  🕹️| __**{lang.text('help_rich_presence')}:**__ `{config_selfbot.prefix}presence`
  📖| __**{lang.text('help_templates')}:**__ `{config_selfbot.prefix}templates`
  🎲| __**{lang.text('help_fun')}:**__ `{config_selfbot.prefix}fun`
  🏯| __**{lang.text('help_raid')}:**__ `{config_selfbot.prefix}raid`
  🔧| __**{lang.text('help_tools')}:**__ `{config_selfbot.prefix}tools`
  ⚙️| __**{lang.text('help_config')}:**__ `{config_selfbot.prefix}config`
  🗃️| __**{lang.text('help_backup')}:**__ `{config_selfbot.prefix}backup`""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def backup(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🗃️| __**{lang.text('help_backup')}:**__
 `{config_selfbot.prefix}backups`: {lang.text('help_backup_backups')}
 `{config_selfbot.prefix}save {lang.text('optional')}[<server_id>]`: {lang.text('help_backup_save')}
 `{config_selfbot.prefix}load <backup_id> {lang.text('optional')}[<server_id>]`: {lang.text('help_backup_load')}
 `{config_selfbot.prefix}delete`: {lang.text('help_backup_delete')}
 🖋️ {lang.text('help_backup_note')}
 💡 {lang.text('help_backup_tip')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def tools(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🔧| __**{lang.text('help_tools')}:**__
 `{config_selfbot.prefix}closealldm`: {lang.text('help_tools_close_dm')}
 `{config_selfbot.prefix}botclosedm`: {lang.text('help_tools_close_dm_bots')}
 `{config_selfbot.prefix}dmall`: {lang.text('help_tools_dmall')}
 `{config_selfbot.prefix}bump <amount>`: {lang.text('help_tools_bump')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def fun(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎲| __**{lang.text('help_fun')}:**__

**Original Fun Commands**
 `{config_selfbot.prefix}cat`: {lang.text('help_fun_cat')}
 `{config_selfbot.prefix}good`: {lang.text('help_fun_good')}
 `{config_selfbot.prefix}call`: {lang.text('help_fun_call')}
 `{config_selfbot.prefix}gift <random/nerd/poor/hit>`: {lang.text('help_fun_gift')}
 `{config_selfbot.prefix}hack`: {lang.text('help_fun_hack')}
 `{config_selfbot.prefix}howfemboy`: {lang.text('help_fun_femboy')}
 `{config_selfbot.prefix}token`: {lang.text('help_fun_token')}
 `{config_selfbot.prefix}hug`: {lang.text('help_fun_hug')}
 `{config_selfbot.prefix}slap`: {lang.text('help_fun_slap')}

**Extra Fun Commands**
 `{config_selfbot.prefix}8ball <question>`: Ask the magic 8-ball a question.
 `{config_selfbot.prefix}coinflip`: Flip a coin.
 `{config_selfbot.prefix}dice [sides]`: Roll a dice (default: 6 sides).
 `{config_selfbot.prefix}roast [@user/user_id]`: Generate a random roast.
 `{config_selfbot.prefix}ship @user1 @user2`: Check compatibility between two users.
 `{config_selfbot.prefix}meme`: Get a random meme.
 `{config_selfbot.prefix}cat2`: Get a random cat image.
 `{config_selfbot.prefix}hug2 [@user/user_id]`: Send a random hug GIF.
 `{config_selfbot.prefix}slap2 [@user/user_id]`: Send a random slap GIF.""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def config(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

⚙️| __**{lang.text('help_config')}:**__
 `{config_selfbot.prefix}nitrosniper`: {lang.text('help_general_sniper')}
 `{config_selfbot.prefix}restart`: {lang.text('help_config_restart')}
 `{config_selfbot.prefix}stop`: {lang.text('help_config_stop')}
 `{config_selfbot.prefix}lang`""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def raid(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🏯| __**{lang.text('help_raid')}:**__
 `{config_selfbot.prefix}spam`: Spam.
 `{config_selfbot.prefix}flood`: Flood.
 `{config_selfbot.prefix}kickall`: {lang.text('help_raid_kick')}
 `{config_selfbot.prefix}banall`: {lang.text('help_raid_banall')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def utils(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

📂| __**{lang.text('help_utils')}:**__
 `{config_selfbot.prefix}ping`: {lang.text('help_general_ping')}
 `{config_selfbot.prefix}snipe`: {lang.text('help_general_snipe')}
 `{config_selfbot.prefix}clear`: {lang.text('help_general_clear')}
 `{config_selfbot.prefix}hype`: {lang.text('help_general_hype')}
 `{config_selfbot.prefix}bio`: {lang.text('help_general_bio')}
 `{config_selfbot.prefix}userinfo`: {lang.text('help_general_user_info')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def voice(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎤| __**{lang.text('help_voice')}:**__
 `{config_selfbot.prefix}joinvc <voice_channel_id>`: {lang.text('help_voice_vc')}
 `{config_selfbot.prefix}joincam <voice_channel_id>`: {lang.text('help_voice_cam')}
 `{config_selfbot.prefix}leavevc`: {lang.text('help_voice_leave')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def tuto(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎮| __**Rich Presence Image Tutorial:**__
{lang.text('tutorial_rpc')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def templates(self, ctx: commands.Context):
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

📖| __**{lang.text('help_templates')}:**__
 `{config_selfbot.prefix}use default`: {lang.text('template_help_default')}
 `{config_selfbot.prefix}use reset`: {lang.text('template_help_reset')}
 `{config_selfbot.prefix}use clear`: {lang.text('template_help_clear')}
 `{config_selfbot.prefix}use hi`: {lang.text('template_help_hi')}
 `{config_selfbot.prefix}use webdeck`: {lang.text('template_help_webdeck')}
 `{config_selfbot.prefix}use omori`: {lang.text('template_help_omori')}
 `{config_selfbot.prefix}use youtube`: {lang.text('template_help_youtube')}
 `{config_selfbot.prefix}use car`: {lang.text('template_help_car')}
 `{config_selfbot.prefix}use nuclear`: {lang.text('template_help_self')}
 `{config_selfbot.prefix}use dark`: {lang.text('template_help_dark')}
 `{config_selfbot.prefix}use python`: {lang.text('template_help_python')}
 `{config_selfbot.prefix}use js`: {lang.text('template_help_js')}
 `{config_selfbot.prefix}use cod`: {lang.text('template_help_cod')}
 `{config_selfbot.prefix}use gta`: {lang.text('template_help_gta')}
 `{config_selfbot.prefix}use tiktok`: {lang.text('template_help_tiktok')}
 💡 {lang.text('template_help_reload')}""", delete_after=config_selfbot.deltime)

    @commands.command()
    async def presence(self, ctx: commands.Context):
        """Waiting for discord.pyself to add buttons links.
    `{config_selfbot.prefix}rpc_button_link_one`: {lang.text('rpc_button_link_one_translate')}.
    `{config_selfbot.prefix}rpc_button_link_two`: {lang.text('rpc_button_link_two_translate')}.
        """
        await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🕹️| __**{lang.text('help_rich_presence')}:**__
 `{config_selfbot.prefix}rpc_name`: {lang.text('rpc_name_translate')}
 `{config_selfbot.prefix}rpc_details`: {lang.text('rpc_details_translate')}
 `{config_selfbot.prefix}rpc_state`: {lang.text('rpc_state_translate')}
 `{config_selfbot.prefix}rpc_url`: {lang.text('rpc_url_translate')}
 `{config_selfbot.prefix}rpc_type <play / watch / listen / stream / competing / xbox>`: {lang.text('rpc_type_translate')}
 `{config_selfbot.prefix}rpc_large_image`: {lang.text('rpc_large_image_translate')} (`{config_selfbot.prefix}tuto`!)
 `{config_selfbot.prefix}rpc_large_text`: {lang.text('rpc_large_text_translate')}
 `{config_selfbot.prefix}rpc_small_image`: {lang.text('rpc_small_image_translate')} (`{config_selfbot.prefix}tuto`!)
 `{config_selfbot.prefix}rpc_small_text`: {lang.text('rpc_small_text_translate')}
 `{config_selfbot.prefix}rpc_button_text_one`: {lang.text('rpc_button_text_one_translate')}
 `{config_selfbot.prefix}rpc_button_text_two`: {lang.text('rpc_button_text_two_translate')}""", delete_after=config_selfbot.deltime)
