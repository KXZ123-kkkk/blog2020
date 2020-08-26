<template>
	<smoothres>
		<div class="box1">
			<div class="left">
				<el-tag v-for="(i,index) of tagList" :key='index' class="tag" :type="i.type" effect="light" size='mini'>
					{{i.name}}
				</el-tag>
			</div>
			<div class="right">
				<div class="item animated rotateIn" v-for="(item,index) of blogList" :key='index'>
					<div class=" item_inner">
						<div class="title">
							<router-link :to="{'name':'passage',params:{id:item.id}}"><span style="margin-left: 50px; color: #551A8B;">{{item.title}}</span></router-link>
							<a :href="item.gitHubUrl" style="color: #551A8B;"><span class="iconfont icon-GitHub" style="font-size: 38px; float: right; margin-right: 30px; color: black;"></span></a>
						</div>
						<div class="time">
							<span>{{item.Create_Time}}</span>
						</div>
						<div style="float: right;">
							<img :src="item.img" style=" width: 150px; height: 150px; margin-top: 45px;" />
						</div>
						<div class="body">{{item.subTitle}}
							<router-link :to="{'name':'passage',params:{id:item.id}}"><span class="desc">查看详情</span></router-link>
						</div>
						<router-link :to="{'name':'passage',params:{id:item.id}}">
							<div class="Info">
								<div class="img"><span style="color: #f56c6c;">{{item.leaveMessageCount}}</span></div>
								<span style="font-size: 15px; color: #67c23abf; margin-left: 140px;">回复</span>
							</div>
						</router-link>

					</div>
					
				</div>
			</div>
			<foot></foot>
		</div>
	</smoothres>
</template>

<script>
	import smoothres from './components/Smoothresponse.vue';
	import foot from './components/footer.vue'
	import {
		Blogs
	} from '../api/api.js'
	export default {
		name: 'blog',
		components: {
			smoothres,
			foot
		},
		data() {
			return {
				tagTypeList: ['success', 'info', 'danger', 'warning', 'warning'],
				imgList: [require('../assets/img/blog/烤鸡.png'), require('../assets/img/blog/东东看见一只鸡.png'), require(
						'../assets/img/blog/仙人掌.png'),
					require('../assets/img/blog/小树.png'), require('../assets/img/blog/神器.png'), require('../assets/img/blog/空投.png'),
					require('../assets/img/blog/胜利烟花.png')
				],
				tagList: [],
				blogList: []
			}
		},
		mounted() {
			Blogs().then(res => {
				const data = res.data.results
				let num1 = 0
				for (let i of data) {
					const num = 0
					if (num1 > 6) {
						num1 = 0
					}
					i['img'] = this.imgList[num1]
					num1++
					for (let k of i.Tag) {
						k['type'] = this.tagTypeList[num]
						num++
						if (num > 4) {
							num = 0
						}
					}
				}
				this.tagList = data[0].Tag
				this.blogList = data
			})
		}
	}
</script>

<style lang="scss">
	.box1 {
		width: 800px;


		.left {
			width: 180px;
			display: inline-block;
			float: left;

			.tag {
				margin-top: 30px;
				margin-left: 20px;
				float: left;
			}
		}

		.right {
			width: 600px;
			display: inline-block;

			.item {
				margin-top: 20px;
				width: 500px;
				height: 320px;
				background-color: #c9c9c7;
				padding-top: 15px;
				margin-left: 10px;

				.item_inner {
					text-align: center;
					width: 480px;
					height: 300px;
					margin-left: 10px;
					border: 1px dashed transparent;
					background: linear-gradient(#c9c9c7, #c9c9c7) padding-box,
						repeating-linear-gradient(-45deg, #ccc 0, #ccc 0.25em, white 0, white 0.75em);

					.title {
						cursor: pointer;
						width: 100%;
						margin-top: 30px;
						font-size: 25px;
						font-weight: bold;
						color: #ff0000bd;
					}

					.time {
						margin-top: 20px;
						font-size: 15px;
					}

					.body {
						margin-left: 60px;
						margin-top: 70px;
						text-align: left;

						.desc {
							cursor: pointer;
							margin-left: 5px;
							color: #3a8ee6c7;
						}
					}

					.Info {
						margin-top: 10px;
						font-size: 20px;
						text-align: center;
						cursor: pointer;

						.img {
							margin-left: 200px;
							background-image: url('../assets/img/info.png');
							width: 75px;
							height: 75px;
							line-height: 75px;
						}

						// width: 30px;
						// height: 30px;
					}
				}
			}
		}
	}
</style>
