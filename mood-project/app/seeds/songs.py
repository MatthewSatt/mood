from app.models import db, Song


def seed_songs():
    song1 = Song(
         name='Bored to Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=1)
    song2 = Song(
         name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=1)
    song3 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=1)
    song4 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=1)
    song5 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=1)
    song6 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=1)
    song7 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=1)
    song8 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=1)
    song9 = Song(
        name='Get Low', artist='Lil Jon', song_image="https://i.ytimg.com/vi/ZN43UoyAbwg/hqdefault.jpg", song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646539628/Lil_Jon_The_East_Side_Boyz_-_Get_Low_feat._Ying_Yang_Twins_Official_Audio_suxdlq.mp3", rating=2, userId=1, moodlistId=1)
    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    db.session.add(song9)
    db.session.commit()


def undo_seeds():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
