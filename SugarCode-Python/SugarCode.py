"""
该库包含了所有与SugarCode有关的操作
例如SugarCode的编译与反编译
dumps为将SugarCode反编译为json格式
loads为将标准json(SC)编译为SugarCode

————————————————————————————————————————————————————————————

SugarCode语法：

 · 用“@条件”表示一个新的触发器,且接下来的所有调用均为条件

 · 用“@效果”表示一个触发器条件的输入完毕，且接下来的所有调用均为效果

 · 用“>”表示一个新调用的开始

 · 用“|”表示调用的函数的参数的输入

 · 用“,”来隔开参数

 · 用“""”来表示一个文本类型，且允许换行

 · 用“T与F”表示一个布尔类型

 · 用“123这类普通数字”表示一个数字类型(支持小数)

 · 用“[]”来表示一个数据组

 · 用“#注释#”来表示一个注释

当文本内需要输入“"”时，用“反斜线+"”来表示

当参数只有一个时,允许不用[]将参数括起来

当参数不止一个时,必须用[]将参数括起来

————————————————————————————————————————————————————————————

SugarCode转化:
True->T
False->F
123->123

————————————————————————————————————————————————————————————

SugarCode实例：
@条件

    >needMode | "主动"

@效果

    >actWeight | 50
    
#以上效果将在模式为主动时触发#

@条件

    >needMode | "被动"

@效果

    >proPW | [0,1,0,100]

    >addBuff | [0,"燃烧1",[20,false,100,100]]

#以上效果将在模式为被动时触发#
"""
class SgcDumpError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message

from decimal import *
def dumps(sugarCodeS:str)->list:
    """
    编译SugarCode
    """
    codeS=[]
    antMode=False
    nowMode=""
    size=len(sugarCodeS)
    nowPmts=[]
    nowObj=[]
    nowName=""
    nowNode={"条件":[],"效果":[]}
    getName=False
    skipMode=True
    getPmt=False
    pmtType="未知"
    digit=0
    ngeMode=False
    minDigitDeep=1
    idx=-1
    def insertPmt(deep:int,obj:any)->None:
        nonlocal nowPmts
        aimList=nowPmts
        for i in range(deep):
            aimList=aimList[-1]
        aimList.append(obj)
    while idx<size-1:
        idx+=1
        try:
            if skipMode:
                if sugarCodeS[idx] in [" ","\n"]:
                    continue
                else:
                    skipMode=False
            if sugarCodeS[idx] == '#':
                antMode=not antMode
            elif antMode:
                continue
            elif getName :
                if sugarCodeS[idx] in [" ","\n","|"]:
                    getName=False
                    skipMode=True
                else:
                    nowName+=sugarCodeS[idx]
                if sugarCodeS[idx] == "|":
                    idx-=1
                
            elif sugarCodeS[idx] == "@" and idx<=size-3:
                #print(getPmt)
                if len(nowPmts)==1:
                    nowPmts=nowPmts[0]
                if nowName != "":
                    nowObj.append({"调用":nowName,"参数":nowPmts})
                nowPmts=[]
                getPmt=False
                if sugarCodeS[idx:idx+3] == "@条件":
                    if nowMode == "":
                        nowMode="条件"
                        nowObj=[]
                        skipMode=True
                    elif nowMode == "效果":
                        nowNode["效果"]=nowObj
                        codeS.append(nowNode)
                        nowObj=[]
                        nowMode="条件"
                        skipMode=True
                        nowNode={"条件":[],"效果":[]}
                elif sugarCodeS[idx:idx+3] == "@效果":
                    if nowMode == "":
                        nowMode="效果"
                        nowObj=[]
                        skipMode=True
                    elif nowMode == "条件":
                        nowNode["条件"]=nowObj
                        nowMode="效果"
                        nowObj=[]
                        skipMode=True
                #print(getPmt)
            elif sugarCodeS[idx] == ">":
                getPmt=False
                if len(nowPmts):
                    if len(nowPmts)==1:
                        nowPmts=nowPmts[0]
                    nowObj.append({"调用":nowName,"参数":nowPmts})
                nowPmts=[]
                nowName=""
                getName=True
                skipMode=True

            elif getPmt:
                #print("ISpmt")
                
                if sugarCodeS[idx].isdigit() or sugarCodeS[idx]=="-":
                    #print("isdigit")
                    ngeMode=False
                    digit=Decimal(0)
                    minDigitDeep=1
                    minDigitMode=False
                    if sugarCodeS[idx]=="-":
                        ngeMode=True
                        idx+=1
                    while idx<=size-1 and (sugarCodeS[idx].isdigit() or sugarCodeS[idx]=="."):
                        if sugarCodeS[idx].isdigit():
                            if minDigitMode:
                                digit+=Decimal(int(sugarCodeS[idx]))*(Decimal('0.1')**minDigitDeep)
                                minDigitDeep+=1
                            else:
                                digit=digit*10+Decimal(int(sugarCodeS[idx]))
                        else:
                            minDigitMode=True
                        idx+=1
                    if ngeMode:
                        digit=-digit
                    insertPmt(pmtDeep,float(digit))
                elif sugarCodeS[idx]=='"':
                    string=""
                    idx+=1
                    while idx<=size-1 and (sugarCodeS[idx]!='"' or sugarCodeS[idx-1]=='\\'):
                        if sugarCodeS[idx]=='"' and sugarCodeS[idx-1]=="\\":
                            string=string[0:-1]
                        string+=sugarCodeS[idx]
                        idx+=1
                    insertPmt(pmtDeep,string)
                elif sugarCodeS[idx]=="T":
                    insertPmt(pmtDeep,True)
                elif sugarCodeS[idx]=="F":
                    insertPmt(pmtDeep,False)
                elif sugarCodeS[idx]=="[":
                    if pmtDeep!=-1:
                        insertPmt(pmtDeep,[])
                    pmtDeep+=1
                elif sugarCodeS[idx]=="]":
                    pmtDeep-=1
                elif sugarCodeS[idx]=="." and pmtType=="数字":
                    pmtType="小数"
                    minDigitDeep=1
                elif idx==size-1 or not sugarCodeS[idx+1]==",":
                    pmtType="未知"
                skipMode=True
            elif sugarCodeS[idx] == "|":
                nowPmt=""
                getPmt=True
                skipMode=True
                pmtDeep=0
                tempIdx=idx+1
                while sugarCodeS[tempIdx] in [" ","\n"]:
                    tempIdx+=1
                #print(f"“{sugarCodeS[tempIdx]}”")
                if sugarCodeS[tempIdx]=="[":
                    pmtDeep=-1
        except:
            raise SgcDumpError(f"SugarCode编译异常！错误出现在第[{idx+1}]字符“{sugarCodeS[idx]}”") from None
    if len(nowPmts)==1:
        nowPmts=nowPmts[0]
    nowObj.append({"调用":nowName,"参数":nowPmts})
    nowNode["效果"]=nowObj
    codeS.append(nowNode)
    return codeS

def loads(sugarCode:list)->str:
    """
    反编译SugarCode
    """
    codeS=[]
    for group in sugarCode:
        codeS.append("@条件")
        for node in group["条件"]:
            codeS.append(f"    >{node['调用']} | {load(node['参数'])}")
        codeS.append("@效果")
        for node in group["效果"]:
            codeS.append(f"    >{node['调用']} | {load(node['参数'])}")
        codeS.append("")
    return "\n".join(codeS)

def load(obj:any)->str:
    """
    将单个对象编译为SugarCode格式
    """
    if type(obj) == type([]):
        return (f"[{','.join(list(map(load,obj)))}]")
    elif type(obj) == type(""):
        string='\\\"'.join(obj.split("\""))
        return f'"{string}"'
    elif type(obj) == type(True):
        return "T" if obj else "F"
    elif type(obj) == type(123) or type(obj) == type(1.1):
        return f"{obj}"
    
def CheckCFQZ(CFQ:list)->bool:
    """
    监测一个列表是否满足SugarCode列表条件
    """
    if type(CFQ)!=type([]): return False
    for i in CFQ:
        if type(i)!=type({}): return False
        if "条件" not in i or "效果" not in i: return False
        if type(i["条件"])!=type([]) or type(i["效果"])!=type([]): return False
        for j in i["条件"]:
            if type(j)!=type({}): return False
            if "调用" not in j or "参数" not in j: return False
        for j in i["效果"]:
            if type(j)!=type({}): return False
            if "调用" not in j or "参数" not in j: return False
    return True