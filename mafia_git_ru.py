import random
import discord

token = '' #Вписать токен Вашего бота
client = discord.Client()
moderator = ''#Вписать Ваше полное имя

cards = ['Дон мафии', 'Мафия', 'Доктор', 'Путана','Мирный житель','Мирный житель','Коммисар']
#Регулируете список ролей, в зависимости от кол-ва пользователей. После окончания игры перезапустите бота для начала новой.
members = [] 
killed=[] 
roles=[]
alibi = []

@client.event
async def on_ready():     
    print('Мафия уже в городе!')#Идентификатор запуска, после его появления можно писать боту
    
@client.event
async def on_message(message):

    msg = message.content.lower()
    author = str(message.author)
    name, tag = author.split('#')

    if name != '':#Вписать имя бота без тэга
        
        if msg == '!mafia': 
            if cards != []:
                choice = random.choice(cards)
                members.append(name.lower())
                cards.remove(choice)
                roles.append(name + ' - ' + choice)
                await message.channel.send(choice)
                print(name, 'получил свою роль!)')
            else:
                await message.channel.send('Все роли разобраны! Дождитесь окончания игры или напишите ' + moderator)

        if msg == '!members':
            if members != []:
                await message.channel.send('Участники: ' + ', '.join(members))
            if killed != []:
                await message.channel.send('Выбывшие: ' + ', '.join(killed))
            if alibi != []:
                await message.channel.send('Алиби: ' + alibi[0])
            
        if '!kill' in msg:
            n = msg.replace('!kill ', '')
            members.remove(n)
            killed.append(n)

        if '!add' in msg:
            role = msg.replace('!add ', '')
            roles.append(role)
            mem, role1 = role.split(' - ')
            members.append(mem)
            
        if msg == '!roles':
            print('Запрос от ' + name)
            ans = str(input('Разрешить доступ? '))
            if ans == '1' or ans.lower() == 'да' or ans.lower() == 'yes':
                await message.channel.send(', '.join(roles))
            else:
                await message.channel.send('Вам отказано в доступе')

        if '!alibi' in msg:
            alibi.clear()
            alibi.append(msg.replace('!alibi ', ''))

        if '!heal' in msg:
            healed = msg.replace('!heal ', '')
            killed.remove(healed)
            members.add(healed)

        if msg == '!mafia_help':
            await message.channel.send('Команда !alibi [Имя Игрока] для выдачи алиби игроку. Команда !mafia нужна для получения роли, в начале игры пишите эту комманду в лс боту для получения роли. !members - показывает живых и выбывших участников. !kill (Первоначальное имя игрока в дискорде). !add (Имя игрока - Роль) - добавляет игрока в игру. Желательно, чтобы эту команду писал ведущий боту в лс. !kill- убивает игрока. !roles - выдает имя игрока и его роль. Команда для ведущего. !heal (Имя игрока) - добавляет игрока в список участников, кроме списка для ведущего. !role (Имя игрока - Роль) - добавляет игрока в список ведущего.')

client.run(token)
