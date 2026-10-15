#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Intelligent Text Analyzer

print("Welcome to Intelligent Text Analyzer!")
print("Enter your text below:")

text = input("> ")

print("\nYour text has been received successfully.")
print("\nYour text:")
print(text) 


# In[2]:


# Step 1: Basic Text Analysis 
words = text.split()
word_count = len(words) 
character_count = len(text) 
character_count_no_spaces = len("".join(text.split())) 
sentence_count = text.count(".") + text.count("!") + text.count("?")
print("\n--- Text Analysis Report ---")
print("Total words:", word_count)
print("Total characters:", character_count)
print("Characters without spaces:", character_count_no_spaces)
print("Total sentences:", sentence_count) 


# In[3]:


# Step 2: Word Frequency Analysis 
clean_text = text.lower()
for symbol in ".,!?;:":
    clean_text = clean_text.replace(symbol, "")
words = clean_text.split()
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print("\n--- Word Frequency Report ---")
for word, count in word_frequency.items():
    print(word, ":", count) 


# In[4]:


# Step 3: Rank Words by Frequency 
sorted_words = sorted(
    word_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)
print("\n--- Most Frequent Words ---")
for word, count in sorted_words:
    print(f"{word}: {count}") 


# In[5]:


# Step 4: Compare Two Texts
text_2 = input("Enter a second text to compare: ")
def get_words(text):
    text = text.lower()
    for symbol in ".,!?;:":
        text = text.replace(symbol, "")
    return set(text.split())
words_1 = get_words(text)
words_2 = get_words(text_2)
common_words = words_1.intersection(words_2)
all_words = words_1.union(words_2)
if all_words:
    similarity = len(common_words) / len(all_words) * 100
else:
    similarity = 0
print("\n--- Text Comparison Report ---")
print("Common words:", sorted(common_words))
print("Number of common words:", len(common_words))
print(f"Word similarity: {similarity:.2f}%") 


# In[6]:


# Step 5: Find Repeated Words
repeated_words = {}
for word, count in word_frequency.items():
    if count > 1:
        repeated_words[word] = count
print("\n--- Repeated Words Report ---")
if repeated_words:
    for word, count in repeated_words.items():
        print(f"{word}: {count} times")
else:
    print("No repeated words found.") 


# In[7]:


# Step 6: Final Analysis Report 
print(chr(10) + chr(61) * 35)
print("INTELLIGENT TEXT ANALYZER")
print(chr(61) * 35)

print(chr(10) + "1. BASIC STATISTICS")
print("Total words:", len(text.split()))
print("Total characters:", len(text))
print("Characters without spaces:", len("".join(text.split()))) 
print("Total sentences:", text.count(".") + text.count("!") + text.count("?"))

print(chr(10) + "2. TOP 3 MOST FREQUENT WORDS")
for word, count in sorted_words[:3]:
    print(word + ": " + str(count))

print(chr(10) + "3. REPEATED WORDS")
if repeated_words:
    for word, count in repeated_words.items():
        print(word + ": " + str(count) + " times")
else:
    print("No repeated words found.")

print(chr(10) + "4. TEXT COMPARISON")
print("Common words:", ", ".join(sorted(common_words)))
print("Word similarity:", str(round(similarity, 2)) + "%")

print(chr(10) + chr(61) * 35)
print("Analysis completed successfully!")
print(chr(61) * 35) 


# In[8]:


# Step 7: Keyword Analysis

stop_words = {
    "is", "am", "are", "the", "a", "an", "and",
    "in", "on", "of", "to", "for", "i", "it",
    "my", "me", "because", "this", "that", "with"
}

keywords = []

for word, count in sorted_words:
    if word not in stop_words:
        keywords.append((word, count))

print("\n--- KEYWORD ANALYSIS ---")

if keywords:
    for word, count in keywords[:5]:
        print(word + ": " + str(count))
else:
    print("No keywords found.") 


# In[9]:


# Step 8: Unique Words and Longest Word

words = text.split()
clean_words = []

for word in words:
    word = word.lower()

    for symbol in ".,!?;:()":
        word = word.replace(symbol, "")

    if word:
        clean_words.append(word)

unique_words = set(clean_words)

print("\n--- WORD ANALYSIS ---")
print("Total words:", len(clean_words))
print("Unique words:", len(unique_words))

if clean_words:
    longest_word = max(clean_words, key=len)
    print("Longest word:", longest_word)
    print("Length of longest word:", len(longest_word))
else:
    print("No words found.") 


# In[10]:


# Step 9: Interactive Menu

print("\n===== INTELLIGENT TEXT ANALYZER =====")
print("1. Basic Text Statistics")
print("2. Word Frequency")
print("3. Keyword Analysis")
print("4. Unique Words and Longest Word")
print("5. Compare Two Texts")

choice = input("\nChoose an option (1-5): ")

if choice == "1":
    print("\nTotal words:", len(text.split()))
    print("Total characters:", len(text))
    print("Total sentences:", text.count(".") + text.count("!") + text.count("?"))

elif choice == "2":
    for word, count in sorted_words:
        print(word, ":", count)

elif choice == "3":
    for word, count in keywords[:5]:
        print(word, ":", count)

elif choice == "4":
    print("Unique words:", len(unique_words))
    if clean_words:
        print("Longest word:", max(clean_words, key=len))

elif choice == "5":
    print("Common words:", ", ".join(sorted(common_words)))
    print("Word similarity:", str(round(similarity, 2)) + "%")

else:
    print("Invalid choice. Please select a number from 1 to 5.") 


# In[11]:


# Step 10: Save Analysis Report

report = "INTELLIGENT TEXT ANALYZER\n"
report += "=" * 30 + "\n"
report += "Total words: " + str(len(text.split())) + "\n"
report += "Total characters: " + str(len(text)) + "\n"
report += "Unique words: " + str(len(unique_words)) + "\n"

if clean_words:
    longest_word = max(clean_words, key=len)
    report += "Longest word: " + longest_word + "\n"

report += "\nWord Frequency:\n"

for word, count in sorted_words:
    report += word + ": " + str(count) + "\n"

with open("text_analysis_report.txt", "w") as file:
    file.write(report)

print("Report saved successfully!")
print("File name: text_analysis_report.txt") 

