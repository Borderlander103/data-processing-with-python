import os
from ftplib import FTP, error_perm

ftp = FTP("ftp.pyclass.com")

print("hello world")

def ftpDownloader(stationID, startYear, endYear, host="ftp.pyclass.com", user="student@pyclass.com", password="student123"):
    ftp=FTP(host)
    ftp.login(user, password)
    print(ftp.nlst())
    if not os.path.exists("C:\\Users\\brichardson\\Catalyte\\DataEngineering_ADT\\DataProcessingWithPython\\weather-data"):
        os.makedirs("C:\\Users\\brichardson\\Catalyte\\DataEngineering_ADT\\DataProcessingWithPython\\weather-data")
    os.chdir("C:\\Users\\brichardson\\Catalyte\\DataEngineering_ADT\\DataProcessingWithPython\\weather-data")
    for year in range(startYear, endYear+1):
        fullpath = "/Data/%s/%s-%s.gz" % (year, stationID, year)
        filename = os.path.basename(fullpath)
        try:
            with open(filename, 'wb') as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
            print("%s has been successfully downloaded" % filename)
        except error_perm:
            print("%s is not available" % filename)
            os.remove(filename)
    ftp.close()

# ftpDownloader("010010-99999", 2010, 2014)

ids = ["010010-99999", "010014-99999", "010015-99999", "010020-99999"]

for name in ids:
    ftpDownloader(name, 2010, 2014)