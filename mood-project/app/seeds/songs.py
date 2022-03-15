from app.models import db, Song


def seed_songs():
    song1 = Song(
         name='Song1', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=1)
    song2 = Song(
         name='Song2', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=1)
    song3 = Song(
        name='Song3', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=2)
    song4 = Song(
        name='Song4', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=2)
    song5 = Song(
        name='Song5', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=3)
    song6 = Song(
        name="Song6", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=3)
    song7 = Song(
        name='Song7', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=4)
    song8 = Song(
        name='Song8', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=5)
    # song9 = Song(
        # name='Get Low', artist='Lil Jon', song_image="https://i.ytimg.com/vi/ZN43UoyAbwg/hqdefault.jpg", song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646539628/Lil_Jon_The_East_Side_Boyz_-_Get_Low_feat._Ying_Yang_Twins_Official_Audio_suxdlq.mp3", rating=2, userId=1, moodlistId=1)
    song10 = Song(
        name='Song9', artist='Maroon5', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645638125/Maroon_5_-_Memories_Official_Video_lwngsa.mp4", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=5)
    song11 = Song(
        name='Song10', artist='A Day to Remember', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645734897/A_Day_To_Remember_-_If_It_Means_A_Lot_To_You_ouienm.mp4", rating=2, userId=1, moodlistId=6)
    song12 = Song(
        name='Song11', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=2, userId=1, moodlistId=6)
    song13 = Song(
        name='Song12', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", rating=2, userId=1, moodlistId=7)
    song14 = Song(
         name='Song13', artist='Lil Jon', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646539628/Lil_Jon_The_East_Side_Boyz_-_Get_Low_feat._Ying_Yang_Twins_Official_Audio_suxdlq.mp3", rating=2, userId=1, moodlistId=8)
    song15 = Song(
         name='Song14', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=9)
    song16 = Song(
         name='Song15', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=10)
    song17 = Song(
        name='Song16', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=11)
    song18 = Song(
        name='Song17', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=12)
    song19 = Song(
        name='Song18', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=13)
    song20 = Song(
        name="Song19", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=14)
    song21 = Song(
        name='Song20', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=15)
    song22 = Song(
        name='Song21', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=15)


    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    # db.session.add(song9)
    db.session.add(song10)
    db.session.add(song11)
    db.session.add(song12)
    db.session.add(song13)
    db.session.add(song14)
    db.session.add(song15)
    db.session.add(song16)
    db.session.add(song17)
    db.session.add(song18)
    db.session.add(song19)
    db.session.add(song20)
    db.session.add(song21)
    db.session.add(song22)

    db.session.commit()


def undo_seeds():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
