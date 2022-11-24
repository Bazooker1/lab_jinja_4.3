from jinja2 import Template
import sqlite3
from get_library_model import get_publisher, get_author, get_genre, get_card
genresIds = (3, 5, 6)
authorsIds = (1, 6, 7, 8)
publishersIds = (3,)
# устанавливаем соединение с базой данных
conn = sqlite3.connect("library.sqlite")
df_author = get_author(conn)
df_publisher = get_publisher(conn)
df_genre = get_genre(conn)
df_card = get_card(conn, publishersIds, genresIds, authorsIds)

# закрываем соединение с базой
conn.close()
# открываем файл и читаем шаблон
f_template = open('get_library_templ.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
 authors=df_author,
 publishers=df_publisher,
 genres=df_genre,
 card=df_card,
 selectedAuthors = authorsIds,
 selectedPublishers = publishersIds,
 selectedGenres = genresIds,
 len = len
 )
#создаем файл для HTML-страницы
f = open('template.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
