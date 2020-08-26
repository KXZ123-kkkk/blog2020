<template>
	<div>
		<div class="message_box" v-for="(item,index) of leaveMessage">
			<div class="line"></div>
			<div class="content" >
				<div class="aside" style="float: left;">
					<img :src="item.headingImg" width="50" height="50" />
				</div>
				<div class="right">
					<div class="right_1">
						<span class="span_1">{{item.nickName}}</span>
						<span class="span_2">第{{index+1}}楼</span>
					</div>
					<div class="message">
						<span class="mes_content">{{item.content}}</span>
					</div>
					<div class="reply">
						<span style="color: #b5a8a8;font-size: 15px; margin-top: 10px;">
							{{item.created_time}}
						</span>

						<div class="replyList" v-if="item.replyList.length != 0">
							<div class="line"></div>
							<div v-for="(k,key) of item.replyList" :key='key' style="">
								<img :src="k.headingImg" width="50" height="50" />
								<span style="color:  rgb(105 178 154 / 90%); font-size: 18px; margin-left: 20px;">{{k.replyName}}</span>
								<span style="color: black; font-size: 12px; margin-left: 10px;">回复:</span>
								<span style="margin-left: 30px;font-size: 17px;color: black;font-weight: bold;opacity: .7;">{{k.content}}</span>
								<div><span style="margin-left: 300px; color: #b5a8a8;font-size: 15px; margin-top: 10px;">
										{{k.created_time}}
									</span></div>
								<div class="line"></div>
							</div>
						</div>
						<span style="display:flex; justify-content: left; margin-left: 500px; 15px; font-size: 15px; color: #bba477; cursor: pointer;"
						 @click="reply(item,index)">回复</span>
						<div v-show="showReply == index">
							<el-input type="textarea" :autosize="{ minRows: 1, maxRows: 2}" placeholder="我想说....." v-model="item.reply"
							 style="width: 600px;">
							</el-input>
							<el-button style="background: linear-gradient(270deg,#c3b69c,#ceaa98); width: 80px; color: white; font-size: 10px;"
							 round @click='sendReply()'>发送回复</el-button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'replyAndLeave',
		props: {
			showReply: Number,
			leaveMessage:{
				type:Array,
				default: () => []
			}
		},
		data() {
			return {
				
			}
		},
		methods: {
			sendReply() {
				this.$emit('sendReply')
			},
			reply(item, index) {
				this.$emit('reply', item, index)
			}
		},
		mounted() {
			// console.log(this.leaveMessage)
		},
		watch:{
			leaveMessage:{
				handler(n,o){
					this.leaveMessage = n
				},
			deep:true,
			immediate: true,
			},
	}}
</script>

<style lang="scss">
	.message_box {
		width: 100%;
		margin-top: 10px;

		.content {
			width: 100%;
			overflow-y: auto;
			.aside {
				display: inline-block;
				height: 110px;
				width: 50px;
				margin-left: 15px;
			}

			.right {
				display: inline-block;
				width: 700px;
				// height: 110px;

				.right_1 {
					float: right;
					width: 100%;
					height: 30px;

					.span_1 {
						margin-left: 10px;
						color: #bba477;
						font-size: 18px;
					}

					.span_2 {
						margin-left: 12px;
						color: #cdc5b4;
						font-size: 14px;
					}
				}

				.message {
					float: right;
					width: 100%;

					.mes_content {
						margin-left: 80px;
						font-size: 17px;
						color: black;
						font-weight: bold;
						opacity: .7;
					}
				}

				.reply {
					float: right;
					width: 100%;
					margin-top: 10px;

					.replyList {
						display: inline;
						width: 500px;
					}
				}
			}
		}


		.line {
			margin-bottom: 5px;
			width: 100%;
			height: 2px;
			opacity: .5;
			background-color: #cdc5b4;
		}
	}
</style>
