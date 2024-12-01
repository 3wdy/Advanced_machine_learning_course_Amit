class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            with open(self.file_path, 'r') as f:
                self.file = f.readlines()
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            self.file = []

    def count_lines(self):
        return len(self.file)

    def count_words(self):
        count = 0
        for line in self.file:
            count += len(line.split())
        return count

    def count_characters(self):
        count = 0
        for line in self.file:
            count += len(line)
        return count

    def display_content(self):
        for line in self.file:
            print(line, end='')

if __name__ == '__main__':
    tf = TextFileReader(r'D:\AMIT\Tasks\Task_4\FileInfo.txt')
    print("Number of lines = " + str(tf.count_lines()))
    print("Number of words = " + str(tf.count_words()))
    print("Number of characters = " + str(tf.count_characters()))
    tf.display_content()
