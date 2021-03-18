import os 
import glob
import patoolib

def extractFiles(indir = "weather-data", out="extracted"):
    os.chdir(indir)
    archives = glob.glob("*.gz")
    if not os.path.exists(out):
        os.makedirs(out)
    files = os.listdir("extracted")
    for archive in archives:
        if archive[:-3] not in files:
            patoolib.extract_archive(archive, outdir = out)

extractFiles()