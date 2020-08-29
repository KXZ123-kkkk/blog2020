<template>
	<div id="app">
		<div>
			<div v-show='show' class="ll">
				<keep-alive>
					<Aplayer @pause='pause' @play='play' class='music' ref="aplayer" :volume.sync="0.04" :music="{
				    title: 'save Me！',
				    artist: '忘了',
					src:'https://kouxianzheng.oss-cn-chengdu.aliyuncs.com/music/DEAMN%20-%20Save%20Me.flac'	  }"
					 :list='musicList' :mini='false' :listFolded='true' :float='true' :mutex='false' />
				</keep-alive>
			</div>
			<keep-alive v-if="this.$route.meta.isRouterAlive">
				<router-view v-if="isRouterAlive"></router-view>
			</keep-alive>
			<div v-else>
				<router-view v-if="isRouterAlive"></router-view>
			</div>

		</div>

	</div>
</template>

<script>
	import {
		Musics,
		webRead
	} from './api/api.js'
	import Aplayer from 'vue-aplayer'
	import axios from 'axios'
	export default {
		name: 'App',
		components: {
			Aplayer
		},
		provide() {
			return {
				reload: this.reload
			}
		},
		data() {
			return {
				musicList: [],
				isRouterAlive: true,
				show: true,
			}
		},
		methods: {
			reload() {
				this.isRouterAlive = false;
				this.$nextTick(function() {
					this.isRouterAlive = true;
				})
			},
			go() {
				if (this.route == 'music' || this.route == 'cartoons' || this.route == 'cartoon') {
					return false
				} else {
					return true
				}
			},
			pause(){
				this.$store.state.playing = false
			},
			play(){
				this.$store.state.playing = true
			}
		},
		mounted() {
			if (this.musicList.length == 0 && this.$store.state.webReadPerson == 0) {
				axios.all([webRead(), Musics()]).then(axios.spread((webRead, music) => {
					const data = music.data.results
					this.musicList = data

					const record = webRead.data.websiteReadPerson
					this.$store.dispatch('savewebReadPerson', record)
				}))
			}
			if (this.musicList.length == 0) {
				Musics().then(res => {
					const data = res.data.results
					this.musicList = data
				})
			} else if (this.$store.state.webReadPerson == 0) {
				webRead().then(res => {
					const record = res.data.websiteReadPerson
					this.$store.dispatch('savewebReadPerson', record)
				})
			}

		},
		watch: {
			$route(route) {
				let currentTime = this.$refs.aplayer.audio.currentTime
				this.reload();
				setTimeout(() => {
					this.route = route.name
					if (this.route == 'music' || this.route == 'cartoons' || this.route == 'cartoon') {
						this.$refs.aplayer.audio.currentTime = currentTime
						this.$refs.aplayer.audio.pause()
						this.$store.state.playing = false
						this.show = false
					} else {
						if (this.$store.state.playing) {
							this.$refs.aplayer.audio.currentTime = currentTime
							this.$refs.aplayer.audio.play()
							this.show = true
						} else {
							this.$refs.aplayer.audio.currentTime = currentTime
							this.show = true
						}
					}
				}, 1)

			}
		},
	}
</script>

<style lang="scss">
	@import url("./assets/scss/basic.scss");
	@import url("./assets/scss/reset.scss");
	@import url("./assets/scss/mixin.scss");

	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;

		.ll {
			position: fixed;
			z-index: 999;
			bottom: 100px;
			left: 30px;

			.music {
				width: 300px;
			}
		}
	}
</style>
