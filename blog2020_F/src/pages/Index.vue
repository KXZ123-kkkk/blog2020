<template>
	<smoothres>
		
			<div class="menu_wrapper">
				<div class="item_left">
					<div class="item animated flipInX" :style="[item.style]" v-for="(item,index) of menuList_left" :key='index'>
						<div :style="item.img"></div>
						<router-link :to="`/${item.title}`">
							<div class="circle_left">
								<div class="icon-wrapper"><i class="iconfont" :class="item.iconfont" :style="[item.style_icon]"></i></div>
							</div>
						</router-link>
						<div><span class="word">{{item.title}}</span></div>
					</div>
				</div>
				<div class="item_right">
					<div class="item animated flipInX" :style="[item.style]" v-for="(item,index) of menuList_right" :key='index'>
						<div :style="item.img"></div>
						<router-link :to="`/${item.title}`">
							<div class="circle_right">
								<div class="icon-wrapper"><i class="iconfont" :class="item.iconfont" :style="[item.style_icon]"></i></div>
							</div>
						</router-link>
						<span class="word">{{item.title}}</span>
					</div>
				</div>
			</div>
			<foot></foot>
			<!-- <div class="footer">
				<div class="visit">
					访问人数：{{this.$store.state.webReadPerson}}
				</div>
				<div class="saying">
					Nothing is impossible, Everything is possible!
				</div>
			</div> -->
		
	</smoothres>
</template>

<script>
	import smoothres from './components/Smoothresponse.vue'
	import foot from './components/footer.vue'
	export default {
		name: 'index',
		data() {
			return {
				isGrid: false,
				isMenu: true,
				menuList_left: [{
						title: 'Blog',
						iconfont: 'icon-blog',
						style: {
							'background-color': 'rgb(0 255 55 / 17%)'
						},
						style_icon: {
							'color': 'rgb(0 255 55 / 17%)'
						},
						img: {
							width: '350px',
							height: '255px',
							backgroundImage: 'url(' + require('../assets/img/index/index-4.png') + ')'
						}
					},
					{
						title: 'Message',
						iconfont: 'icon-message',
						style_icon: {
							'color': '#ff00814d'
						},
						style: {
							'background-color': '#ff00814d'
						},
						img: {
							width: '350px',
							height: '255px',
							backgroundImage: 'url(' + require('../assets/img/index/index-5.png') + ')'
						}
					},
					{
						title: 'Example',
						iconfont: 'icon-GitHub',
						style_icon: {
							'color': 'rgb(145 255 0 / 31%)'
						},
						style: {
							'background-color': 'rgb(145 255 0 / 31%)'
						},
						img: {
							width: '350px',
							height: '255px',
							backgroundImage: 'url(' + require('../assets/img/index/index-2.png') + ')'
						}
					}
				],
				menuList_right: [{
						title: 'Music',
						iconfont: 'icon-music',
						style_icon: {
							'color': '#ff0000ba'
						},
						style: {
							'background-color': '#ff0000ba'
						},
						img: {
							width: '350px',
							height: '255px',
							backgroundImage: 'url(' + require('../assets/img/index/index-1.png') + ')'
						}
					},
					{
						title: 'Me',
						iconfont: 'icon-my',
						style_icon: {
							'color': '#ffd40075'
						},
						style: {
							'background-color': '#ffd40075'
						},
						img: {
							width: '350px',
							height: '255px',
							backgroundImage: 'url(' + require('../assets/img/index/index-3.png') + ')'
						}
					}, {
						title: 'Cartoon',
						iconfont: 'icon-cartoon',
						style_icon: {
							'color': '#409eff96'
						},
						style: {
							'background-color': '#409eff96'
						},
						img: {
							width: '350px',
							height: '255px',
							backgroundImage: 'url(' + require('../assets/img/index/index-6.png') + ')'
						}
					}
				],
			}
		},
		components: {
			smoothres,
			foot
		},
		methods: {
			changeMenu() {


			}
		}
	}
</script>

<style lang="scss">
	@import '../assets/scss/mixin.scss';

	.footer {
		float: left;
		width: 100%;
		font-weight: bold;
		font-style: oblique;
		text-align: center;
		color: black;

		.saying {
			font-size: 20px;
			margin-bottom: 20px;
		}

		.visit {
			font-size: 15px;
		}
	}

	.menu_wrapper {
		width: 740px;
		z-index: -1;
		.item_left {
			float: left;
			width: 350px;
			background-color: #cdc5b4;
			height: 1640px;

			.item {
				margin-top: 30px;
				width: 350px;
				height: 450px;
				background-color: blue;
				box-shadow: 0 8px 16px hsla(40, 33%, 60%, .99);

				.circle_left {
					margin-top: -70px;
					margin-left: 120px;
					width: 140px;
					height: 140px;
					line-height: 140px;
					text-align: center;
					border-radius: 70px;
					background-color: white;
					cursor: pointer;

					.icon-wrapper {
						&:hover {
							transform: scale(1.5, 1.5);
							transition: transform .5s;
						}

						transform: scale(1, 1);
						transition: transform .5s;

						.iconfont {
							font-size: 60px;
							font-weight: bold;

						}
					}

				}

				.word {
					font-size: 50px;
					font-weight: bold;
					margin-left: 100px;
				}
			}
		}

		.item_right {
			margin-top: 100px;
			float: right;
			height: 1640px;
			width: 350px;
			background-color: #cdc5b4;

			.item {
				margin-top: 30px;
				width: 350px;
				height: 450px;
				background-color: blue;
				box-shadow: 0 8px 16px hsla(40, 33%, 60%, .99);

				.circle_right {
					margin-top: -78px;
					margin-left: 80px;
					width: 140px;
					height: 140px;
					line-height: 140px;
					text-align: center;
					border-radius: 70px;
					background-color: white;
					cursor: pointer;

					.icon-wrapper {
						&:hover {
							transform: scale(1.5, 1.5);
							transition: transform .5s;
						}

						transform: scale(1, 1);
						transition: transform .5s;

						.iconfont {
							font-size: 60px;
							font-weight: bold;

						}
					}
				}

				.word {
					margin-left: 60px;
					font-size: 50px;
					font-weight: bold;
				}
			}
		}
	}
</style>
