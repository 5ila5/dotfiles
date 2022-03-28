import asyncio
from libqtile.log_utils import logger
import subprocess

rolloPosToSet = -1
def getRolloPos():
    if rolloPosToSet != -1:
        return str(rolloPosToSet)
    result = subprocess.check_output(["python", "/home/silas/.config/qtile/mywidget/rollo.py","get"],encoding='utf8')
    #logger.warning(result)
    return str(result).replace("\n","")


async def changeRollo(val):
    global rolloPosToSet
    #logger.error("test")
    logger.error("changeRollo rolloPos ")
     
    logger.error(str(rolloPosToSet))
    logger.error("val:")
    logger.error(str(val))
    if rolloPosToSet == -1:
        logger.error("in if")
        toSet = int(getRolloPos())

    else:
        logger.error("in else")
        toSet = rolloPosToSet
   

    logger.error("getRolloPos(): "+str(getRolloPos()) + " as int:" + str(int(getRolloPos())))
    logger.error("toSet before add:"+str(toSet))
    toSet+=val

    logger.error("toSet after add:"+str(toSet))
    
    if toSet<0 or toSet > 100:
        logger.error("toSet ("+str(toSet)+") out of scope returning")
        return
   
    
    logger.error("rolloPosToSet")

    logger.error(str(rolloPosToSet))
    rolloPosToSet = toSet
    await asyncio.sleep(1)
    logger.error(str(rolloPosToSet))

    logger.error(str(rolloPosToSet==toSet))
    if rolloPosToSet == toSet:
        result = subprocess.check_output(["python", "/home/silas/.config/qtile/mywidget/rollo.py","set", str(rolloPosToSet)],encoding='utf8')
    
    rolloPosToSet = -1

def increseRollo():
    logger.error("increseRollo")
    global rolloPosToSet
    logger.error("1")
    logger.error(str(rolloPosToSet))
    logger.error("2")
    asyncio.create_task(changeRollo(5))


def decreseRollo():
    global rolloPosToSet
    logger.error("decreseRollo")
    asyncio.create_task(changeRollo(-5))