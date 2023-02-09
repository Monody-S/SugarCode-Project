"""
该库包含了所有与SugarCode有关的操作
例如SugarCode的编译与反编译
dumps为将SugarCode反编译为json格式
loads为将标准json(SC)编译为SugarCode
详细内容见https://github.com/Monody-S/SugarCode-Project/tree/main/SugarCode-Python
————————————————————————————————————————————————————————————

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
def dumps(
        sugarCodeS:str,
        noCondition:bool=False,
        cdKeyword:str="条件",
        ectKeyword:str="效果",
        outSring1:str="调用",
        outSring2:str="参数"
    )->list:
    """
    编译SugarCode
     · noCondition - 无条件
     · cdKeyword   - 条件关键词
     · ectKeyword  - 效果关键词
     · outSring1   - 输出关键词1
     · outSring2   - 输出关键词2
    """
    codeS=[]
    antMode=False
    nowMode=""
    size=len(sugarCodeS)
    nowPmts=[]
    nowObj=[]
    nowName=""
    nowNode={cdKeyword:[],ectKeyword:[]}
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
            elif sugarCodeS[idx] == "@":
                #print(getPmt)
                if len(nowPmts)==1:
                    nowPmts=nowPmts[0]
                if nowName != "":
                    nowObj.append({outSring1:nowName,outSring2:nowPmts})
                nowPmts=[]
                getPmt=False
                if idx+len(cdKeyword)<size and sugarCodeS[idx:idx+len(cdKeyword)+1] == f"@{cdKeyword}":
                    if nowMode == "":
                        nowMode=cdKeyword
                        nowObj=[]
                        skipMode=True
                    elif nowMode == ectKeyword:
                        nowNode[ectKeyword]=nowObj
                        codeS.append(nowNode)
                        nowObj=[]
                        nowMode=cdKeyword
                        skipMode=True
                        nowNode={cdKeyword:[],ectKeyword:[]}
                elif idx+len(ectKeyword)<size and sugarCodeS[idx:idx+len(ectKeyword)+1] == f"@{ectKeyword}":
                    if nowMode == "":
                        nowMode=ectKeyword
                        nowObj=[]
                        skipMode=True
                    elif nowMode == cdKeyword:
                        nowNode[cdKeyword]=nowObj
                        nowMode=ectKeyword
                        nowObj=[]
                        skipMode=True
                #print(getPmt)
            elif sugarCodeS[idx] == ">":
                getPmt=False
                if len(nowPmts):
                    if len(nowPmts)==1:
                        nowPmts=nowPmts[0]
                    nowObj.append({outSring1:nowName,outSring2:nowPmts})
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
                    insertPmt(pmtDeep,float(digit) if minDigitMode else int(digit))
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
    nowObj.append({outSring1:nowName,outSring2:nowPmts})
    nowNode[ectKeyword]=nowObj
    codeS.append(nowNode)
    if noCondition:
        temp=[]
        for group in codeS:
            temp+=group[ectKeyword]
        return temp
    return codeS

def loads(
        sugarCode:list,
        indent:int=4,
        noCondition:bool=False,
        cdKeyword:str="条件",
        ectKeyword:str="效果",
        inSring1:str="调用",
        inSring2:str="参数"
    )->str:
    """
    反编译SugarCode
     · indent      - 首行缩进[0,+∞)
     · noCondition - 无条件
     · cdKeyword   - 条件关键词
     · ectKeyword  - 效果关键词
     · inSring1    - 输入关键词1
     · inSring2    - 输入关键词2
    """
    codeS=[]
    for group in sugarCode:
        codeS.append(f"@{cdKeyword}")
        if not noCondition:
            for node in group[cdKeyword]:
                codeS.append(f"{' '*indent}>{node[inSring1]} | {load(node[inSring2])}")
        codeS.append(f"@{ectKeyword}")
        for node in group[ectKeyword]:
            codeS.append(f"{' '*indent}>{node[inSring1]} | {load(node[inSring2])}")
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
    
def CheckSgcList(
        sgcList:list,
        cdKeyword:str="条件",
        ectKeyword:str="效果",
        inSring1:str="调用",
        inSring2:str="参数"
    )->bool:
    """
    监测一个列表是否满足SugarCode列表条件
     · cdKeyword   - 条件关键词
     · ectKeyword  - 效果关键词
     · inSring1    - 输入关键词1
     · inSring2    - 输入关键词2
    """
    if type(sgcList)!=type([]): 
        return False
    
    for i in sgcList:

        if type(i)!=type({}): 
            return False
        if cdKeyword not in i or ectKeyword not in i: 
            return False
        if type(i[cdKeyword])!=type([]) or type(i[ectKeyword])!=type([]): 
            return False
        
        for j in i[cdKeyword]+i[ectKeyword]:
            if type(j)!=type({}): 
                return False
            if inSring1 not in j or inSring2 not in j: 
                return False
            if type(j[inSring1]) != type(str):
                return False
            
    return True