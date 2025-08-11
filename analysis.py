#!/usr/bin/env python
# coding: utf-8

# # Анализ данных
#                               
# >* **Имя файла:** ``Анализ датасета гонок Формулы-1 в период с 1950-2024 год.``
# >* **Автор:** ``Иманалиева Патимат``
# >* **Дата создания:** ``19.06.2024``
# >* **Дата последней модификации:**  ``22.06.2024 ``
# >* **Связанные файлы:** ``drivers_updated.csv, teams_updated.csv``
# >* **Описание:** ``датасет по данным о набор данных о победителях гонок Формулы-1, начиная с первого сезона 1950 года и заканчивая последними доступными данными в 2024 году. Данные были взяты с базы данных Kaggle.com``
# >* **Версия Python:** ``3.6``

# Набор данных включает в себя полную **информацию о победителях гонок Формулы-1**, начиная *с первого сезона 1950 года и заканчивая последними доступными данными в 2024 году*.
# 
# *   **Pos:** Позиция гонщика в гонке.
# *   **Driver:** Имя гонщика.
# *   **Nationality:** Национальность гонщика.
# *   **Car:** Модель автомобиля, на котором гонщик выступает.
# *   **PTS:** Количество набранных очков.
# *   **year:** Год, в котором была проведена гонка.
# *   **Code:** Код гонки.

# ## Используемые графики для визуализации данных
# 
# 1. Графики по максимальному количеству очков (PTS) по годам (Bar Plot)
# 2. График сравнения результатов двух гонщиков разной национальности в период с 2003-2008 (Line Plot)
# 3. Распределение очков по командам, набравших более 200 очков (Box Plot)
# 4. Топ 10 лучших гонщиков по набранным очкам (Horizomtal Bar Plot)
# 5. Уникальные национальности с количеством набранных очков более 200 (Bar Plot)
# 6. Анимированный график для каждого гонщика набранных очков по годам (Bar Plot)
# 7. Распределение побед среди гонщиков (Pie Chart)
# 
# 
# ## Особенности графиков
# 
# 1. Использование единой цветовой гаммы для единого оформления данных из датасета
# 2. Добавление заголовков, меток осей, сетки для лучшей интерпретируемости данных.
# 3. Разметки графиков находятся в оптимальном диапазоне по ширине, чтобы обеспечить комфортное и удобное восприятие информации.
# 4. Имеется пример анимированного графика для отслеживания динамики изменения данных в датасете.
# 

# ## Этапы работы
# 
# 1. Загрузка и чтение файла в формате CSV.
# 2. Знакомство с датасетом.
# 3. Фильтрация и сортировка данных. Группировка данных в зависимости от запроса.
# 4. Визуализация данных с помощью различных типов графиков.

# # Часть Первая. Чтение файла и знакомство с датасетом

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_1 = pd.read_csv('data/drivers_updated.csv') #название файла в директории
df_1.head(5) #выводим первые 5 значений


# In[8]:


# информация для размерности и количестве строк 
print(df_1.shape)
#информация обо всех гонщиках
print(*df_1.Driver.unique(), len(df_1.Driver.unique()))


# In[3]:


# 1661 строка и 399 уникальных участника гонок в период с 1950 до 2024 года


# In[9]:


# можно посмотреть национальности и машины 
print(*df_1.Nationality.unique()) 
print(*df_1.Car.unique())


# In[10]:


print(len(df_1.Nationality.unique())) #37 национальностей
print(len(df_1.Car.unique())) #205 машин


# In[11]:


#Теперь хочется посмотреть на максимальное количество очков за весь период игр
df_1.PTS.max()


# In[12]:


max_year = df_1[df_1.PTS >= df_1.PTS.max()]
max_year


# In[13]:


#самый высокий балл за всю истоию игр в 2023 году набрал Макс на Ред булл машине - 575 очков.


# # Графики по максимальному количеству очков (PTS) по годам

# ## А что тогда с PTS остальных годов?
# 
# Можно построить **столбчатую диаграмму** - для визуализации максимального количества очков по годам. Она удобна в сравнении значений между категориями и отображения временных изменений.

# Для удобства и наглядности с сохранением информативности я разбиваю временной период на 6 графиков разных промежутков: с *1950-1962, 1963 - 1975, 1976 - 1988, 1989-2001, 2002-2011, 2012-2024* для наглядности. Каждый график размещается отдельно.

# In[14]:


time_ranges = [ (1950, 1962), (1963, 1975)]
pts_max = {}
for start_year, end_year in time_ranges:
    pts_max[(start_year, end_year)] = df_1[(df_1['year'] >= start_year) & (df_1['year'] <= end_year)].groupby('year')['PTS'].max()

fig, ax = plt.subplots(2, 1, figsize=(12,6)) 

axes = ax.flatten()
palette = ['steelblue', 'lightsteelblue']

for i, ((start_year, end_year), pts_max_year) in enumerate(pts_max.items()):
    axes[i].bar(pts_max_year.index, pts_max_year, color=palette[i % len(palette)])
    axes[i].set_title(f'Maximum Score (PTS) for racing between {start_year}-{end_year}')
    axes[i].set_xlabel('Year', size = 10)
    axes[i].set_ylabel('Max PTS', size = 10)

# Установка одинаковой шкалы на оси Y
ax[0].set_ylim(0, max(max(pts_max_year) for pts_max_year in pts_max.values()))
ax[1].set_ylim(0, max(max(pts_max_year) for pts_max_year in pts_max.values()))

plt.tight_layout()
plt.show()


# In[15]:


time_ranges = [ (1976,1988),(1989, 2001)]
pts_max = {}
for start_year, end_year in time_ranges:
    pts_max[(start_year, end_year)] = df_1[(df_1['year'] >= start_year) & (df_1['year'] <= end_year)].groupby('year')['PTS'].max()

fig, ax = plt.subplots(2, 1, figsize=(12,6)) 

axes = ax.flatten()

palette = ['darkslateblue', 'lightslategray']

for i, ((start_year, end_year), pts_max_year) in enumerate(pts_max.items()):
    axes[i].bar(pts_max_year.index, pts_max_year, color=palette[i % len(palette)])
    axes[i].set_title(f'Maximum Score (PTS) for racing between {start_year}-{end_year}')
    axes[i].set_xlabel('Year', size = 10)
    axes[i].set_ylabel('Max PTS', size = 10)

# Установка одинаковой шкалы на оси Y
ax[0].set_ylim(0, max(max(pts_max_year) for pts_max_year in pts_max.values()))
ax[1].set_ylim(0, max(max(pts_max_year) for pts_max_year in pts_max.values()))

plt.tight_layout()
plt.show()


# In[41]:


time_ranges = [ (2002, 2011), (2012, 2024)]
pts_max = {}
for start_year, end_year in time_ranges:
    pts_max[(start_year, end_year)] = df_1[(df_1['year'] >= start_year) & (df_1['year'] <= end_year)].groupby('year')['PTS'].max()

fig, ax = plt.subplots(2, 1, figsize=(12,6)) 

axes = ax.flatten()

palette = ['darkslateblue', 'steelblue', 'lightsteelblue', 'lavender']

for i, ((start_year, end_year), pts_max_year) in enumerate(pts_max.items()):
    axes[i].bar(pts_max_year.index, pts_max_year, color=palette[i % len(palette)])
    axes[i].set_title(f'Maximum Score (PTS) for racing between {start_year}-{end_year}')
    axes[i].set_xlabel('Year', size = 10)
    axes[i].set_ylabel('Max PTS', size = 10)
    
# Установка одинаковой шкалы на оси Y
ax[0].set_ylim(0, max(max(pts_max_year) for pts_max_year in pts_max.values()))
ax[1].set_ylim(0, max(max(pts_max_year) for pts_max_year in pts_max.values()))

plt.tight_layout()
plt.show()


# Наблюдается *положительная тендеция*, связанная с увеличением количества очков (PTS) по годам. На самом деле это оказалось связано с изменением в начислении баллов игрокам:
# 
# * В 1988 году система начисления очков была следующей: 1-е место - 9 очков, 2-е место - 6 очков, 3-е место - 4 очка.
# * В 1989 году система была изменена: 1-е место - 10 очков, 2-е место - 6 очков, 3-е место - 4 очка. Что видно в небольшом увеличении очков.
# * Постепенные изменения ... патя надо почитать я больше ничего не нашла про изменеия очков...
# 

# # График сравнения результатов двух гонщиков разной национальности в период с 2003-2008

# In[16]:


#отфильтруем данные, содержащие все данные о гонках с Фернандо или Рубенса
driver_data = df_1[(df_1['Driver'] == 'Fernando  Alonso ') | (df_1['Driver'] == 'Rubens  Barrichello ')]
driver_data.head(1)


# In[17]:


plt.figure(figsize=(15, 6))

sns.lineplot( data=driver_data, x='year', y='PTS', hue='Driver', marker='o', palette = palette)
palette = ['darkslateblue', 'steelblue', 'lightsteelblue', 'lavender']
plt.title(f'Comparison of points between Rubens Barrichello and Fernando Alonso over the years', size = 15)
plt.xlabel('Year', size = 13)
plt.ylabel('Count', size = 13)
plt.legend(title='Driver')


plt.show()


# Как видно, сравнительный анализ можно проводить в период с 2003 - 2008 год. Отфильтруем датасет и построим новый график.

# In[18]:


driver_data1 = driver_data[(driver_data.year >= 2003) & (driver_data.year <= 2008)]


# In[19]:


plt.figure(figsize=(15, 6), facecolor = 'white')
sns.lineplot(data=driver_data1, x='year', y='PTS', hue='Driver', marker='o', palette = palette)
palette = ['darkslateblue', 'steelblue', 'lightsteelblue', 'lavender']
plt.title(f'Comparison of points between Rubens Barrichello and Fernando Alonso over the years', size = 15)
plt.xlabel('Year', size = 13)
plt.ylabel('Count', size = 13)
plt.legend(title='Driver')

plt.show()


# В сравнении видно, что у Рубенса за период совместного участия в играх наблюдалось с 2005 года большее количество очков

# # Распределение очков по командам, набравших PTS больше 200

# In[22]:


import seaborn as sns
import pandas as pd
df = pd.read_csv('data/teams_updated.csv')
data = df[df['PTS'] > 200]


# In[23]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15, 6))
palette = ['darkslateblue', 'steelblue', 'lightsteelblue', 'lavender']

sns.boxplot(x='Team', y='PTS', data=data, palette= palette)

plt.title('Distribution of Points by Team',  size = 18, color = 'darkslategray')
plt.xlabel('Team')
plt.ylabel('Points')
plt.xticks(rotation=90)
plt.grid(True, alpha = 0.2)
plt.show()


# # Топ 10 лучших гонщиков по набранным очкам

# In[24]:


top_drivers = df_1.groupby('Driver')['PTS'].sum().nlargest(10)
plt.figure(figsize=(15, 6))
palette = ['darkslateblue', 'steelblue', 'lightsteelblue', 'lavender']
top_drivers.plot(kind='barh', color= palette)
plt.title('Top 10 Drivers by Points', size = 17)
plt.xlabel('Driver', size = 15)
plt.ylabel('Total Points', size = 15)
plt.grid(True, alpha = 0.2)
plt.show()


# # Уникальные национальности с количеством набранных очков более 200

# In[25]:


df_2 = df_1[df_1.PTS > 200]
# Подсчет уникальных национальностей и их количества
nationality_count = df_2['Nationality'].value_counts()
palette = ['darkslateblue', 'steelblue', 'lightsteelblue', 'lavender']
plt.figure(figsize=(15, 6))
nationality_count.plot(kind='bar', color= palette)
plt.title('Races by Nationality', size = 17)
plt.xlabel('Nationality', size = 10)
plt.ylabel('Count')
plt.grid(True, alpha = 0.3)
plt.show()


# # Анимированный график для каждого гонщика набранных очков по годам
# 

# In[35]:


import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'notebook' 

df = pd.read_csv('data/drivers_updated.csv')
driver_years_pts = df.groupby(['Driver', 'year'])['PTS'].sum().reset_index()

palette = ['darkslateblue', 'steelblue', 'lightsteelblue', 'lavender']

fig = px.bar(driver_years_pts, x='Driver', y='PTS', animation_frame='year', range_y=[0, 800],
             color_discrete_sequence=palette)
fig.update_layout(title='Points Accumulation Over Years')

# Показываем график
fig.show()


# # Распределение побед среди гонщиков

# In[36]:


import pandas as pd
import plotly.express as px

# Определение победителей каждого года
winners = df.loc[df.groupby('year')['PTS'].idxmax()]

winner_counts = winners['Driver'].value_counts().reset_index()
winner_counts.columns = ['Driver', 'Wins']
winner_counts = winner_counts[winner_counts.Wins >2]
winner_counts


# In[37]:


palette = ['darkslateblue', 'steelblue', 'lavender']
fig_pie = px.pie(winner_counts, values='Wins', names='Driver', title='Distribution of Wins Among Drivers', 
                 color_discrete_sequence=palette)
fig_pie.show()


# In[ ]:




