from app.models import db, Song


def seed_songs():
    song1 = Song(
         name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=1)
    song2 = Song(
         name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=1)
    song3 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=2)
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
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=1)
    song10 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=1)


    song11 = Song(
         name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=2)
    song12 = Song(
         name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=2)
    song13 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=2)
    song14 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=2)
    song15 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=2)
    song16 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=2)
    song17 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=2)
    song18 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=2)
    song19 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=2)
    song20 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=2)


    song21 = Song(
         name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=3)
    song22 = Song(
         name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=3)
    song23 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=3)
    song24 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=3)
    song25 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=3)
    song26 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=3)
    song27 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=3)
    song28 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=3)
    song29 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=3)
    song30 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=3)



    song31 = Song(
         name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=4)
    song32 = Song(
         name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=4)
    song33 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=4)
    song34 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=4)
    song35 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=4)
    song36 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=4)
    song37 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=4)
    song38 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=4)
    song39 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=4)
    song40 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=4)


    song41 = Song(
         name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=5)
    song42 = Song(
         name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=5)
    song43 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=5)
    song44 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=5)
    song45 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=5)
    song46 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=4)
    song47 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=5)
    song48 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=5)
    song49 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=5)
    song50 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=5)


    song51 = Song(
         name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=17)
    song52 = Song(
         name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=17)
    song53 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=17)
    song54 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=17)
    song55 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=17)
    song56 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=17)
    song57 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=17)
    song58 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=17)
    song59 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=17)
    song60 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=17)

    song61 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=6)
    song62 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=6)
    song63 = Song(
           name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=6)
    song64 = Song(
           name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=6)
    song65 = Song(
           name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=6)
    song66 = Song(
           name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=6)
    song67 = Song(
           name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=6)
    song68 = Song(
           name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=6)
    song69 = Song(
           name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=6)
    song70 = Song(
           name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=6)
    song71 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=7)
    song72 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=7)
    song73 = Song(
           name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=7)
    song74 = Song(
           name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=7)
    song75 = Song(
           name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=7)
    song76 = Song(
           name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=7)
    song77 = Song(
           name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=7)
    song78 = Song(
           name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=7)
    song79 = Song(
           name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=7)
    song80 = Song(
           name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=7)

    song81 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=8)
    song82 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=8)
    song83 = Song(
           name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=8)
    song84 = Song(
           name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=8)
    song85 = Song(
           name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=8)
    song86 = Song(
           name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=8)
    song87 = Song(
           name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=8)
    song88 = Song(
           name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=8)
    song89 = Song(
           name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=8)
    song90 = Song(
           name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=8)

    song91 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=9)
    song92 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=9)
    song93 = Song(
           name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=9)
    song94 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=9)
    song95 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=9)
    song96 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=9)
    song97 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=9)
    song98 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=9)
    song99 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=9)
    song100 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=9)

    song101 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=10)
    song102 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=10)
    song103 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=10)
    song104 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=10)
    song105 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=10)
    song106 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=10)
    song107 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=10)
    song108 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=10)
    song109 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=10)
    song110 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=10)

    song111 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=11)
    song112 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=11)
    song113 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=11)
    song114 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=11)
    song115 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=11)
    song116 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=11)
    song117 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=11)
    song118 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=11)
    song119 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=11)
    song120 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=11)

    song121 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=12)
    song122 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=12)
    song123 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=12)
    song124 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=12)
    song125 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=12)
    song126 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=12)
    song127 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=12)
    song128 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=12)
    song129 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=12)
    song130 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=12)

    song131 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=13)
    song132 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=13)
    song133 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=13)
    song134 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=13)
    song135 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=13)
    song136 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=13)
    song137 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=13)
    song138 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=13)
    song139 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=13)
    song140 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=13)

    song141 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=14)
    song142 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=14)
    song143 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=14)
    song144 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=14)
    song145 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=14)
    song146 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=14)
    song147 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=14)
    song148 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=14)
    song149 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=14)
    song150 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=14)

    song151 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=15)
    song152 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=15)
    song153 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=15)
    song154 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=15)
    song155 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=15)
    song156 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=15)
    song157 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=15)
    song158 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=15)
    song159 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=15)
    song160 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=15)

    song161 = Song(
            name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=1, moodlistId=16)
    song162 = Song(
            name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=1, moodlistId=16)
    song163 = Song(
        name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=1, moodlistId=16)
    song164 = Song(
        name='Warriyo', artist='Mortals', rating=2, song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635285/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_Release_yullsu.mp4', userId=1, moodlistId=16)
    song165 = Song(
        name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=1, moodlistId=16)
    song166 = Song(
        name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=1, moodlistId=16)
    song167 = Song(
        name='Despacito', artist='Luis Fonsi', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637555/Luis_Fonsi_Despacito_Lyrics___Lyric_Video_ft._Daddy_Yankee_iea59a.mp3", rating=2, userId=1, moodlistId=16)
    song168 = Song(
        name='Holiday', artist='Greenday', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1646537937/Green_Day_-_Holiday_Audio_dmdgnp.mp3", song_image="https://i.ytimg.com/vi/l2hA8g1cNvQ/hqdefault.jpg", rating=2, userId=1, moodlistId=16)
    song169 = Song(
        name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=1, moodlistId=16)
    song170 = Song(
        name='Maybe', artist='MGK', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647554436/Machine_Gun_Kelly_maybe_ft._Bring_Me_The_Horizon_Official_Visualizer_jrpjyq.mp4", rating=2, userId=1, moodlistId=16)

    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    db.session.add(song9)
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
    db.session.add(song23)
    db.session.add(song24)
    db.session.add(song25)
    db.session.add(song26)
    db.session.add(song27)
    db.session.add(song28)
    db.session.add(song29)
    db.session.add(song30)
    db.session.add(song31)
    db.session.add(song32)
    db.session.add(song33)
    db.session.add(song34)
    db.session.add(song35)
    db.session.add(song36)
    db.session.add(song37)
    db.session.add(song38)
    db.session.add(song39)
    db.session.add(song40)
    db.session.add(song41)
    db.session.add(song42)
    db.session.add(song43)
    db.session.add(song44)
    db.session.add(song45)
    db.session.add(song46)
    db.session.add(song47)
    db.session.add(song48)
    db.session.add(song49)
    db.session.add(song50)
    db.session.add(song51)
    db.session.add(song52)
    db.session.add(song53)
    db.session.add(song54)
    db.session.add(song55)
    db.session.add(song56)
    db.session.add(song57)
    db.session.add(song58)
    db.session.add(song59)
    db.session.add(song60)
    db.session.add(song61)
    db.session.add(song62)
    db.session.add(song63)
    db.session.add(song64)
    db.session.add(song65)
    db.session.add(song66)
    db.session.add(song67)
    db.session.add(song68)
    db.session.add(song69)
    db.session.add(song70)
    db.session.add(song71)
    db.session.add(song72)
    db.session.add(song73)
    db.session.add(song74)
    db.session.add(song75)
    db.session.add(song76)
    db.session.add(song77)
    db.session.add(song78)
    db.session.add(song79)
    db.session.add(song80)
    db.session.add(song81)
    db.session.add(song82)
    db.session.add(song83)
    db.session.add(song84)
    db.session.add(song85)
    db.session.add(song86)
    db.session.add(song87)
    db.session.add(song88)
    db.session.add(song89)
    db.session.add(song90)
    db.session.add(song91)
    db.session.add(song92)
    db.session.add(song93)
    db.session.add(song94)
    db.session.add(song95)
    db.session.add(song96)
    db.session.add(song97)
    db.session.add(song98)
    db.session.add(song99)
    db.session.add(song100)
    db.session.add(song101)
    db.session.add(song102)
    db.session.add(song103)
    db.session.add(song104)
    db.session.add(song105)
    db.session.add(song106)
    db.session.add(song107)
    db.session.add(song108)
    db.session.add(song109)
    db.session.add(song110)
    db.session.add(song111)
    db.session.add(song112)
    db.session.add(song113)
    db.session.add(song114)
    db.session.add(song115)
    db.session.add(song116)
    db.session.add(song117)
    db.session.add(song118)
    db.session.add(song119)
    db.session.add(song120)
    db.session.add(song121)
    db.session.add(song122)
    db.session.add(song123)
    db.session.add(song124)
    db.session.add(song125)
    db.session.add(song126)
    db.session.add(song127)
    db.session.add(song128)
    db.session.add(song129)
    db.session.add(song130)
    db.session.add(song131)
    db.session.add(song132)
    db.session.add(song133)
    db.session.add(song134)
    db.session.add(song135)
    db.session.add(song136)
    db.session.add(song137)
    db.session.add(song138)
    db.session.add(song139)
    db.session.add(song140)
    db.session.add(song141)
    db.session.add(song142)
    db.session.add(song143)
    db.session.add(song144)
    db.session.add(song145)
    db.session.add(song146)
    db.session.add(song147)
    db.session.add(song148)
    db.session.add(song149)
    db.session.add(song150)
    db.session.add(song151)
    db.session.add(song152)
    db.session.add(song153)
    db.session.add(song154)
    db.session.add(song155)
    db.session.add(song156)
    db.session.add(song157)
    db.session.add(song158)
    db.session.add(song159)
    db.session.add(song160)
    db.session.add(song161)
    db.session.add(song162)
    db.session.add(song163)
    db.session.add(song164)
    db.session.add(song165)
    db.session.add(song166)
    db.session.add(song167)
    db.session.add(song168)
    db.session.add(song169)
    db.session.add(song170)

    db.session.commit()


def undo_seeds():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
