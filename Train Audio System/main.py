import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def texttoSpeech(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext,lang=language, slow=False)
    myobj.save(filename)

#Func. return pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('mp3.mpeg')
    #1.Generate Kripya dhayaande dijiye
    start = 31000
    finish = 32800 
    audioProcessed = audio[start:finish]
    audioProcessed.export('1_hindi.mp3', format="mp3")
    

    # 3- Generate se chalkar
    start = 36800
    finish = 37520 
    audioProcessed = audio[start:finish]
    audioProcessed.export('3_hindi.mp3', format="mp3")

    

    #5. Generate ke rastestart = 31000
    finish = 32800 
    audioProcessed = audio[start:finish]
    audioProcessed.export('5_hindi.mp3', format="mp3")

    
    #7.Generate -ko  jaane wali gaadi sankya
    start = 120000
    finish = 121000 
    audioProcessed = audio[start:finish]
    audioProcessed.export('7_hindi.mp3', format="mp3")

    

    #9 Generate Kuch hi samay mai platform no.
    start = 31000
    finish = 32800 
    audioProcessed = audio[start:finish]
    audioProcessed.export('9_hindi.mp3', format="mp3")

    
    #11.par aarahi hai
    
    start = 31000
    finish = 32800 
    audioProcessed = audio[start:finish]
    audioProcessed.export('11_hindi.mp3', format="mp3")

    

def generateAnnouncement(filename):
    df = pd.read_csv(r"F:\Data\Codes\Projects\Python Projects\Train Audio System\All_Indian_Trains.csv")
    df.head()
    print(df)
        
    for index, item in df.iterrows():
        #2 Generate FROM-CITY
        texttoSpeech(item['From'],'2_hindi.mp3')   

        #4.Generate Via City
        texttoSpeech(item['Station Name'],'4_hindi.mp3')

        #6.Generate to citystart
        texttoSpeech(item['To'],'6_hindi.mp3')

        #8.Generate Train no. and Name
        texttoSpeech(item['Train No.']+" "+ item['train Name'],'8_hindi.mp3')

        #10.Generate platform no.
        texttoSpeech(item['islno'],'10_hindi.mp3')
        for i in range(1,12):
            audios = [f"i_hindi.mp3"]
        return audios

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['Train No']}_{index+1}.mp3", format = "mp3")


if __name__ =="__main__":
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("All_Indian_Trains.csv")

