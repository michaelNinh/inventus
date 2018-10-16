import sqlite3
import json


"""
- add the data colm to the correct table
- for each creator, get the last recorded video
- date_last_video = date last recorded

"""

def get_all_creatorIds():
    """
    gets all the creator IDs that we have recorded

    :return:
    array of STR, creatorIds
    """
    connection = sqlite3.connect('core.db')
    c = connection.cursor()
    #
    c.execute(
        """
        SELECT creatorID
        FROM creator_stats
        """
    )
    creatorIdArray = []
    masterCreatorIdList = c.fetchall()
    for tupleItem in masterCreatorIdList:
        creatorIdArray.append(tupleItem[0])
    return creatorIdArray


def get_last_video_recorded_date(masterCreatorList):
    """
    given a creatorId, find when the last video was recorded
    :param masterCreatorList: [creatorId(Str)]
    :return: [creatorId (STR), date_last_video(STR)]
    """

    idAndDateArray = []

    connection = sqlite3.connect('core.db')
    c = connection.cursor()

    for creatorId in masterCreatorList:
        creatorIdTuple = (creatorId,)

        # this code gets the last recorded date
        c.execute("""
                        SELECT * FROM video
                        WHERE creatorID = ?
                        """, creatorIdTuple)
        try:
            getDate = c.fetchall()[0]
            lastVideoDate = getDate[2].split('T')[0]
            print(lastVideoDate)
            idAndDateArray.append([creatorId, lastVideoDate])
        except IndexError:
            lastVideoDate = 'no date'
            print('no date')
            idAndDateArray.append([creatorId, lastVideoDate])
        # end code block

    connection.commit()
    connection.close()

    return idAndDateArray


def updateCreatorStatsWithDate(creatorDatePairings):
    """
    given an array of arrays containing creatorId + Date, update into the DB
    :param creatorDatePairings: [[creatorId(str), date(str)]]
    :return: None
    """

    connection = sqlite3.connect('core.db')
    c = connection.cursor()

    for pairing in creatorDatePairings:
        creatorId = pairing[0]
        lastDate = pairing[1]

        c.execute("""
                UPDATE creator_stats
                SET date_last_video = ?
                WHERE creatorId = ?
                """, (lastDate, creatorId))

        print("updating" + " " + creatorId)

    connection.commit()
    connection.close()





allCreatorIds = get_all_creatorIds()
masterPairings = get_last_video_recorded_date(allCreatorIds)
updateCreatorStatsWithDate(masterPairings)


