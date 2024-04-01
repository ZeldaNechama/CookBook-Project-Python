class Recepee:
    """Models the Items in a recipe"""

    def __init__(self, preperationtime, difficullty, isDyatic, type, recepeeName, ingredient1, ingredient2, ingredient3,
                 ingredient4, ingredient5):
        self.preperationtime = preperationtime
        self.isDyatic = isDyatic
        self.difficullty = difficullty
        self.type = type
        self.recepeeName = recepeeName
        self.ingredients = {
            "ingredient1": {ingredient1}, "ingredient2": {ingredient2}, "ingredient3": {ingredient3},
            "ingredient4": {ingredient4}, "ingredient5": {ingredient5}
        }

    def isDyatic(self):
        """Return true if recepei is dyatic or fakse if it's not"""
        if self.isDyatic == 'true':
            return 'true'
        else:
            return 'false'

    def whatType(self):
        """Return which type is the recepie if:pareve,dairy or meat"""
        if self.type == 'p':
            return 'Pareve'
        elif self.type == 'd':
            return 'dairy'
        else:
            return 'Meet'

    def showIngredients(self):
        """Shows all ingredients of an recipei"""
        print(f"Your Receipe:{self.recepeeName}  Ingredients: {self.ingredients}")


class RecepeiBook:
    """Modles a book of recepies acorfing to categories"""

    def __init__(self):
        self.book = {
            "cakesAndCookeis": [
                Recepee(recepeeName='choclateChipCookeis', difficullty='easy', isDyatic='false', type='p',
                        preperationtime=30, ingredient1='flour', ingredient2='oil', ingredient3='choclateChip',
                        ingredient4='bakingPowder', ingredient5='suger'),
                Recepee(recepeeName='', difficullty='easy', isDyatic='false', type='p', preperationtime=30,
                        ingredient1='flour', ingredient2='oil', ingredient3='choclateChip', ingredient4='bakingPowder',
                        ingredient5='suger'),
                Recepee(recepeeName='VenileCake', difficullty='hard', isDyatic='false', type='d', preperationtime=60,
                        ingredient1='flour', ingredient2='oil', ingredient3='vanilaPuding', ingredient4='milk',
                        ingredient5='suger'),
                Recepee(recepeeName='saltyCookeis', difficullty='easy', isDyatic='true', type='p', preperationtime=25,
                        ingredient1='flour', ingredient2='oil', ingredient3='salt', ingredient4='water',
                        ingredient5='sesmeeiseeds')
            ],
            "dessrets": [

                Recepee(recepeeName='Orio IceCream', difficullty='easy', isDyatic='false', type='m', preperationtime=15,
                        ingredient1='orio cookeis', ingredient2='milk', ingredient3='suger', ingredient4='shament',
                        ingredient5='considerate milk'),
                Recepee(recepeeName='sofflee', difficullty='hard', isDyatic='false', type='p',
                        preperationtime=30,
                        ingredient1='flour', ingredient2='oil', ingredient3='choclate', ingredient4='bakingPowder',
                        ingredient5='suger'),
                Recepee(recepeeName='StrawberyBannasheike', difficullty='hard', isDyatic='true', type='p',
                        preperationtime=120,
                        ingredient1='strawbries', ingredient2='mapel', ingredient3='water', ingredient4='banana',
                        ingredient5='walnuts')
            ]
        }

    def getAllRecepies1(self):
        """Returns all Names of recepies"""
        listR = []
        for category, recipes in self.book.items():
            for value in recipes:
                print(value.recepeeName)
                listR.append(value.recepeeName)
        return listR

    def getAllRecepies(self):
        """Returns all Names of recepies"""
        for category, recipes in self.book.items():
            for value in recipes:
                print(value.recepeeName)
                value.showIngredients()

    def addRecepei(self, category, preperationtime, difficullty, isDyatic, type, recepeeName, ingredient1,
                   ingredient2,
                   ingredient3,
                   ingredient4, ingredient5):
        """Adds a recepei to the recepeiBook acour"""
        re = Recepee(preperationtime=preperationtime, difficullty=difficullty, isDyatic=isDyatic,
                     recepeeName=recepeeName, type=type, ingredient1=ingredient1,
                     ingredient2=ingredient2, ingredient3=ingredient3, ingredient4=ingredient4,
                     ingredient5=ingredient5)
        """Adds according to type  a new recipe"""
        self.book[category].append(re)


    def getRecepiesByDifficulty(self, difficulty):
        """Returns a list of all the recipes sorted by difficulty level using lambda"""
        resepies = []
        for catagory, resepei in self.book.items():
            resepies.extend(filter(lambda r: r.difficullty == difficulty, resepei))

        return resepies

    def getRecepiesByRequiremets(self, difficulty, type, isDyatic, preperationtime):
        """Returns a list of all the recipes sorted by difficulty level using lambda"""
        resepies = []
        for catagory, resepei in self.book.items():
            resepies.extend(filter(lambda
                                       r: r.difficullty == difficulty and r.type == type and r.isDyatic == isDyatic and t.preperationtime == preperationtime,
                                   resepei))

        return resepies
