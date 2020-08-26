<template>
	<smoothres>
		<div class="cartoon_1">
			<div class="advice"><span style="margin-left: 30px;">我推荐的动漫</span></div>
			<div class="contain_both animated flipInY" v-for="(item,index) of adviceList" :key='index'>
				<div>
					<router-link :to="{'name':'cartoon',params:{id:item.id}}">
						<img :src="item.videoImg" width="136" height="180" />
					</router-link>
					<div style="margin-top: 10px;"><span>{{item.mainName}}</span></div>
					<div><span>共{{item.totalNum}}集</span></div>
				</div>

			</div>
			<div @click="addCartoons_advice" v-show="isGet(1)" style="display: inline-block; cursor: pointer;"><span style="color: #b400ffab; margin-left: 20px; font-size: 15px;">加载更多>></span></div>
		</div>
		<div class="cartoon_2">
			<div class="like"><span style="margin-left: 30px;">我喜欢的动漫</span></div>
			<div class="contain_both animated flipInY" v-for="(item,index) of loveList" :key='index'>
				<div>
					<router-link :to="{'name':'cartoon',params:{id:item.id}}">
						<img :src="item.videoImg" width="136" height="180" />
					</router-link>
					<div style="margin-top: 10px;"><span>{{item.mainName}}</span></div>
					<div><span>共{{item.totalNum}}集</span></div>
				</div>
			</div>
		</div>
		<div @click="addCartoons_like" v-show="isGet(2)" style="display: inline-block; cursor: pointer;"><span style="color: #b400ffab; margin-left: 20px; font-size: 15px;">加载更多>></span></div>
		</div>
		<foot></foot>
	</smoothres>
</template>

<script>
	import smoothres from './components/Smoothresponse.vue'
	import foot from './components/footer.vue'
	import {
		Cartoons
	} from '../api/api.js'
	import axios from 'axios'
	export default {
		name: 'cartoon',
		components: {
			smoothres,
			foot
		},
		data() {
			return {
				page: 1,
				pagesize: 8,
				adviceList: [],
				loveList: [],
				next1: '',
				next2: '',
			}
		},
		methods: {
			initData() {
				axios.all([Cartoons({
					params: {
						page: this.page,
						pageSize: this.pagesize,
						search: 'advice'
					}
				}), Cartoons({
					params: {
						page: this.page,
						pageSize: this.pagesize,
						search: 'like'
					}
				})]).then(axios.spread((adviceData, likeData) => {
					const data1 = adviceData.data
					for (let i of data1.results) {
						this.adviceList.push(i)
					}
					this.next1 = data1.next
					const data2 = likeData.data
					this.next2 = data2.next
					for (let i of data2.results) {
						this.loveList.push(i)
					}
				}))

			},
			addCartoons_advice() {
				this.page++
				Cartoons({
					params: {
						page: this.page,
						pageSize: this.pagesize,
						search: 'advice'
					}
				}).then(res => {
					const data = res.data
					this.next1 = data.next
					for (let i of data.results) {
						this.adviceList.push(i)
					}
				})
			},
			addCartoons_like() {
				this.page++
				Cartoons({
					params: {
						page: this.page,
						pageSize: this.pagesize,
						search: 'like'
					}
				}).then(res => {
					const data = res.data
					this.next2 = data.next
					for (let i of data.results) {
						this.loveList.push(i)
					}
				})
			},
			isGet(val) {
				if (val == 1) {
					if (this.next1 == null) {
						return false
					} else {
						return true
					}
				} else {
					if (this.next2 == null) {
						return false
					} else {
						return true
					}
				}

			}
		},
		mounted() {
			this.initData()
		}
	}
</script>

<style lang="scss">

	.cartoon_1 {
		.advice {
			font-size: 19px;
			color: #165da7;
			background-color: #bbc3cc;
		}

		.contain_both {
			margin-top: 20px;
			margin-left: 20px;
			width: 140px;
			height: 220px;
			margin-top: 20px;
			display: inline-flex;
			justify-content: center;
		}
	}

	.cartoon_2 {
		margin-top: 60px;

		.like {
			font-size: 19px;
			color: #a71616;
			background-color: #cab6b6;
		}

		.contain_both {
			margin-top: 20px;
			margin-left: 20px;
			width: 140px;
			height: 220px;
			margin-top: 20px;
			display: inline-flex;
			justify-content: center;
		}
	}
</style>
