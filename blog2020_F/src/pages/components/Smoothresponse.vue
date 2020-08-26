<template>
	<div class="container">
		<el-backtop :bottom="100">
			<div>
				<i class="el-icon-upload2"></i>
			</div>
		</el-backtop>
		
		<el-row>
			<MenuA v-show='isGrid' class='Menu'></MenuA>
			<div class="animated jackInTheBox"><el-calendar v-model="value" class='canlender' v-show="showCanl()">
			</el-calendar></div>
			<el-col class="box" :xs="{span:24,offset:0}" :sm="{span:12,offset:6}" :md="{span:12,offset:6}" :lg="{span:12,offset:6}">
				<slot></slot>
			</el-col>
			
		</el-row>
		<Aplayer v-if="go()" class='music' :music="{
		    title: 'cloud 9',
		    artist: 'tobu',
			src:'http://47.113.81.118:8888/media/music/save Me.flac'
		  }"
		 :list='musicList' :mini='false' :listFolded='true' :float='true' :mutex='false' />
		
	</div>
	
</template>

<script>
	import MenuA from './menu.vue'
	import Aplayer from 'vue-aplayer'
	import {
		Musics
	} from '../../api/api.js'
	export default {
		name: 'smoothRes',
		components: {
			MenuA,
			Aplayer
		},
		data() {
			return {
				isGrid: true,
				musicList: [],
				route: this.$route.name,
				value: new Date()
			}
		},
		methods: {
			go() {
				if (this.route == 'music' || this.route == 'cartoons' || this.route == 'cartoon') {
					return false
				} else {
					return true
				}
			},
			showCanl(){
				if (this.route == 'passage'){
					return false
				} else {
					return true
				}
			}
		},
		mounted() {
			Musics().then(res => {
				const data = res.data.results
				this.musicList = data
			})
		}
	}
</script>

<style lang="scss">
	.container {
		width: 100%;
		.el-calendar-table .el-calendar-day{
			height: 30px;
		}
		.canlender{
			border-radius: 5px;
			width: 320px;
			float: right;
			// right: 50px;
		}
		.music {
			width: 300px;
			position: fixed;
			bottom: 50px;
			left: 50px;
		}

		.menu {
			font-size: 50px;
			margin-left: 25px;
			margin-top: 1.25rem;
		}
	}
</style>
