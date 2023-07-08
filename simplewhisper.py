import whisper
import os

outputFile = open(r"transcriptionOutput.txt","a+")
#this script allows the user to specify the whisper model used during the transcription process. by default, it is set to 'small'. while more accurate, the larger models ('medium, large, large_v2') are far more resource intensive and require a substantial amount of memory.
#to select a single file to transcribe, uncomment the following three lines, and specify a filepath in the transcribe()method.

#model = whisper.load_model("small")
#result = model.transcribe("testaudio.m4a")
#print(result["text"])

# to transcribe a batch of audio files, and output them into a single text file, with tags to represent the filename the transcription originated from, uncomment the following 9 lines, and specify a directory path within the listdir() method.
for x in os.listdir("clips"):
     if x.endswith(".mp3"):
         model = whisper.load_model("large")
         result = model.transcribe("clips/" + x)
         outputStr = result["text"]
         outputFile.write("Transcription result from file: " + x + " : " + "\n")
         outputFile.write(outputStr)
         outputFile.write("\n")
         print(result["text"])
