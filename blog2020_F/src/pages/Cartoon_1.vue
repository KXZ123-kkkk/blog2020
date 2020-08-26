<template>
	<smoothres class="box4">
		<div class="title5 animated bounceInDown">
			<span style="margin-left: 40px;">{{videoInfo.mainName}}</span>
			<router-link to="/Cartoon"><span style="float: right; margin-right: 20px; cursor: pointer;color: rgb(85, 26, 139); ">back>></span></router-link>
		</div>
		<div class="Head1 ">
			<img class="animated bounceInLeft" :src="videoInfo.videoImg" style="margin-left: 30px;" />
			<div class="animated bounceInRight" style="display: inline-block; width: 400px;float: right; margin-top: 50px;">
				<span style="overflow-wrap:break-word; margin-left: 20px; font-size: 15px;">{{videoInfo.simpleIntroduce}}</span>
				<div style="margin-top: 10px;">
					<el-button style="display: inline-block;float: right;" type='primary' round @click='first()'>观看第一集</el-button>
				</div>
			</div>
		</div>
		<div class="content2 animated bounceInUp">
			<div class="title2"><span>剧集</span></div>
			<div class="video" v-for="(item,index) of videoInfo.videoInfo" :key='index'>
				<el-button type='warning' plain size='mini' @click='showVideo(item)'>第{{index+1}}集</el-button>
			</div>
		</div>
		<foot></foot>
		<el-dialog :before-close="handleClose" :title="currentVideo.subName" :visible.sync="dialogFormVisible" v-if='dialogFormVisible'>
			<video crossOrigin="https://saas.jialingmm.net/" controls width="100%" :ref='currentVideo.id'>
				<source :src="currentVideo.url" />
			</video>
		</el-dialog>
	</smoothres>
</template>

<script>
	import smoothres from './components/Smoothresponse.vue'
	import foot from './components/footer.vue'
	import {
		Cartoon
	} from '../api/api.js'
	export default {
		name: 'cartoon_1',
		components: {
			smoothres,
			foot
		},
		data() {
			return {
				videoInfo: {},
				dialogFormVisible: false,
				currentVideo: {}
			}
		},
		methods: {
			first(){
				this.currentVideo = this.videoInfo.videoInfo[0]
				this.dialogFormVisible = true
			},
			showVideo(item) {
				this.currentVideo = item
				this.dialogFormVisible = true
			},
			handleClose(done) {
				this.$confirm('确认关闭？')
					.then(_ => {
						done();
					})
					.catch(_ => {});
			}
		},
		mounted() {
			let id = this.$route.params.id
			Cartoon(id).then(res => {
				const data = res.data
				this.videoInfo = data
			})
		}
	}
</script>

<style lang="scss">
	.box4{
		
		.title5 {
			background-color: #0089ff6b;
			font-size: 18px;
			height: 30px;
			line-height: 30px;
		}
		
		.Head1 {
			margin-top: 20px;
		
		}
		
		.content2 {
			width: 600px;
			margin-top: 40px;
			height: 140px;
		
			.title2 {
				background-color: #ff00b140;
				font-size: 18px;
				height: 30px;
				line-height: 30px;
				width: 80px;
				text-align: center;
		
			}
		
			.video {
				display: inline-block;
				margin-left: 20px;
				font-size: 14px;
				margin-top: 20px;
			}
		}
		
		
	}
</style>
