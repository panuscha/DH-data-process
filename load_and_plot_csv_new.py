import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

file_path = 'data/b_only_subset.csv'
out_B = 'data/csv/ucla_B.csv'
out_ret = 'data/csv/ucla_ret.csv'
out_smz = 'data/csv/ucla_smz.csv'
out_int = 'data/csv/ucla_int.csv'
out_cle = 'data/csv/ucla_cle.csv'
out_trl = 'data/csv/ucla_trl.csv'

data = pd.read_csv(out_int, delimiter=',')




# year_tags = {'years': [], 
#             'figures': [],
#             'descriptions': [],
#             'genres': []}
# figures = {}
# descriptions = {}
# genres = {}

# def flatten(l):
#     return [item for sublist in l for item in sublist]



# sorted_genres_desc = dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))    

# first_x = 30   
# figures_keys = list(sorted_genres_desc.keys())[:first_x]
# frequencies = list(sorted_genres_desc.values())[:first_x]
# frequencies = [ x/len(df.index) for x in frequencies]

# # Plotting the frequencies
# plt.bar(figures_keys, frequencies)
# plt.xlabel('Genre')
# plt.ylabel('Proportion')
# plt.title('Genre Proportion')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility if needed

# sorted_figures_desc = dict(sorted(figures.items(), key=lambda x: x[1], reverse=True))    

# first_x = 30    
# figures_keys = list(sorted_figures_desc.keys())[:first_x]
# frequencies = list(sorted_figures_desc.values())[:first_x]
# frequencies = [ x/len(df.index) for x in frequencies]

# # Plotting the frequencies
# plt.bar(figures_keys, frequencies)
# plt.xlabel('Figures')
# plt.ylabel('Proportion')
# plt.title('Figures Propotion')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility if needed

# sorted_descriptions_desc = dict(sorted(descriptions.items(), key=lambda x: x[1], reverse=True))    

# first_x = 30    
# descriptions_keys  = list(sorted_descriptions_desc.keys())[:first_x]
# frequencies = list(sorted_descriptions_desc.values())[:first_x]         
# frequencies = [ x/len(df.index) for x in frequencies]

# # Plotting the frequencies
# plt.bar(descriptions_keys, frequencies)
# plt.xlabel('Descriptions')
# plt.ylabel('Proportion')
# plt.title('Descriptions Proportions')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility if needed

# data =  pd.DataFrame.from_dict(year_tags)

# most_common_genre = data.groupby('year')['genre'].apply(lambda x: Counter(str(topic) for topics in x for topic in topics).most_common(1)[0][0] if any(x) > 0 else None)

# plt.bar(most_common_genre.index, most_common_genre.values)
# plt.xlabel('Year')
# plt.ylabel('Most Common Genre')
# plt.title('Most Common Genre per Year')
# plt.xticks(list(most_common_genre.index))
# plt.xticks(rotation=45)


# data =  pd.DataFrame.from_dict(year_tags)

# # Filter out rows where 'descriptions' is empty
# data_filtered = data[data['descriptions'].apply(lambda x: len(x) > 0)]

# most_common_description = data_filtered.groupby('years')['descriptions'].apply(lambda x: Counter(topic for topics in x for topic in topics).most_common(1)[0][0] if len(x) > 0 else None)

# plt.bar(most_common_description.index, most_common_description.values)
# plt.xlabel('Year')
# plt.ylabel('Most Common Description')
# plt.title('Most Common Description per Year')
# plt.xticks(list(most_common_description.index))
# plt.xticks(rotation=45)


#data =  pd.DataFrame.from_dict(year_tags)

# Filter out rows where 'figures' is empty
# data_filtered = data[data['figures'].apply(lambda x: len(x) > 0)]

# most_common_figure = data_filtered.groupby('year')['figures'].apply(lambda x: Counter(str(topic) for topics in x for topic in topics).most_common(1)[0][0] if len(x) > 0 else None)

# plt.bar(most_common_figure.index, most_common_figure.values)
# plt.xlabel('Year')
# plt.ylabel('Most Common Figure')
# plt.title('Most Common Figure per Year')
# plt.xticks(list(most_common_figure.index))
# plt.xticks(rotation=45)



plt.show()                      
