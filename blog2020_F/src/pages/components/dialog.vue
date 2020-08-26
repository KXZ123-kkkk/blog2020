<template>
	<div class="Dialog">
		<el-dialog title="确认信息" :visible.sync="dialogVisible" width="25%" :before-close="handleClose" :modal-append-to-body='false'>
			<el-form class="form">
				<el-form-item label="内容:">
					<el-input type="textarea" style="width: 80%" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入内容" v-model="sendInfo.content">
					</el-input>
				</el-form-item>
				<el-form-item label="昵称:">
					<el-input size='small' style="width: 80%" placeholder="必填" v-model="sendInfo.nickName"></el-input>
				</el-form-item>
				<el-form-item label="邮箱:">
					<el-input size='small' style="width: 80%" placeholder="选填" v-model="sendInfo.email"></el-input>
				</el-form-item>
				<el-form-item label="城市:">
					<el-input size='small' style="width: 80%" placeholder="选填" v-model="sendInfo.city"></el-input>
				</el-form-item>
			</el-form>
			<div style="float: right;">
				<el-button size='mini' plain @click="handleClose()">取 消</el-button>
				<el-button size='mini' plain type="primary" @click="send()">确定发送</el-button>
			</div>

			</span>
		</el-dialog>
	</div>
</template>

<script>
	import {
		leaveMessages,
		replyMessages,
		createLeaveMessages,
		createReplyMessages
	} from '../../api/api.js'
	export default {
		name: 'kialog',
		props: {
			textarea: '',
			dialogVisible: false,
			index: 0,
			owmerS:''
		},
		watch: {
			textarea(val) {
				this.sendInfo.content = val
			}
		},
		data() {
			return {
				sendInfo: {
					content: this.textarea,
					nickName: '',
					email: '',
					city: ''
				}
			}
		},
		methods: {
			check() {
				if (this.sendInfo.nickName == '' || this.sendInfo.content == '') {
					this.$message.warning('请填写必填项')
					return false
				}
				return true
			},
			handleClose() {
				this.$emit('close', false)
			},
			send() {
				this.sendInfo.owner = this.owmerS
				if (this.check()) {
					if (this.index == 0) {
						// this.sendInfo.owner = this.owner
						createLeaveMessages(this.sendInfo).then(res => {
							let data = res.data
							if (data.status != 0) {
								this.$message.error(data.msg)
							} else {
								this.$message.success('发言成功！')
								this.sendInfo.nickName = ''
								this.email = ''
								this.city = ''
								this.$emit('close', false)
							}
						})
					} else {
						const Info = this.sendInfo
						Info['leave'] = this.index
						Info['replyName'] = Info['nickName']
						delete Info['nickName']
						createReplyMessages(Info).then(res => {
							let data = res.data
							if (data.status != 0) {
								this.$message.error(data.msg)
							} else {
								this.$message.success('回复成功！')
								this.$emit('close', false)
							}
						})
					}
				}
			}
		},



	}
</script>

<style lang="scss">
	.Dialog {
		.form {}

		.el-dialog {
			border-radius: 20px;
		}

	}
</style>
