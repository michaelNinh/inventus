"""

How does the flow of logic work? 

Run "keyword search" 
-> Get a list of channels associated with keywords 
-> save these channel IDs into the database
 
run "get channel videos"
-> Return list of Video IDs associated with a channel
-> save these video IDs and associate them with a channel ID

run "video_statistics"
-> for each video ID available in the database 
-> if there are no available statistics, run function
-> get relevant information about video ID


On running statistics....
-> At the moment I am cutting out any outlier video performances...at some point it would be valuable to go back
and save outlier videos...look for trends on what works and doesn't
-> need to account for variance i.e. start saving standard deviations in DB
-> need to account for 'video favorites' for channel stats



TO DO:
- grab creator geographic data
- get category of videos
- approximate which vertical channel specializes is
=][
- need way for spreadsheet to talk to database
- overall channel performance statistics
- it is possible to pull category ID, on the video level
- skipping scraping of favorite number, problem with using Pandas, cannot convert NaN float into INT

"""
def test():
    d = {'a': 1}

    if 'b' in d:
        print('inside')
    else:
        print('not inside')


test()





