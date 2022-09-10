import random
import time
import os
import PySimpleGUI as sg
import pickle
import math

banner = (
'      ^\n'
'     / \\\n'
'    /   \\\n'
'    | D |\n'
'    | I |\n'
'    | C |\n'
'    | E |\n'
'    |   |\n'
'    | R |\n'
'    | O |\n'
'    | L |\n'
'    | L |\n'
'\___| E |___/\n'
' \--- R ---/\n'
'     | |\n'
'     |t|\n'
'     |w|\n'
'     (c)\n',
'                      / /\n'
'                     / /\n'
'                    / / \n'
'              \____/_/____/\n'
'|\          ^    /   / /|\n'
'| \________/ \__/___/_/ |\n'
'|   _____      ____     |\n'
'|  |  __ \    |  _  \   |\n'
'|  | |  \ |   | |_| /   |\n'
'|  | |__/ |   | ___ \   |\n'
'|  |_____/    |_|  \_\  |\n'
'|         Made          |\n'
'|          BY           |\n'
' \   Tidewatercoder    /\n'
'  \___________________/\n'
'      /   /\n'
'     /   /\n'
'     \  /\n'
'      \/\n',
'      t  /  _______  \\\n'
'        |  / / | \ \  |  w\n'
'        |  \ \ | / /  |\n'
'     c   \  -------  /\n'
'              |D|\n'
'              |I|\n'
'              |C|\n'
'              |E|\n'
'              | |\n'
'              |R|\n'
'              |O|\n'
'              |L|\n'
'              |L|\n'
'              |E|\n'
'              |R|\n'
'              | |\n')
banran = random.choice(banner)
print(banran)
dice = {'d4': '1,2,3,4', 'd6': '1,2,3,4,5,6', 'd8': '1,2,3,4,5,6,7,8', 'd10': '1,2,3,4,5,6,7,8,9,10',
            'd12': '1,2,3,4,5,6,7,8,9,10,11,12', 'd20': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20'}
class Monster():
    def __init__(self,ARM,HP,STR,DEX,CON,INT,WIS,CHA,DES,ALI,MT,SPEED,SKILLS,DI):
        self.ARM = ARM
        self.HP = HP
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.DES = DES
        self.ALI = ALI
        self.MT = MT
        self.SPEED = SPEED
        self.SKILLS = SKILLS
        self.DI = DI

    def Attack_Defend(attdef,ans,name,dicetotd = {}):
        attdefroll = ''
        for i in dicetotd.keys():
            # try:
                diinput,modstat,adpe = dicetotd[i]
                ans2 = ''
                modlist = []
                ARM, HP, STR, DEX, CON, INT, WIS, CHA, DES, ALI, MT, SPEED, SKILLS, DI = \
                    ans.ARM, ans.HP, ans.STR, ans.DEX, ans.CON, ans.INT, ans.WIS, ans.CHA, \
                    ans.DES, ans.ALI, ans.MT, ans.SPEED, ans.SKILLS, ans.DI
                for i in STR, DEX, CON, INT, WIS, CHA:
                    i = int(i)
                    i = i - 10
                    i = i / 2
                    i = math.floor(i)
                    modlist.append(i)
                mSTR, mDEX, mCON, mINT, mWIS, mCHA = modlist
                modlist2 = {'str': mSTR, 'dex': mDEX, 'con': mCON, 'int': mINT, 'wis': mWIS, 'cha': mCHA}
                if modstat != []:
                    for i in modstat:
                        i = i.lower()
                        if i == 'str' or i == 'dex' or i == 'con' or i == 'int' or i == 'wis' or i == 'cha':
                            ans2 = modlist2[i]
                if diinput == '' or diinput == None:
                    sg.PopupError("Please Input dice ")
                    return
                x = RollDice(diinput,'attdef')
                x = int(x)
                for i2 in diinput:
                    pass
                if ans2 != '' and ans2 != None:
                    x += int(ans2)
                    if attdef == 'Attack':
                        attdefroll += f'Attack Roll \n{name} {diinput} + {ans2} = {str(x)}\n'
                        # sg.Popup(f'Attack Roll \n{name} {diinput} + {ans2} =', x)
                    elif attdef == 'Saving Roll':
                        # sg.Popup(f'Saving Roll \n{name} {diinputi} + {ans2} =', x)
                       attdefroll += f'Save Roll \n{name} {diinput} + {ans2} = {str(x)}\n'
                else:
                    if attdef == 'Attack':
                        # sg.Popup(f'Attack Roll \n{name} {diinput} =', x)
                        attdefroll += f'Attack Roll \n{name} {diinput} = {str(x)}\n'
                    elif attdef == 'Saving Roll':
                        # sg.Popup(f'Saving Roll \n{name} {diinput} =', x)
                        attdefroll += f'Save Roll \n{name} {diinput} = {str(x)} \n'
        sg.Popup(attdefroll)
            # except ValueError:
            #     sg.PopupError("ValueError")

def RollDice(dd,direct):
    ditime = 0
    ditime1 = ''
    plus = 0
    comdice = 0
    dlt = []
    dl = ''
    iteration = 0
    grandtotal = {}
    grand1 = ''
    test = '2d12+12 d6 4d4-3'
    addn = ''  # Combines the two characters after + if its double digits
    calc = ''
    rolleddice = ''
    while True:
        something = ''
        # print("Type 'test' to see an example\n you can also type exit to leave!")
        # dd = input('Dice needs ').lower()
        if dd == 'exit':
            exit()
        elif dd == 'directory':
            1==1
        elif dd == 'test':
            dd = test
            sg.Popup(f'{test}\nAs you can see, you can put the number of times to roll the dice, what dice value, '
                  'adding or subtracting value from the dice, and you can even roll multiple dice at once.')
            dd = dd.split(' ')
            # sg.Popup('As you can see, you can put the number of times to roll the dice, what dice value, '
            #       'adding or subtracting value from the dice, and you can even roll multiple dice at once.')
            sg.Popup('Make sure when adding dice you must only put spaces between'
                  ' the different dice like so d4+1 d12+2, NOT d4 + 1 d12 + 2.')
        else:
            try:
                dd = dd.split(' ')
            except Exception:
                1==1
        while True:
            for i in dd:
                iteration += 1
                if iteration >= 2:
                    dlt *= 0
                    plus = 0
                    ditime = 0
                    ditime1 = ''
                    ditime1 = ''
                    comdice = 0
                    addn = 0
                    addn = ''
                # Resets the info in the variables so they can be reused.
                dd3 = i
                for i in dd3:
                    if i != 'd':
                        place = dd3.find(i)
                        ditime1 += i
                        dd3 = dd3[:place] + '' + dd3[place + 1:]
                        ditime = int(ditime1)
                    elif i == 'd':
                        break

                for i in dd3:
                    if i == ' ':
                        continue
                    elif i == '+' or i == '-':
                        plus += 1
                        calc = i
                    elif plus == 1:
                        addn += i
                    elif i == 'd':
                        dl = i
                    else:
                        dl += i
                if addn != '':
                    addn = int(addn)
                dlt.append(dl)

                for i in dlt:
                    key = dice[i]
                    print(i)
                    key = key.split(',')
                    if ditime == 0:
                        ditime += 1
                    for i in range(ditime):
                        diceroll = random.choice(key)
                        i += 1
                        print(f'{dl} roll {i} =', diceroll)
                        comdice += int(diceroll)
                        diceroll = 0

                    if addn != 0 and addn != '':
                        if calc == '+':
                            total = int(comdice) + addn
                            print(f'{comdice} + {addn} =', total,'\n')
                            # if dl in grandtotal:
                            dl = str(ditime)+dl
                            grandtotal[dl] = total
                            rolleddice += dl+' + '+str(addn)+' = '+str(total) + '\n'
                        elif calc == '-':
                            total = int(comdice) - addn
                            print(f'{comdice} - {addn} =', total,'\n')
                            dl = str(ditime)+dl
                            grandtotal[dl] = total
                            rolleddice += dl+' - '+str(addn)+' = '+str(total) + '\n'
                    else:
                        print(f'{comdice}')
                        dl = str(ditime)+dl
                        grandtotal[dl] = int(comdice)
                        total = comdice
                        rolleddice += dl+' = '+str(total)+'\n'
            for i in grandtotal:
                grand1 += str(i)+' = '+str(grandtotal[i])+'\n'
            print(grand1)
            if direct == 'rolldice':
                return rolleddice
            elif direct == 'attdef':
                return total
            break
        break
def rolldice2():
    didis = ''
    for i in dice.keys():
        didis += i+' '
    dicekey = []
    valdicepl = []
    valdiceti = []
    dicesel = []
    for i in dice.keys():
        dicex = [sg.Spin([x for x in range(0, 101)], key=f'{i}ss', s=(7, 2), enable_events=True),
                 sg.T('x'), sg.Checkbox(i, key=f'{i}'),
                 sg.T('+'), sg.Spin([x for x in range(0, 101)], key=f'{i}+', s=(4, 2), enable_events=True)]
        dicekey.append(dicex)
        valdicepl.append(f'{i}+')
        valdiceti.append(f'{i}ss')
    layout=[[sg.MenubarCustom([['Menu',['Main Menu']]])],
            [sg.Col(dicekey)],
            [sg.Button("Submit")]]
    window = sg.Window('Dice',layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Submit':
            # RollDice(values['_DICE_'])\
            # sg.Popup(RollDice(values['_DICE_']))
            dikey = ''
            diti = ''
            dipl = ''
            for i, x, z in zip(valdicepl, valdiceti, dice.keys()):
                # print(i,x,z)
                if i in values:
                    if values[i] > 0:
                        dipl = i+str(values[i])
                        values[i] = 0
                if x in values:
                    if values[x] > 0:
                        diti = i+str(values[x])
                        values[x] = 0
                if z in values:
                    if values[z] == True:
                        dikey = z
                        values[z] = False
                if dikey == '':
                    continue
                elif dikey in diti and dikey in dipl:
                    diti = diti.split('+')
                    diti = diti[-1]
                    dipl = dipl.split('+')
                    dipl = dipl[-1]
                    if diti != '' and dipl != '':
                        dicesel.append(diti + dikey + '+' + dipl)
                elif dikey in diti:
                    diti = diti.split('+')
                    diti = diti[-1]
                    if diti != '' and dipl == '':
                        dicesel.append(diti + dikey)
                elif dikey in dipl:
                    dipl = dipl.split('+')
                    dipl = dipl[-1]
                    if diti == '' and dipl != '':
                        dicesel.append(dikey + '+' + dipl)
                elif dikey not in dipl and dikey not in diti:
                    dicesel.append(dikey)
                diti = ''
                dipl = ''
                dikey = ''
            xroll = RollDice(dicesel,'rolldice')
            sg.Popup(xroll)
            dicesel *= 0
        elif event == 'Main Menu':
            window.close()
            directory()
            break
def Monstermaker():
        monstermaker = {}
        frametxt = [[sg.Text('Name')],
                [sg.Text('Armor')],
                   [sg.Text("Hitpoints")],
                   [sg.Text("Strength")],
                  [sg.Text("Dexterity")],
                  [sg.Text("Constitution")],
                  [sg.Text('Intelligence')],
                  [sg.Text('Wisdom')],
                  [sg.Text('Charisma')]]
        framein = [[sg.Input(size=(10,10),key='_NAME_')],
                   [sg.Input(size=(10,10),key='armor')],
                   [sg.Input(size=(10,10),key='hitpoints')],
                   [sg.Input(size=(10,10),key='str1')],
                  [sg.Input(size=(10,10),key='dex')],
                  [sg.Input(size=(10,10),key='con')],
                  [sg.Input(size=(10,10),key='int1')],
                  [sg.Input(size=(10,10),key='wis')],
                  [sg.Input(size=(10,10),key='cha')]]
        frameother = [[sg.Column([[sg.Text("Alignment")],[sg.Text("Monster Type")],
                                  [sg.T('Speed')],
                                  [sg.T("Skills")],
                                  [sg.T("Damage Immunity")]]),
                       sg.Column([[sg.Combo(('Lawful Good','Neutral Good','Chaotic Good',
                                 'Lawful Neutral','True Neutral','Chaotic Neutral',
                                 'Lawful Evil','Neutral Evil','Chaotic Evil'),size=(11,20))],
                                  [sg.Input(size=(10,10),key="_TYPE_")],
                                  [sg.Input(size=(10,10),key="_SPE_")],
                                  [sg.Input(size=(10,10),key="_SKI_")],
                                  [sg.Input(size=(10,10),key="_DI_")]])]]
        monsdis = [[sg.Text('Monsters Created')],[sg.Multiline(size=(20,20),key='_MON_')]]
        framemulti = [[sg.Text("Description")],[sg.Multiline(size=(82,10),key='DESC')]]
        layout = [[sg.MenubarCustom([['Menu',['Main Menu','Load','Save','Delete','Purge']]])],
                  [sg.Column(frametxt),sg.Column(framein),
                   sg.VerticalSeparator(),sg.Column(frameother),
                   sg.VerticalSeparator(),
                   sg.Column(monsdis)],
                  [sg.HorizontalSeparator()],
                  [sg.Column(framemulti)],
                  [sg.Button("Submit")]]
        window = sg.Window('Monster Maker',layout)
        while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                        window.close()
                        exit()
                elif event == 'Submit':
                    if 'monsterfile.pickle' in os.listdir():
                        with open('monsterfile.pickle','rb') as g:
                            monstermaker = pickle.load(g)
                    # SPEED, SKILLS, DI
                    armor = values['armor']
                    hitpoints = values['hitpoints']
                    str1 = values['str1']
                    dex = values['dex']
                    con = values['con']
                    int1 = values['int1']
                    wis = values['wis']
                    cha = values['cha']
                    des1 = values['DESC']
                    ali = values[1]
                    mt = values['_TYPE_']
                    spe = values["_SPE_"]
                    ski = values['_SKI_']
                    di = values['_DI_']
                    monname = values['_NAME_']
                    makemon = Monster(armor, hitpoints, str1, dex, con, int1, wis, cha, des1,ali,mt,spe,ski,di)
                    monstermaker[monname] = makemon
                    monsters = ''
                    window.find_element('_MON_').Update(monname)
                    with open('monsterfile.pickle','wb') as g:
                        pickle.dump(monstermaker,g,protocol=pickle.HIGHEST_PROTOCOL)
                elif event == 'Save':
                    with open('monsterfile.pickle', 'wb') as g:
                            pickle.dump(monstermaker, g, protocol=pickle.HIGHEST_PROTOCOL)
                    monsters = ''
                    for i in monstermaker.keys():
                        monsters += i+'\n'
                    window.find_element('_MON_').Update(monsters)
                elif event == "Load":
                    if 'monsterfile.pickle' in os.listdir():
                        with open('monsterfile.pickle','rb') as g:
                           monstermaker = pickle.load(g)
                        monsters = ''
                        for i in monstermaker.keys():
                            monsters += i+'\n'
                        window.find_element('_MON_').Update(monsters)
                    else:
                        sg.Popup("No monsters have been created yet!")
                elif event == 'Delete':
                    Delete(monstermaker)
                    monsters = ''
                    for i in monstermaker.keys():
                        monsters += i+'\n'
                    window.find_element('_MON_').Update(monsters)
                elif event == 'Main Menu':
                    window.close()
                    directory()
                elif event == 'Purge':
                    monstermaker.clear()
                    with open('monsterfile.pickle','wb') as g:
                        pickle.dump(monstermaker,g,protocol=pickle.HIGHEST_PROTOCOL)

def Delete(monstermaker):
    monsters = []
    for i in monstermaker.keys():
        monsters.append(i)
    layout = [[sg.Combo(monsters)],
              [sg.Button("Delete")]]
    window = sg.Window("Delete",layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'Delete':
            monstermaker.pop(values[0])
            with open('monsterfile.pickle','wb') as g:
                pickle.dump(monstermaker,g,protocol=pickle.HIGHEST_PROTOCOL)

def MonsterBook():
    monname = sg.Column([[sg.T(key='_PAGE')]])
    monname2 = sg.Column([[sg.T(key="_PAGE2",size=(25,0))]])
    mondet = sg.Column([[sg.Text(key='_PAGE3',enable_events=True)]])
    mondet2 = sg.Column([[sg.T(key='_PAGE4',enable_events=True)]])
    mondis = sg.Column([[sg.T(key='_PAGE5')]])
    monsters = {}
    monslist = []
    keyassign = {}
    turn = 0
    x = 0
    if 'monsterfile.pickle' in os.listdir():
        with open('monsterfile.pickle','rb') as g:
            monsters = pickle.load(g)
            if monsters == {}:
                sg.popup_error("No monsters found!")
                directory()
    elif 'monsterfile.pickle' not in os.listdir():
        sg.popup_error("Error no monster file found!")
        directory()
    lenmon = len(monsters)
    for i in monsters.keys():
        x+=1
        monslist.append(i)
        keyassign[x] = i
    layout = [[sg.MenubarCustom([['Menu',['Main Menu']]])],
              [sg.Combo(monslist),sg.Button("View")],
              [sg.Spin([x for x in range(1,lenmon+1)],s=(7,2),enable_events=True), sg.Button('GoTo')],
              [[sg.HorizontalSeparator()]],
              [[monname,monname2],[mondet,mondet2],[mondis]],
              [sg.Button('Previous Page'),sg.Button('Next Page')]]
    window = sg.Window('Book of Monsters',layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == 'View' or event == 'GoTo' or event == 'Next Page' or event == 'Previous Page':
            if event == 'GoTo':
                if values[1] not in keyassign:
                    continue
                ans2 = keyassign[values[1]]
                turn = values[1]
                ans = monsters[ans2]
                x = ans2
            elif event == 'View':
                x = values[0]
                if x == '':
                    continue
                for i in keyassign.keys():
                    if keyassign[i] == x:
                        turn = i
                ans = monsters[x]
            elif event == 'Next Page':
                turn += 1
                if turn not in keyassign.keys():
                    turn-=1
                    continue
                ans2 = keyassign[turn]
                ans = monsters[ans2]
                x = ans2
            elif event == 'Previous Page':
                print(turn)
                turn -= 1
                if turn not in keyassign.keys():
                    turn+=1
                    continue
                ans2 = keyassign[turn]
                ans = monsters[ans2]
                x = ans2
                print(x)
                # exit()
            ARM, HP, STR, DEX, CON, INT, WIS, CHA, DES, ALI, MT, SPEED, SKILLS, DI = \
                ans.ARM, ans.HP, ans.STR, ans.DEX, ans.CON, ans.INT, ans.WIS, ans.CHA, \
                ans.DES, ans.ALI, ans.MT, ans.SPEED, ans.SKILLS, ans.DI
            modstat2 = []
            for i in STR,DEX,CON,INT,WIS,CHA:
                i = int(i)
                i = i - 10
                i = i / 2
                i = math.floor(i)
                # modstat2 += str(i)+'\n'
                modstat2.append(str(i))
            STR2,DEX2,CON2,INT2,WIS2,CHA2 = modstat2
            monstername = x + '\n' + ARM + '\n' + HP + '\n' + SPEED + '\n' + SKILLS + '\n' + DI
            monstername2 ='Name' + '\n' + 'Armor' + '\n' + 'HP' + '\n' + 'Speed' + '\n' + 'Skills' + '\n' + 'Dam Immun'
            statvalues = 'V' + '    ' + 'Mod' + '\n' + STR + '    ' + STR2 + '\n' + DEX + '    ' + DEX2 + '\n' \
                         + CON + '    ' + CON2 + '\n' + INT + '    ' + INT2 + '\n' + WIS + '    ' + WIS2 + '\n' \
                         + CHA + '    ' + CHA2
            namestats = 'Stats' + '\n' + 'STR' + '\n' + 'DEX''\n' + 'CON' + '\n' + 'INT' + '\n' + "WIS" + '\n' + "CHA"
            mondis2 = 'DES' + '\n' + DES
            window.find_element('_PAGE').Update(monstername2)
            window.find_element('_PAGE2').Update(monstername)
            window.find_element('_PAGE3').Update(namestats)
            window.find_element('_PAGE4').Update(statvalues)
            window.find_element('_PAGE5').Update(mondis2)
        elif event == 'Main Menu':
            window.close()
            directory()


def directory():
    layout = [[sg.Button("RollDice"),sg.Button("Monster Maker"),
               sg.Button("Book of Monsters"),sg.Button("Battle Page")]]
    window = sg.Window("Main Menu",layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            exit()
        elif event == 'RollDice':
            window.close()
            rolldice2()
            break
        elif event == 'Monster Maker':
                window.close()
                Monstermaker()
        elif event == 'Book of Monsters':
            window.close()
            MonsterBook()
        elif event == "Battle Page":
            window.close()
            Battle()

def Battle(tabb2 = {}):
    monsters = {}
    monslist = []
    tabb3 = []
    dicekey = []
    statl = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    statl2 = []
    valdiceti = []
    valdicepl = []
    ########
    diti = ''
    dipl = ''
    dicesel = ''
    modstat = []
    dicetotd = {}
    dicetotal = []
    ###
    for i in statl:
        statx = [sg.Checkbox(i, key=f'{i}')]
        statl2.append(statx)
    for i in dice.keys():
        dicex = [sg.Spin([x for x in range(0, 101)], key=f'{i}ss', s=(7, 2), enable_events=True),
                 sg.T('x'), sg.Checkbox(i, key=f'{i}'),
                 sg.T('+'), sg.Spin([x for x in range(0, 101)], key=f'{i}+', s=(4, 2), enable_events=True)]
        dicekey.append(dicex)
        valdicepl.append(f'{i}+')
        valdiceti.append(f'{i}ss')
    for i in tabb2.keys():
        tabb3.append(tabb2[i])
    if 'monsterfile.pickle' in os.listdir():
        with open('monsterfile.pickle','rb') as g:
            monsters = pickle.load(g)
    else:
        sg.PopupError("No monsters found")
    for i in monsters.keys():
        monslist.append(i)
    adpe = [sg.Checkbox('Advantage',key='ADVAN')],[sg.Checkbox('Penalty',key='PENALTY')]
    layout = [[sg.Menu([['Menu',['Main Menu']]])],
              [sg.Combo(monslist),sg.Button("Fighters")],
              [sg.TabGroup(tabb3,key='_TABBY')],
              [[sg.Column(dicekey),
               sg.Column(statl2),
               sg.Column(adpe)],
               [sg.Button("Submit"),sg.Button("Remove")]],
              [sg.Button('Attack'),sg.Button("Saving Roll")]]
    window = sg.Window('Battle Page', layout)
    while True:
        adpe2 = ''
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "Fighters":
            x = values[1]
            if x == '' or x == None:
                continue
            ans = monsters[x]
            ARM, HP, STR, DEX, CON, INT, WIS, CHA, DES,ALI,MT,SPEED,SKILLS,DI = \
                ans.ARM, ans.HP, ans.STR, ans.DEX, ans.CON, ans.INT, ans.WIS, ans.CHA,\
                ans.DES,ans.ALI,ans.MT,ans.SPEED,ans.SKILLS,ans.DI
            modstat2 = []
            for i in STR, DEX, CON, INT, WIS, CHA:
                i = int(i)
                i = i - 10
                i = i / 2
                i = math.floor(i)
                # modstat2 += str(i)+'\n'
                modstat2.append(str(i))
            STR2, DEX2, CON2, INT2, WIS2, CHA2 = modstat2
            monstername = sg.T(x + '\n'+ALI+'\n' + ARM + '\n' + HP+ '\n'+SPEED+'\n'+SKILLS+'\n'+DI)
            monstername2 = sg.T('Name' + '\n'+'Alignment'+'\n' + 'Armor' + '\n' + 'HP'+'\n'+'Speed'+'\n'+'Skills'+'\n'+'Dam Immun')
            statvalues = 'V' + '    ' + 'Mod' + '\n' + STR + '    ' + STR2 + '\n' + DEX + '    ' + DEX2 + '\n'\
                          + CON + '    ' + CON2 + '\n' + INT + '    ' + INT2 + '\n' + WIS + '    ' + WIS2 + '\n'\
                         + CHA + '    ' + CHA2
            namestats = 'Stats' + '\n' + 'STR' + '\n' + 'DEX''\n' + 'CON' + '\n' + 'INT' + '\n' + "WIS" + '\n' + "CHA"
            mondis2 = 'DES' + '\n' + DES
            tabb = sg.Tab(f'{x}',[[monstername2,monstername],
                [sg.T(namestats),sg.T(statvalues)],
                [sg.T(mondis2)]])
            window.find_element('_TABBY').add_tab(tabb)
            tabb2[f'{x}'] = tabb
        elif event == 'Main Menu':
            window.close()
            directory()
            break
        elif event == 'Submit':
            dikey = ''
            diti = ''
            dipl = ''
            dicesel = ''
            for i, x, z in zip(valdicepl, valdiceti, dice.keys()):
                # print(i,x,z)
                if i in values:
                    if values[i] > 0:
                        dipl = str(values[i])
                        values[i] = 0
                if x in values:
                    if values[x] > 0:
                        diti = str(values[x])
                        values[x] = 0
                if z in values:
                    if values[z] == True:
                        dikey = z
                        values[z] = False
                for i in statl:
                    # print(statl)
                    if i in values:
                        if values[i] == True:
                            modstat.append(i)
                            values[i] = False
                if dikey == '':
                    continue
                elif diti != '' and dipl != '':
                    dicesel = diti + dikey + '+' + dipl
                elif diti != '' and dipl == '':
                    dicesel = diti + dikey
                elif diti == '' and dipl != '':
                    dicesel = dikey + '+' + dipl
                elif diti == '' and dipl == '':
                    dicesel = dikey
                diti = ''
                dipl = ''
                dikey = ''
                if values['ADVAN'] == True and values['PENALTY'] == True:
                    sg.PopupError("Cant have advantage and penalty selected at the same time!")
                    continue
                elif values['ADVAN'] == True:
                    adpe2 = 'ADVAN'
                elif values['PENALTY'] == True:
                    adpe2 = 'PENALTY'
                if values['_TABBY'] == None:
                    continue
                for i in dicesel, modstat, adpe2:
                    dicetotal.append(i)
                dicetotd[values['_TABBY']] = dicetotal
                print(dicetotd)
                dicesel = ''
                dicetotal = []
        elif event == 'Remove':
            try:
                dicetotd.pop(values['_TABBY'])
                print(dicetotd)
            except KeyError:
                sg.PopupError("Error: Monster Not On The List!")
                print("List",dicetotd)
        elif event == 'Attack' or event == 'Saving Roll':
            # try:
            if dicetotd != {}:
                Monster.Attack_Defend(event,monsters[values['_TABBY']],values['_TABBY'],dicetotd)
            dicetotal = []
            dicetotd = {}
            modstat *= 0
if __name__ == '__main__':
    directory()