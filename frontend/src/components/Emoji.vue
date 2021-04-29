<template>
  <div>
    <div v-for="track in tracks">
      <div class="track">
        <img :src="track.albumArt" style="width: 100px; display: inline-block;" />
        <div class="track-info">
          <div class="track-title">{{ track.song }}</div>
          <div class="track-artist">{{ track.artist }}</div>
        </div>
        <a :href="track.embedSrc"><!-- @click="playSong(track.songUrl)"> -->
        <svg class="play-button" width="60px" height="60px" viewBox="0 0 750 750" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:1.5;">
          <g transform="matrix(1,0,0,1,-55.3586,-63.2518)">
            <g transform="matrix(1.26277,0,0,1.26277,-121.959,-115.246)">
              <path d="M334.579,291.874L334.579,585.304L593.691,437.321L334.579,291.874Z" style="fill:rgb(221,221,221);stroke:rgb(221,221,221);stroke-width:15.84px;"/>
            </g>
            <g transform="matrix(1,0,0,1,-65.3586,23.5464)">
              <circle cx="495.359" cy="414.347" r="364.641" style="fill:none;stroke:rgb(221,221,221);stroke-width:20px;"/>
            </g>
          </g>
        </svg>
        </a>
      </div>
    </div>
    <div id="main">
      <div class="emoji" v-for="e in emojis.slice(0, 130)">
        <span @click="sendEmoji(e)">{{ e }}</span>
      </div>
    </div>
  </div>
</template>

<style>
html {
}

div#input-box {
  margin-left: auto;
  margin-right: auto;
  width: 30vw;
}

div#main {
  margin-top: 10em;
}

div.emoji {
  display: inline-block;
  font-size: 5em;
  height: 1em;
  cursor: pointer;
}

.track {
  margin: auto;
  width: 500px;
  height: 120px;
  background: #333;
  padding: 10px;
  margin-top: 3em;
}

.prompt {
  margin-bottom: 10px;
  margin-top: 25px;
}

.track-info {
  display: inline-block;
  vertical-align: top;
  height: 60px;
  padding-top: 10px;
  padding-left: 15px;
  font-size: 1.4em;
}

.track-title, .bot-prompt {
  font-family: 'Nunito Sans', sans-serif;;
  color: #DDD;
  font-weight: bold;
  margin: 10px;
}

.bot-prompt {
  width: 80%;
  margin-left: 20%;
  color: #23db59;
  text-align: right;
}

.track-artist, .top-prompt {
  font-family: 'Nunito Sans', sans-serif;;
  color: #AAA;
  margin: 10px;
}

.top-prompt {
  width: 80%;
  color: #FFF;
  font-weight: bold;
}

.play-button {
  float: right;
  margin-top: 20px;
  margin-right: 20px;
}

.play-button:hover {
  cursor: pointer;
}

</style>

<script>
import axios from 'axios'
// import $ from '../../static/jquery.min'
import JSON5 from 'json5'
import qs from 'qs'
import emoji from 'emoji.json'
export default {
  mounted () {
    this.isMobile = window.matchMedia('only screen and (max-width: 760px)').matches
    $('.ui.dropdown').dropdown()
    $('.ui.accordion').accordion()
    $('.ui.sidebar').sidebar('setting', 'dimPage', false)
                    .sidebar('setting', 'closable', this.isMobile)
                    .sidebar('setting', 'transition', 'overlay')
                    .sidebar('setting', 'mobileTransition', 'overlay')
                    .sidebar('setting', 'scrollLock', false)
    if (!this.isMobile) $('#sidebar').sidebar('show')
    axios.get(this.server + '/presets')
    .then(response => {
      this.presets = response.data.presets
    })

    const headers = {
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      auth: {
        username: this.clientId,
        password: this.clientSecret
      }
    }
    const data = {
      grant_type: 'client_credentials'
    }

    axios.post(
      'https://accounts.spotify.com/api/token',
      qs.stringify(data),
      headers
    )
    .then(response => {
      this.accessToken = response.data.access_token
    })
  },
  data () {
    return {
      clientId: 'clientId',
      clientSecret: 'clientSecret',
      accessToken: null,
      loading: false,
      done: false,
      streaming: false,
      tracks:[{
        song: 'Anywhere With You Is H...',
        artist: 'Kurt Hugo Schneider',
        albumArt: 'https://i.scdn.co/image/ab67616d0000b27322a8499fc093e0e2fc8c45c2',
        songUrl: 'https://open.spotify.com/track/3QW9sihUUzSke7zlDJyCgA',
        embedSrc: 'spotify:track:3QW9sihUUzSke7zlDJyCgA?play=true'
      }],
      a: `Got anything for me?`,
      b: 'Try cheering up with this!',
      server: '',
      // server: 'http://localhost:8000',
      preset: 'none',
      isMobile: false,
      response: '',
      albumArt: 'https://i.scdn.co/image/ab67616d0000b27322a8499fc093e0e2fc8c45c2',
      artist: 'Kurt Hugo Schneider',
      song: 'Anywhere With You Is H...',
      nTries: 0,
      historyLength: 5,
      embedSrc: 'spotify:track:3QW9sihUUzSke7zlDJyCgA?play=true',
      emojis: emoji.map(e => e.char),
      showEmojis: false,
    }
  },
  computed: {
  },
  watch: {
  },
  methods: {
    async sendEmoji (emoji) {
      this.a = emoji
      this.query()
    },
    async getSong () {
      this.tracks = []
      const path = this.server + `/recommendemoji/${this.a}`
      axios.post(path)
      .then(response => {
        const rawResponse = response.data.songs
        this.tracks = response.data.songs.map(song => {
          return {
            song: song.song.substr(0, 18),
            artist: song.artist.substr(0, 18),
            albumArt: '',
            songUrl: '',
            embedSrc: ''
          }
        })
      })
    },
    async query () {
      this.loading = true
      this.done = false
      this.nTries = 0
      this.getSong()
    },
    playSong (trackUrl) {
      this.embedSrc = trackUrl.replace('track', 'embed/track') + ':play'
      // console.log(document.getElementsByTagName('button'))
      // setTimeout(function(){ document.querySelectorAll('[title="Play"]').click() }, 500);
      
    }
  },
  created () {
  }
}
</script>
