# -*- coding: utf-8 -*-
"""
txt to csv


usage:
    python3 _data/raw/txt_2_csv.py


rich text to markdown"
    https://euangoddard.github.io/clipboard2markdown/

"""

import os  # for os.listdir
import csv # for csv.writer


class Article:
    """
    simple article class
    """

    __HEADERS = ["categories", "others"] + ["section", "index", "title", "src", "authur", "demo_src"]

    def __init__(self, line, section):
        self.section = section
        # 2\. [title](src), authur [demo code](demo_src)\
        self.index, line = self.slice(line, '.', None, -1, 1, None)
        # [title](src), authur [demo code](demo_src)\
        self.title, line = self.slice(line, ']', 1, None, 1, None)
        # (src), authur [demo code](demo_src)\
        self.src, line = self.slice(line, ')', 1, None, 2, None)
        if "demo" in line:
            # authur [demo code](demo_src)\
            self.authur, line = self.slice(line, '[', None, None, None, None)
            # [demo code](demo_src)\
            _, line = self.slice(line, '(', None, None, None, None)
            # (demo_src)\
            self.demo_src, _ = self.slice(line, ')', 1, None, None, None)
        else:
            # authur\
            self.authur = line
            self.demo_src = ""
        # authur\
        if self.authur.endswith("\\"):
            self.authur = self.authur[:-1]
        # print(str(self))

    def __str__(self):
        return str(self.to_csv())

    def to_csv(self):
        result = []
        for i in self.__HEADERS:
            result.append(getattr(self, i, ""))
        return result

    @staticmethod
    def to_csv_header():
        return Article.__HEADERS

    @staticmethod
    def slice(str, chr, a=None, b=None, c=None, d=None):
        index = str.find(chr)
        left = str[0:index].strip()
        right = str[index:].strip()
        return (left[a:b].strip(), right[c:d].strip())


class Txt2Csv:
    """
    Txt2Csv
    """

    def __init__(self):
        self.current_section = ""
        self.articles = []
        self.csv = []

    def main(self):
        """to csv"""
        print("hello world!")

    def read(self, file_path):
        """read txt"""
        with open(file_path, "r", encoding="utf-8") as txt_file:
            for line in txt_file:
                if line.startswith("Section"):
                    self.current_section = line.split(':')[1].strip()
                    # print(self.current_section)
                elif line.startswith("-") or line == "\n":
                    pass
                else:
                    article = Article(line, self.current_section)
                    self.articles.append(article)
        return self

    def to_csv(self):
        self.csv = map(lambda x: x.to_csv(), self.articles)
        return self

    def write(self, file_path):
        with open(file_path, 'w') as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            write.writerow(Article.to_csv_header())
            write.writerows(self.csv)
        return self


if __name__ == "__main__":
    SRC_FOLDER = "_data/raw/"
    DES_FOLDER = "_data/"

    for file in os.listdir(SRC_FOLDER):
        if file.endswith(".txt"):
            txt_2_csv = Txt2Csv()
            txt_2_csv.read(SRC_FOLDER+file)
            txt_2_csv.to_csv()
            txt_2_csv.write(DES_FOLDER+file.replace(".txt", ".csv"))
