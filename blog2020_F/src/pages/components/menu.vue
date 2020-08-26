<template>
	<div class="box">
		<div class="menu el-icon-s-grid animated bounceInDown" @click="DialogVisible">
		</div>
			<div v-show="dialog">
				<div class="mask" @click="closeDialog()">
					
				</div>
				<div class="dialog">
					<div class="buttonSelf" v-for="(item,index) of menuList" :key='index'  @click='closeDialog()'>
						<router-link :to="`/${item.title}`">
							<div class="wrapper_header"><i :class="item.icon" style="font-size: 50px; color: white;"></i></div>
							<div class="wrapper_footer"><span class="word">{{item.title}}</span></div>
						</router-link>
					</div>
				</div>
				
			</div>
	</div>

</template>

<script>
	export default {
		name: 'menuA',
		data() {
			return {
				menuList: [{
					icon: 'el-icon-house',
					title: 'Home'
				}, {
					icon: 'el-icon-edit',
					title: 'Blog'
				}, {
					icon: 'el-icon-headset',
					title: 'Music'
				}, {
					icon: 'el-icon-chat-round',
					title: 'Message'
				}, {
					icon: 'el-icon-user',
					title: 'Me'
				}, {
					icon: 'el-icon-video-play',
					title: 'Cartoon'
				}, {
					icon: 'el-icon-lollipop',
					title: 'Example'
				}, {
					icon: 'el-icon-ship',
					title: 'Github'
				}, {
					icon: 'el-icon-eleme',
					title: 'Email'
				}],
				dialog: false,
			}
		},
		methods: {
			DialogVisible() {
				this.dialog = this.dialog === true ?
					false : true
			},
			closeDialog() {
				this.dialog = this.dialog === true ?
					false : true;
			}
		}
	}
</script>

<style lang="scss">
	@import '../../assets/scss/mixin.scss';
	@keyframes fadeIn {
			0% {
				z-index: -1;
				opacity: 0;
			}
	
			100% {
				opacity: 0.5;
				z-index: 999;
			}
		}
	
		@keyframes fadeIn1 {
			0% {
				z-index: -1;
				opacity: 0;
			}
	
			100% {
				opacity: 1;
				z-index: 999;
			}
		}
	
		@keyframes fadeOut {
			0% {
				opacity: 0.5;
				z-index: 999;
			}
	
			100% {
				z-index: -1;
				opacity: 0;
			}
		}
		@keyframes fadeOut1 {
			0% {
				opacity: 1;
				z-index: 999;
			}
		
			100% {
				z-index: -1;
				opacity: 0;
			}
		}
	.box {
		.mask {
					@include position(fixed);
					background-color: #000000 !important;
					opacity: .5;
					z-index: 999;
				}
		
				.fadeIn {
					animation: fadeIn 1s;
				}
		
				.fadeOut {
					animation: fadeOut 1s;
				}
				.fadeOut1 {
					animation: fadeOut1 1s;
				}
		
				.fadeIn1 {
					animation: fadeIn1 1s;
				}

		.dialog {
			@include position(fixed, 300px, 50%, 660px, auto);
			transform: translate(-50%, -50%);
			opacity: 1;
			width: 400px;
			height: 400px;
			z-index: 1111;

			.buttonSelf {
				text-align: center;
				line-height: 110px;
				width: 110px;
				height: 110px;
				border: solid white 1px;
				display: inline-block;
				margin-left: 20px;
				margin-bottom: 20px;
				cursor: pointer;
				border-radius: 10px;

				.word {
					font-size: 20px;
					color: white;
				}

				.wrapper_header {
					height: 40px;
				}

				.wrapper_footer {
					height: 25px;
				}
			}
		}
	}
</style>
