import pymysql
import time
from datetime import datetime

movie = pymysql.connect(host="localhost", user="root", password="4646", db="movie")
cursor = movie.cursor(pymysql.cursors.DictCursor)


def select_by_title(title):
    sql = '''
    select *
    from title_basics
    where originalTitle = %s || primaryTitle = %s;
    '''
    begin_time = time.time()
    cursor.execute(sql, (title, title))
    end_time = time.time()
    row = cursor.fetchone()
    while row:
        print(f"Movie ID: {row['tconst']}, "
              f"Title: {row['originalTitle']}, "
              f"Type: {row['titleType']}, "
              f"Year: {row['startYear']}, ")
        row = cursor.fetchone()
    return {'count': cursor.rowcount, 'execution': round(end_time - begin_time, 4)}


def select_by_actor(actor, order_by):
    sql1 = '''
    select *
    from name_basics nb, title_principals tp, title_basics tb, title_ratings tr
    where nb.nconst = tp.nconst
    and tb.tconst = tp.tconst
    and tr.tconst = tb.tconst
    and tb.titleType = 'movie'
    and nb.primaryName = %s
    order by tr.averageRating desc
    '''
    sql2 = '''
        select *
        from name_basics nb, title_principals tp, title_basics tb, title_ratings tr
        where nb.nconst = tp.nconst
        and tb.tconst = tp.tconst
        and tr.tconst = tb.tconst
        and tb.titleType = 'movie'
        and nb.primaryName = %s
        order by tr.numVotes desc
        '''
    begin_time = time.time()
    if order_by == '1':
        cursor.execute(sql1, actor)
    elif order_by == '2':
        cursor.execute(sql2, actor)
    end_time = time.time()
    row = cursor.fetchone()
    while row:
        print(f"Movie ID: {row['tconst']}, "
              f"Actor ID: {row['nconst']}, "
              f"Title: {row['originalTitle']}, "
              f"Year: {row['startYear']}, "
              f"Rating: {row['averageRating']}, "
              f"Number of votes: {row['numVotes']},")
        row = cursor.fetchone()
    return {'count': cursor.rowcount, 'execution': round(end_time - begin_time, 4)}


def select_by_director(director):
    sql = '''
    select *
    from title_basics tb, title_crew tc, name_basics nb 
    where tb.tconst = tc.tconst
    and tc.directors = nb.nconst
    and nb.primaryName = %s
    and tb.titleType = 'movie'
    order by tb.startYear
    '''
    begin_time = time.time()
    cursor.execute(sql, director)
    end_time = time.time()
    row = cursor.fetchone()
    while row:
        print(f"Movie ID: {row['tconst']}, "
              f"Director ID: {row['nconst']}, "
              f"Title: {row['originalTitle']}, "
              f"Year: {row['startYear']}, ")
        row = cursor.fetchone()
    return {'count': cursor.rowcount, 'execution': round(end_time - begin_time, 4)}


def select_by_genre(genre, order_by):
    sql1 = '''
    select *
    from title_basics tb, title_ratings tr force index (title_ratings_averageRating_index)
    where tb.tconst = tr.tconst 
    and tb.genres like %s
    and tb.titleType = 'movie'
    order by tr.averageRating desc
    limit 50
    '''
    sql2 = '''
    select *
    from title_basics tb, title_ratings tr force index (title_ratings_numVotes_index)
    where tb.tconst = tr.tconst 
    and tb.genres like %s
    and tb.titleType = 'movie'
    order by tr.numVotes desc 
    limit 50
    '''
    begin_time = time.time()
    if order_by == '1':
        cursor.execute(sql1, '%' + genre + '%')
    elif order_by == '2':
        cursor.execute(sql2, '%' + genre + '%')
    end_time = time.time()
    row = cursor.fetchone()
    while row:
        print(f"Movie ID: {row['tconst']}, "
              f"Title: {row['originalTitle']}, "
              f"Rating: {row['averageRating']}, "
              f"Number of votes: {row['numVotes']},")
        row = cursor.fetchone()
    return {'count': cursor.rowcount, 'execution': round(end_time - begin_time, 4)}


def select_oldest_actor():
    sql = '''
    select *
    from name_basics nb
    where nb.deathYear is null
    and nb.birthYear is not null
    order by nb.birthYear
    limit 1
    '''
    begin_time = time.time()
    cursor.execute(sql)
    end_time = time.time()
    row = cursor.fetchone()
    while row:
        print(f"Actor ID: {row['nconst']}, "
              f"Name: {row['primaryName']}, "
              f"Age: {datetime.today().year - row['birthYear'] + 1}, "
              f"BirthYear: {row['birthYear']}, ")
        row = cursor.fetchone()
    return {'count': cursor.rowcount, 'execution': round(end_time - begin_time, 4)}


def select_actor_movie_count_actor(actor):
    sql = '''
    select nb.*, count(*) count
    from name_basics nb,
    title_principals tp,
    title_basics tb
    where nb.nconst = tp.nconst
    and tb.tconst = tp.tconst
    and tb.titleType = 'movie'
    and nb.primaryName = %s
    group by nb.nconst;
    '''
    begin_time = time.time()
    cursor.execute(sql, actor)
    end_time = time.time()
    row = cursor.fetchone()
    while row:
        print(f"Actor ID: {row['nconst']}, "
              f"Name: {row['primaryName']}, "
              f"Count: {row['count']}")
        row = cursor.fetchone()
    return {'count': cursor.rowcount, 'execution': round(end_time - begin_time, 4)}
