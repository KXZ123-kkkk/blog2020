<template>
	<smoothres>
		<div class="box2 animated zoomIn">
			<div class="back">
				<div style="display: inline-block; cursor: pointer; width: 100px;" @click="Back">
					<i class="el-icon-d-arrow-left" style="font-size: 30px;color: #b63535;"></i>
					<span style="font-size: 20px; margin-left: 5px;color: #b63535;">Back</span>
				</div>
				<span style="float: right; margin-top: 10px; margin-right: 20px; font-size: 15px;">文章阅读数{{readNum}}</span>
			</div>
			<div class="content11">
				<div class="title2">
					<span>{{title}}</span>
					<a :href="githubUrl" target="_blank"><i class="iconfont icon-GitHub" style="float: right; margin-right: 30px;font-size: 35px; margin-top: 10px;"></i></a>
				</div>
				<div class="Body2" v-for="(item, index) of passageList" :key='index'>
					<div class="passage2">
						<div class="P_title2">
							<span>{{item.title}}</span>
							<div class="line2"></div>
						</div>
						<div class="P_content2">
							<span style="width: 800px; display:block; white-space:pre-wrap;word-wrap : break-word ;overflow: hidden ;">{{item.content}}</span>
						</div>
						<div class="img2" v-for="(k,key) of item.imgs">
							<img  :src="k.url" />
						</div>
						<div class="code2">
							<pre><code class="language-javascript line-numbers" v-html="item.code"></code></pre>
						</div>
					</div>
				</div>
				<easy-send style="margin-left: 50px;" :owner='owners'></easy-send>
			</div>
		</div>
	</smoothres>
</template>

<script>
	import axios from 'axios'
	import smoothres from './components/Smoothresponse.vue';
	import MenuA from './components/menu.vue';
	import Kialog from './components/dialog.vue';
	import Reply from './components/replyAndLeave.vue'
	import easySend from './components/easySend.vue'
	import {
		leaveMessages,
		replyMessages,
		createLeaveMessages,
		Blog,
		Blogs
	} from '../api/api.js'
	export default {
		name: 'passage',
		components: {
			smoothres,
			smoothres,
			MenuA,
			Kialog,
			Reply,
			easySend
		},
		data() {
			return {
				owners: this.$route.params.id,
				html: '',
				readNum: Number,
				passageList: [],
				githubUrl: '',
				title: '',
			}
		},
		methods: {
			Back() {
				this.$router.push('/Blog')
			},

			ininData() {
				Blog(this.$route.params.id).then((res) => {
						const data = res.data.passage
						this.passageList = data
						this.title = res.data.title
						let baseUrl = 'http://127.0.0.1:8000/media/'
						this.readNum = res.data.blogReadPerson
						this.githubUrl = res.data.gitHubUrl
					}

				)
			},

		},
		mounted() {
			this.ininData()
		},
		updated() {
			
		}
	}
</script>

<style lang="scss">
	.box2 {
		width: 1000px;
		background-color: #c9c9c7;

		.content11 {
			margin-top: 10px;
			margin-left: 10px;
			width: 980px;
			border: 1px dashed #0000004f;

			.title2 {
				margin-top: 20px;
				font-size: 50px;
				font-weight: bold;
				text-align: center;
			}

			.Body2 {
				display: block;

				.passage2 {
					.P_title2 {
						margin-left: 20px;
						margin-top: 80px;
						font-size: 22px;
						font-weight: bold;

						.line2 {
							margin-top: 10px;
							margin-left: 15px;
							width: 900px;
							height: 1px;
							background-color: #0000004d;
						}
					}

					.P_content2 {
						margin-top: 20px;
						margin-left: 60px;
						font-size: 20px;
					}

					.img2 {
						margin-top: 50px;
						margin-left: 50px;
						width: 800px;
					}

					.code2 {
						margin-left: 50px;
						width: 800px;
						background-color: #272822;

						.H_b {
							color: #66d9ef;
						}

						.H_g {
							color: #a6e22e;
						}

						.H_o {
							color: #fd971f;
						}

						.H_y {
							color: #e6db74;
						}

						.H_p {
							color: #ae81ff;
						}
					}
				}
			}

			.Body1 {
				margin-left: 50px;
				margin-top: 20px;
				box-shadow: 0 8px 16px hsla(40, 33%, 60%, .99);
				width: 800px;
				background-color: white;
				border-radius: 5px;
				text-align: center;

				.message_input {
					margin-top: 60px;
					width: 600px;
					border: 1px solid #cdc5b4;
					border-radius: 4px;
				}

				.box11 {
					margin-top: 30px;
					text-align: left;


					.title11 {
						font-size: 25px;
						margin-left: 15px;
						color: #cdb4b4;
					}
				}
			}
		}
	}
</style>
