<template>
	<div class="container_123">
		<div class="body_404 animated tada">
			<div class="content_404">
				<span style="font-size: 20px; display: block; margin-left: 150px; margin-top: 20px;">404错误！抱歉您要找的页面不存在!!(正在加班开发中┗( ▔, ▔ )┛.....)</span>
				<div style="display: inline-flex; align-items: center;justify-content: center;">
					<img class="img1" src="../assets/img/404/ds-1.gif" width="200" height="200" />
					<el-tag type='sucess' style="display: block;">卧槽！页面不见了！！！</el-tag>
				</div>
				
				<img class="img2" src="../assets/img/404/ds-2.png" width="200" height="200" />
				<el-button type='warning' plain round style="margin-bottom: 20px;" @click='Back'>揍一顿管理员</el-button>
			</div>

		</div>
	</div>
</template>

<script>
	import smoothres from './components/Smoothresponse.vue'
	export default {
		name: 'message',
		components: {
			smoothres
		},
		methods:{
			Back(){
				this.$router.push('/index')
			}
		}
	}
</script>

<style lang="scss">
	.container_123 {
		height: 720px;
		background-color: #91ff0026;
		.body_404 {
			padding-top: 200px;
			margin-left: 400px;

			.content_404 {
				width: 800px;
				border: solid 1px;

				.img1 {
					margin-top: 100px;
				}

				.img2 {
					margin-top: 100px;
					float: right;
				}
			}
		}
	}
</style>
