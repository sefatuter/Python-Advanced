import pandas as pd

df = pd.read_csv('C:/Users/SefaPc/Desktop/btkPythonL/17_Data/datasets/GBvideos.csv')

#1- İlk 10 kaydı getiriniz.

result = df.head(10)

#2- İkinci 5 kaydı getiriniz.

result = df[5:].head()

#3- Datasette bulunan kolon isimleri ve sayısını bulunuz.

result = df.columns
result = len(df.columns)

#4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed, description)

df.drop(['video_id','thumbnail_link', 'trending_date','comments_disabled','ratings_disabled', 'video_error_or_removed', 'description'], axis=1, inplace=True)


#5- Beğenme (Like) ve Beğenmeme (Dislike) sayılarının ortalaması?

result = df['likes'].mean()
result = df['dislikes'].mean()


#6- ilk 50 videonun like ve dislike kolonlarını getiriniz.

result = df[['likes', 'dislikes', 'title']].head(50)

#7- En çok görüntülenen video hangisidir?

result = df.loc[df['views'].argmax()]['title']


#8- En düşük görüntülenen video hangisidir?

result = df.loc[df['views'].argmin()]['title']

#9- En fazla görüntülenen ilk 10 video hangisidir?

result = df.sort_values('views',ascending=False)['views']
result = result.head(10)


#10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getir.

result = df.groupby('category_id').mean('category_id').sort_values('likes')['likes']


#11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.

result = df.groupby('category_id').sum().sort_values('comment_count', ascending=False)['comment_count']

#12- Her kategoride kaç video vardır?

result = df['category_id'].value_counts()

#13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.

df['title_len'] = df['title'].apply(len)

#14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.

df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))

#15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

def rate(dataset):
    likesList = list(dataset['likes'])
    dislikesList = list(dataset['dislikes'])
    
    liste = list(zip(likesList, dislikesList))
    
    rateList = []
    
    for like,dislike in liste:
        if(like + dislike) == 0:
            rateList.append(0)
        else:
            rateList.append(like/(like+dislike))
    
    return rateList

df['like_rate'] = rate(df)

print(df.sort_values('like_rate', ascending=False)[['title', 'likes', 'dislikes', 'like_rate']])

print(result)
