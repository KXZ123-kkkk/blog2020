<template>
	<div class="Body1" ref='body'>
		<div>
			<el-input class="message_input" type="textarea" :autosize="{ minRows: 4, maxRows: 8}" placeholder="请输入你想留下的内容"
			 v-model="textarea2">
			</el-input>
			<div>
				<el-button style="background: linear-gradient(270deg,#c3b69c,#ceaa98); width: 80px; color: white; font-size: 10px; margin-top: 20px;"
				 round @click='sendMessage()'>发送留言</el-button>
			</div>
		</div>
		<div class="box11" v-if="this.total != 0">
			<span class="title11">留言({{total}})</span>

			<Reply @reply='Replyit' :leaveMessage='leaveMessageLists'  @sendReply='sendreply' :showReply='showreply'></Reply>


			<div style="height: 10px;"></div>
		</div>
		<div v-else style="height: 40px; line-height: 40px;">
			<span style="color: ; font-size: 15px; margin-bottom: 3px; font-weight: bold; color: #0072ff94;">当前还没有人评论，快来做一楼吧！</span>
		</div>
		<el-button v-show="showLoad" :loading='loading' style="background-color: #00ff8480; margin-bottom: 5px;" @click='loadMore()'>点击加载更多</el-button>
		<Kialog :owmerS='owner' :textarea='textarea2' :index='index1' :dialogVisible='showDialog' @close='closeDialog'></Kialog>
	</div>
</template>

<script>
	import axios from 'axios'
	import smoothres from './Smoothresponse.vue';
	import MenuA from './menu.vue';
	import Kialog from './dialog.vue';
	import Reply from './replyAndLeave.vue'
	import {
		leaveMessages,
		replyMessages,
		createLeaveMessages
	} from '../../api/api.js'
	export default {
		name: 'easySend',
		props: [
			'owner'
		],
		components: {
			smoothres,
			MenuA,
			Kialog,
			Reply
		},
		data() {
			return {
				textarea2: '',
				index1: -1,
				showDialog: false,
				showreply: -1,
				total: 0,
				replyMessage_choice: Object,
				leaveMessageLists: [],
				pagesize: 5,
				page: 1,
				loading: false,
				showLoad: true,
				tip: 0
			}
		},
		methods: {
			loadMore() {
				this.page++
				this.loading = true
				setTimeout((() => {
					this.ininData()
					this.loading = false
				}), 1000)
			},
			ininData() {
				axios.all([leaveMessages({
					params: {
						page: this.page,
						pageSize: this.pagesize,
						search: this.owner
					}
				}), replyMessages({
					params: {
						search: this.owner
					}
				})]).then(axios.spread((leaveData, replyData) => {
					this.total = leaveData.data.count
					const data1 = leaveData.data.results
					if (leaveData.data.next == null) {
						this.showLoad = false
					}
					if (this.tip == 1) {
						this.leaveMessageLists = []
						for (let i of data1) {
							i['reply'] = ''
							i['replyList'] = []
							this.leaveMessageLists.push(i)
						}
						this.tip = 0
					} else {
						for (let i of data1) {
							i['reply'] = ''
							i['replyList'] = []
							this.leaveMessageLists.push(i)
						}
						this.$store.dispatch('saveLeaveMessages',data1)
					}

					const data2 = replyData.data.results
					for (let i of this.leaveMessageLists) {
						i['replyList'] = []
					}
					for (let i of data2) {
						let id = i.leave
						for (let k of this.leaveMessageLists) {
							if (k.id == id) {
								k['replyList'].push(i)
							}
						}
					}
					
				}))
			},
			check() {
				if (this.textarea2 == '') {
					this.$notify({
						title: '提示',
						message: '无法发送空信息',
						offset: 200
					});
					return false
				} else {
					return true
				}

			},
			sendMessage() {
				if (this.check()) {
					this.index1 = 0
					this.showDialog = true
				} else {
				}

			},
			Replyit(row, index) {
				this.replyMessage_choice = row
				this.showreply = index
				this.index1 = row.id
			},
			sendreply() {
				this.textarea2 = this.replyMessage_choice.reply
				if (this.check()) {
					this.showDialog = true
				}
			},
			closeDialog(state) {
				this.showreply = -1
				this.textarea2 = ''
				this.tip = 1
				this.showDialog = state
				this.ininData()
				
				// this.$emit('init')
			}
		},
		mounted() {
			this.ininData()
		}
	}
</script>

<style lang="scss">
	.Body1 {
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
</style>
