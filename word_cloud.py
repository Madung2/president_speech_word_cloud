#!pip install wordcloud nltk

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

# 파일로부터 텍스트를 읽어오는 함수
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
text = read_text_from_file('노무현-취임사.txt')
print(text)

# NLTK 불용어 목록을 다운로드합니다. 한국어 불용어는 별도로 추가해야 할 수 있습니다.
nltk.download('stopwords')

# 한국어 불용어 목록을 추가합니다. 필요에 따라 불용어를 추가하거나 삭제하세요.
stop_words = set(stopwords.words('english'))  # 예시이므로 'english'로 되어 있습니다. 한국어는 별도의 처리가 필요합니다.
my_stop_words = ["입니다", "합니다", "..."]  # 한국어 불용어 예시
stop_words.update(my_stop_words)



# 불용어를 제거합니다.
words = text.split()
meaningful_words = [word for word in words if word.lower() not in stop_words]
cleaned_text = " ".join(meaningful_words)

# 워드 클라우드를 생성합니다.
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_words, 
                min_font_size = 10).generate(cleaned_text)

# 워드 클라우드를 시각화합니다.
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()
