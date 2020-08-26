<template>
	<div class="container">
		<el-backtop :bottom="100">
			<div>
				<i class="el-icon-upload2"></i>
			</div>
		</el-backtop>
		<el-row>
			<el-col :xs="{span:24,offset:0}" :sm="{span:24,offset:0}" :md="{span:24,offset:0}" :lg="{span:24,offset:0}">
				<div class="Header animated zoomInRight">
					<MenuA class='Menu' style='color: red;'></MenuA>
					<div class="Info">
						<h1 class="word">博客真的很难写!</h1>
						<h3>悄悄地去努力,这才是你现在需要当做目标的事。早安ヽ(￣▽￣)ﾉ</h3>
					</div>
					<div class="img">
						<img src="https://kouxianzheng.oss-cn-chengdu.aliyuncs.com/img/Header.gif" width="150" height="100" />
						<el-tooltip class="item" effect="dark" content="GitHub!通往成功的捷径!" placement="top-start">
							<a href="https://github.com/" style="margin-top: 110px;" target="_blank">
								<span class="iconfont icon-GitHub" style="color: red; font-size: 80px; cursor: pointer;"></span>
							</a>
						</el-tooltip>
						<img src="../assets/img/Me/header1.gif" width="150" height="100" />
					</div>
					<easySend :owner='owners' class='animated zoomInLeft' style='margin-left: 370px;'></easySend>
				</div>
				<foot></foot>
			</el-col>
		</el-row>
	</div>
</template>

<script>
	import axios from 'axios'
	import smoothres from './components/Smoothresponse.vue';
	import MenuA from './components/menu.vue';
	import Kialog from './components/dialog.vue';
	import Reply from './components/replyAndLeave.vue'
	import easySend from './components/easySend.vue'
	import foot from './components/footer.vue'
	import {
		leaveMessages,
		replyMessages,
		createLeaveMessages
	} from '../api/api.js'
	export default {
		name: 'me',
		components: {
			smoothres,
			MenuA,
			Kialog,
			Reply,
			easySend,
			foot
		},
		data() {
			return {
				owners:'1',
			}
		}
	}
</script>

<style lang="scss">
	.container {
		width: 100%;

		.menu {
			font-size: 50px;
			margin-left: 25px;
			margin-top: 1.25rem;
		}

		.Header {
			width: 100%;
			background-image: url(https://kouxianzheng.oss-cn-chengdu.aliyuncs.com/img/header.png);
			background-repeat: no-repeat;

			.img {
				display: flex;
				justify-content: space-between;

				img {
					margin-top: 110px;
				}

			}

			.Info {
				text-align: center;

				.word {
					color: #ffeb00;
					font-size: 50px;
				}

				h3 {
					color: white;
					margin-top: 20px;
					font-size: 30px;
				}

			}
		}

		.Body {
			margin-left: 340px;
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

			.box {
				margin-top: 30px;
				text-align: left;


				.title {
					font-size: 25px;
					margin-left: 15px;
					color: #cdb4b4;
				}
			}
		}

	}
</style>
