import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import './SongPlayers.css'


const Player = ({ prop }) => {

  return (
    <AudioPlayer
      src={prop}
      showJumpControls={false}
      layout="stacked"
      className='songplayer'
      customProgressBarSection={[]}
      customControlsSection={["MAIN_CONTROLS", "VOLUME_CONTROLS"]}
      autoPlayAfterSrcChange={false}
    />
  )
};

export default Player;
