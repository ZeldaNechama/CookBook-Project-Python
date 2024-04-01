from datetime import datetime


class DownloadBook:
    def __init__(self):
        """Models a recipe book"""

    def createFileBook(self, book, respeiBookName):
        """"Creates a recipe book from all recipes in data and downloads it to file """
        srtFromList = ""
        for recepei in book:
            srtFromList = srtFromList + recepei + "\n"

        # uses a outside library
        today = str(datetime.now())

        srtFromList += "\n" + 'recipeBook was downloaded on:' + today

        bookFile = open(f"{respeiBookName}.txt", 'w')
        bookFile.write(srtFromList)
        bookFile.close()
