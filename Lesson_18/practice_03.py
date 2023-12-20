# Lesson 18 Classwork; Task 3

# Створіть клас Link, який представляє посилання на веб-сторінку. Кожне посилання має атрибути: URL, назва та опис.
# Знайдіть самостійно потрібний магічний метод і перепишіть його, щоб можна було порівнювати посилання на основі URL.

class Link:
    def __init__(self, URL, name, description):
        self.URL = URL
        self.name = name
        self.description = description

    def __eq__(self, other):
        if self.URL == other.URL:
            return 'True'
        else:
            return 'False'
        
page_1 = Link('http://google.com', 'Google', 'Search engine')
page_2 = Link('http://google.com', 'Google', 'Search engine')
print(page_1==page_2)