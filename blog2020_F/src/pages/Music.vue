<template>
	<smoothres>
		<div class='musics animated rubberBand'>
			<Aplayer :music="music" :list='musicList' :mini='false' :volume.sync="0.04" :float='true' :mutex='true' :autoplay='autoplay' />
			<el-button class="btn2" size='mini' type='warning' plain round @click='upMusic' v-show="up">上一页</el-button>
			<el-button class="btn1" size='mini' type='success' plain round @click='nextMusic' v-show="next">下一页</el-button>
		</div>
		<foot></foot>
	</smoothres>
</template>

<script>
	import smoothres from './components/Smoothresponse.vue'
	import Aplayer from 'vue-aplayer'
	import foot from './components/footer.vue'
	import {
		Musics
	} from '../api/api.js'
	export default {
		name: 'music',
		components: {
			smoothres,
			Aplayer,
			foot
		},
		data() {
			return {
				show: true,
				music: {
					title: 'save Me!',
					artist: '忘了',
					src: 'http://47.113.81.118:8888/media/music/save Me.flac'
				},
				musicList: [],
				autoplay: false,
				page: 1,
				pageSize: 15,
				next: true,
				up: false,
			}

		},
		methods: {
			initData() {
				Musics({
					params: {
						page: this.page,
						pageSize: this.pagesize
					}
				}).then(res => {
					if (res.data.next == null) {
						this.next = false
					} else {
						this.next = true
					}
					if (res.data.previous == null) {
						this.up = false
					} else {
						this.up = true
					}

					console.log(res.data)
					const data = res.data.results
					this.musicList = data
				})
			},
			handleClick(row, index) {
				this.music = row
				this.autoplay = true
			},
			nextMusic() {
				this.page++
				this.up = true
				this.initData()
			},
			upMusic() {
				this.page--
				this.initData()
			}
		},
		mounted() {
			this.initData()
		}
	}
</script>

<style lang="scss">
	.musics {
		height: 560px;
		width: 749px;
		background-image: url(../assets/img/blog/小树.png);
		background-size: 250px;

		.btn1 {
			position: fixed;
			bottom: 60px;
			right: 310px;
		}

		.btn2 {
			position: fixed;
			bottom: 60px;
			left: 310px;
		}
	}

</style>
