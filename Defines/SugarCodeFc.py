"""
SugarCode的效果库与条件库
(抢劫版)
"""
trigs = {
    "min_coin": {"介绍": "(最低金币，int)", "参数": ["int"]},
    "max_coin": {"介绍": "(最高金币，int)", "参数": ["int"]},
    "act_weight": {"介绍": "(主动权值，int)", "参数": ["int"]},
    "pass_weight": {"介绍": "(被动权值，int)", "参数": ["int"]},
    "Aact_weight": {"介绍": "(目标主动权值，int)", "参数": ["int"]},
    "Apass_weight": {"介绍": "(目标被动权值，int)", "参数": ["int"]},
    "speed": {"介绍": "(速度改变,[目标,改变量])", "参数": ["int", "float"]},
    "attact": {"介绍": "(攻击力改变,[目标,改变量])", "参数": ["int", "float"]},
    "trueAttact": {"介绍": "(最终伤害值改变,[目标,改变量])", "参数": ["int", "float"]},
    "defense": {"介绍": "(防御值改变,[目标,改变量])", "参数": ["int", "float"]},
    "fre": {"介绍": "(抢劫次数上限改变……,int)", "参数": ["int"]},
    "costFre": {"介绍": "(本次抢劫次数消耗改变……int,int(目标，数))", "参数": ["int", "int"]},
    "SeeChaMay": {"介绍": "(有偏差的查看对方权值并计算几率,bool)", "参数": ["bool"]},
    "SeeCha": {"介绍": "(精准的查看对方权值并计算几率,bool)", "参数": ["bool"]},
    "pro_get": {"介绍": "(百分比获取金币,[百分比，最低获得，最高获得])", "参数": ["float", "float", "float"]},
    "get_coin": {"介绍": "(固定额外获得金币,int)", "参数": ["int"]},
    "get_coin_random": {"介绍": "(额外获得范围内金币,[int,int])", "参数": ["int", "int"]},
    "AllToAct": {"介绍": "(无条件被动权值全转变为主动权值,bool)", "参数": ["bool"]},
    "coinMp": {"介绍": "(金币倍数，[额外倍数，最低获得，最高获得])", "参数": ["float", "float", "float"]},
    "loseCoinMp": {"介绍": "(失败金币倍数，[额外倍数，最低获得，最高获得])", "参数": ["float", "float", "float"]},
    "toMeCoinMp": {"介绍": "(金币倍数，[对方对自己的额外倍数，最低获得，最高获得])", "参数": ["float", "float", "float"]},
    "toMeLoseCoinMp": {"介绍": "(金币倍数，[对方对自己失败的额外倍数，最低获得，最高获得])", "参数": ["float", "float", "float"]},
    "appendString": {"介绍": "(在抢劫消息后追加文字(<n>为换行)，str)", "参数": ["str"]},
    "appendString2": {"介绍": "(在抢劫消息后追加数字，int)", "参数": ["int"]},
    "endAll": {"介绍": "(结束整个触发器组,bool)", "参数": ["bool"]},
    "endNumber": {"介绍": "(跳过编号为……的触发器，（编号从0开始），int)", "参数": ["int"]},
    "minCoin": {"介绍": "(最低保险金币改变……,int)", "参数": ["int"]},
    "delBuff": {"介绍": "(删除目标的buff,[int,int,float,str](目标[0自己,1敌方],模式[0非exbuff,1好buff,2debuff,3exbuff],附着度要求[正为高于,负为低于],模式[0随机选择,1全部删除,其他情况视为id指定删除]))", "参数": ["int", "int", "float", "str"]},
    "addBuff": {"介绍": "(添加buff,[int,str,[float,bool,float,int]](目标[0自己,1敌方],buffId,buff属性[附着度，是否锁定附着度，初始时长(s)，持续回合]))", "参数": ["int", "str", ["float", "bool", "float", "int"]]},
    "expGetPro": {"介绍": "(熟练度获取倍率[float,float,float][百分比，最低获得，最高获得])", "参数": ["float", "float", "float"]},
    "changeBuffSelf": {"介绍": "(改变buff的属性,[int,int,float,str,float,str](目标[0自己,1敌方]，模式[0非exbuff,1好buff,2debuff,3exbuff],附着度要求[正为高于,负为低于],模式[0随机选择,1全部改变,其他情况视为id指定改变],改变值,属性名(持续时间，附着度，剩余回合)))", "参数": ["int", "int", "float", "str", "float", "str"]},
    "proAW": {"介绍": "(比例改变主动权值,[int,float,float,float](目标[0自己,1敌方],改变比例，最低改变量，最高改变量))", "参数": ["int", "float", "float", "float"]},
    "proPW": {"介绍": "(比例改变被动权值,[int,float,float,float](目标[0自己,1敌方],改变比例，最低改变量，最高改变量))", "参数": ["int", "float", "float", "float"]},
    "proAttact": {"介绍": "(比例改变攻击力,[int,float,float,float](目标[0自己,1敌方],改变比例，最低改变量，最高改变量))", "参数": ["int", "float", "float", "float"]},
    "proTrueAttact": {"介绍": "(比例改变最终伤害值,[int,float,float,float](目标[0自己,1敌方],改变比例，最低改变量，最高改变量))", "参数": ["int", "float", "float", "float"]},
    "proDefense": {"介绍": "(比例改变防御力,[int,float,float,float](目标[0自己,1敌方],改变比例，最低改变量，最高改变量))", "参数": ["int", "float", "float", "float"]},
    "proSpeed": {"介绍": "(比例改变速度值,[int,float,float,float](目标[0自己,1敌方],改变比例，最低改变量，最高改变量))", "参数": ["int", "float", "float", "float"]},
    "addweatherSelfToAW": {"介绍": "(将天气属性的值加到主动权值内,[str(天气属性),int(0为自己，1为对方),float(倍率),float(最小量),float(最大量)])", "参数": ["str", "int", "float", "float", "float"]},
    "addweatherSelfToPW": {"介绍": "(将天气属性的值加到被动权值内,[str(天气属性),int(0为自己，1为对方),float(倍率),float(最小量),float(最大量)])", "参数": ["str", "int", "float", "float", "float"]},
    "miniItemNumChange": {"介绍": "(小道具数量改变,[int,str,int],(目标(0我1敌) 小道具名 改变数量(可以为负))))", "参数": ["int", "str", "int"]},
    "addGselfDvaLevel": {"介绍": "(增加查看属性的偏差等级,[int,int],(目标(0我1敌人),增加量))", "参数": ["int", "int"]},
    "noPrCoin": {"介绍": "(取消所有最低保险效果,(int,(目标(0我1敌))))", "参数": ["int"]},
    "canNotCountinue": {"介绍": "(终止该轮抢劫，并提示,str(提示内容))", "参数": ["str"]},
    "addLabelNumToTempNum": {"介绍": "(将目标所有装备的某标签数加到临时变量中,[int,str,str],(目标,标签名,临时变量名))", "参数": ["int", "str", "str"]},
    "SetNum": {"介绍": "(设置变量的值,(str,int))", "参数": ["str", "int"]},
    "NumAdd": {"介绍": "(变量增加,(str,int))", "参数": ["str", "int"]},
    "NumDec": {"介绍": "(变量减少,(str,int))", "参数": ["str", "int"]},
    "NumMul": {"介绍": "(变量乘以,(str,int))", "参数": ["str", "int"]},
    "NumDiv": {"介绍": "(变量除以,(str,int))", "参数": ["str", "int"]},
    "NumRound": {"介绍": "(变量保留到小数点后……位,(str,int))", "参数": ["str", "int"]},
    "DelNum": {"介绍": "(删除变量,(str))", "参数": ["str"]},
    "powerAdd": {"介绍": "能量增加((目标(0我1敌)),int)", "参数": ["int", "int"]},
    "noFreCost": {"介绍": "(本次抢劫不消耗次数,bool)", "参数": ["bool"]},

    "numChange-S": {"介绍": "(私有变量改变[int,str,int,float](目标，变量名，改变模式[0-保留……位小数 1-加 2-减 3-乘 4-除 5-取余 6-次方 7-整除 8-开方 9-赋值 10-取较大 11-取较小]，改变量))", "参数": ["int", "str", "int", "float"]},
    "newTempNum": {"介绍": "(新建临时变量，当整个触发器组运行完毕后就删除,[str,int](变量名，初始值))", "参数": ["str", "int"]},
    "tempNumChange": {"介绍": "(临时变量改变,[str,int,float](变量名，改变模式[0-保留……位小数 1-加 2-减 3-乘 4-除 5-取余 6-次方 7-整除 8-开方 9-赋值 10-取较大 11-取较小]，改变量))", "参数": ["str", "int", "float"]},
    "addEquRuneLevelToTN": {"介绍": "(将某装备符文词条等级添加到临时变量里,[int,str,str,str](目标,装备类型名,词条名,临时变量名))", "参数": ["int", "str", "str", "str"]},

    "newTempString": {"介绍": "(新建临时字符串，当整个触发器组运行完毕后就删除,[str,str](变量名，初始字符))", "参数": ["str", "str"]},
    "tempStringSlic": {"介绍": "(临时字符串切片，与Python切片格式一致,[str,int,int,int](变量名，起始下标，终止下标，步长))", "参数": ["str", "int", "int", "int"]},
    "tempStringAppend": {"介绍": "(临时字符串追加,在字符串后追加内容,[str,str](变量名，内容))", "参数": ["str", "str"]},
    "tempStringAppend2": {"介绍": "(临时字符串追加,在字符串后追加数值,[str,float](变量名，数值))", "参数": ["str", "int"]},
    "tempStringMbi": {"介绍": "(临时字符串自乘(翻倍),[str,int](变量名，数值))", "参数": ["str", "int"]},
    "appendEquNameToTs": {"介绍": "(将用户的装备名追加到临时字符串之后,[int,str,str](目标,变量名,装备类型))", "参数": ["int", "str", "str"]},
    "addTsSizeToTn": {"介绍": "(将临时字符串的长度添加到临时变量之中,[str,str](字符串名，变量名))", "参数": ["str", "str"]},

    "apStrToSelfString": {"介绍": "(将字符串追加到自己属性显示框,[str](字符串))", "参数": ["str"]},
    "apDigitToSelfString": {"介绍": "(将数字追加到自己属性显示框,[str](字符串))", "参数": ["float"]},
    "apProBarToSelfString": {"介绍": "(将浮点数[0~1]做成进度条追加到自己属性显示框,[str](字符串))", "参数": ["float"]},
    "apBalBarToSelfString": {"介绍": "(将两个数值做成平衡条追加到自己属性显示框,[str](字符串))", "参数": ["float", "float"]},

    "removeCard": {"介绍": "删除今日卡片,(目标,下标)", "参数": ["int", "int"]},
    "setEquUseTime": {"介绍": "标记装备技能使用时间(目标，装备名)", "参数": ["int", "str"]},
    "hpAdd": {"介绍": "目标血量改变,(目标,改变值,是否可在血量为0时触发),[int,int,bool]", "参数": ["int", "int", "bool"]},
    "hpMaxAdd": {"介绍": "目标血量上限改变,(目标,改变值),[int,int,bool]", "参数": ["int", "int", "bool"]},

    "changeTime": {"介绍": "BUFF专属 (当前buff时间改变…,int)", "参数": ["int"]},
    "changeRound": {"介绍": "BUFF专属 (当前buff回合改变…,int)", "参数": ["int"]},
    "changeDeep": {"介绍": "BUFF专属 (当前buff附着度改变…,int)", "参数": ["int"]},
    "addDeepToAW": {"介绍": "BUFF专属 (将附着度的值加到主动权值内,[int(0为自己，1为对方),float(倍率)])", "参数": ["int", "float"]},
    "decDeepToAW": {"介绍": "BUFF专属 (将附着度的值减到主动权值内,[int(0为自己，1为对方),float(倍率)])", "参数": ["int", "float"]},
    "addDeepToPW": {"介绍": "BUFF专属 (将附着度的值加到被动权值内,[int(0为自己，1为对方),float(倍率)])", "参数": ["int", "float"]},
    "decDeepToPW": {"介绍": "BUFF专属 (将附着度的值减到被动权值内,[int(0为自己，1为对方),float(倍率)])", "参数": ["int", "float"]},
    "addSelfToTempNum": {"介绍": "BUFF专属 (将某属性加到临时变量中,[str属性名(附着度),str临时变量名])", "参数": ["str", "str"]},

    "PushNewEventToSystem": {"介绍": "(新增抢劫事件进入系统,[int,int,str,str,str],(方向(0-正向发动一次抢劫,1-逆向发动一次抢劫),延迟时间,额外模式(模式之间用|隔开),己方额外触发组(jsonSugarCode),敌方额外触发组(jsonSugarCode)))", "参数": ["int", "int", "str", "str", "str"]},

    "ImoprtSgc": {"介绍": "(导入SugarCode文件编译并插入到该组触发组之后,[str,bool],(SugarCode名,是否允许有相同标签的SugarCode触发组被导入)", "参数": ["str", "bool"]},

    "pass": {"介绍": "打备注用的", "参数": ["str"]}
}
"""
SugarCode效果库
"""

needs = {
    "aim_lv": {"介绍": "(触发道具时，对面等级要求（正为最低，负为最高）,int)", "参数": ["int"]},
    "aim_pro": {"介绍": "(触发道具时，对面熟练度要求（正为最低，负为最高）,float)", "参数": ["float"]},
    "aim_coin": {"介绍": "(触发道具时，对面金币要求（正为最低，负为最高）,int)", "参数": ["int"]},
    "WeValueDiff": {"介绍": "(触发道具时，对面等级相对自己要求（正为高于，负为低于，含等于）,int)", "参数": ["int"]},
    "WeValueDiff2": {"介绍": "(触发道具时，对面等级相对自己要求（高于相对值1，低于相对值2，含等于）", "参数": ["int", "int"]},
    "randomNum": {"介绍": "(随机数（开始就生成，1~100）的要求（正为最低，负为最高）,int)", "参数": ["int"]},
    "proba": {"介绍": "(完全随机数（监测该条件时就生成）该条件为真的几率为……(0~100),int)", "参数": ["int"]},
    "needMode": {"介绍": "(触发道具必须在……模式下（str,主动/被动）)", "参数": ["str"]},
    "attactModeNeed": {"介绍": "(攻击模式需要……(bool:是否开启))", "参数": ["bool"]},
    "minCoin": {"介绍": "(最低金币量增加……，int)", "参数": ["int"]},
    "haveBuff": {"介绍": "(某Buff要求,[int,str,bool],(目标(0为自己，1为对方),buffId,True为有，False为没有))", "参数": ["int", "str", "bool"]},
    "buffLayerNeed": {"介绍": "(buff层数要求,[int,str,int,bool],(目标,buffID,层数要求(正为大于,负为小于),是否考虑等于情况))", "参数": ["int", "str", "int", "bool"]},
    "weightNeed": {"介绍": "(调用该触发器时，权值要求,[int,int,float,bool],(目标(0为自己,1为对方),权值(0为主动,1为被动),数值要求(正为大于，负为低于),是否考虑等于情况))", "参数": ["int", "int", "float", "bool"]},
    "equNeed": {"介绍": "(装备要求,[int,str,bool],(目标(0为自己,1为对方),装备名,(True为已装备,False为没装备)))", "参数": ["int", "str", "bool"]},
    "suitNeed": {"介绍": "(套装要求,[int,str,bool],(目标(0为自己,1为对方),装备名,(True为已装备,False为没装备)))", "参数": ["int", "str", "bool"]},
    "weatherNeed": {"介绍": "(天气要求,[str,bool],(天气名id(天气名),要求处于该天气为……))", "参数": ["str", "bool"]},
    "weatherLabelNeed": {"介绍": "(天气标签要求,[str,bool],(标签名，持有该标签为……))", "参数": ["str", "bool"]},
    "weatherSelfNeed": {"介绍": "(天气某属性要求,[str,int,int,bool],(属性名,数值,1-大于/2-小于,是否考虑等于))", "参数": ["str", "int", "int", "bool"]},
    "preTimeNeed": {"介绍": "(时间段要求,[str,bool],(当前处于(深夜/凌晨/早上&中午/下午&晚上)为(bool)))", "参数": ["str", "bool"]},
    "miniItemNeed": {"介绍": "(小道具要求,[int,str,int,bool],(目标(0我1敌) 小道具名 正为大于,负为小于 是否考虑等于情况))", "参数": ["int", "str", "int", "bool"]},
    "powerNeed": {"介绍": "(能量值要求,[int,float,bool])(目标,要求(正为高于,负为小于),是否考虑等于情况)", "参数": ["int", "float", "bool"]},
    "hpNeed": {"介绍": "(血量值要求,[int,float,bool])(目标,要求(正为高于,负为小于),是否考虑等于情况)", "参数": ["int", "float", "bool"]},
    "equRuneNeed": {"介绍": "某装备符文词条要求([int,str,str,bool](目标,装备名,符文词条名,是否拥有))", "参数": ["int", "str", "str", "bool"]},
    "equRuneLevelNeed": {"介绍": "(某装备符文词条等级要求(默认0),[int,str,str,int,bool](目标,装备类型名,词条名,词条等级要求(正为大于,负为小于),是否考虑等于情况))", "参数": ["int", "str", "str", "int", "bool"]},
    "equRuneStoneNeed": {"介绍": "某装备符文石要求([int,str,str,bool](目标,装备类型名,符文石名,是否拥有))", "参数": ["int", "str", "str", "bool"]},
    "equLabelNeed": {"介绍": "(某装备标签要求,[int,str,str,bool],(目标,装备类型名,标签名,是否拥有))", "参数": ["int", "str", "str", "bool"]},
    "equLabelNumNeed": {"介绍": "(目标装备标签数量要求,[int,str,int,bool],(目标,标签名,正为大于、负为小于,是否考虑等于情况))", "参数": ["int", "str", "int", "bool"]},


    "TimeNeed": {"介绍": "BUFF专属 (当前buff持续时间要求……(正为高于，负为低于),[int,bool])", "参数": ["int", "bool"]},
    "RoundNeed": {"介绍": "BUFF专属 (当前buff剩余回合要求……(正为高于，负为低于),[int,bool])", "参数": ["int", "bool"]},
    "DeepNeed": {"介绍": "BUFF专属 (当前Buff附着度要求……(正为高于，负为低于),[int,bool])", "参数": ["int", "bool"]},
    "cprNums": {"介绍": "BUFF专属 (数值比较,[float,float,int](值1，值2，0-小于/1-等于/2-大于/3-小于等于/4-大于等于/5-不等于))", "参数": ["float", "float", "int"]},

    "checkTempString": {"介绍": "(判断字符串的内容是否与目标字符串一致,[str,str](字符串，目标字符串))", "参数": ["str", "str"]},

    "fixEquNeed": {"介绍": "符文词条专属 (当前词条安装装备要求……(装备名,是/否),[str,bool])", "参数": ["str", "bool"]},
    "fixEquTypeNeed": {"介绍": "符文词条专属 (当前词条安装装备类型要求……(装备类型,是/否),[str,bool])", "参数": ["str", "bool"]},

    "pass": {"介绍": "打备注用的", "参数": ["str"]}
}
"""
SugarCode条件库
"""
