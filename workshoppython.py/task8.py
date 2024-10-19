#open file and count the number 

input_file="C:/Users/toka_/Desktop/AMIT/advanced_machine_learning_course_Amit/workshoppython.py/test.txt"
def file_read(input_file):
    #input_file = open("input_file.txt", "r")
    text = input_file.read()
    input_file.close()
    text = text.replace('\n', ' ')
    words = text.split(' ')
    unique_words = set(words)
    word_counts = {word: 0 for word in unique_words}
    for i in unique_words:
        for j in words:
            if i == j:
                word_counts[i] += 1
                output_file = open("C:/Users/toka_/Desktop/AMIT/advanced_machine_learning_course_Amit/workshoppython.py/output.txt", "w")
                for word in word_counts:
                    output_file.write("{}: {}\n".format(word, word_counts[word]))
                    output_file.close()

file_read(input_file)