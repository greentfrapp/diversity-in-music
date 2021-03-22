<template>
  <div>
    <div id="sidebar" class="ui right sidebar vertical menu">
      <div class="ui container fluid">
        <div class="ui form">
          <h3>Add Prompt</h3>
          <div class="field">
            <!-- <label>Prompt</label> -->
            <!-- <input type="text" v-model="a"> -->
            <textarea v-model="a" style="height: 30vh;" :class="{streaming: streaming}"></textarea>
          </div>
          <div class="error">
            {{ this.errorMessage }}
          </div>
          <button class="ui green button" :class="{disabled: loading}" @click="query" :disabled="loading || streaming">Submit</button>
          <div class="ui accordion">
            <div class="title">
              <i class="dropdown icon"></i>
              Details
            </div>
            <div class="content">
              <p>
                Given a prompt, we get you out of a rut by recommending you something new and different!
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div id="main" class="pusher">
    <div id="sidebarButton" class="ui big launch left attached fixed button">
      <i class="content icon"></i>
      <span class="text">Menu</span>
    </div>
    <div id="a" class="ui large form">
      <!-- <h3 class="ui dividing header">Demo</h3> -->
      <div class="demo">
        <div class="status-bar">
          <span style="color: white;">12:00</span>
          <img src="static/status-bar.svg" style="width: 20%; float: right;" />
        </div>
        <h1 id="demo-title">Discover</h1>
        <div v-for="track in tracks">
          <div class="prompt">
            <div class="top-prompt">
              {{ track.promptA }}
            </div>
            <div class="bot-prompt">
              {{ track.promptB }}
            </div>
          </div>
          <div class="track">
            <img :src="track.albumArt" style="width: 60px; display: inline-block;" />
            <div class="track-info">
              <div class="track-title">{{ track.song }}</div>
              <div class="track-artist">{{ track.artist }}</div>
            </div>
            <a :href="track.songUrl">
            <svg class="play-button" width="30px" height="30px" viewBox="0 0 750 750" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:1.5;">
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
      </div>
    </div>
    </div>
  </div>
</template>

<style>
html {
  /*overflow: hidden;*/
  background-image: linear-gradient(red, yellow);
}

#sidebar {
  padding: 25px;
}

#sidebarButton {
  position: absolute;
  right: 0;
  padding: 0.5em;
}

.pushable > .pusher {
  overflow: scroll;
}

code {
  background: #EDEDED;
}

.fading {
  animation: fade 2s linear infinite;
}

@keyframes fade {
  0% { opacity: 0.5; }
  50% { opacity: 0; }
  100% { opacity: 0.5; }
}

#main {
  height: 100vh;
  text-align: left;
  display: grid;
  grid-template-columns: 75% 25%;
  grid-template-rows: 5vh auto 10vh;
  grid-template-areas:
    ". panel"
    "a panel"
    ". panel";
}

@media only screen and (max-width: 760px) {
  #main { grid-template-columns: 100% 0%; }
}

#panel {
  grid-area: panel;
  background: #f5f6fa;
  padding: 20px;
}

#a, #b {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}

#a {
  grid-area: a;
  padding-top: 20px;
}

#b {
  grid-area: b;
}

.ui.input:not(.disabled) input[disabled] {
  opacity: 1;
}

#space {
  grid-area: space;
}

#reset {
  grid-area: reset;
}

#primer textarea,
#output textarea {
  font-size: 0.9em;
  line-height: 1.5;
}

#primer textarea.streaming {
  /*animation: stream 2s linear infinite;*/
  border: 3px solid #f1c40f;
}

@keyframes stream {
  0% { opacity: 0.5; }
  50% { opacity: 1.0; }
  100% { opacity: 0.5; }
}

#output textarea.done {
  border: 3px solid #1ff9a1;
}

.error {
  color: red;
  margin-top: 10px;
}

#response {
  margin-top: 15px;
}

#response textarea {
  border: none;
  resize: none;
}

#sender,
#subject {
  width: 30vw;
  display: inline-block;
}

.demo {
  height: 80vh;
  max-height: 650px;
  overflow-y: scroll;
  margin: auto;
  width: 390px;
  background: #222;
  padding: 20px;
  box-shadow: 2px 2px 5px 2px #888888;
}

#demo-title {
  font-family: 'Avenir';
  font-weight: 500;
  color: #EEE;
  padding-bottom: 5px;
  border-bottom: 3px solid #28773f;
  display: inline-block;
}

.track {
  margin: auto;
  width: 350px;
  height: 80px;
  background: #333;
  padding: 10px;
}

.prompt {
  margin-bottom: 10px;
  margin-top: 25px;
}

.track-info {
  display: inline-block;
  vertical-align: top;
  height: 60px;
  padding-top: 5px;
  padding-left: 15px;
}

.track-title, .bot-prompt {
  font-family: 'Avenir';
  color: #DDD;
  font-weight: bold;
  margin: 3px;
}

.track-artist, .top-prompt {
  font-family: 'Avenir';
  color: #AAA;
  margin: 3px;
}

.play-button {
  float: right;
  margin-top: 15px;
  margin-right: 10px;
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
        promptA: `You have been listening to sad songs lately...`,
        promptB: 'Try cheering up with this!',
        song: 'Dear Theodosia',
        artist: 'Leslie Odom Jr.',
        albumArt: 'https://i.scdn.co/image/ab67616d0000b273d72fb5571087bca0a2fed008',
        songUrl: 'https://open.spotify.com/album/1kCHru7uhxBUdzkm4gzRQc'
      }],
      a: `You have been listening to sad songs lately...`,
      b: 'Try cheering up with this!',
      server: '',
      // server: 'http://localhost:8000',
      stop: '',
      temperature: '0.3',
      maxTokens: '500',
      errorMessage: '',
      preset: 'none',
      isMobile: false,
      response: '',
      albumArt: 'https://i.scdn.co/image/ab67616d0000b273d72fb5571087bca0a2fed008',
      artist: 'Leslie Odom Jr.',
      song: 'Dear, Theodosia',
      nTries: 0
    }
  },
  computed: {
  },
  watch: {
  },
  methods: {
    async getSong () {
      const path = this.server + '/recommend'
      axios.get(path, {
        params: {
          prompt: this.a
        }
      })
      .then(response => {
        this.b = response.data.choices[0].text.split('<SONG>')[0]
        const query = response.data.choices[0].text.split('<SONG>')[1].split('</SONG>')[0]
        console.log(query)
        const song = query.split('by')[0]
        const artist = query.split(' by ')[1]
        axios.get('https://api.spotify.com/v1/search', {
          headers: {
            Authorization: 'Bearer ' + this.accessToken
          },
          params: {
            q: song,
            type: 'track',
            limit: 10,
          }
        })
        .then(response => {
          if (response.data.tracks.items.length === 0 && this.nTries < 3) {
            this.nTries += 1
            this.getSong()
          } else {
            let song = response.data.tracks.items.find(song => {
              song.artists[0].name.includes(artist)
            })
            if (!song) song = response.data.tracks.items[0]
            this.albumArt = song.album.images[0].url
            this.artist = song.artists[0].name
            if (this.artist.length > 25) this.artist = this.artist.substr(0, 22) + '...'
            this.song = song.name
            if (this.song.length > 25) this.song = this.song.substr(0, 22) + '...'
            this.songUrl = song.external_urls.spotify
            let newTracks = [{
              promptA: this.a,
              promptB: this.b,
              song: this.song,
              artist: this.artist,
              albumArt: this.albumArt,
              songUrl: this.songUrl
            }]
            this.tracks.slice(0, 2).forEach(t => newTracks.push(t))
            this.tracks = newTracks
            this.loading = false
            this.done = true
          }
        })
      })
    },
    async query () {
      this.loading = true
      this.done = false
      this.nTries = 0
      this.getSong()
    }
  },
  created () {
  }
}
</script>
